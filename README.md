# PDF Compressor (Python + Ghostscript)

This project provides a simple Python script to compress large PDF files for easier sharing or uploading.  
It uses **Ghostscript** for maximum compression, with an optional pure Python fallback (`pikepdf`).

---

## 🚀 Features
- Compress PDFs from 13 MB → ~5 MB or less (depending on settings).
- Multiple quality presets (`/screen`, `/ebook`, `/printer`, `/prepress`).
- Optional **pure Python mode** using `pikepdf` (lighter compression, no Ghostscript needed).
- Works on **macOS, Linux, and Windows**.

---

## 📦 Installation

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/pdf-compressor.git
cd pdf-compressor
```

### 2. Create and activate a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate   # macOS / Linux
venv\Scripts\activate      # Windows (PowerShell)
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Install Ghostscript (required for best compression)

macOS (Homebrew):
```bash
brew install ghostscript
```

Linux (Debian/Ubuntu):
```bash
sudo apt-get install ghostscript
```

Windows:
1. Download from Ghostscript official site - https://www.ghostscript.com/download/gsdnld.html
2. Install and add gswin64c.exe to your PATH.

Verify installation:
```bash
which gs         # macOS/Linux
gswin64c -version   # Windows
```

### 🛠 USAGE:
Run the compressor:
```bash
python main.py
```
Default behavior:
- Reads input.pdf - rename your desire pdf file to compress to input.pdf or change the file name in the code to your file name
- Writes compressed.pdf into the output folder in the project
- Uses /ebook settings (good balance between size and quality)
- Downsamples images to 100 DPI


### Customize compression:
Inside compress_pdf.py, you can change:
- Input/output file names
- Quality preset (/screen, /ebook, /printer, /prepress)
- Image resolution (DPI)

Example (aggressive compression):
```bash
compress_pdf("input.pdf", "compressed.pdf", dpi=72)
```

### ⚙️ Requirements:
- Python 3.8+
- Ghostscript (system dependency)
- Optional: pikepdf

