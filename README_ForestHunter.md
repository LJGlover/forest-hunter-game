# Forest Hunter Game

A classic Pac-Man style game set in a forest environment where you play as a hunter collecting deer while avoiding wolves.

## Latest Improvements ✨

- **DYNAMIC SCORING SYSTEM**: Real-time score updates with bonus points for higher levels
- **TOP SCORE TRACKING**: Current and top scores displayed at top of screen during gameplay
- **TOP 10 LEADERBOARD**: Persistent leaderboard with player name entry for high scores
- **BONUS POINT SYSTEM**: Enhanced scoring for deer, wolves, and level completion
- **MUCH Slower Wolves**: Wolves now move every 120 frames (2 seconds) - extremely manageable!
- **Realistic Deer Graphics**: Detailed deer with body, head, antlers, legs, hooves, and tail
- **Deer Protection Rule**: Game ends if you accidentally shoot a deer - you must COLLECT them by walking!
- **Enhanced Game Over**: Shows specific reason for game ending with helpful messages
- **Realistic Rifles**: Guns now look like proper rifles with barrels, stocks, scopes, and trigger guards
- **Spacebar Firing**: Press SPACEBAR to fire your rifle and shoot bullets at wolves
- **Visible Rifle in Hand**: When hunter has a rifle, it's clearly visible in their hand facing the movement direction
- **Bullet System**: Yellow bullets travel across the screen and kill wolves on contact
- **Enhanced Wolf Graphics**: More realistic and detailed wolf sprites with proper animal features
- **Mountain Welcome Screen**: Beautiful mountain background with forest level map
- **Retro Cartoon Styling**: Large, outlined fonts with golden title and pulsing effects

## Game Features

- **Dynamic Scoring**: Real-time score updates with level-based bonuses
- **Leaderboard System**: Top 10 high scores with player names
- **Detailed Characters**: Hunter appears as a man wearing a deerstalker hat, wolves look like realistic animals
- **Realistic Wildlife**: Deer have detailed graphics with prominent antlers, body, legs, and hooves
- **Forest Theme**: Navigate through detailed forest mazes with clear trees and forest paths
- **Step-by-Step Movement**: Precise control with one step per key press
- **Wildlife Protection**: Must collect deer by walking - shooting them ends the game!
- **Rifle Combat**: Collect rifles and use spacebar to fire bullets at wolves only
- **Progressive Difficulty**: Each level increases deer requirements and introduces new challenges
- **Wolf AI**: Intelligent wolves that hunt the player and emerge from caves (now at very slow, manageable speed)
- **Weapon System**: Collect realistic rifles to defend yourself against wolves
- **Multiple Levels**: Different forest layouts as you progress up the mountain

## How to Play

### Controls
- **WASD** or **Arrow Keys**: Move the hunter one step at a time
- **SPACEBAR**: Fire your rifle at wolves (NOT deer!)
- **Space**: Start game / Continue to next level
- **R**: Restart after game over
- **Type name + ENTER**: Submit name for high score

### Scoring System 🏆

#### Dynamic Score Display
- **Current Score**: Displayed in gold at top-left of screen
- **Top Score**: Displayed in white at top-center of screen
- **Level**: Displayed in green at top-right of screen
- **Real-time Updates**: Score updates immediately when points are earned

#### Point Values
- **Deer Collection**: 10 + (level × 5) points
  - Level 1: 15 points per deer
  - Level 2: 20 points per deer
  - Level 3: 25 points per deer, etc.
- **Wolf Kill**: 50 + (level × 10) + (number of wolves × 5) points
  - Base 50 points + level bonus + difficulty bonus
  - Higher levels and more wolves = more points
- **Level Completion Bonus**: 100 × level + (deer needed × 20) points
  - Level 1: 100 + (5 × 20) = 200 bonus points
  - Level 2: 200 + (8 × 20) = 360 bonus points
  - Level 3: 300 + (11 × 20) = 520 bonus points, etc.

#### Leaderboard System
- **Top 10 Scores**: Persistent leaderboard saved to file
- **Name Entry**: Enter your name for high scores
- **Score Tracking**: Shows rank, name, score, and level reached
- **Highlighted Entry**: Your current score highlighted in gold
- **Automatic Saving**: Scores saved automatically to `forest_hunter_scores.json`

