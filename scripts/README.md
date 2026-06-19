# OFFICE UTILITY SCRIPTS

These are shared utility scripts for document processing, adapted from the anthropics/skills docx skill patterns. Full implementations are in the original JOBS-OS repo and the anthropics/skills repo.

## Available Scripts

### office/unpack.py
Unpack .docx/.pptx/.xlsx to raw XML for inspection or editing.
```bash
python scripts/office/unpack.py document.docx unpacked/
```

### office/pack.py
Repack edited XML back to .docx/.pptx/.xlsx.
```bash
python scripts/office/pack.py unpacked/ document.docx
```

### office/validate.py
Validate OOXML file against ISO/IEC 29500 schema.
```bash
python scripts/office/validate.py document.docx
```

### office/soffice.py
LibreOffice headless wrapper for format conversion.
```bash
python scripts/office/soffice.py --headless --convert-to pdf document.docx
python scripts/office/soffice.py --headless --convert-to docx document.doc
```

### accept_changes.py
Accept all tracked changes in a .docx file.
```bash
python scripts/accept_changes.py input.docx output.docx
```

### recalc.py
Recalculate all formulas in an .xlsx file (LibreOffice-based).
```bash
python scripts/recalc.py spreadsheet.xlsx
```

## Dependencies
- python-docx (for programmatic DOCX creation)
- openpyxl + pandas (for XLSX)
- pypdf + pdfplumber + reportlab (for PDF)
- LibreOffice (for format conversion and recalc)
- pandoc (for text extraction)
- Poppler (for PDF-to-image)
