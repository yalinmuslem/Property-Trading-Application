# Property Trading Application

Aplikasi jual beli properti yang dibangun dengan Tornado Python framework. Aplikasi ini memiliki 3 modul utama:

## 🏗️ Arsitektur Aplikasi

### 1. **Listing Service** (`services/listing_service.py`)
- Mengelola CRUD operasi untuk listing properti
- Filter dan pencarian properti
- Manajemen status properti (tersedia, terjual, disewa)
- Pencarian properti berdasarkan lokasi
- Properti unggulan (featured)

### 2. **User Service** (`services/user_service.py`)
- Autentikasi dan autorisasi pengguna
- Manajemen profil pengguna
- Role-based access control (Admin, Agent, Buyer, Seller)
- JWT token management
- Statistik pengguna

### 3. **Public API Layer** (`api/`)
- REST API endpoints
- Request/response handling
- Error handling dan validasi
- CORS support
- API documentation

## 📁 Struktur Proyek

```
property_app/
├── main.py                 # Entry point aplikasi
├── config/
│   └── settings.py         # Konfigurasi aplikasi
├── models/
│   ├── property.py         # Model dan schema properti
│   └── user.py            # Model dan schema user
├── services/
│   ├── listing_service.py  # Business logic untuk properti
│   └── user_service.py     # Business logic untuk user
├── api/
│   ├── base_handler.py     # Base handler dengan utilities
│   ├── user_handlers.py    # API handlers untuk user
│   ├── property_handlers.py # API handlers untuk properti
│   └── routes.py          # Konfigurasi routing
├── utils/
│   ├── auth.py            # Authentication utilities
│   ├── database.py        # Database connection manager
│   └── validation.py      # Validation utilities
└── .env.example           # Template environment variables
```

## 🚀 Cara Menjalankan

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Setup Environment
```bash
# Copy file environment
copy .env.example .env

# Edit file .env sesuai konfigurasi Anda
```

### 3. Setup Database
Pastikan MongoDB sudah terinstall dan berjalan:
```bash
# Default MongoDB connection: mongodb://localhost:27017/property_trading
```

### 4. Jalankan Aplikasi
```bash
cd property_app
python main.py
```

Aplikasi akan berjalan di: http://localhost:8080

## 📚 API Documentation

### Authentication Endpoints
- `POST /api/auth/register` - Register pengguna baru
- `POST /api/auth/login` - Login pengguna

### User Endpoints
- `GET /api/users/profile` - Get profil user (auth required)
- `PUT /api/users/profile` - Update profil user (auth required)
- `PUT /api/users/password` - Ganti password (auth required)
- `GET /api/users/stats` - Statistik user (auth required)
- `GET /api/users/my-properties` - Properti milik user (auth required)

### Property Endpoints
- `GET /api/properties` - List properti dengan filter
- `POST /api/properties` - Buat listing baru (auth required)
- `GET /api/properties/{id}` - Detail properti
- `PUT /api/properties/{id}` - Update properti (owner only)
- `DELETE /api/properties/{id}` - Hapus properti (owner only)
- `GET /api/properties/featured` - Properti unggulan
- `GET /api/properties/nearby` - Pencarian berdasarkan lokasi

### System Endpoints
- `GET /api/health` - Health check
- `GET /api/` - API documentation

## 🔐 Authentication

Aplikasi menggunakan JWT (JSON Web Token) untuk autentikasi. Setelah login, sertakan token di header:

```
Authorization: Bearer <your-jwt-token>
```

## 👥 User Roles

1. **Admin** - Akses penuh ke semua fitur
2. **Agent** - Dapat membuat dan mengelola listing properti
3. **Seller** - Dapat membuat dan mengelola listing properti milik sendiri
4. **Buyer** - Dapat melihat properti dan mengelola profil

## 🔍 Filter dan Pencarian

API mendukung berbagai filter untuk pencarian properti:

- `property_type`: house, apartment, office, land, warehouse
- `status`: available, sold, rented, pending
- `min_price` / `max_price`: Range harga
- `min_area` / `max_area`: Range luas area
- `bedrooms`: Jumlah kamar tidur
- `bathrooms`: Jumlah kamar mandi
- `city`: Nama kota
- `search`: Pencarian di title/description

### Contoh Request:
```
GET /api/properties?property_type=house&min_price=500000000&max_price=2000000000&city=Jakarta&page=1&limit=20
```

## 📍 Pencarian Berdasarkan Lokasi

```
GET /api/properties/nearby?lat=-6.2088&lng=106.8456&radius=10&limit=20
```

## 🗄️ Database Schema

### Users Collection
```javascript
{
  _id: ObjectId,
  email: String,
  username: String,
  password_hash: String,
  first_name: String,
  last_name: String,
  phone: String,
  role: String, // admin, agent, buyer, seller
  status: String, // active, inactive, suspended
  created_at: Date,
  updated_at: Date,
  // ... other fields
}
```

### Properties Collection
```javascript
{
  _id: ObjectId,
  title: String,
  description: String,
  property_type: String, // house, apartment, office, land, warehouse
  status: String, // available, sold, rented, pending
  price: Number,
  area: Number,
  bedrooms: Number,
  bathrooms: Number,
  address: Object,
  coordinates: Object, // {lat: Number, lng: Number}
  owner_id: ObjectId,
  created_at: Date,
  updated_at: Date,
  views: Number,
  // ... other fields
}
```

## 🔧 Konfigurasi

Semua konfigurasi dapat diatur melalui environment variables atau file `.env`:

- `PORT`: Port server (default: 8080)
- `DEBUG`: Mode debug (default: False)
- `SECRET_KEY`: Secret key untuk JWT
- `MONGO_HOST`: Host MongoDB
- `MONGO_PORT`: Port MongoDB
- `MONGO_DB_NAME`: Nama database

## 🧪 Testing

Untuk testing API, Anda dapat menggunakan tools seperti:
- Postman
- curl
- HTTPie
- Insomnia

Contoh menggunakan curl:
```bash
# Register user baru
curl -X POST http://localhost:8080/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "username": "testuser",
    "password": "password123",
    "confirm_password": "password123",
    "first_name": "John",
    "last_name": "Doe",
    "role": "seller"
  }'
```

## 📝 TODO / Future Enhancements

- [ ] File upload untuk gambar properti
- [ ] Email verification
- [ ] SMS verification
- [ ] Real-time notifications
- [ ] Advanced search dengan Elasticsearch
- [ ] Caching dengan Redis
- [ ] Rate limiting
- [ ] API versioning
- [ ] Unit tests
- [ ] Docker containerization

## 📄 License

MIT License - Silakan gunakan untuk keperluan pembelajaran atau komersial.

## 👨‍💻 Developer

Dibuat oleh **Yalinulloh** untuk pembelajaran Tornado Python framework.

---

**Happy Coding! 🚀**
