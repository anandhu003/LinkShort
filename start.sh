#!/bin/bash

# LinkShort - Docker Setup Script

echo "🚀 LinkShort - Docker Setup"
echo "================================"

# Check Docker
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed. Please install Docker first."
    exit 1
fi

echo "✅ Docker found"

# Check Docker Compose
if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose is not installed. Please install Docker Compose first."
    exit 1
fi

echo "✅ Docker Compose found"

echo ""
echo "📦 Building Docker image..."
docker-compose build

echo ""
echo "🎯 Starting LinkShort..."
docker-compose up

echo ""
echo "✨ LinkShort is running!"
echo "📱 Access at: http://localhost:8000"
echo "📚 API Docs: http://localhost:8000/docs"
