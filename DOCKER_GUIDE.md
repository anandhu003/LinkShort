# LinkShort - URL Shortener API

A modern, professional URL shortener built with FastAPI and featuring a beautiful animated frontend.

## 🚀 Quick Start

### Prerequisites
- Docker & Docker Compose
- OR Python 3.8+

## Option 1: Docker (Recommended)

### Build and Run with Docker Compose

```bash
# Clone the repository
git clone https://github.com/anandhu003/LinkShort.git
cd LinkShort

# Start the application
docker-compose up --build

# The app will be available at http://localhost:8000
```

### Build Docker Image Only

```bash
docker build -t linkshort:latest .
docker run -p 8000:8000 linkshort:latest
```

## Option 2: Local Setup

### Install Dependencies

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Run the Server

```bash
uvicorn main:app --reload
```

Access the app at: `http://127.0.0.1:8000`

## 📁 Project Structure

```
LinkShort/
├── main.py                 # FastAPI application
├── database.py             # Database connection
├── models.py               # SQLAlchemy models
├── schemas.py              # Pydantic schemas
├── crud.py                 # Database operations
├── index.html              # Frontend UI
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker configuration
├── docker-compose.yml      # Docker Compose config
├── .dockerignore           # Docker ignore file
└── url_shortener.db        # SQLite database
```

## 🎯 Features

### Core Features
- ✅ Generate short URLs with random codes
- ✅ Custom aliases for personalized short links
- ✅ Click tracking and analytics
- ✅ URL expiration dates
- ✅ QR code generation
- ✅ Copy-to-clipboard functionality

### Frontend Features
- ✅ Modern, animated UI
- ✅ Dark/Light theme toggle
- ✅ Real-time statistics dashboard
- ✅ Responsive design (mobile-friendly)
- ✅ QR code display for each shortened URL
- ✅ URL management (create, edit, delete)

## 📊 API Endpoints

### Create Short URL
```bash
POST /api/shorten
{
  "original_url": "https://example.com/very/long/url",
  "custom_alias": "mylink",          # Optional
  "expires_at": "2026-12-31T23:59:59" # Optional
}
```

### Get All URLs
```bash
GET /api/urls?skip=0&limit=10
```

### Get URL Info
```bash
GET /api/info/{short_code}
```

### Redirect & Track
```bash
GET /{short_code}  # Redirects to original URL + counts click
```

### Get Analytics
```bash
GET /api/analytics/{short_code}
```

### Update URL
```bash
PUT /api/urls/{short_code}
{
  "original_url": "https://new-url.com",
  "expires_at": "2026-12-31T23:59:59"
}
```

### Delete URL
```bash
DELETE /api/urls/{short_code}
```

## 🎨 Technology Stack

### Backend
- **Framework:** FastAPI
- **Server:** Uvicorn
- **Database:** SQLite with SQLAlchemy ORM
- **Validation:** Pydantic

### Frontend
- **HTML5** with modern CSS3
- **Vanilla JavaScript** (no dependencies)
- **QR Code Library:** qrcodejs
- **Responsive Design:** Mobile-friendly CSS Grid

### DevOps
- **Containerization:** Docker
- **Orchestration:** Docker Compose

## 📱 Browser Support

- Chrome/Edge 90+
- Firefox 88+
- Safari 14+
- Mobile browsers (iOS Safari, Chrome Mobile)

## 🔐 Security Features

- URL validation (must start with http:// or https://)
- CORS enabled for frontend integration
- Database session management
- Error handling and validation

## 🌍 Environment Variables

Create a `.env` file (optional):

```
DATABASE_URL=sqlite:///./url_shortener.db
```

## 📝 API Documentation

Interactive API docs available at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 🐛 Troubleshooting

### Port Already in Use
```bash
# Change port in docker-compose.yml or use:
docker-compose up -p 8001 --build
```

### Database Issues
```bash
# Delete database and restart
rm url_shortener.db
docker-compose up --build
```

### Permission Issues
```bash
sudo docker-compose up --build
```

## 🚀 Deployment

### Deploy to Heroku
1. Create a Heroku account
2. Install Heroku CLI
3. Run: `heroku create linkshort` 
4. Deploy: `git push heroku main`

### Deploy to AWS/Digital Ocean
Use the Docker image:
```bash
docker build -t linkshort:latest .
# Push to registry and deploy
```

## 📊 Database Schema

### URLs Table
```sql
CREATE TABLE urls (
    id INTEGER PRIMARY KEY,
    original_url VARCHAR NOT NULL,
    short_code VARCHAR UNIQUE NOT NULL,
    custom_alias VARCHAR UNIQUE,
    clicks INTEGER DEFAULT 0,
    created_at DATETIME DEFAULT NOW(),
    expires_at DATETIME,
    is_active BOOLEAN DEFAULT TRUE
);
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Push and create a Pull Request

## 📄 License

MIT License - feel free to use this project!

## 👨‍💻 Author

Built with ❤️ by Anandhu

## 📞 Support

For issues or questions, create an issue on GitHub!

---

**Live Demo:** http://127.0.0.1:8000
**GitHub:** https://github.com/anandhu003/LinkShort
