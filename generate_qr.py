from pathlib import Path
from reportlab.graphics.barcode.qr import QrCodeWidget
from reportlab.graphics.shapes import Drawing
from reportlab.graphics import renderSVG

BASE = "https://trungpham116.github.io/gt1-labs/"
FILES = [
    "lab1-mien-xac-dinh.html",
    "lab2-x-tien-toi.html",
    "lab3-lo-tren-do-thi.html",
    "lab4-gioi-han-mot-phia.html",
    "lab5-gioi-han-hai-phia.html",
    "lab6-va-lo-lien-tuc.html",
]

out = Path(__file__).parent / "qr"
out.mkdir(exist_ok=True)
for number, filename in enumerate(FILES, 1):
    qr = QrCodeWidget(BASE + filename)
    x1, y1, x2, y2 = qr.getBounds()
    size = 720
    scale = size / max(x2 - x1, y2 - y1)
    drawing = Drawing(size, size, transform=[scale, 0, 0, scale, 0, 0])
    drawing.add(qr)
    renderSVG.drawToFile(drawing, str(out / f"qr-lab{number}.svg"))
