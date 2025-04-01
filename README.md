# 🧪 Lab nâng cao: Docker Compose - Tự viết file cấu hình cho hệ thống Fullstack

## 🎯 Mục tiêu
- Học cách tự viết file `docker-compose.yml` cho ứng dụng gồm:
  - Frontend React
  - Backend Flask
  - Database MySQL
  - Reverse proxy NGINX

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
200lab-lab2/
├── backend/
├── frontend/
├── nginx/
├── .env
└── (bạn sẽ tự tạo docker-compose.yml)
```

---

## 🧠 Yêu cầu học viên

Tự viết file `docker-compose.yml` với các yêu cầu sau:

### 1. `frontend` service
- Build từ thư mục `./frontend`
- Gắn volume để có thể sửa code
- Nối mạng với các service khác

### 2. `backend` service
- Build từ thư mục `./backend`
- Mount volume source code
- Truyền biến môi trường `FLASK_ENV=development`
- `depends_on` với service `db`

### 3. `db` service
- Sử dụng image `mysql:5.7`
- Dùng biến môi trường trong file `.env` để cấu hình:
  - `MYSQL_ROOT_PASSWORD`
  - `MYSQL_DATABASE`
- Mount volume để lưu trữ dữ liệu

### 4. `nginx` service
- Dùng image `nginx:alpine`
- Mount file cấu hình `./nginx/default.conf` vào đúng vị trí NGINX
- Publish port 80
- `depends_on`: frontend và backend

### 5. Tạo network dùng chung tên `lab-net`
### 6. Tạo volume tên `db_data` để dùng cho MySQL

---

## 📌 Gợi ý

Bạn có thể xem lại cú pháp mẫu Compose từ tài liệu hoặc buổi học trước:
- `build`, `ports`, `volumes`, `environment`, `depends_on`, `networks`

---

## 🚀 Chạy thử sau khi hoàn tất

```bash
docker compose up --build
```

---

## 🧹 Dọn dẹp sau khi xong

```bash
docker compose down -v
```

---

## ✅ Kết quả mong đợi

- Truy cập `http://localhost` → thấy giao diện React
- React gọi API `http://localhost/api` → hiển thị nội dung từ Flask → kết nối MySQL
