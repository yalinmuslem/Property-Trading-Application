# Property Trading Application

The property buying and selling application built with Tornado Python Framework.This application has 3 main modules:

## 🏗️ Application architecture

### 1. **Listing Service** (`services/listing_service.py`)
- Stores all the information about properties that are available to rent and buy

### 2. **User Service** (`services/user_service.py`)
- Stores information about all the users in the system

### 3. **Public API Layer** (`api/`)
- Set of APIs that are exposed to the web/public

## 📁 Project structure

```
property_app/
├── main.py                 # Entry point aplikasi
├── config/
│   └── settings.py         # Application configuration
├── models/
│   ├── property.py         # Property Model and Schema
│   └── user.py            # User model and schema
├── services/
│   ├── listing_service.py  # Business logic for property
│   └── user_service.py     # Business logic for users
├── api/
│   ├── base_handler.py     # Base handler with utilities
│   ├── user_handlers.py    # API Handlers for User
│   ├── property_handlers.py # API Handlers for Property
│   └── routes.py          # Routing configuration
├── utils/
│   ├── database.py        # databaseConnectionManager
└── .env.example           # Template environment variables
```

## 🚀 Way of running

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
Make sure Mongodb has been installed and running:
```bash
# Default MongoDB connection: mongodb://localhost:27017/property_trading_app
```

### 4. Run the application
```bash
cd property_app
python main.py
```

The application will run on: http://localhost:8080

## 📚 API Documentation

### User Endpoints
- `GET /users` - Returns all the users available in the db (sorted in descending order of creation date).
```
URL: GET /users

Parameters:
page_num = int # Default = 1
page_size = int # Default = 10
```
```json
Response:
{
    "result": true,
    "users": [
        {
            "id": 1,
            "name": "Suresh Subramaniam",
            "created_at": 1475820997000000,
            "updated_at": 1475820997000000,
        }
    ]
}
```
- `GET /users/1` - Retrieve a user by ID
```
URL: GET /users/{id}
```
```json
Response:
{
    "result": true,
    "user": {
        "id": 1,
        "name": "Suresh Subramaniam",
        "created_at": 1475820997000000,
        "updated_at": 1475820997000000,
    }
}
```
- `POST /users` - Create user
```
URL: POST /users
Content-Type: application/x-www-form-urlencoded

Parameters: (All parameters are required)
name = str
```
```json
Response:
{
    "result": true,
    "user": {
        "id": 1,
        "name": "Suresh Subramaniam",
        "created_at": 1475820997000000,
        "updated_at": 1475820997000000,
    }
}
```

### Property Endpoints
- `GET /listings` - Returns all the listings available in the db (sorted in descending order of creation date). Callers can use page_num and page_size to paginate through all the listings available. Optionally, you can specify a user_id to only retrieve listings created by that user.
```
URL: GET /listings

Parameters:
page_num = int # Default = 1
page_size = int # Default = 10
user_id = str # Optional. Will only return listings by this user if specified
```
```json
Response:
{
    "result": true,
    "listings": [
        {
            "id": 1,
            "user_id": 1,
            "listing_type": "rent",
            "price": 6000,
            "created_at": 1475820997000000,
            "updated_at": 1475820997000000,
        }
    ]
}
```
- `POST /listings` - Create listing
```
URL: POST /listings
Content-Type: application/x-www-form-urlencoded

Parameters: (All parameters are required)
user_id = int
listing_type = str
price = int
```
```json
Response:
{
    "result": true,
    "listing": {
        "id": 1,
        "user_id": 1,
        "listing_type": "rent",
        "price": 6000,
        "created_at": 1475820997000000,
        "updated_at": 1475820997000000,
    }
}
```

### Public User Endpoints
- `GET /public-api/users` - Get all the listings available in the system (sorted in descending order of creation date). Callers can use page_num and page_size to paginate through all the listings available. Optionally, you can specify a user_id to only retrieve listings created by that user.
```
URL: GET /public-api/listings

Parameters:
page_num = int # Default = 1
page_size = int # Default = 10
user_id = str # Optional
```
```json
{
    "result": true,
    "listings": [
        {
            "id": 1,
            "listing_type": "rent",
            "price": 6000,
            "created_at": 1475820997000000,
            "updated_at": 1475820997000000,
            "user": {
                "id": 1,
                "name": "Suresh Subramaniam",
                "created_at": 1475820997000000,
                "updated_at": 1475820997000000,
            },
        }
    ]
}
```
- `POST /public-api/users` - Create user
```
URL: POST /public-api/users
Content-Type: application/json
```
```json
Request body: (JSON body)
{
    "name": "Lorel Ipsum"
}
```
```json
Response:
{
    "user": {
        "id": 1,
        "name": "Lorel Ipsum",
        "created_at": 1475820997000000,
        "updated_at": 1475820997000000,
    }
}
```
### Property Endpoints
- `GET /public-api/listings` - Get all the listings available in the system (sorted in descending order of creation date). Callers can use page_num and page_size to paginate through all the listings available. Optionally, you can specify a user_id to only retrieve listings created by that user.
```
URL: GET /public-api/listings

Parameters:
page_num = int # Default = 1
page_size = int # Default = 10
user_id = str # Optional
```
```json
{
    "result": true,
    "listings": [
        {
            "id": 1,
            "listing_type": "rent",
            "price": 6000,
            "created_at": 1475820997000000,
            "updated_at": 1475820997000000,
            "user": {
                "id": 1,
                "name": "Suresh Subramaniam",
                "created_at": 1475820997000000,
                "updated_at": 1475820997000000,
            },
        }
    ]
}
```
- `POST /public-api/listings` - Create listing
```
URL: POST /public-api/listings
Content-Type: application/json
```
```json
Request body: (JSON body)
{
    "user_id": 1,
    "listing_type": "rent",
    "price": 6000
}
```
```json
Response:
{
    "listing": {
        "id": 143,
        "user_id": 1,
        "listing_type": "rent",
        "price": 6000,
        "created_at": 1475820997000000,
        "updated_at": 1475820997000000,
    }
}
```
## 🗄️ Database Schema

### Users Collection
```json
{
  _id: ObjectId,
  id: 1,
  name: "Suresh Subramaniam",
  created_at: 1475820997000000,
  updated_at: 1475820997000000,
}
```

### Properties Collection
```json
{
  _id: ObjectId,
  user_id: 1,
  listing_type: "rent",
  price: 6000,
  created_at: 1475820997000000,
  updated_at: 1475820997000000,
}
```

## 🔧 Configuration

All configurations can be adjusted through the Environment Variables or Files `.env`:

- `PORT`: Port server (default: 8080)
- `DEBUG`: Mode debug (default: False)
- `MONGO_HOST`: Host MongoDB
- `MONGO_PORT`: Port MongoDB
- `MONGO_DB_NAME`: namaDatabase

## 🧪 Testing

For fire testing, you can use tools such as:
- Postman
- curl
- HTTPie
- Insomnia

## 👨‍💻 Developer

Made by ** Yalinulloh ** for excercise Tornado Python Framework.

---

**Happy Coding! 🚀**
