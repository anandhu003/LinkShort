from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.responses import RedirectResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List
import os
from database import engine, get_db, Base
from models import URLModel
from schemas import URLCreate, URLResponse, URLUpdate
from crud import (
    create_short_url, get_url_by_code, increment_clicks,
    get_all_urls, delete_url, update_url
)

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="URL Shortener", version="1.0.0")

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ============ CREATE ============
@app.post("/api/shorten", response_model=URLResponse, status_code=status.HTTP_201_CREATED)
async def shorten_url(url_data: URLCreate, db: Session = Depends(get_db)):
    """
    Create a shortened URL
    
    - **original_url**: The full URL to shorten (required)
    - **custom_alias**: Optional custom short code
    - **expires_at**: Optional expiration datetime
    """
    try:
        db_url = create_short_url(db, url_data)
        return db_url
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

# ============ READ ============
@app.get("/api/urls", response_model=List[URLResponse])
async def list_all_urls(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """
    Get all shortened URLs with pagination
    
    - **skip**: Number of records to skip (default: 0)
    - **limit**: Number of records to return (default: 10)
    """
    urls = get_all_urls(db, skip=skip, limit=limit)
    return urls

@app.get("/api/info/{short_code}", response_model=URLResponse)
async def get_url_info(short_code: str, db: Session = Depends(get_db)):
    """
    Get information about a shortened URL
    
    - **short_code**: The short code or custom alias
    """
    url = get_url_by_code(db, short_code)
    if not url:
        raise HTTPException(status_code=404, detail="URL not found or expired")
    return url

# ============ REDIRECT (with click tracking) ============
@app.get("/{short_code}")
async def redirect_to_url(short_code: str, db: Session = Depends(get_db)):
    """
    Redirect to original URL and track the click
    
    - **short_code**: The short code or custom alias
    """
    url = get_url_by_code(db, short_code)
    if not url:
        raise HTTPException(status_code=404, detail="URL not found or expired")
    
    # Increment click count
    increment_clicks(db, url.id)
    
    # Redirect to original URL
    return RedirectResponse(url=url.original_url, status_code=301)

# ============ UPDATE ============
@app.put("/api/urls/{short_code}", response_model=URLResponse)
async def update_shortened_url(short_code: str, url_data: URLUpdate, db: Session = Depends(get_db)):
    """
    Update a shortened URL
    
    - **short_code**: The short code to update
    - **original_url**: New original URL
    - **expires_at**: New expiration time (optional)
    """
    url = update_url(db, short_code, url_data.original_url)
    if not url:
        raise HTTPException(status_code=404, detail="URL not found")
    
    # Update expiration if provided
    if url_data.expires_at:
        url.expires_at = url_data.expires_at
        db.commit()
    
    return url

# ============ DELETE ============
@app.delete("/api/urls/{short_code}")
async def delete_shortened_url(short_code: str, db: Session = Depends(get_db)):
    """
    Delete a shortened URL
    
    - **short_code**: The short code to delete
    """
    success = delete_url(db, short_code)
    if not success:
        raise HTTPException(status_code=404, detail="URL not found")
    
    return {"message": "URL deleted successfully"}

# ============ ANALYTICS ============
@app.get("/api/analytics/{short_code}")
async def get_url_analytics(short_code: str, db: Session = Depends(get_db)):
    """
    Get analytics for a shortened URL
    
    - **short_code**: The short code
    """
    url = get_url_by_code(db, short_code)
    if not url:
        raise HTTPException(status_code=404, detail="URL not found or expired")
    
    return {
        "short_code": url.short_code,
        "original_url": url.original_url,
        "clicks": url.clicks,
        "created_at": url.created_at,
        "custom_alias": url.custom_alias
    }

# ============ HEALTH CHECK ============
@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "message": "URL Shortener API is running",
        "docs": "/docs"
    }

# ============ FRONTEND ============
@app.get("/")
async def serve_frontend():
    """Serve the frontend HTML"""
    html_file = os.path.join(os.path.dirname(__file__), "index.html")
    if os.path.exists(html_file):
        return FileResponse(html_file, media_type="text/html")
    return {"message": "Frontend not found"}
