import subprocess
import os

def compress_pdf(input_path, output_path, dpi=100):
    """
    Compress a PDF using Ghostscript.
    
    Args:
        input_path (str): Path to the original PDF.
        output_path (str): Path for the compressed PDF.
        dpi (int): Target DPI for images (lower = smaller file size).
    """
    try:
        subprocess.run([
            "gs",
            "-sDEVICE=pdfwrite",
            "-dCompatibilityLevel=1.4",
            "-dPDFSETTINGS=/ebook",  # options: /screen /ebook /printer /prepress
            f"-dColorImageResolution={dpi}",
            f"-dGrayImageResolution={dpi}",
            f"-dMonoImageResolution={dpi}",
            "-dNOPAUSE",
            "-dQUIET",
            "-dBATCH",
            f"-sOutputFile={output_path}",
            input_path
        ], check=True)
        
        before = os.path.getsize(input_path) / (1024*1024)
        after = os.path.getsize(output_path) / (1024*1024)
        print(f"✅ Compression complete: {before:.2f} MB → {after:.2f} MB")
    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    compress_pdf("input.pdf", "output/compressed.pdf", dpi=100)
