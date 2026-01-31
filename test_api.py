#!/usr/bin/env python3
"""
URL Shortener API Test Script
Tests all CRUD operations
"""

import requests
import json
from time import sleep

BASE_URL = "http://127.0.0.1:8000"

def test_create():
    """Test CREATE - POST /api/shorten"""
    print("\n" + "="*50)
    print("TEST 1: CREATE - POST /api/shorten")
    print("="*50)
    
    data = {
        "original_url": "https://www.google.com/search?q=fastapi",
        "custom_alias": "google"
    }
    
    response = requests.post(f"{BASE_URL}/api/shorten", json=data)
    print(f"Status: {response.status_code}")
    print(f"Response:\n{json.dumps(response.json(), indent=2)}")
    
    return response.json()

def test_read_all(url_data):
    """Test READ - GET /api/urls"""
    print("\n" + "="*50)
    print("TEST 2: READ ALL - GET /api/urls")
    print("="*50)
    
    response = requests.get(f"{BASE_URL}/api/urls")
    print(f"Status: {response.status_code}")
    print(f"Response:\n{json.dumps(response.json(), indent=2)}")

def test_read_info(short_code):
    """Test READ - GET /api/info/{short_code}"""
    print("\n" + "="*50)
    print(f"TEST 3: GET INFO - GET /api/info/{short_code}")
    print("="*50)
    
    response = requests.get(f"{BASE_URL}/api/info/{short_code}")
    print(f"Status: {response.status_code}")
    print(f"Response:\n{json.dumps(response.json(), indent=2)}")

def test_redirect(short_code):
    """Test REDIRECT - GET /{short_code}"""
    print("\n" + "="*50)
    print(f"TEST 4: REDIRECT - GET /{short_code}")
    print("="*50)
    
    response = requests.get(f"{BASE_URL}/{short_code}", allow_redirects=False)
    print(f"Status: {response.status_code}")
    print(f"Location: {response.headers.get('location', 'N/A')}")
    print("(Should redirect to original URL)")

def test_analytics(short_code):
    """Test ANALYTICS - GET /api/analytics/{short_code}"""
    print("\n" + "="*50)
    print(f"TEST 5: ANALYTICS - GET /api/analytics/{short_code}")
    print("="*50)
    
    response = requests.get(f"{BASE_URL}/api/analytics/{short_code}")
    print(f"Status: {response.status_code}")
    print(f"Response:\n{json.dumps(response.json(), indent=2)}")

def test_update(short_code):
    """Test UPDATE - PUT /api/urls/{short_code}"""
    print("\n" + "="*50)
    print(f"TEST 6: UPDATE - PUT /api/urls/{short_code}")
    print("="*50)
    
    data = {
        "original_url": "https://github.com",
    }
    
    response = requests.put(f"{BASE_URL}/api/urls/{short_code}", json=data)
    print(f"Status: {response.status_code}")
    print(f"Response:\n{json.dumps(response.json(), indent=2)}")

def test_delete(short_code):
    """Test DELETE - DELETE /api/urls/{short_code}"""
    print("\n" + "="*50)
    print(f"TEST 7: DELETE - DELETE /api/urls/{short_code}")
    print("="*50)
    
    response = requests.delete(f"{BASE_URL}/api/urls/{short_code}")
    print(f"Status: {response.status_code}")
    print(f"Response:\n{json.dumps(response.json(), indent=2)}")

def test_health():
    """Test Health Check"""
    print("\n" + "="*50)
    print("TEST 0: HEALTH CHECK - GET /health")
    print("="*50)
    
    response = requests.get(f"{BASE_URL}/health")
    print(f"Status: {response.status_code}")
    print(f"Response:\n{json.dumps(response.json(), indent=2)}")

if __name__ == "__main__":
    print("\n🚀 URL Shortener API - Comprehensive Test")
    
    try:
        # Test health
        test_health()
        
        # Test CREATE
        url_data = test_create()
        short_code = url_data.get("short_code")
        
        # Test READ ALL
        test_read_all(url_data)
        
        # Test READ INFO
        test_read_info(short_code)
        
        # Test REDIRECT (click tracking)
        test_redirect(short_code)
        
        # Test ANALYTICS
        test_analytics(short_code)
        
        # Test UPDATE
        test_update(short_code)
        
        # Test ANALYTICS again (to verify update)
        test_analytics(short_code)
        
        # Test DELETE
        test_delete(short_code)
        
        print("\n" + "="*50)
        print("✅ All tests completed!")
        print("="*50 + "\n")
        
    except requests.exceptions.ConnectionError:
        print("❌ ERROR: Could not connect to server.")
        print("Make sure the server is running: uvicorn main:app --reload")
    except Exception as e:
        print(f"❌ ERROR: {str(e)}")
