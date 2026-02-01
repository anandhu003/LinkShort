#!/bin/bash

# Stop and remove containers
echo "🛑 Stopping containers..."
docker-compose down

# Remove images
echo "🗑️ Removing images..."
docker rmi linkshort-linkshort -f

echo "✅ Cleanup complete"