### Important Rules ⚠️
- **COLLECT deer by walking into them** - this is how you progress
- **SHOOT wolves with rifles** - they are dangerous predators
- **DON'T shoot deer** - this will end the game immediately!
- **Wolves move very slowly** - you have plenty of time to plan
- **Higher levels = more bonus points** - risk vs reward!

### Combat System
- **Rifle Collection**: Pick up rifles scattered throughout the forest
- **Firing**: Press SPACEBAR to shoot bullets in the direction you're facing
- **Target Wolves Only**: Only shoot at wolves - shooting deer ends the game!
- **Bullet Travel**: Yellow bullets travel across the screen
- **Wolf Elimination**: Bullets kill wolves on contact
- **Rifle Duration**: Rifles last for 10 seconds (600 frames)
- **Auto-Respawn**: New wolves spawn from caves when others are killed

### Movement System
- **Step-by-Step**: Each key press moves the hunter exactly one grid space
- **Precise Control**: No continuous movement - plan each step carefully
- **Direction Facing**: Hunter and rifle face the direction of movement

### Objective
- **Collect deer** by walking into them (required amount increases each level)
- **Avoid wolves** that roam the forest (they move very slowly now)
- **Use rifles** to shoot wolves from a distance
- **Protect wildlife** - never shoot deer!
- **Achieve high scores** - compete for the top 10 leaderboard!
- **Survive** and progress through increasingly difficult levels

### Game Elements

#### Hunter (Man with Deerstalker Hat)
- Detailed character with brown coat and distinctive deerstalker hat
- **Realistic rifle appears in hand** when carrying a weapon
- **Direction-based rifle positioning** (rifle points where hunter faces)
- Faces the direction of movement
- Starts at position (1,1) in each level

#### Deer (Realistic Wildlife) 🦌
- **Detailed deer graphics**: Brown body with tan belly, realistic proportions
- **Prominent antlers**: Multi-branched antlers clearly visible
- **Four legs with hooves**: Realistic leg positioning and black hooves
- **Head with eyes and nose**: Detailed facial features
- **Tail**: Small deer tail
- **Golden glow**: Subtle glow effect to indicate they're collectible
- **COLLECT ONLY**: Walk into them to collect - shooting them ends the game!
- **Dynamic Scoring**: Points increase with level (10 + level × 5)
- Required amount increases each level (5, 8, 11, 14...)

#### Rifles (Realistic Weapons)
- **Detailed rifle graphics**: Barrel, wooden stock, trigger guard, scope
- **Highly visible**: Yellow glow effect makes them easy to spot in the maze
- **Realistic appearance**: Look like proper hunting rifles
- **Direction-aware**: Rifle in hunter's hand points in movement direction
- Last for 10 seconds when picked up
- Fire yellow bullets with spacebar

#### Wolves (Enhanced Realistic Sprites)
- **MUCH Slower Movement**: Now move every 120 frames (2 seconds) - extremely manageable!
- **Detailed Appearance**: Proper wolf anatomy with snout, ears, tail, and four paws
- **Directional Sprites**: Wolf head and features orient based on movement direction
- **Enhanced Features**: Body shadows, paw pads, and realistic proportions
- **Red, Orange, Purple, Pink** colored wolves hunt you
- **Red glowing eyes** for intimidation
- Move intelligently toward the hunter (very slowly)
- **Dynamic Scoring**: Points increase with level and difficulty
- Can be killed by rifle bullets
- When killed, a new wolf spawns from a cave
- Always maintain 4+ wolves in the game

#### Scoring Display
- **Top Score Bar**: Always visible at top of screen during gameplay
- **Current Score**: Gold text showing your current points with comma formatting
- **Top Score**: White text showing the highest score achieved
- **Level Display**: Green text showing current level
- **Real-time Updates**: Score updates immediately when points are earned

#### Leaderboard Features
- **High Score Detection**: Automatically detects when you achieve a top 10 score
- **Name Entry Screen**: Type your name (up to 15 characters) and press ENTER
- **Top 10 Display**: Shows rank, name, score, and level for top 10 players
- **Current Player Highlight**: Your score highlighted in gold on the leaderboard
- **Persistent Storage**: Scores saved to JSON file and loaded on game start

#### Game Over System
- **Name Entry**: Prompted to enter name for high scores
- **Specific reasons**: Shows why the game ended
- **Deer protection message**: Special warning if you shot a deer
- **Helpful reminders**: Instructions on proper deer collection
- **Wolf attack message**: Different message for wolf encounters
- **Full Leaderboard**: Shows complete top 10 after game ends

