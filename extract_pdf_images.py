#!/usr/bin/env python3
"""
Extract images from PDF files and save them for use in README.
"""
import sys
import os
from pathlib import Path

try:
    import fitz  # PyMuPDF
    HAS_PYMUPDF = True
except ImportError:
    HAS_PYMUPDF = False
    try:
        from pdf2image import convert_from_path
        HAS_PDF2IMAGE = True
    except ImportError:
        HAS_PDF2IMAGE = False

def extract_images_pymupdf(pdf_path, output_dir):
    """Extract images using PyMuPDF."""
    doc = fitz.open(pdf_path)
    images = []
    
    for page_num in range(len(doc)):
        page = doc[page_num]
        image_list = page.get_images()
        
        for img_index, img in enumerate(image_list):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            
            # Save image
            pdf_name = Path(pdf_path).stem
            image_filename = f"{pdf_name}_page{page_num+1}_img{img_index+1}.{image_ext}"
            image_path = os.path.join(output_dir, image_filename)
            
            with open(image_path, "wb") as img_file:
                img_file.write(image_bytes)
            
            images.append(image_path)
            print(f"Extracted: {image_filename}")
    
    doc.close()
    return images

def extract_images_pdf2image(pdf_path, output_dir):
    """Extract images using pdf2image (converts pages to images)."""
    images = convert_from_path(pdf_path)
    pdf_name = Path(pdf_path).stem
    saved_paths = []
    
    for i, image in enumerate(images):
        image_filename = f"{pdf_name}_page{i+1}.png"
        image_path = os.path.join(output_dir, image_filename)
        image.save(image_path, "PNG")
        saved_paths.append(image_path)
        print(f"Extracted: {image_filename}")
    
    return saved_paths

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 extract_pdf_images.py <pdf_file1> [pdf_file2] ...")
        sys.exit(1)
    
    # Create output directory
    output_dir = "docs/images"
    os.makedirs(output_dir, exist_ok=True)
    
    pdf_files = sys.argv[1:]
    
    if HAS_PYMUPDF:
        print("Using PyMuPDF to extract images...")
        for pdf_path in pdf_files:
            if os.path.exists(pdf_path):
                print(f"\nProcessing: {pdf_path}")
                extract_images_pymupdf(pdf_path, output_dir)
            else:
                print(f"Warning: {pdf_path} not found")
    elif HAS_PDF2IMAGE:
        print("Using pdf2image to convert pages to images...")
        for pdf_path in pdf_files:
            if os.path.exists(pdf_path):
                print(f"\nProcessing: {pdf_path}")
                extract_images_pdf2image(pdf_path, output_dir)
            else:
                print(f"Warning: {pdf_path} not found")
    else:
        print("Error: No PDF library available. Please install one of:")
        print("  pip install PyMuPDF")
        print("  pip install pdf2image")
        print("\nNote: pdf2image also requires poppler-utils:")
        print("  brew install poppler")
        sys.exit(1)

if __name__ == "__main__":
    main()
