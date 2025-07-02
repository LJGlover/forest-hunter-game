# 🏹 Forest Hunter Game
+      2: 
+      3: A classic Pac-Man style game set in a beautiful forest environment where you play as a hunter collecting deer while avoiding wolves. Built with Python and Pygame.
+      4: 
+      5: ![Forest Hunter](https://img.shields.io/badge/Python-3.7+-blue.svg)
+      6: ![Pygame](https://img.shields.io/badge/Pygame-2.0+-green.svg)
+      7: ![License](https://img.shields.io/badge/License-MIT-yellow.svg)
+      8: 
+      9: ## 🎮 Game Features
+     10: 
+     11: - **🦌 Realistic Wildlife**: Detailed deer and wolf sprites with proper animal features
+     12: - **🏔️ Mountain Adventure**: Progress through different forest levels on a mountain
+     13: - **🔫 Rifle Combat**: Collect and use realistic rifles to defend against wolves
+     14: - **🏆 Dynamic Scoring**: Level-based bonus points and competitive leaderboard system
+     15: - **🎯 Step-by-Step Movement**: Precise grid-based movement for strategic gameplay
+     16: - **🌲 Beautiful Graphics**: Detailed forest environments with stable, non-flashing visuals
+     17: - **🎵 Retro Style**: Cartoon-style fonts and mountain background welcome screen
+     18: 
+     19: ## 🚀 Quick Start
+     20: 
+     21: ### Prerequisites
+     22: - Python 3.7 or higher
+     23: - Pygame 2.0 or higher
+     24: 
+     25: ### Installation
+     26: 
+     27: 1. **Clone the repository:**
+     28:    ```bash
+     29:    git clone https://github.com/yourusername/forest-hunter-game.git
+     30:    cd forest-hunter-game
+     31:    ```
+     32: 
+     33: 2. **Install Pygame:**
+     34:    ```bash
+     35:    pip install pygame
+     36:    ```
+     37: 
+     38: 3. **Run the game:**
+     39:    ```bash
+     40:    python forest_hunter_game.py
+     41:    ```
+     42: 
+     43: 4. **Test features (optional):**
+     44:    ```bash
+     45:    python test_game_features.py
+     46:    ```
+     47: 
+     48: ## 🎯 How to Play
+     49: 
+     50: ### Controls
+     51: - **WASD** or **Arrow Keys**: Move the hunter one step at a time
+     52: - **SPACEBAR**: Fire your rifle at wolves (NOT deer!)
+     53: - **Space**: Start game / Continue to next level
+     54: - **R**: Restart after game over
+     55: - **Type name + ENTER**: Submit name for high score
+     56: 
+     57: ### Objective
+     58: - **🦌 COLLECT deer** by walking into them (required amount increases each level)
+     59: - **🐺 AVOID wolves** that roam the forest (they move very slowly)
+     60: - **🔫 USE rifles** to shoot wolves from a distance
+     61: - **🛡️ PROTECT wildlife** - never shoot deer or the game ends!
+     62: - **🏆 ACHIEVE high scores** - compete for the top 10 leaderboard!
+     63: 
+     64: ### ⚠️ Important Rules
+     65: - **COLLECT deer by walking into them** - this is how you progress
+     66: - **SHOOT wolves with rifles** - they are dangerous predators  
+     67: - **DON'T shoot deer** - this will end the game immediately!
+     68: - **Wolves move very slowly** - you have plenty of time to plan
+     69: 
+     70: ## 🏆 Scoring System
+     71: 
+     72: ### Point Values
+     73: - **Deer Collection**: 10 + (level × 5) points
+     74:   - Level 1: 15 points per deer
+     75:   - Level 2: 20 points per deer
+     76:   - Level 3: 25 points per deer, etc.
+     77: - **Wolf Kill**: 50 + (level × 10) + (number of wolves × 5) points
+     78: - **Level Completion Bonus**: 100 × level + (deer needed × 20) points
+     79: 
+     80: ### Leaderboard
+     81: - **Top 10 Scores**: Persistent leaderboard saved locally
+     82: - **Name Entry**: Enter your name for high scores
+     83: - **Real-time Display**: Current and top scores shown during gameplay
+     84: 
+     85: ## 🎨 Game Elements
+     86: 
+     87: ### 🏹 Hunter (Man with Deerstalker Hat)
+     88: - Detailed character with brown coat and distinctive deerstalker hat
+     89: - Realistic rifle appears in hand when carrying a weapon
+     90: - Direction-based rifle positioning
+     91: 
+     92: ### 🦌 Deer (Realistic Wildlife)
+     93: - Detailed deer graphics with brown body, antlers, legs, and hooves
+     94: - Golden glow effect to indicate they're collectible
+     95: - Must be collected by walking - shooting them ends the game!
+     96: 
+     97: ### 🐺 Wolves (Enhanced Realistic Sprites)
+     98: - Much slower movement (every 2 seconds) - very manageable
+     99: - Detailed appearance with snout, ears, tail, and four paws
+    100: - Red, orange, purple, pink colored wolves with glowing red eyes
+    101: - Move intelligently toward the hunter
+    102: 
+    103: ### 🔫 Rifles (Realistic Weapons)
+    104: - Detailed rifle graphics with barrel, stock, trigger guard, and scope
+    105: - Yellow glow effect makes them easy to spot
+    106: - Last for 10 seconds when picked up
+    107: - Fire yellow bullets with spacebar
+    108: 
+    109: ## 🌲 Forest Environments
+    110: 
+    111: - **Level 1**: Sparse Forest - Open areas with scattered trees
+    112: - **Level 2**: Dense Forest - Thick tree coverage with clearings  
+    113: - **Level 3**: Winding Paths - Maze-like forest trails
+    114: - **Level 4+**: Wild Forest - Challenging layouts
+    115: 
+    116: ## 📁 Project Structure
+    117: 
+    118: ```
+    119: forest-hunter-game/
+    120: ├── forest_hunter_game.py      # Main game file
+    121: ├── test_game_features.py      # Feature testing script
+    122: ├── README.md                  # This file
+    123: ├── README_ForestHunter.md     # Detailed game documentation
+    124: ├── .gitignore                 # Git ignore file
+    125: └── forest_hunter_scores.json  # Leaderboard data (created automatically)
+    126: ```
+    127: 
+    128: ## 🛠️ Technical Details
+    129: 
+    130: - **Language**: Python 3.7+
+    131: - **Graphics**: Pygame 2.0+
+    132: - **Resolution**: 1000x800 pixels
+    133: - **Frame Rate**: 60 FPS
+    134: - **Movement**: Step-by-step grid-based
+    135: - **AI**: Simple pathfinding for wolves
+    136: - **Storage**: JSON file for leaderboard persistence
+    137: 
+    138: ## 🎯 Game Strategy Tips
+    139: 
+    140: 1. **Score Maximization**: Focus on reaching higher levels for maximum bonus points
+    141: 2. **Deer Priority**: Collect deer efficiently to unlock level completion bonuses
+    142: 3. **Rifle Strategy**: Only use rifles on wolves - never on deer!
+    143: 4. **Wolf Management**: Use rifles to clear paths when wolves block deer
+    144: 5. **Safety First**: Don't risk shooting deer - game over means no leaderboard entry!
+    145: 
+    146: ## 🐛 Known Issues
+    147: 
+    148: - None currently reported
+    149: 
+    150: ## 🤝 Contributing
+    151: 
+    152: Contributions are welcome! Please feel free to submit a Pull Request.
+    153: 
+    154: 1. Fork the project
+    155: 2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
+    156: 3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
+    157: 4. Push to the branch (`git push origin feature/AmazingFeature`)
+    158: 5. Open a Pull Request
+    159: 
+    160: ## 📝 License
+    161: 
+    162: This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
+    163: 
+    164: ## 🎮 Screenshots
+    165: 
+    166: *Screenshots coming soon!*
+    167: 
+    168: ## 🔄 Version History
+    169: 
+    170: - **v1.0.0** - Initial release with basic gameplay
+    171: - **v2.0.0** - Added realistic graphics and improved wolf AI
+    172: - **v3.0.0** - Added rifle combat system and bullet mechanics
+    173: - **v4.0.0** - Added dynamic scoring and leaderboard system
+    174: 
+    175: ## 🙏 Acknowledgments
+    176: 
+    177: - Built with Python and Pygame
+    178: - Inspired by classic Pac-Man gameplay
+    179: - Wildlife protection theme promotes responsible hunting ethics
+    180: 
+    181: ---
+    182: 
+    183: **Enjoy hunting in the forest! 🏔️🦌🔫🐺🏆**
+    184: 
+    185: *Remember: Collect deer, shoot wolves, protect wildlife, and aim for the top score!*# forest-hunter-game
A vibe-coded retro Pac-Man maze game where the hunter has to kill wolves and collect deer. The game is set in forest worlds on a mountain. It includes dynamic scoring, realistic graphics, and an arcade-style leaderboard. 
