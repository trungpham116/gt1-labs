Đây là gói triển khai web cho 3 lab.

Bước 1 — Upload toàn bộ file trong thư mục này lên một host tĩnh
  Ví dụ:
  - GitHub Pages
  - Cloudflare Pages
  - Netlify
  - Một web host tĩnh nội bộ

Bước 2 — Sau khi có BASE URL công khai, tạo QR thật
  Ví dụ nếu URL gốc là:
    https://example.com/gt1-labs/
  thì chạy:
    python generate_qr.py https://example.com/gt1-labs/

  Script sẽ tạo:
    qr-index.png
    qr-lab0.png
    qr-lab1.png
    qr-lab2.png

Bước 3 — Chia sẻ cho sinh viên
  - Chia sẻ trang chính: index.html
  - Hoặc chia sẻ từng lab riêng lẻ:
      lab0-x-tien-toi.html
      lab1-lo-tren-do-thi.html
      lab2-gioi-han-mot-phia.html

Cấu trúc file chính:
  index.html
  lab0-x-tien-toi.html
  lab1-lo-tren-do-thi.html
  lab2-gioi-han-mot-phia.html
  generate_qr.py
  README_DEPLOY.txt

Gợi ý nhanh:
  Nếu cần rất nhanh, anh có thể đưa cả thư mục này lên GitHub Pages hoặc Cloudflare Pages.
