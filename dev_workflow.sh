#!/bin/bash

# Forest Hunter Game - Development Workflow Script
# Helps with common development tasks

echo "🏹 Forest Hunter Game - Development Workflow"
echo "==========================================="

show_menu() {
    echo ""
    echo "Choose an option:"
    echo "1. 🎮 Run the game"
    echo "2. 🧪 Run tests"
    echo "3. 📊 Check git status"
    echo "4. 🚀 Sync to GitHub"
    echo "5. 📝 View README"
    echo "6. 🏆 View current leaderboard"
    echo "7. 🔄 Create new version"
    echo "8. ❌ Exit"
    echo ""
}

while true; do
    show_menu
    read -p "Enter your choice (1-8): " choice
    
    case $choice in
        1)
            echo "🎮 Starting Forest Hunter Game..."
            python3 forest_hunter_game.py
            ;;
        2)
            echo "🧪 Running tests..."
            python3 test_game_features.py
            ;;
        3)
            echo "📊 Git status:"
            git status
            ;;
        4)
            echo "🚀 Syncing to GitHub..."
            ./sync_to_github.sh
            ;;
        5)
            echo "📝 Opening README..."
            cat README.md
            ;;
        6)
            echo "🏆 Current leaderboard:"
            if [ -f "forest_hunter_scores.json" ]; then
                cat forest_hunter_scores.json
            else
                echo "No scores yet - play the game to create leaderboard!"
            fi
            ;;
        7)
            echo "🔄 Creating new version..."
            echo "Current version tags:"
            git tag
            echo ""
            read -p "Enter new version (e.g., v4.1.0): " version
            read -p "Enter version description: " description
            git tag -a "$version" -m "$description"
            git push origin "$version"
            echo "✅ Version $version created and pushed to GitHub!"
            ;;
        8)
            echo "👋 Goodbye! Happy hunting!"
            exit 0
            ;;
        *)
            echo "❌ Invalid option. Please choose 1-8."
            ;;
    esac
    
    echo ""
    read -p "Press Enter to continue..."
done
