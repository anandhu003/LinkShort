# LinkShort - URL Shortener API

A production-ready URL shortener application built with FastAPI, PostgreSQL, and Docker.

**Live Demo:** https://github.com/anandhu003/LinkShort

---

## Features ✅

- ✅ Create shortened URLs with custom aliases
- ✅ Track click statistics and analytics
- ✅ URL expiration support
- ✅ Beautiful animated web frontend with dark mode
- ✅ QR code generation for shortened URLs
- ✅ PostgreSQL database with Docker
- ✅ Adminer database management UI
- ✅ RESTful API with automatic documentation
- ✅ Container-ready with Docker Compose

---

## Tech Stack

| Component | Technology |
|-----------|-----------|
| Backend | FastAPI 0.104.1 |
| Server | Uvicorn 0.24.0 |
| Database | PostgreSQL 15 |
| ORM | SQLAlchemy 2.0.23 |
| Frontend | Vanilla JS + HTML5/CSS3 |
| Containerization | Docker & Docker Compose |
| Database UI | Adminer |

---

## Project Structure

```
FastApi/
├── main.py                    # FastAPI app with all endpoints
├── database.py                # PostgreSQL connection & session
├── models.py                  # SQLAlchemy ORM models
├── schemas.py                 # Pydantic validation schemas
├── crud.py                    # CRUD operations logic
├── index.html                 # Frontend UI
├── requirements.txt           # Python dependencies
├── Dockerfile                 # Container image
├── docker-compose.yml         # Multi-service orchestration
├── .env                       # Environment variables
└── README.md                  # This file
```

---

## Database Schema

**URLModel:**
```python
- id (primary key)
- original_url (full URL to redirect to)
- short_code (unique 6-char identifier)
- custom_alias (optional custom short code)
- clicks (number of redirects)
- created_at (timestamp)
- expires_at (optional expiration date)
- is_active (status flag)
```

---

## API Endpoints

### 1. CREATE - Shorten a URL
```http
POST /api/shorten
Content-Type: application/json

{
  "original_url": "https://www.example.com/very/long/url",
  "custom_alias": "myshort",
  "expires_at": "2026-12-31T23:59:59"
}
```

**Response:** `201 Created`
```json
{
  "short_code": "abc123",
  "original_url": "https://www.example.com/very/long/url",
  "custom_alias": "myshort",
  "clicks": 0,
  "created_at": "2026-02-01T12:00:00",
  "expires_at": "2026-12-31T23:59:59",
  "is_active": true
}
```

### 2. READ - Get All URLs
```http
GET /api/urls?skip=0&limit=10
```

### 3. READ - Get URL Info
```http
GET /api/info/{short_code}
```

### 4. REDIRECT - Visit shortened URL
```http
GET /{short_code}
```
Redirects to original URL and increments click count.

### 5. UPDATE - Modify URL
```http
PUT /api/urls/{short_code}
Content-Type: application/json

{
  "original_url": "https://new-url.com",
  "expires_at": "2026-03-31T23:59:59"
}
```

### 6. DELETE - Remove URL
```http
DELETE /api/urls/{short_code}
```

### 7. ANALYTICS - View statistics
```http
GET /api/analytics/{short_code}
```

### 8. HEALTH CHECK
```http
GET /health
```

---

## Quick Start

### Option 1: Docker Compose (Recommended)

```bash
# Start all services
docker compose up --build

# Services available at:
# - API: http://localhost:8000
# - Frontend: http://localhost:8000
# - Adminer: http://localhost:8080
# - PostgreSQL: localhost:5433
```

### Option 2: Manual Setup

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Set environment variables
export DATABASE_URL="postgresql://linkshort:linkshort@localhost:5432/linkshort"

# 3. Start PostgreSQL (if not running)
# On Linux: sudo systemctl start postgresql
# On macOS: brew services start postgresql

# 4. Run the server
uvicorn main:app --reload

