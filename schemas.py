from pydantic import BaseModel, HttpUrl
from typing import Optional
from datetime import datetime

class URLCreate(BaseModel):
    original_url: str
    custom_alias: Optional[str] = None
    expires_at: Optional[datetime] = None

class URLResponse(BaseModel):
    id: int
    original_url: str
    short_code: str
    custom_alias: Optional[str]
    clicks: int
    created_at: datetime
    expires_at: Optional[datetime]
    is_active: bool
    
    class Config:
        from_attributes = True

class URLUpdate(BaseModel):
    original_url: str
    expires_at: Optional[datetime] = None
