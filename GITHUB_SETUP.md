# 🚀 GitHub Setup Instructions

Follow these steps to get your Forest Hunter Game on GitHub and set up automatic syncing.

## Step 1: Create GitHub Repository

1. **Go to [GitHub.com](https://github.com)** and sign in
2. **Click the "+" icon** in the top right corner
3. **Select "New repository"**
4. **Fill in the details:**
   - Repository name: `forest-hunter-game`
   - Description: `A classic Pac-Man style forest hunting game with realistic graphics, dynamic scoring, and leaderboards`
   - Make it **Public** (so others can see your game)
   - **DON'T** check "Add a README file" (we already have one)
5. **Click "Create repository"**

## Step 2: Connect Your Local Repository

After creating the repository, GitHub will show you some commands. Use these instead:

```bash
# Navigate to your game directory
cd /Users/leonglover/forest-hunter-game

# Add your GitHub repository as the remote origin
git remote add origin https://github.com/YOUR_USERNAME/forest-hunter-game.git

# Push your code to GitHub
git branch -M main
git push -u origin main
```

**🔥 IMPORTANT: Replace `YOUR_USERNAME` with your actual GitHub username!**

## Step 3: Update Your Email (Optional but Recommended)

```bash
# Set your email for this repository
git config user.email "your-actual-email@example.com"

# Or set it globally for all repositories
git config --global user.email "your-actual-email@example.com"
```

## Step 4: Verify Everything Works

```bash
# Check your remote repository
git remote -v

# Check your recent commits
git log --oneline -5
```

## 🔄 Future Updates - Easy Syncing

### Option 1: Use the Sync Script (Recommended)
```bash
./sync_to_github.sh
```

### Option 2: Use the Development Workflow
```bash
./dev_workflow.sh
```
Then choose option 4 to sync to GitHub.

### Option 3: Manual Git Commands
```bash
git add .
git commit -m "Your update message"
git push origin main
```

## 🏷️ Creating Releases

When you want to create a new version:

```bash
# Create and push a new version tag
git tag -a v4.1.0 -m "Version 4.1.0 - Added new features"
git push origin v4.1.0
```

Or use the development workflow script (option 7).

## 📁 Repository Structure

Your GitHub repository will contain:

```
forest-hunter-game/
├── forest_hunter_game.py      # Main game file
├── test_game_features.py      # Feature testing
├── README.md                  # Main documentation
├── README_ForestHunter.md     # Detailed game guide
├── LICENSE                    # MIT License
├── .gitignore                 # Git ignore rules
├── sync_to_github.sh          # Easy sync script
├── dev_workflow.sh            # Development menu
└── GITHUB_SETUP.md            # This file
```

## 🎯 What Gets Synced

- ✅ All game code and updates
- ✅ Documentation changes
- ✅ New features and bug fixes
- ❌ Score files (ignored by .gitignore)
- ❌ Python cache files (ignored by .gitignore)

## 🔧 Troubleshooting

### Authentication Issues
If you get authentication errors, you may need to:
1. Set up a Personal Access Token on GitHub
2. Use SSH keys instead of HTTPS
3. Check GitHub's authentication documentation

### Permission Denied
```bash
# Make sure scripts are executable
chmod +x sync_to_github.sh
chmod +x dev_workflow.sh
```

### Wrong Remote URL
```bash
# Check current remote
git remote -v

# Update remote URL if needed
git remote set-url origin https://github.com/YOUR_USERNAME/forest-hunter-game.git
```

## 🎉 Success!

Once set up, you can:
- 🌐 View your game at: `https://github.com/YOUR_USERNAME/forest-hunter-game`
- 🚀 Easily sync updates with `./sync_to_github.sh`
- 🏷️ Create releases and versions
- 📊 Track your development history
- 🤝 Allow others to contribute or fork your game

**Happy coding and hunting! 🏹🦌🐺**
