# 🔧 Cara Menjalankan:

## 1. Jalankan script otomatis:
```bash
run.bat
```

## 2. Atau manual:
```bash
pip install -r requirements.txt
copy property_app\.env.example property_app\.env
cd property_app
python main.py
```

## 3. Aplikasi akan berjalan di: http://localhost:8080


# 🛠️ Technologies Used:
Framework: Tornado Python
Database: MongoDB dengan Motor (async driver)
Authentication: JWT tokens
Validation: Marshmallow
Password: bcrypt
Environment: python-dotenv