# Access at http://localhost:8000
```

---

## Adminer - Database Management

Access the database UI at: **http://localhost:8080**

**Login Details:**
- **System:** PostgreSQL
- **Server:** `db` (or `localhost:5433` if running locally)
- **Username:** `linkshort`
- **Password:** `linkshort`
- **Database:** `linkshort`

From Adminer, you can:
- View all shortened URLs
- Check click statistics
- Manage database records
- Export data

---

## API Documentation

Interactive API docs available at:
- **Swagger UI:** http://localhost:8000/docs
- **ReDoc:** http://localhost:8000/redoc

---

## Frontend Features

### Web Interface
- 🌙 Dark/Light theme toggle
- 📱 Responsive design
- ⚡ Real-time URL generation
- 📊 Statistics dashboard
- 🎨 Animated interface
- 📋 URL history with copy button
- 🔗 QR code generation

---

## Environment Variables

Create a `.env` file in the project root:

```env
DATABASE_URL=postgresql://linkshort:linkshort@db:5432/linkshort
```

---

## Docker Compose Services

### 1. PostgreSQL Database
```yaml
- Image: postgres:15-alpine
- Port: 5433 (external) → 5432 (internal)
- Volume: postgres_data (persists data)
- Health Check: Active
```

### 2. Adminer UI
```yaml
- Image: adminer:latest
- Port: 8080
- Depends on: PostgreSQL
```

### 3. LinkShort API
```yaml
- Image: fastapi-linkshort
- Port: 8000
- Depends on: PostgreSQL (with health check)
- Reload: Enabled for development
```

---

---

## Step 1: Setup & Database ✅ COMPLETED

### What we implemented:

1. **Database Setup** (`database.py`)
   - PostgreSQL database with SQLAlchemy ORM
   - Session management with dependency injection
   - Connection pooling with `pool_pre_ping=True`

2. **Database Model** (`models.py`)
   - URLModel with 8 columns for complete URL management
   - Timestamps for creation and expiration tracking
   - Click counter for analytics

3. **Pydantic Schemas** (`schemas.py`)
   - URLCreate (for creating new shortened URLs)
   - URLResponse (for returning data)
   - URLUpdate (for updating URLs)

4. **CRUD Operations** (`crud.py`)
   - `generate_short_code()` - Random 6-character code
   - `create_short_url()` - Create new shortened URL
   - `get_url_by_code()` - Retrieve by short code
   - `increment_clicks()` - Track clicks
   - `get_all_urls()` - List with pagination
   - `delete_url()` - Remove URL
   - `update_url()` - Update original URL

5. **FastAPI Endpoints** (`main.py`)
   - All CRUD operations fully implemented and tested

---

## Testing

### Using cURL

```bash
# Create shortened URL
curl -X POST http://localhost:8000/api/shorten \
  -H "Content-Type: application/json" \
  -d '{"original_url": "https://www.github.com/anandhu003/LinkShort"}'

# Get all URLs
curl http://localhost:8000/api/urls

# Get URL info
curl http://localhost:8000/api/info/abc123

# Redirect (visit shortened URL)
curl -L http://localhost:8000/abc123

# Get analytics
curl http://localhost:8000/api/analytics/abc123

# Update URL
curl -X PUT http://localhost:8000/api/urls/abc123 \
  -H "Content-Type: application/json" \
  -d '{"original_url": "https://new-url.com"}'

# Delete URL
curl -X DELETE http://localhost:8000/api/urls/abc123
```

---

## Deployment

### Using Docker Compose

```bash
# Build and start all services
docker compose up --build

# Stop services
docker compose down

# View logs
docker compose logs -f

# Stop and remove volumes (clean reset)
docker compose down -v
```

### Production Checklist

- [ ] Update `.env` with strong database credentials
- [ ] Set `PYTHONUNBUFFERED=1` in production
- [ ] Use HTTPS (nginx reverse proxy)
- [ ] Configure CORS properly for your domain
- [ ] Set up automated backups for PostgreSQL
- [ ] Monitor container health
- [ ] Use secrets management for credentials

---

## Architecture

```
┌─────────────────┐
│   Web Browser   │
│   (Frontend)    │
└────────┬────────┘
         │
         ▼
┌─────────────────────────────────────┐
│   LinkShort API (Uvicorn/FastAPI)   │
│     Port: 8000                      │
└────────────┬────────────────────────┘
             │
      ┌──────┴────────┬─────────────┐
      ▼               ▼             ▼
┌──────────────┐ ┌─────────────┐ ┌──────────────┐
│  PostgreSQL  │ │   Adminer   │ │    Docker    │
│  Database    │ │     UI      │ │   Network    │
│  Port: 5433  │ │ Port: 8080  │ │   Bridge     │
└──────────────┘ └─────────────┘ └──────────────┘
```

---

## Learning Outcomes

- ✅ FastAPI framework and async endpoints
- ✅ SQLAlchemy ORM with PostgreSQL
- ✅ Pydantic models for data validation
- ✅ CRUD operations and REST patterns
- ✅ Database relationships and constraints
- ✅ Docker containerization
- ✅ Docker Compose multi-service orchestration
- ✅ Frontend development with vanilla JS
- ✅ QR code generation
- ✅ Click tracking and analytics
- ✅ URL expiration logic

---

## Troubleshooting

### Port Already in Use
```bash
# Free up port 8000
lsof -ti:8000 | xargs kill -9

# Free up port 5433
lsof -ti:5433 | xargs kill -9
```

### Database Connection Error
```bash
# Check if PostgreSQL container is healthy
docker ps

# View container logs
docker compose logs db
```

### Adminer Login Issues
- Ensure PostgreSQL is running: `docker ps`
- Check credentials in `.env` file
- Verify database exists: `db` service should show `(healthy)`

---

## Support

For issues or questions:
- 📧 Email: 03anandhunandhu@gmail.com
- 🐙 GitHub: https://github.com/anandhu003/LinkShort

---

**Made with ❤️ by Anandhu**
