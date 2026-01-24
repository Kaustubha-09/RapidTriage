#!/bin/bash
# Extract images from PDFs using macOS Preview
# This script opens PDFs in Preview and provides instructions for manual export

PDF1="/Users/kaustubha/Library/Application Support/Cursor/User/workspaceStorage/684a007758a88aff435087bb078fcb33/pdfs/06e6e9da-9579-4f03-9aba-9a4aa15ace0b/Project_Progress_Report_RapidTriage_AI.pdf"
PDF2="/Users/kaustubha/Library/Application Support/Cursor/User/workspaceStorage/684a007758a88aff435087bb078fcb33/pdfs/78c049f2-c3c8-4f18-ab16-477ac7ecb2c5/RapidTriage_AI(Final Report).pdf"

OUTPUT_DIR="docs/images"
mkdir -p "$OUTPUT_DIR"

echo "Attempting to extract images from PDFs..."
echo "PDF 1: $PDF1"
echo "PDF 2: $PDF2"

# Try using sips to convert PDF pages (may not work for all PDFs)
# Alternative: Use Python with pdf2image if poppler is installed
# Or manually export from Preview

# For now, let's try using Python with a different approach
python3 << 'PYTHON_SCRIPT'
import sys
import os
from pathlib import Path

# Try to use PyPDF2 or another library
try:
    import PyPDF2
    print("PyPDF2 found")
except ImportError:
    print("PyPDF2 not found. Trying alternative methods...")
    
    # Try using macOS's built-in tools
    import subprocess
    
    pdf1 = "/Users/kaustubha/Library/Application Support/Cursor/User/workspaceStorage/684a007758a88aff435087bb078fcb33/pdfs/06e6e9da-9579-4f03-9aba-9a4aa15ace0b/Project_Progress_Report_RapidTriage_AI.pdf"
    pdf2 = "/Users/kaustubha/Library/Application Support/Cursor/User/workspaceStorage/684a007758a88aff435087bb078fcb33/pdfs/78c049f2-c3c8-4f18-ab16-477ac7ecb2c5/RapidTriage_AI(Final Report).pdf"
    
    output_dir = "docs/images"
    os.makedirs(output_dir, exist_ok=True)
    
    # Use qlmanage to export PDF pages as images
    for pdf_path in [pdf1, pdf2]:
        if os.path.exists(pdf_path):
            pdf_name = Path(pdf_path).stem.replace(" ", "_")
            print(f"Processing: {pdf_name}")
            # qlmanage -t -s 1000 -o output_dir pdf_path
            # This would export but qlmanage syntax is different
            print(f"  Found PDF: {pdf_path}")
        else:
            print(f"  PDF not found: {pdf_path}")

PYTHON_SCRIPT

echo ""
echo "Manual extraction instructions:"
echo "1. Open PDFs in Preview"
echo "2. For each page with images/diagrams:"
echo "   - Select the image"
echo "   - Copy (Cmd+C)"
echo "   - Open Preview > New from Clipboard"
echo "   - Export as PNG to docs/images/"
echo ""
echo "Or use online tools like:"
echo "- https://www.ilovepdf.com/extract-images-from-pdf"
echo "- https://smallpdf.com/extract-images-from-pdf"
