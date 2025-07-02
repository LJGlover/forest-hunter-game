#!/bin/bash

# Forest Hunter Game - GitHub Sync Script
# Run this script whenever you want to sync changes to GitHub

echo "🏹 Forest Hunter Game - GitHub Sync"
echo "=================================="

# Check if we're in the right directory
if [ ! -f "forest_hunter_game.py" ]; then
    echo "❌ Error: Please run this script from the forest-hunter-game directory"
    exit 1
fi

# Add all changes
echo "📁 Adding all changes..."
git add .

# Check if there are any changes to commit
if git diff --staged --quiet; then
    echo "✅ No changes to commit"
    exit 0
fi

# Get commit message from user
echo "💬 Enter commit message (or press Enter for default):"
read -r commit_message

if [ -z "$commit_message" ]; then
    commit_message="Update Forest Hunter Game - $(date '+%Y-%m-%d %H:%M:%S')"
fi

# Commit changes
echo "💾 Committing changes..."
git commit -m "$commit_message"

# Push to GitHub
echo "🚀 Pushing to GitHub..."
git push origin main

echo "✅ Successfully synced to GitHub!"
echo "🌐 View your repository at: https://github.com/YOUR_USERNAME/forest-hunter-game"
