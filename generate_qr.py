from pathlib import Path
import sys

try:
    import qrcode
except ImportError:
    raise SystemExit("Thiếu thư viện qrcode. Cài bằng: pip install qrcode[pil]")

if len(sys.argv) < 2:
    raise SystemExit("Cách dùng: python generate_qr.py https://your-domain/path/")

base = sys.argv[1].strip().rstrip("/") + "/"
targets = {
    "qr-index.png": base + "index.html",
    "qr-lab0.png": base + "lab0-x-tien-toi.html",
    "qr-lab1.png": base + "lab1-lo-tren-do-thi.html",
    "qr-lab2.png": base + "lab2-gioi-han-mot-phia.html",
}

out = Path(".")
for filename, url in targets.items():
    img = qrcode.make(url)
    img.save(out / filename)
    print(f"Đã tạo {filename} -> {url}")
print("Xong.")
