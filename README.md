# URL Shortener API - FastAPI Project

## Step 1: Setup & Database ✅ COMPLETED

### What we implemented:

1. **Database Setup** (`database.py`)
   - SQLite database with SQLAlchemy ORM
   - Session management with dependency injection

2. **Database Model** (`models.py`)
   ```
   URLModel:
   - id (primary key)
   - original_url (full URL)
   - short_code (unique identifier)
   - custom_alias (optional custom short code)
   - clicks (track page visits)
   - created_at (timestamp)
   - expires_at (optional expiration)
   - is_active (status flag)
   ```

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

### API Endpoints:

#### CREATE
```
POST /api/shorten
{
  "original_url": "https://www.example.com/very/long/url",
  "custom_alias": "myshort",  (optional)
  "expires_at": "2026-02-28T00:00:00"  (optional)
}
```

#### READ
```
GET /api/urls?skip=0&limit=10  (List all with pagination)
GET /api/info/{short_code}     (Get URL details)
```

#### REDIRECT (Click Tracking)
```
GET /{short_code}  (Redirect to original URL + increment clicks)
```

#### UPDATE
```
PUT /api/urls/{short_code}
{
  "original_url": "https://new-url.com",
  "expires_at": "2026-03-31T00:00:00"
}
```

#### DELETE
```
DELETE /api/urls/{short_code}
```

#### ANALYTICS
```
GET /api/analytics/{short_code}
(Returns: short_code, original_url, clicks, created_at, custom_alias)
```

---

## Project Structure:
```
FastApi/
├── main.py                 # FastAPI app with all endpoints
├── database.py             # Database connection & session
├── models.py               # SQLAlchemy ORM models
├── schemas.py              # Pydantic validation schemas
├── crud.py                 # CRUD operations logic
├── requirements.txt        # Python dependencies
├── url_shortener.db        # SQLite database (auto-created)
└── README.md               # This file
```

---

## Features Implemented:

✅ **Path Parameters** - Using `{short_code}` in endpoints
✅ **Redirection** - 301 redirects with click tracking
✅ **Database Basics** - SQLAlchemy ORM with SQLite
✅ **Generate Short URLs** - Random or custom codes
✅ **Track Click Count** - Increments on each visit
✅ **Expiry Time** - URLs can expire based on date
✅ **Custom Aliases** - User-defined short codes

---

## Next Steps (Phase 2-5):

**Phase 2**: Enhanced validation & error handling ✅ (Included in CRUD)
**Phase 3**: Analytics dashboard (if needed)
**Phase 4**: Rate limiting (if needed)
**Phase 5**: Advanced features (if needed)

---

## To Run:

```bash
# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn main:app --reload

# Visit API docs
http://localhost:8000/docs
```

---

**Learning Outcomes from Step 1:**
- ✅ SQLAlchemy ORM & database relationships
- ✅ Pydantic schemas for validation
- ✅ FastAPI dependency injection
- ✅ CRUD patterns in FastAPI
- ✅ Path parameters & query parameters
- ✅ HTTP status codes
