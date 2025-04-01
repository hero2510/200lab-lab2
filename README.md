# 🧪 Lab nâng cao: Docker Compose - Fullstack App (React + Flask + MySQL + Nginx)

## 🎯 Mục tiêu
- Deploy ứng dụng fullstack gồm frontend React, backend Flask, database MySQL.
- Reverse proxy qua nginx.
- Mount volume để reload code và lưu dữ liệu bền vững.
- Sử dụng biến môi trường qua file `.env`.

---

## 🧱 Kiến trúc hệ thống

```
[Browser]
   ↓
[nginx reverse proxy]
   ├── /api/* → backend (Flask)
   └── /     → frontend (React)
   
[backend] → [MySQL]
```

---

## 📁 Cấu trúc thư mục

```
docker-compose-full-lab/
├── backend/
├── frontend/
├── nginx/
├── .env
└── docker-compose.yml
```

---

## 🚀 Hướng dẫn chạy lab

### 1. Clone hoặc giải nén source code

```bash
cd docker-compose-full-lab
```

### 2. Khởi động hệ thống

```bash
docker compose up --build
```

### 3. Truy cập

- Frontend: http://localhost
- API Backend: http://localhost/api

### 4. Kiểm tra dữ liệu từ React → Flask → MySQL

---

## 🧹 Dọn dẹp sau khi xong lab

```bash
docker compose down -v
```

---

## ✅ Kết quả mong đợi

- Giao diện React gọi API và hiển thị dữ liệu từ MySQL.
- Có thể sửa code backend/frontend và thấy thay đổi ngay (volume).
- MySQL giữ được dữ liệu khi container khởi động lại.
