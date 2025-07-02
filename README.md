# 🏹 Forest Hunter Game

A classic Pac-Man style game set in a beautiful forest environment where you play as a hunter collecting deer while avoiding wolves. Built with Python and Pygame.

![Forest Hunter](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Pygame](https://img.shields.io/badge/Pygame-2.0+-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🎮 Game Features

- **🦌 Realistic Wildlife**: Detailed deer and wolf sprites with proper animal features
- **🏔️ Mountain Adventure**: Progress through different forest levels on a mountain
- **🔫 Rifle Combat**: Collect and use realistic rifles to defend against wolves
- **🏆 Dynamic Scoring**: Level-based bonus points and competitive leaderboard system
- **🎯 Step-by-Step Movement**: Precise grid-based movement for strategic gameplay
- **🌲 Beautiful Graphics**: Detailed forest environments with stable, non-flashing visuals
- **🎵 Retro Style**: Cartoon-style fonts and mountain background welcome screen

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- Pygame 2.0 or higher

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/forest-hunter-game.git
   cd forest-hunter-game
   ```

2. **Install Pygame:**
   ```bash
   pip install pygame
   ```

3. **Run the game:**
   ```bash
   python forest_hunter_game.py
   ```

4. **Test features (optional):**
   ```bash
   python test_game_features.py
   ```

## 🎯 How to Play

### Controls
- **WASD** or **Arrow Keys**: Move the hunter one step at a time
- **SPACEBAR**: Fire your rifle at wolves (NOT deer!)
- **Space**: Start game / Continue to next level
- **R**: Restart after game over
- **Type name + ENTER**: Submit name for high score

### Objective
- **🦌 COLLECT deer** by walking into them (required amount increases each level)
- **🐺 AVOID wolves** that roam the forest (they move very slowly)
- **🔫 USE rifles** to shoot wolves from a distance
- **🛡️ PROTECT wildlife** - never shoot deer or the game ends!
- **🏆 ACHIEVE high scores** - compete for the top 10 leaderboard!

### ⚠️ Important Rules
- **COLLECT deer by walking into them** - this is how you progress
- **SHOOT wolves with rifles** - they are dangerous predators  
- **DON'T shoot deer** - this will end the game immediately!
- **Wolves move very slowly** - you have plenty of time to plan

## 🏆 Scoring System

### Point Values
- **Deer Collection**: 10 + (level × 5) points
  - Level 1: 15 points per deer
  - Level 2: 20 points per deer
  - Level 3: 25 points per deer, etc.
- **Wolf Kill**: 50 + (level × 10) + (number of wolves × 5) points
- **Level Completion Bonus**: 100 × level + (deer needed × 20) points

### Leaderboard
- **Top 10 Scores**: Persistent leaderboard saved locally
- **Name Entry**: Enter your name for high scores
- **Real-time Display**: Current and top scores shown during gameplay

## 🎨 Game Elements

### 🏹 Hunter (Man with Deerstalker Hat)
- Detailed character with brown coat and distinctive deerstalker hat
- Realistic rifle appears in hand when carrying a weapon
- Direction-based rifle positioning

### 🦌 Deer (Realistic Wildlife)
- Detailed deer graphics with brown body, antlers, legs, and hooves
- Golden glow effect to indicate they're collectible
- Must be collected by walking - shooting them ends the game!

### 🐺 Wolves (Enhanced Realistic Sprites)
- Much slower movement (every 2 seconds) - very manageable
- Detailed appearance with snout, ears, tail, and four paws
- Red, orange, purple, pink colored wolves with glowing red eyes
- Move intelligently toward the hunter

### 🔫 Rifles (Realistic Weapons)
- Detailed rifle graphics with barrel, stock, trigger guard, and scope
- Yellow glow effect makes them easy to spot
- Last for 10 seconds when picked up
- Fire yellow bullets with spacebar

## 🌲 Forest Environments

- **Level 1**: Sparse Forest - Open areas with scattered trees
- **Level 2**: Dense Forest - Thick tree coverage with clearings  
- **Level 3**: Winding Paths - Maze-like forest trails
- **Level 4+**: Wild Forest - Challenging layouts

## 📁 Project Structure

```
forest-hunter-game/
├── forest_hunter_game.py      # Main game file
├── test_game_features.py      # Feature testing script
├── README.md                  # This file
├── README_ForestHunter.md     # Detailed game documentation
├── .gitignore                 # Git ignore file
└── forest_hunter_scores.json  # Leaderboard data (created automatically)
```

## 🛠️ Technical Details

- **Language**: Python 3.7+
- **Graphics**: Pygame 2.0+
- **Resolution**: 1000x800 pixels
- **Frame Rate**: 60 FPS
- **Movement**: Step-by-step grid-based
- **AI**: Simple pathfinding for wolves
- **Storage**: JSON file for leaderboard persistence

## 🎯 Game Strategy Tips

1. **Score Maximization**: Focus on reaching higher levels for maximum bonus points
2. **Deer Priority**: Collect deer efficiently to unlock level completion bonuses
3. **Rifle Strategy**: Only use rifles on wolves - never on deer!
4. **Wolf Management**: Use rifles to clear paths when wolves block deer
5. **Safety First**: Don't risk shooting deer - game over means no leaderboard entry!

## 🐛 Known Issues

- None currently reported

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎮 Screenshots

*Screenshots coming soon!*

## 🔄 Version History

- **v1.0.0** - Initial release with basic gameplay
- **v2.0.0** - Added realistic graphics and improved wolf AI
- **v3.0.0** - Added rifle combat system and bullet mechanics
- **v4.0.0** - Added dynamic scoring and leaderboard system

## 🙏 Acknowledgments

- Built with Python and Pygame
- Inspired by classic Pac-Man gameplay
- Wildlife protection theme promotes responsible hunting ethics

---

**Enjoy hunting in the forest! 🏔️🦌🔫🐺🏆**

*Remember: Collect deer, shoot wolves, protect wildlife, and aim for the top score!*
