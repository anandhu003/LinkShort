import random
import string
from sqlalchemy.orm import Session
from models import URLModel
from schemas import URLCreate
from datetime import datetime

def generate_short_code(length: int = 6) -> str:
    """Generate a random short code"""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def is_valid_url(url: str) -> bool:
    """Basic URL validation"""
    return url.startswith(('http://', 'https://'))

def create_short_url(db: Session, url_data: URLCreate) -> URLModel:
    """Create a new shortened URL"""
    
    # Validate URL
    if not is_valid_url(url_data.original_url):
        raise ValueError("Invalid URL format. Must start with http:// or https://")
    
    # Check if custom alias is provided
    if url_data.custom_alias:
        existing = db.query(URLModel).filter(
            URLModel.custom_alias == url_data.custom_alias
        ).first()
        if existing:
            raise ValueError("Custom alias already taken")
        short_code = url_data.custom_alias
    else:
        # Generate unique short code
        short_code = generate_short_code()
        while db.query(URLModel).filter(URLModel.short_code == short_code).first():
            short_code = generate_short_code()
    
    # Create URL entry
    db_url = URLModel(
        original_url=url_data.original_url,
        short_code=short_code,
        custom_alias=url_data.custom_alias,
        expires_at=url_data.expires_at
    )
    
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url

def get_url_by_code(db: Session, short_code: str) -> URLModel:
    """Get original URL by short code"""
    url = db.query(URLModel).filter(
        URLModel.short_code == short_code
    ).first()
    
    if not url:
        return None
    
    # Check if expired
    if url.expires_at and url.expires_at < datetime.utcnow():
        url.is_active = False
        db.commit()
        return None
    
    return url

def increment_clicks(db: Session, url_id: int) -> None:
    """Increment click count for a URL"""
    url = db.query(URLModel).filter(URLModel.id == url_id).first()
    if url:
        url.clicks += 1
        db.commit()

def get_all_urls(db: Session, skip: int = 0, limit: int = 10):
    """Get all URLs with pagination"""
    return db.query(URLModel).offset(skip).limit(limit).all()

def delete_url(db: Session, short_code: str) -> bool:
    """Delete a shortened URL"""
    url = db.query(URLModel).filter(URLModel.short_code == short_code).first()
    if url:
        db.delete(url)
        db.commit()
        return True
    return False

def update_url(db: Session, short_code: str, original_url: str) -> URLModel:
    """Update original URL"""
    url = db.query(URLModel).filter(URLModel.short_code == short_code).first()
    if url:
        if not is_valid_url(original_url):
            raise ValueError("Invalid URL format")
        url.original_url = original_url
        db.commit()
        db.refresh(url)
        return url
    return None