#### Welcome Screen Features
- **Mountain Background**: Beautiful layered mountain scenery
- **Forest Level Map**: Visual indicators showing different forest types on the mountain
- **Retro Cartoon Fonts**: Large, outlined golden title with shadow effects
- **Pulsing Start Text**: Animated "Press SPACE" instruction
- **Updated Instructions**: Clear rules about deer collection vs wolf shooting
- **Level Indicators**: Shows Forest 1 (Sparse), Forest 2 (Dense), Forest 3 (Winding), Forest 4+ (Wild)

#### Forest Environment
- **Stable Visuals**: No flashing or random color changes
- **Clear Trees**: Detailed trees with trunks and canopies
- **Forest Paths**: Dirt paths with grass patches
- **Level Variation**: Different forest types (sparse, dense, winding)

#### Caves (Black Circles)
- Wolf spawn points
- Located in dead ends and corners
- New wolves emerge when others are killed

### Level Progression
- Each level has a different forest layout
- Deer requirement increases by 3 each level
- **Bonus points increase with level** - higher risk, higher reward!
- Forest appearance changes (sparse, dense, winding paths)
- Represents climbing higher up the mountain

## Scoring Strategy 💰

### Maximize Your Score
1. **Focus on Higher Levels**: Bonus points increase significantly with each level
2. **Efficient Deer Collection**: Plan routes to collect deer quickly for level bonuses
3. **Strategic Wolf Elimination**: More wolves on screen = higher points per kill
4. **Level Completion Bonuses**: Complete levels for massive bonus points
5. **Risk vs Reward**: Higher levels are harder but offer much better scoring

### Point Optimization Tips
- **Deer Strategy**: Collect deer efficiently to reach level bonuses faster
- **Wolf Management**: Let wolves accumulate for higher kill bonuses (but stay safe!)
- **Level Progression**: Push for higher levels where all points are multiplied
- **Rifle Usage**: Use rifles strategically to maximize wolf kill bonuses
- **Safety First**: Don't risk shooting deer - game over means no leaderboard entry!

## Wildlife Protection Rules 🦌

### What You MUST Do:
1. **Collect deer by walking into them** - this is the only way to progress
2. **Shoot wolves with rifles** - they are dangerous predators
3. **Protect wildlife** - deer are to be collected, not harmed

### What Ends the Game:
1. **Shooting a deer** - Game over with wildlife protection message
2. **Being caught by a wolf** - Game over with predator attack message

### Important Reminders:
- Deer have golden glow to show they're collectible
- Rifles are for wolves only
- Walking into deer collects them safely
- Shooting deer violates wildlife protection rules

## Combat Strategy

### Rifle Usage
1. **Collect Rifles**: Look for detailed rifle graphics with yellow glow
2. **Target Wolves Only**: Never aim at deer - this ends the game!
3. **Positioning**: Face the direction you want to shoot before firing
4. **Timing**: Rifles last 10 seconds - use them wisely
5. **Range Combat**: Shoot wolves from a distance to stay safe
6. **Bullet Management**: Bullets have limited range - get close enough

### Wolf Avoidance (Much Easier Now!)
1. **Very Slow Movement**: Wolves move every 2 seconds - extremely manageable
2. **Predictable Movement**: You have plenty of time to plan your moves
3. **Safe Distance**: Use rifles to eliminate threats from afar
4. **Cave Awareness**: Stay away from caves where new wolves spawn

### Deer Collection
1. **Walk Into Them**: Simply move your hunter onto a deer's position
2. **Don't Shoot**: Shooting deer ends the game immediately
3. **Plan Routes**: Efficiently collect deer while avoiding wolves
4. **Golden Glow**: Look for the subtle glow indicating collectible deer

## Visual Improvements

### Scoring Display
- **Dynamic Top Bar**: Real-time score display at top of screen
- **Color-coded Information**: Gold score, white top score, green level
- **Comma Formatting**: Large numbers displayed with commas for readability
- **Always Visible**: Score information always available during gameplay

### Hunter Character
- Realistic human figure with deerstalker hat
- Brown coat and blue trousers
- Flesh-colored head with detailed hat
- **Realistic rifle appears in hand when armed**
- **Direction-based rifle orientation**

