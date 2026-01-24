# Extracting Images from PDF Reports

This guide explains how to extract images and diagrams from the project PDF reports for use in the README.

## Quick Method (macOS)

### Using Preview (Manual)

1. Open the PDF in Preview
2. Navigate to the page with the image/diagram
3. Select the image (click and drag to select)
4. Copy (Cmd+C)
5. Open Preview > File > New from Clipboard
6. Export as PNG: File > Export > Format: PNG
7. Save to `docs/images/` with a descriptive name

### Using Command Line (Automated)

For extracting thumbnails:
```bash
cd docs/images
qlmanage -t -s 1000 -o . "/path/to/PDF.pdf"
```

For full-page images, install poppler:
```bash
brew install poppler
pip3 install pdf2image
python3 extract_pdf_images.py "/path/to/PDF1.pdf" "/path/to/PDF2.pdf"
```

## Online Tools

- [iLovePDF - Extract Images](https://www.ilovepdf.com/extract-images-from-pdf)
- [SmallPDF - Extract Images](https://smallpdf.com/extract-images-from-pdf)
- [PDF24 - Extract Images](https://tools.pdf24.org/en/extract-images)

## Image Naming Convention

Use descriptive names:
- `progress_report_workflow.png` - Workflow diagrams
- `final_report_architecture.png` - Architecture diagrams
- `results_table.png` - Results tables
- `methodology_diagram.png` - Methodology diagrams

## Adding Images to README

After extracting images, add them to the README using:

```markdown
![Description](docs/images/filename.png)
*Caption text*
```