### Deer Graphics (Enhanced!)
- **Realistic deer body**: Brown with tan belly, proper proportions
- **Detailed antlers**: Multi-branched antlers clearly visible
- **Four legs with hooves**: Realistic positioning and black hooves
- **Facial features**: Eyes, nose, and snout
- **Collectible glow**: Golden outline to indicate they can be collected
- **Much larger and more identifiable** than before

### Rifle Graphics
- **In Maze**: Detailed rifles with barrel, stock, trigger guard, scope, and yellow glow
- **In Hand**: Direction-aware rifle positioning based on hunter movement
- **Realistic Design**: Proper hunting rifle appearance
- **High Visibility**: Easy to spot and identify in the forest

### Wolf Characters (Enhanced!)
- **Much Slower Movement**: 2x slower than before for perfect visibility and planning
- **Detailed Wolf Body**: Proper elliptical body with shadow/depth
- **Realistic Head**: Direction-based head with snout and nose
- **Pointed Ears**: Triangular ears that match body color
- **Glowing Red Eyes**: Intimidating red eyes (1-2 depending on direction)
- **Four Paws**: Realistic leg positioning with paw pads
- **Tail**: Direction-appropriate tail positioning
- **Color Variations**: Red, orange, purple, pink with darker shadows

### Leaderboard Interface
- **Golden Title**: "🏆 TOP 10 SCORES 🏆" in gold with trophy emojis
- **Organized Display**: Rank, Name, Score, Level columns
- **Current Player Highlight**: Your score highlighted in gold
- **Professional Layout**: Clean, easy-to-read leaderboard design

### Welcome Screen
- **Mountain Landscape**: Multi-layered mountain background with sky gradient
- **Forest Level Map**: Visual path showing progression through different forest types
- **Retro Typography**: Large golden title with thick black outline
- **Animated Elements**: Pulsing start instruction
- **Clear Instructions**: Updated to emphasize deer collection vs wolf shooting

### Forest Environment
- Stable, non-flashing tree colors
- Detailed tree trunks and canopies
- Varied forest floor with grass patches
- Clear visual distinction between paths and trees
- Level-based forest themes

## Installation & Running

1. Make sure you have Python and pygame installed:
   ```bash
   pip install pygame
   ```

2. Run the game:
   ```bash
   python forest_hunter_game.py
   ```

3. Test the features:
   ```bash
   python test_game_features.py
   ```

## Game Strategy Tips

1. **Score Maximization**: Focus on reaching higher levels for maximum bonus points
2. **Take Your Time**: With very slow wolves (2-second intervals), plan every move carefully
3. **Deer Priority**: Collect deer efficiently to unlock level completion bonuses
4. **Rifle Strategy**: Only use rifles on wolves - never on deer!
5. **Safe Collection**: Plan routes to collect deer while staying away from wolves
6. **Wolf Management**: Use rifles to clear paths when wolves block deer
7. **Cave Awareness**: Stay away from caves where new wolves spawn
8. **Direction Planning**: Face your target direction before pressing spacebar
9. **Range Combat**: Keep distance and shoot wolves before they get close
10. **Bullet Conservation**: Bullets have limited range - don't waste shots
11. **Wildlife Protection**: Remember - deer are friends, wolves are threats!
12. **Leaderboard Goals**: Aim for the top 10 - higher levels = higher scores!

## Technical Details

- Built with Python and Pygame
- 1000x800 pixel window
- 60 FPS gameplay
- Step-by-step grid-based movement
- Enhanced detailed sprite graphics
- Much slower wolf AI (120-frame update cycle - 2 seconds)
- Dynamic scoring system with level-based bonuses
- Persistent leaderboard system (JSON file storage)
- Real-time score display and tracking
- Player name input system
- Bullet physics system with collision detection
- Wildlife protection collision system
- Game over reason tracking and display
- Realistic rifle graphics and mechanics
- Spacebar firing system
- Stable visual rendering (no flashing)
- Retro cartoon font styling
- Mountain background with level mapping
- Procedurally generated forest mazes

## Files Created
- `forest_hunter_game.py` - Main game file
- `forest_hunter_scores.json` - Leaderboard data (created automatically)
- `test_game_features.py` - Feature testing script
- `README_ForestHunter.md` - This documentation

Enjoy hunting in the forest with dynamic scoring, competitive leaderboards, realistic wildlife, extremely manageable wolf speed, and important wildlife protection rules! 🏔️🦌🔫🐺🏆

**Remember: Collect deer, shoot wolves, protect wildlife, and aim for the top score!**
