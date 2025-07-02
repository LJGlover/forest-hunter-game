import pygame
import random
import math
import sys
import json
import os
from enum import Enum

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (34, 139, 34)
DARK_GREEN = (0, 100, 0)
BROWN = (139, 69, 19)
GRAY = (128, 128, 128)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
PINK = (255, 192, 203)

# Game settings
CELL_SIZE = 20
MAZE_WIDTH = SCREEN_WIDTH // CELL_SIZE
MAZE_HEIGHT = (SCREEN_HEIGHT - 100) // CELL_SIZE  # Leave space for UI

class GameState(Enum):
    MENU = 1
    PLAYING = 2
    GAME_OVER = 3
    LEVEL_COMPLETE = 4

class Direction(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

class Entity:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.direction = Direction.RIGHT
        self.speed = 1
        
    def move(self, maze):
        new_x = int(self.x + self.direction.value[0] * self.speed)
        new_y = int(self.y + self.direction.value[1] * self.speed)
        
        # Check bounds and walls
        if (0 <= new_x < MAZE_WIDTH and 0 <= new_y < MAZE_HEIGHT and 
            maze[new_y][new_x] != 1):
            self.x = new_x
            self.y = new_y
            return True
        return False
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, 
                         (self.x * CELL_SIZE + CELL_SIZE // 2, 
                          self.y * CELL_SIZE + CELL_SIZE // 2), 
                         CELL_SIZE // 2 - 2)

class Hunter(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, BLUE)
        self.has_gun = False
        self.gun_timer = 0
        self.deer_collected = 0
        self.bullets = []  # Store active bullets
        
    def update(self):
        if self.gun_timer > 0:
            self.gun_timer -= 1
            if self.gun_timer == 0:
                self.has_gun = False
        
        # Update bullets
        for bullet in self.bullets[:]:
            bullet['x'] += bullet['dx'] * 2  # Bullet speed
            bullet['y'] += bullet['dy'] * 2
            bullet['life'] -= 1
            
            # Remove bullets that are out of bounds or expired
            if (bullet['life'] <= 0 or 
                bullet['x'] < 0 or bullet['x'] >= MAZE_WIDTH or 
                bullet['y'] < 0 or bullet['y'] >= MAZE_HEIGHT):
                self.bullets.remove(bullet)
    
    def fire_gun(self, maze):
        """Fire the gun in the current direction"""
        if self.has_gun:
            # Create bullet
            bullet = {
                'x': float(self.x),
                'y': float(self.y),
                'dx': self.direction.value[0],
                'dy': self.direction.value[1],
                'life': 30  # Bullet travels for 30 frames
            }
            self.bullets.append(bullet)
            return True
        return False
    
    def draw(self, screen):
        center_x = self.x * CELL_SIZE + CELL_SIZE // 2
        center_y = self.y * CELL_SIZE + CELL_SIZE // 2
        
        # Draw body (brown coat)
        body_color = (139, 69, 19)  # Brown
        pygame.draw.ellipse(screen, body_color, 
                           (center_x - 6, center_y - 2, 12, 10))
        
        # Draw head (flesh color)
        head_color = (255, 220, 177)
        pygame.draw.circle(screen, head_color, (center_x, center_y - 6), 4)
        
        # Draw deerstalker hat
        hat_color = (101, 67, 33)  # Dark brown
        # Hat crown
        pygame.draw.ellipse(screen, hat_color, 
                           (center_x - 5, center_y - 12, 10, 6))
        # Hat brim
        pygame.draw.ellipse(screen, hat_color, 
                           (center_x - 6, center_y - 10, 12, 3))
        # Hat flaps
        pygame.draw.ellipse(screen, hat_color, 
                           (center_x - 8, center_y - 9, 4, 6))
        pygame.draw.ellipse(screen, hat_color, 
                           (center_x + 4, center_y - 9, 4, 6))
        
        # Draw arms
        arm_color = body_color
        pygame.draw.circle(screen, arm_color, (center_x - 7, center_y), 2)
        pygame.draw.circle(screen, arm_color, (center_x + 7, center_y), 2)
        
        # Draw legs
        leg_color = (0, 0, 139)  # Dark blue
        pygame.draw.ellipse(screen, leg_color, 
                           (center_x - 3, center_y + 4, 2, 6))
        pygame.draw.ellipse(screen, leg_color, 
                           (center_x + 1, center_y + 4, 2, 6))
        
        # Draw rifle if has one (much more visible and realistic)
        if self.has_gun:
            rifle_color = (64, 64, 64)  # Dark gray
            wood_color = (139, 69, 19)  # Brown wood stock
            
            if self.direction == Direction.RIGHT:
                # Rifle barrel
                pygame.draw.rect(screen, rifle_color, 
                               (center_x + 6, center_y - 2, 12, 3))
                # Rifle stock
                pygame.draw.rect(screen, wood_color, 
                               (center_x + 4, center_y - 1, 4, 5))
                # Rifle sight
                pygame.draw.rect(screen, rifle_color, 
                               (center_x + 16, center_y - 1, 2, 1))
                
            elif self.direction == Direction.LEFT:
                # Rifle barrel
                pygame.draw.rect(screen, rifle_color, 
                               (center_x - 18, center_y - 2, 12, 3))
                # Rifle stock
                pygame.draw.rect(screen, wood_color, 
                               (center_x - 8, center_y - 1, 4, 5))
                # Rifle sight
                pygame.draw.rect(screen, rifle_color, 
                               (center_x - 18, center_y - 1, 2, 1))
                
            elif self.direction == Direction.UP:
                # Rifle barrel
                pygame.draw.rect(screen, rifle_color, 
                               (center_x - 2, center_y - 18, 3, 12))
                # Rifle stock
                pygame.draw.rect(screen, wood_color, 
                               (center_x - 1, center_y - 8, 5, 4))
                # Rifle sight
                pygame.draw.rect(screen, rifle_color, 
                               (center_x - 1, center_y - 18, 1, 2))
                
            else:  # DOWN
                # Rifle barrel
                pygame.draw.rect(screen, rifle_color, 
                               (center_x - 2, center_y + 6, 3, 12))
                # Rifle stock
                pygame.draw.rect(screen, wood_color, 
                               (center_x - 1, center_y + 4, 5, 4))
                # Rifle sight
                pygame.draw.rect(screen, rifle_color, 
                               (center_x - 1, center_y + 16, 1, 2))
        
        # Draw bullets
        for bullet in self.bullets:
            bullet_x = int(bullet['x'] * CELL_SIZE + CELL_SIZE // 2)
            bullet_y = int(bullet['y'] * CELL_SIZE + CELL_SIZE // 2)
            pygame.draw.circle(screen, YELLOW, (bullet_x, bullet_y), 2)

class Wolf(Entity):
    def __init__(self, x, y, color):
        super().__init__(x, y, color)
        self.target_x = x
        self.target_y = y
        self.ai_timer = 0
        
    def update_ai(self, hunter_x, hunter_y, maze):
        self.ai_timer += 1
        if self.ai_timer >= 120:  # Update AI every 120 frames (much slower movement - 2 seconds)
            self.ai_timer = 0
            
            # Simple AI: move towards hunter
            dx = hunter_x - self.x
            dy = hunter_y - self.y
            
            # Choose direction based on distance
            possible_directions = []
            
            if abs(dx) > abs(dy):
                if dx > 0:
                    possible_directions.append(Direction.RIGHT)
                else:
                    possible_directions.append(Direction.LEFT)
            else:
                if dy > 0:
                    possible_directions.append(Direction.DOWN)
                else:
                    possible_directions.append(Direction.UP)
            
            # Add random movement for unpredictability
            all_directions = [Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT]
            possible_directions.extend(random.choices(all_directions, k=2))
            
            # Try directions until one works
            for direction in possible_directions:
                old_direction = self.direction
                self.direction = direction
                if self.can_move(maze):
                    break
                self.direction = old_direction
    
    def can_move(self, maze):
        new_x = int(self.x + self.direction.value[0])
        new_y = int(self.y + self.direction.value[1])
        return (0 <= new_x < MAZE_WIDTH and 0 <= new_y < MAZE_HEIGHT and 
                maze[new_y][new_x] != 1)
    
    def draw(self, screen):
        center_x = self.x * CELL_SIZE + CELL_SIZE // 2
        center_y = self.y * CELL_SIZE + CELL_SIZE // 2
        
        # Draw wolf body (larger, more realistic)
        body_color = self.color
        shadow_color = (max(0, self.color[0] - 40), 
                       max(0, self.color[1] - 40), 
                       max(0, self.color[2] - 40))
        
        # Main body
        pygame.draw.ellipse(screen, body_color, 
                           (center_x - 8, center_y - 4, 16, 10))
        # Body shadow/depth
        pygame.draw.ellipse(screen, shadow_color, 
                           (center_x - 7, center_y - 2, 14, 6))
        
        # Draw wolf head based on direction
        head_color = body_color
        if self.direction == Direction.RIGHT:
            head_x, head_y = center_x + 7, center_y - 3
            # Snout
            pygame.draw.ellipse(screen, head_color, (head_x, head_y, 6, 6))
            pygame.draw.ellipse(screen, shadow_color, (head_x + 2, head_y + 1, 4, 4))
            # Nose
            pygame.draw.circle(screen, BLACK, (head_x + 5, head_y + 2), 1)
            # Eyes
            pygame.draw.circle(screen, (255, 50, 50), (head_x + 1, head_y + 1), 1)
            # Ears
            pygame.draw.polygon(screen, shadow_color, [
                (head_x + 1, head_y - 1), (head_x - 1, head_y - 4), (head_x + 2, head_y - 2)
            ])
            pygame.draw.polygon(screen, shadow_color, [
                (head_x + 3, head_y - 1), (head_x + 1, head_y - 4), (head_x + 4, head_y - 2)
            ])
            
        elif self.direction == Direction.LEFT:
            head_x, head_y = center_x - 7, center_y - 3
            # Snout
            pygame.draw.ellipse(screen, head_color, (head_x - 6, head_y, 6, 6))
            pygame.draw.ellipse(screen, shadow_color, (head_x - 4, head_y + 1, 4, 4))
            # Nose
            pygame.draw.circle(screen, BLACK, (head_x - 5, head_y + 2), 1)
            # Eyes
            pygame.draw.circle(screen, (255, 50, 50), (head_x - 1, head_y + 1), 1)
            # Ears
            pygame.draw.polygon(screen, shadow_color, [
                (head_x - 1, head_y - 1), (head_x + 1, head_y - 4), (head_x - 2, head_y - 2)
            ])
            pygame.draw.polygon(screen, shadow_color, [
                (head_x - 3, head_y - 1), (head_x - 1, head_y - 4), (head_x - 4, head_y - 2)
            ])
            
        elif self.direction == Direction.UP:
            head_x, head_y = center_x, center_y - 7
            # Head
            pygame.draw.ellipse(screen, head_color, (head_x - 3, head_y - 3, 6, 6))
            pygame.draw.ellipse(screen, shadow_color, (head_x - 2, head_y - 2, 4, 4))
            # Snout
            pygame.draw.ellipse(screen, head_color, (head_x - 1, head_y - 5, 2, 3))
            # Nose
            pygame.draw.circle(screen, BLACK, (head_x, head_y - 4), 1)
            # Eyes
            pygame.draw.circle(screen, (255, 50, 50), (head_x - 1, head_y - 2), 1)
            pygame.draw.circle(screen, (255, 50, 50), (head_x + 1, head_y - 2), 1)
            # Ears
            pygame.draw.polygon(screen, shadow_color, [
                (head_x - 2, head_y - 3), (head_x - 4, head_y - 6), (head_x - 1, head_y - 4)
            ])
            pygame.draw.polygon(screen, shadow_color, [
                (head_x + 2, head_y - 3), (head_x + 4, head_y - 6), (head_x + 1, head_y - 4)
            ])
            
        else:  # DOWN
            head_x, head_y = center_x, center_y + 5
            # Head
            pygame.draw.ellipse(screen, head_color, (head_x - 3, head_y, 6, 6))
            pygame.draw.ellipse(screen, shadow_color, (head_x - 2, head_y + 1, 4, 4))
            # Snout
            pygame.draw.ellipse(screen, head_color, (head_x - 1, head_y + 4, 2, 3))
            # Nose
            pygame.draw.circle(screen, BLACK, (head_x, head_y + 5), 1)
            # Eyes
            pygame.draw.circle(screen, (255, 50, 50), (head_x - 1, head_y + 2), 1)
            pygame.draw.circle(screen, (255, 50, 50), (head_x + 1, head_y + 2), 1)
            # Ears
            pygame.draw.polygon(screen, shadow_color, [
                (head_x - 2, head_y), (head_x - 4, head_y - 3), (head_x - 1, head_y + 1)
            ])
            pygame.draw.polygon(screen, shadow_color, [
                (head_x + 2, head_y), (head_x + 4, head_y - 3), (head_x + 1, head_y + 1)
            ])
        
        # Draw wolf tail
        tail_color = body_color
        if self.direction == Direction.RIGHT:
            tail_x, tail_y = center_x - 9, center_y
            pygame.draw.ellipse(screen, tail_color, (tail_x - 3, tail_y - 1, 6, 3))
        elif self.direction == Direction.LEFT:
            tail_x, tail_y = center_x + 9, center_y
            pygame.draw.ellipse(screen, tail_color, (tail_x - 3, tail_y - 1, 6, 3))
        elif self.direction == Direction.UP:
            tail_x, tail_y = center_x, center_y + 7
            pygame.draw.ellipse(screen, tail_color, (tail_x - 1, tail_y - 3, 3, 6))
        else:  # DOWN
            tail_x, tail_y = center_x, center_y - 9
            pygame.draw.ellipse(screen, tail_color, (tail_x - 1, tail_y - 3, 3, 6))
        
        # Draw legs (four paws)
        leg_color = shadow_color
        paw_positions = [
            (center_x - 5, center_y + 4),  # Front left
            (center_x - 2, center_y + 4),  # Back left
            (center_x + 2, center_y + 4),  # Back right
            (center_x + 5, center_y + 4)   # Front right
        ]
        
        for paw_x, paw_y in paw_positions:
            pygame.draw.circle(screen, leg_color, (paw_x, paw_y), 2)
            # Paw pads
            pygame.draw.circle(screen, BLACK, (paw_x, paw_y), 1)

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Forest Hunter")
        self.clock = pygame.time.Clock()
        
        # Try to load a retro-style font, fallback to default
        try:
            self.title_font = pygame.font.Font(None, 72)  # Large title font
            self.menu_font = pygame.font.Font(None, 48)   # Menu text font
            self.font = pygame.font.Font(None, 36)        # Regular game font
            self.small_font = pygame.font.Font(None, 24)  # Small text font
        except:
            self.title_font = pygame.font.Font(None, 72)
            self.menu_font = pygame.font.Font(None, 48)
            self.font = pygame.font.Font(None, 36)
            self.small_font = pygame.font.Font(None, 24)
        
        self.state = GameState.MENU
        self.level = 1
        self.score = 0
        self.top_score = 0
        self.game_over_reason = ""  # Track why game ended
        self.player_name = ""
        self.entering_name = False
        self.leaderboard_file = "forest_hunter_scores.json"
        
        # Load leaderboard and top score
        self.leaderboard = self.load_leaderboard()
        if self.leaderboard:
            self.top_score = self.leaderboard[0]['score']
        
        self.reset_level()
        
    def load_leaderboard(self):
        """Load leaderboard from file"""
        try:
            if os.path.exists(self.leaderboard_file):
                with open(self.leaderboard_file, 'r') as f:
                    return json.load(f)
            return []
        except:
            return []
    
    def save_leaderboard(self):
        """Save leaderboard to file"""
        try:
            with open(self.leaderboard_file, 'w') as f:
                json.dump(self.leaderboard, f, indent=2)
        except:
            pass
    
    def add_to_leaderboard(self, name, score, level):
        """Add score to leaderboard"""
        entry = {
            'name': name,
            'score': score,
            'level': level
        }
        
        self.leaderboard.append(entry)
        # Sort by score (descending) and keep top 10
        self.leaderboard.sort(key=lambda x: x['score'], reverse=True)
        self.leaderboard = self.leaderboard[:10]
        
        # Update top score
        if self.leaderboard:
            self.top_score = self.leaderboard[0]['score']
        
        self.save_leaderboard()
    
    def is_high_score(self, score):
        """Check if score qualifies for leaderboard"""
        return len(self.leaderboard) < 10 or score > self.leaderboard[-1]['score']
    
    def reset_level(self):
        self.maze = self.generate_maze()
        self.hunter = Hunter(1, 1)
        self.wolves = []
        self.deer = []
        self.guns = []
        self.caves = []
        
        # Set level parameters first
        self.deer_needed = 5 + (self.level - 1) * 3
        self.wolf_speed = 1  # Keep speed as 1 for integer movement
        
        # Find caves (dead ends or corners)
        self.find_caves()
        
        # Place initial wolves
        wolf_colors = [RED, ORANGE, PURPLE, PINK]
        for i in range(4):
            if self.caves:
                cave = random.choice(self.caves)
                color = wolf_colors[i % len(wolf_colors)]
                self.wolves.append(Wolf(cave[0], cave[1], color))
        
        # Place deer and guns
        self.place_items()
    
        self.maze = self.generate_maze()
        self.hunter = Hunter(1, 1)
        self.wolves = []
        self.deer = []
        self.guns = []
        self.caves = []
        
        # Set level parameters first
        self.deer_needed = 5 + (self.level - 1) * 3
        self.wolf_speed = 1  # Keep speed as 1 for integer movement
        
        # Find caves (dead ends or corners)
        self.find_caves()
        
        # Place initial wolves
        wolf_colors = [RED, ORANGE, PURPLE, PINK]
        for i in range(4):
            if self.caves:
                cave = random.choice(self.caves)
                color = wolf_colors[i % len(wolf_colors)]
                self.wolves.append(Wolf(cave[0], cave[1], color))
        
        # Place deer and guns
        self.place_items()
        
    def generate_maze(self):
        # Create a forest-like maze with different patterns per level
        maze = [[1 for _ in range(MAZE_WIDTH)] for _ in range(MAZE_HEIGHT)]
        
        # Different maze patterns based on level
        if self.level % 3 == 1:
            # Sparse forest
            for y in range(1, MAZE_HEIGHT - 1, 2):
                for x in range(1, MAZE_WIDTH - 1, 2):
                    maze[y][x] = 0
                    if random.random() > 0.3:
                        if x + 1 < MAZE_WIDTH - 1:
                            maze[y][x + 1] = 0
                    if random.random() > 0.3:
                        if y + 1 < MAZE_HEIGHT - 1:
                            maze[y + 1][x] = 0
        elif self.level % 3 == 2:
            # Dense forest with clearings
            for y in range(MAZE_HEIGHT):
                for x in range(MAZE_WIDTH):
                    if random.random() > 0.4:
                        maze[y][x] = 0
            # Create some clearings
            for _ in range(3):
                cx, cy = random.randint(5, MAZE_WIDTH-5), random.randint(5, MAZE_HEIGHT-5)
                for dy in range(-2, 3):
                    for dx in range(-2, 3):
                        if 0 <= cx+dx < MAZE_WIDTH and 0 <= cy+dy < MAZE_HEIGHT:
                            maze[cy+dy][cx+dx] = 0
        else:
            # Winding paths
            for y in range(1, MAZE_HEIGHT - 1):
                for x in range(1, MAZE_WIDTH - 1):
                    if (x + y) % 3 == 0 or random.random() > 0.6:
                        maze[y][x] = 0
        
        # Ensure borders are walls
        for x in range(MAZE_WIDTH):
            maze[0][x] = 1
            maze[MAZE_HEIGHT-1][x] = 1
        for y in range(MAZE_HEIGHT):
            maze[y][0] = 1
            maze[y][MAZE_WIDTH-1] = 1
            
        # Ensure starting position is clear
        maze[1][1] = 0
        
        return maze
    
    def find_caves(self):
        self.caves = []
        for y in range(1, MAZE_HEIGHT - 1):
            for x in range(1, MAZE_WIDTH - 1):
                if self.maze[y][x] == 0:  # Empty space
                    # Count adjacent walls
                    wall_count = 0
                    for dy in [-1, 0, 1]:
                        for dx in [-1, 0, 1]:
                            if dx == 0 and dy == 0:
                                continue
                            if self.maze[y+dy][x+dx] == 1:
                                wall_count += 1
                    
                    # Cave if mostly surrounded by walls
                    if wall_count >= 6:
                        self.caves.append((x, y))
    
    def place_items(self):
        empty_spaces = []
        for y in range(MAZE_HEIGHT):
            for x in range(MAZE_WIDTH):
                if self.maze[y][x] == 0 and (x != 1 or y != 1):  # Not hunter start
                    empty_spaces.append((x, y))
        
        # Place deer
        deer_count = self.deer_needed + 5
        for _ in range(deer_count):
            if empty_spaces:
                pos = random.choice(empty_spaces)
                self.deer.append(pos)
                empty_spaces.remove(pos)
        
        # Place guns
        gun_count = max(3, self.level)
        for _ in range(gun_count):
            if empty_spaces:
                pos = random.choice(empty_spaces)
                self.guns.append(pos)
                empty_spaces.remove(pos)
    
    def handle_input(self):
        # Handle step-by-step movement (one move per key press)
        pass  # Movement now handled in event loop
    
    def move_hunter(self, direction):
        """Move hunter one step in the given direction"""
        if self.state == GameState.PLAYING:
            old_direction = self.hunter.direction
            self.hunter.direction = direction
            
            # Try to move
            if not self.hunter.move(self.maze):
                self.hunter.direction = old_direction
    
    def update(self):
        if self.state == GameState.PLAYING:
            self.hunter.update()
            
            # Update wolves
            for wolf in self.wolves:
                wolf.speed = self.wolf_speed
                wolf.update_ai(self.hunter.x, self.hunter.y, self.maze)
                wolf.move(self.maze)
            
            # Check collisions
            self.check_collisions()
            
            # Check win condition
            if self.hunter.deer_collected >= self.deer_needed:
                # Level completion bonus
                level_bonus = 100 * self.level + (self.deer_needed * 20)
                self.score += level_bonus
                # Update top score if exceeded
                if self.score > self.top_score:
                    self.top_score = self.score
                self.state = GameState.LEVEL_COMPLETE
    
    def check_collisions(self):
        hunter_pos = (self.hunter.x, self.hunter.y)
        
        # Check deer collection (only by walking into them)
        if hunter_pos in self.deer:
            self.deer.remove(hunter_pos)
            self.hunter.deer_collected += 1
            # Base points + bonus for level
            deer_points = 10 + (self.level * 5)  # More points for higher levels
            self.score += deer_points
            # Update top score if exceeded
            if self.score > self.top_score:
                self.top_score = self.score
        
        # Check gun collection
        if hunter_pos in self.guns:
            self.guns.remove(hunter_pos)
            self.hunter.has_gun = True
            self.hunter.gun_timer = 600  # 10 seconds at 60 FPS (longer duration)
        
        # Check bullet collisions
        for bullet in self.hunter.bullets[:]:
            bullet_x = int(bullet['x'])
            bullet_y = int(bullet['y'])
            
            # Check bullet-deer collision (GAME OVER if deer is shot)
            for deer_pos in self.deer:
                if abs(deer_pos[0] - bullet_x) <= 1 and abs(deer_pos[1] - bullet_y) <= 1:
                    # Game over - hunter shot a deer!
                    self.game_over_reason = "You shot a deer! Hunters must protect wildlife!"
                    self.state = GameState.GAME_OVER
                    return
            
            # Check bullet-wolf collision
            for wolf in self.wolves[:]:
                if abs(wolf.x - bullet_x) <= 1 and abs(wolf.y - bullet_y) <= 1:
                    # Wolf hit by bullet
                    self.wolves.remove(wolf)
                    self.hunter.bullets.remove(bullet)
                    # Base points + bonus for level + bonus for difficulty
                    wolf_points = 50 + (self.level * 10) + (len(self.wolves) * 5)
                    self.score += wolf_points
                    # Update top score if exceeded
                    if self.score > self.top_score:
                        self.top_score = self.score
                    
                    # Spawn new wolf from cave
                    if self.caves:
                        cave = random.choice(self.caves)
                        colors = [RED, ORANGE, PURPLE, PINK, (255, 100, 100), (100, 255, 100)]
                        color = random.choice(colors)
                        self.wolves.append(Wolf(cave[0], cave[1], color))
                    break
        
        # Check wolf-hunter collisions (only if direct contact)
        for wolf in self.wolves[:]:
            if abs(wolf.x - self.hunter.x) <= 1 and abs(wolf.y - self.hunter.y) <= 1:
                # Hunter dies
                self.game_over_reason = "You were caught by a wolf!"
                self.state = GameState.GAME_OVER
    
    def draw_maze(self):
        # Draw forest background with stable colors
        forest_colors = [
            (34, 139, 34),   # Forest green
            (0, 100, 0),     # Dark green  
            (46, 125, 50),   # Medium green
            (27, 94, 32)     # Deep green
        ]
        base_color = forest_colors[self.level % len(forest_colors)]
        
        for y in range(MAZE_HEIGHT):
            for x in range(MAZE_WIDTH):
                rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                
                if self.maze[y][x] == 1:  # Wall (tree)
                    # Use consistent tree colors based on position (no random)
                    color_seed = (x * 7 + y * 13) % 40 - 20  # Deterministic variation
                    tree_color = (
                        max(0, min(255, base_color[0] + color_seed)),
                        max(0, min(255, base_color[1] + color_seed)),
                        max(0, min(255, base_color[2] + color_seed))
                    )
                    pygame.draw.rect(self.screen, tree_color, rect)
                    
                    # Add tree trunk (brown)
                    trunk_color = (101, 67, 33)
                    trunk_rect = pygame.Rect(x * CELL_SIZE + CELL_SIZE//3, 
                                           y * CELL_SIZE + CELL_SIZE//2, 
                                           CELL_SIZE//3, CELL_SIZE//2)
                    pygame.draw.rect(self.screen, trunk_color, trunk_rect)
                    
                    # Add tree canopy details
                    canopy_color = (max(0, tree_color[0] + 10), 
                                   max(0, min(255, tree_color[1] + 20)), 
                                   max(0, tree_color[2] + 5))
                    pygame.draw.circle(self.screen, canopy_color, 
                                     (x * CELL_SIZE + CELL_SIZE//2, 
                                      y * CELL_SIZE + CELL_SIZE//3), 
                                     CELL_SIZE//3)
                else:  # Path
                    # Forest floor - dirt/grass path
                    path_color = (160, 130, 98)  # Light brown dirt
                    pygame.draw.rect(self.screen, path_color, rect)
                    
                    # Add some grass patches
                    if (x + y) % 3 == 0:
                        grass_color = (85, 107, 47)  # Dark olive green
                        grass_rect = pygame.Rect(x * CELL_SIZE + 2, y * CELL_SIZE + 2, 
                                               CELL_SIZE - 4, CELL_SIZE - 4)
                        pygame.draw.rect(self.screen, grass_color, grass_rect)
    
    def draw_items(self):
        # Draw deer (more realistic and identifiable)
        for deer_pos in self.deer:
            x, y = deer_pos
            center_x = x * CELL_SIZE + CELL_SIZE // 2
            center_y = y * CELL_SIZE + CELL_SIZE // 2
            
            # Draw deer body (brown/tan)
            deer_body_color = (160, 82, 45)  # Saddle brown
            deer_light_color = (210, 180, 140)  # Tan for belly
            
            # Main body (elliptical)
            pygame.draw.ellipse(self.screen, deer_body_color, 
                               (center_x - 8, center_y - 3, 16, 8))
            # Lighter belly
            pygame.draw.ellipse(self.screen, deer_light_color, 
                               (center_x - 6, center_y - 1, 12, 4))
            
            # Draw deer head
            head_color = deer_body_color
            pygame.draw.ellipse(self.screen, head_color, 
                               (center_x - 3, center_y - 7, 6, 6))
            
            # Draw deer snout/nose
            pygame.draw.ellipse(self.screen, (139, 69, 19), 
                               (center_x - 1, center_y - 5, 2, 3))
            # Black nose
            pygame.draw.circle(self.screen, BLACK, (center_x, center_y - 4), 1)
            
            # Draw deer eyes
            pygame.draw.circle(self.screen, BLACK, (center_x - 1, center_y - 6), 1)
            pygame.draw.circle(self.screen, BLACK, (center_x + 1, center_y - 6), 1)
            
            # Draw prominent antlers (make them very visible)
            antler_color = (101, 67, 33)  # Dark brown
            # Main antler stems
            pygame.draw.line(self.screen, antler_color, 
                           (center_x - 2, center_y - 8), (center_x - 4, center_y - 12), 2)
            pygame.draw.line(self.screen, antler_color, 
                           (center_x + 2, center_y - 8), (center_x + 4, center_y - 12), 2)
            
            # Antler branches (multiple points)
            pygame.draw.line(self.screen, antler_color, 
                           (center_x - 3, center_y - 10), (center_x - 6, center_y - 11), 2)
            pygame.draw.line(self.screen, antler_color, 
                           (center_x - 3, center_y - 11), (center_x - 5, center_y - 14), 2)
            pygame.draw.line(self.screen, antler_color, 
                           (center_x + 3, center_y - 10), (center_x + 6, center_y - 11), 2)
            pygame.draw.line(self.screen, antler_color, 
                           (center_x + 3, center_y - 11), (center_x + 5, center_y - 14), 2)
            
            # Draw deer legs (four legs)
            leg_color = (139, 69, 19)  # Darker brown
            leg_positions = [
                (center_x - 5, center_y + 4),  # Front left
                (center_x - 2, center_y + 4),  # Back left  
                (center_x + 2, center_y + 4),  # Back right
                (center_x + 5, center_y + 4)   # Front right
            ]
            
            for leg_x, leg_y in leg_positions:
                pygame.draw.rect(self.screen, leg_color, (leg_x - 1, leg_y, 2, 4))
                # Hooves
                pygame.draw.circle(self.screen, BLACK, (leg_x, leg_y + 4), 1)
            
            # Draw deer tail
            pygame.draw.ellipse(self.screen, deer_body_color, 
                               (center_x + 7, center_y - 1, 3, 2))
            
            # Add a subtle glow to make deer more visible and collectible
            pygame.draw.circle(self.screen, (255, 215, 0, 30), 
                             (center_x, center_y), CELL_SIZE // 2, 1)
        
        # Draw rifles (more realistic and identifiable)
        for gun_pos in self.guns:
            x, y = gun_pos
            center_x = x * CELL_SIZE + CELL_SIZE // 2
            center_y = y * CELL_SIZE + CELL_SIZE // 2
            
            # Draw rifle with barrel, stock, and details
            rifle_color = (64, 64, 64)  # Dark gray metal
            wood_color = (139, 69, 19)  # Brown wood stock
            
            # Rifle barrel (horizontal)
            pygame.draw.rect(self.screen, rifle_color, 
                           (center_x - 8, center_y - 1, 16, 3))
            # Rifle stock
            pygame.draw.rect(self.screen, wood_color, 
                           (center_x - 10, center_y, 6, 4))
            # Trigger guard
            pygame.draw.rect(self.screen, rifle_color, 
                           (center_x - 2, center_y + 1, 4, 2))
            # Rifle sight
            pygame.draw.rect(self.screen, rifle_color, 
                           (center_x + 6, center_y - 2, 2, 1))
            # Rifle scope (small circle)
            pygame.draw.circle(self.screen, (32, 32, 32), 
                             (center_x, center_y - 3), 2)
            
            # Add a subtle glow to make it more visible
            pygame.draw.circle(self.screen, (255, 255, 0, 50), 
                             (center_x, center_y), CELL_SIZE // 2, 2)
        
        # Draw caves
        for cave_pos in self.caves:
            x, y = cave_pos
            center = (x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2)
            pygame.draw.circle(self.screen, BLACK, center, CELL_SIZE // 3)
    
    def draw_mountain_background(self):
        """Draw a mountain background with forest level indicators"""
        # Sky gradient
        for y in range(SCREEN_HEIGHT // 2):
            color_intensity = int(135 + (120 * y / (SCREEN_HEIGHT // 2)))
            sky_color = (135, 206, min(255, color_intensity))
            pygame.draw.line(self.screen, sky_color, (0, y), (SCREEN_WIDTH, y))
        
        # Mountains (multiple layers for depth)
        mountain_colors = [
            (105, 105, 105),  # Dark gray (back mountains)
            (128, 128, 128),  # Medium gray (middle mountains)
            (169, 169, 169),  # Light gray (front mountains)
        ]
        
        # Back mountains
        mountain_points = [
            (0, SCREEN_HEIGHT // 2),
            (200, SCREEN_HEIGHT // 3),
            (400, SCREEN_HEIGHT // 2 + 50),
            (600, SCREEN_HEIGHT // 4),
            (800, SCREEN_HEIGHT // 2 + 30),
            (SCREEN_WIDTH, SCREEN_HEIGHT // 3),
            (SCREEN_WIDTH, SCREEN_HEIGHT),
            (0, SCREEN_HEIGHT)
        ]
        pygame.draw.polygon(self.screen, mountain_colors[0], mountain_points)
        
        # Middle mountains
        mountain_points2 = [
            (0, SCREEN_HEIGHT // 2 + 100),
            (150, SCREEN_HEIGHT // 2 + 20),
            (350, SCREEN_HEIGHT // 2 + 80),
            (550, SCREEN_HEIGHT // 2 + 10),
            (750, SCREEN_HEIGHT // 2 + 60),
            (SCREEN_WIDTH, SCREEN_HEIGHT // 2 + 40),
            (SCREEN_WIDTH, SCREEN_HEIGHT),
            (0, SCREEN_HEIGHT)
        ]
        pygame.draw.polygon(self.screen, mountain_colors[1], mountain_points2)
        
        # Front mountains
        mountain_points3 = [
            (0, SCREEN_HEIGHT // 2 + 150),
            (100, SCREEN_HEIGHT // 2 + 100),
            (300, SCREEN_HEIGHT // 2 + 130),
            (500, SCREEN_HEIGHT // 2 + 80),
            (700, SCREEN_HEIGHT // 2 + 120),
            (900, SCREEN_HEIGHT // 2 + 90),
            (SCREEN_WIDTH, SCREEN_HEIGHT // 2 + 110),
            (SCREEN_WIDTH, SCREEN_HEIGHT),
            (0, SCREEN_HEIGHT)
        ]
        pygame.draw.polygon(self.screen, mountain_colors[2], mountain_points3)
        
        # Draw forest level indicators on the mountain
        forest_positions = [
            (150, SCREEN_HEIGHT // 2 + 120, "Forest 1\n(Sparse)"),
            (350, SCREEN_HEIGHT // 2 + 100, "Forest 2\n(Dense)"),
            (550, SCREEN_HEIGHT // 2 + 90, "Forest 3\n(Winding)"),
            (750, SCREEN_HEIGHT // 2 + 110, "Forest 4+\n(Wild)")
        ]
        
        for x, y, label in forest_positions:
            # Draw forest indicator (green circle)
            pygame.draw.circle(self.screen, DARK_GREEN, (x, y), 15)
            pygame.draw.circle(self.screen, GREEN, (x, y), 12)
            
            # Draw path line to next forest
            if x < 750:  # Don't draw line from last forest
                next_x = forest_positions[forest_positions.index((x, y, label)) + 1][0]
                next_y = forest_positions[forest_positions.index((x, y, label)) + 1][1]
                pygame.draw.line(self.screen, BROWN, (x + 12, y), (next_x - 12, next_y), 3)
            
            # Draw label
            lines = label.split('\n')
            for i, line in enumerate(lines):
                text = self.small_font.render(line, True, WHITE)
                text_rect = text.get_rect(center=(x, y + 25 + i * 15))
                # Add text shadow
                shadow = self.small_font.render(line, True, BLACK)
                shadow_rect = shadow.get_rect(center=(x + 1, y + 26 + i * 15))
                self.screen.blit(shadow, shadow_rect)
                self.screen.blit(text, text_rect)
        ui_y = MAZE_HEIGHT * CELL_SIZE + 10
        
        # Game info
        level_text = self.font.render(f"Level: {self.level}", True, WHITE)
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        deer_text = self.font.render(f"Deer: {self.hunter.deer_collected}/{self.deer_needed}", True, WHITE)
        gun_text = self.font.render(f"Gun: {'Yes' if self.hunter.has_gun else 'No'}", True, WHITE)
        
        self.screen.blit(level_text, (10, ui_y))
        self.screen.blit(score_text, (150, ui_y))
        self.screen.blit(deer_text, (300, ui_y))
        self.screen.blit(gun_text, (500, ui_y))
        
        # Instructions
        inst_text = self.small_font.render("WASD/Arrows: Move | SPACEBAR: Fire rifle at wolves | COLLECT deer (don't shoot them!)", True, WHITE)
        self.screen.blit(inst_text, (10, ui_y + 40))
    
    def draw_menu(self):
        # Draw mountain background
        self.draw_mountain_background()
        
        # Add semi-transparent overlay for text readability
        overlay = pygame.Surface((SCREEN_WIDTH, 300))
        overlay.set_alpha(180)
        overlay.fill(BLACK)
        self.screen.blit(overlay, (0, 50))
        
        # Title with retro cartoon styling
        title_text = "FOREST HUNTER"
        
        # Create outline effect for retro look
        outline_color = BLACK
        title_color = (255, 215, 0)  # Gold color
        
        # Draw title outline (multiple layers for thick outline)
        for dx in range(-3, 4):
            for dy in range(-3, 4):
                if dx != 0 or dy != 0:
                    outline_surface = self.title_font.render(title_text, True, outline_color)
                    outline_rect = outline_surface.get_rect(center=(SCREEN_WIDTH//2 + dx, 150 + dy))
                    self.screen.blit(outline_surface, outline_rect)
        
        # Draw main title
        title_surface = self.title_font.render(title_text, True, title_color)
        title_rect = title_surface.get_rect(center=(SCREEN_WIDTH//2, 150))
        self.screen.blit(title_surface, title_rect)
        
        # Subtitle with retro styling
        subtitle_text = "Hunt for Deer • Avoid the Wolves • Survive the Mountain!"
        subtitle_color = (255, 255, 255)
        
        # Subtitle outline
        for dx in range(-2, 3):
            for dy in range(-2, 3):
                if dx != 0 or dy != 0:
                    subtitle_outline = self.menu_font.render(subtitle_text, True, BLACK)
                    subtitle_outline_rect = subtitle_outline.get_rect(center=(SCREEN_WIDTH//2 + dx, 220 + dy))
                    self.screen.blit(subtitle_outline, subtitle_outline_rect)
        
        # Main subtitle
        subtitle_surface = self.menu_font.render(subtitle_text, True, subtitle_color)
        subtitle_rect = subtitle_surface.get_rect(center=(SCREEN_WIDTH//2, 220))
        self.screen.blit(subtitle_surface, subtitle_rect)
        
        # Start instruction with pulsing effect
        pulse = abs(math.sin(pygame.time.get_ticks() * 0.005)) * 0.3 + 0.7
        start_color = (int(255 * pulse), int(255 * pulse), int(100 * pulse))
        
        start_text = "Press SPACE to Begin Your Adventure!"
        
        # Start text outline
        for dx in range(-2, 3):
            for dy in range(-2, 3):
                if dx != 0 or dy != 0:
                    start_outline = self.menu_font.render(start_text, True, BLACK)
                    start_outline_rect = start_outline.get_rect(center=(SCREEN_WIDTH//2 + dx, 300 + dy))
                    self.screen.blit(start_outline, start_outline_rect)
        
        # Main start text
        start_surface = self.menu_font.render(start_text, True, start_color)
        start_rect = start_surface.get_rect(center=(SCREEN_WIDTH//2, 300))
        self.screen.blit(start_surface, start_rect)
        
        # Instructions
        instructions = [
            "Navigate through different forest levels on the mountain",
            "COLLECT deer by walking into them (DON'T shoot them!)",
            "Find rifles to defend yourself - Press SPACEBAR to fire at wolves!",
            "Each level gets harder as you climb higher!"
        ]
        
        for i, instruction in enumerate(instructions):
            inst_surface = self.small_font.render(instruction, True, WHITE)
            inst_rect = inst_surface.get_rect(center=(SCREEN_WIDTH//2, 400 + i * 25))
            # Add shadow
            shadow_surface = self.small_font.render(instruction, True, BLACK)
            shadow_rect = shadow_surface.get_rect(center=(SCREEN_WIDTH//2 + 1, 401 + i * 25))
            self.screen.blit(shadow_surface, shadow_rect)
            self.screen.blit(inst_surface, inst_rect)
    
    def draw_ui(self):
        # Top score bar (always visible during gameplay)
        score_bar_height = 30
        pygame.draw.rect(self.screen, (0, 0, 0, 180), (0, 0, SCREEN_WIDTH, score_bar_height))
        
        # Current score (left side)
        current_score_text = self.font.render(f"SCORE: {self.score:,}", True, (255, 215, 0))  # Gold
        self.screen.blit(current_score_text, (10, 5))
        
        # Top score (center)
        top_score_text = self.font.render(f"TOP SCORE: {self.top_score:,}", True, (255, 255, 255))
        top_score_rect = top_score_text.get_rect(center=(SCREEN_WIDTH//2, 15))
        self.screen.blit(top_score_text, top_score_rect)
        
        # Level (right side)
        level_text = self.font.render(f"LEVEL: {self.level}", True, (0, 255, 0))  # Green
        level_rect = level_text.get_rect()
        level_rect.topright = (SCREEN_WIDTH - 10, 5)
        self.screen.blit(level_text, level_rect)
        
        # Game info (below the maze)
        ui_y = MAZE_HEIGHT * CELL_SIZE + score_bar_height + 10
        
        # Game status info
        deer_text = self.font.render(f"Deer: {self.hunter.deer_collected}/{self.deer_needed}", True, WHITE)
        gun_text = self.font.render(f"Rifle: {'Yes' if self.hunter.has_gun else 'No'}", True, WHITE)
        
        self.screen.blit(deer_text, (10, ui_y))
        self.screen.blit(gun_text, (200, ui_y))
        
        # Instructions
        inst_text = self.small_font.render("WASD/Arrows: Move | SPACEBAR: Fire rifle at wolves | COLLECT deer (don't shoot them!)", True, WHITE)
        self.screen.blit(inst_text, (10, ui_y + 40))
    
    def draw_game_over(self):
        # Check if this is a high score
        if not self.entering_name and self.is_high_score(self.score):
            self.entering_name = True
            self.player_name = ""
        
        if self.entering_name:
            # Name input screen
            title_text = self.font.render("NEW HIGH SCORE!", True, (255, 215, 0))  # Gold
            title_rect = title_text.get_rect(center=(SCREEN_WIDTH//2, 150))
            self.screen.blit(title_text, title_rect)
            
            score_text = self.font.render(f"Score: {self.score:,}", True, WHITE)
            score_rect = score_text.get_rect(center=(SCREEN_WIDTH//2, 200))
            self.screen.blit(score_text, score_rect)
            
            prompt_text = self.font.render("Enter your name:", True, WHITE)
            prompt_rect = prompt_text.get_rect(center=(SCREEN_WIDTH//2, 250))
            self.screen.blit(prompt_text, prompt_rect)
            
            # Name input box
            name_box = pygame.Rect(SCREEN_WIDTH//2 - 150, 280, 300, 40)
            pygame.draw.rect(self.screen, WHITE, name_box)
            pygame.draw.rect(self.screen, BLACK, name_box, 2)
            
            name_surface = self.font.render(self.player_name, True, BLACK)
            name_rect = name_surface.get_rect(center=name_box.center)
            self.screen.blit(name_surface, name_rect)
            
            instruction_text = self.small_font.render("Type your name and press ENTER", True, WHITE)
            instruction_rect = instruction_text.get_rect(center=(SCREEN_WIDTH//2, 340))
            self.screen.blit(instruction_text, instruction_rect)
            
        else:
            # Regular game over screen with leaderboard
            game_over_text = self.font.render("GAME OVER", True, RED)
            game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH//2, 100))
            self.screen.blit(game_over_text, game_over_rect)
            
            # Show reason for game over
            if self.game_over_reason:
                reason_text = self.font.render(self.game_over_reason, True, WHITE)
                reason_rect = reason_text.get_rect(center=(SCREEN_WIDTH//2, 140))
                self.screen.blit(reason_text, reason_rect)
            
            # Final score
            score_text = self.font.render(f"Final Score: {self.score:,}", True, WHITE)
            score_rect = score_text.get_rect(center=(SCREEN_WIDTH//2, 180))
            self.screen.blit(score_text, score_rect)
            
            # Add reminder about deer protection
            if "deer" in self.game_over_reason.lower():
                reminder_text = self.small_font.render("Remember: Collect deer by walking into them, don't shoot them!", True, YELLOW)
                reminder_rect = reminder_text.get_rect(center=(SCREEN_WIDTH//2, 210))
                self.screen.blit(reminder_text, reminder_rect)
            
            # Leaderboard
            self.draw_leaderboard(240)
            
            restart_text = self.font.render("Press R to Restart", True, WHITE)
            restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH//2, 720))
            self.screen.blit(restart_text, restart_rect)
    
    def draw_leaderboard(self, start_y):
        """Draw the top 10 leaderboard"""
        title_text = self.font.render("🏆 TOP 10 SCORES 🏆", True, (255, 215, 0))  # Gold
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH//2, start_y))
        self.screen.blit(title_text, title_rect)
        
        # Header
        header_y = start_y + 40
        rank_text = self.small_font.render("RANK", True, WHITE)
        name_text = self.small_font.render("NAME", True, WHITE)
        score_text = self.small_font.render("SCORE", True, WHITE)
        level_text = self.small_font.render("LEVEL", True, WHITE)
        
        self.screen.blit(rank_text, (SCREEN_WIDTH//2 - 200, header_y))
        self.screen.blit(name_text, (SCREEN_WIDTH//2 - 100, header_y))
        self.screen.blit(score_text, (SCREEN_WIDTH//2 + 50, header_y))
        self.screen.blit(level_text, (SCREEN_WIDTH//2 + 150, header_y))
        
        # Draw line under header
        pygame.draw.line(self.screen, WHITE, 
                        (SCREEN_WIDTH//2 - 220, header_y + 25), 
                        (SCREEN_WIDTH//2 + 200, header_y + 25), 2)
        
        # Leaderboard entries
        for i, entry in enumerate(self.leaderboard[:10]):
            y_pos = header_y + 40 + (i * 30)
            
            # Highlight current player's score
            color = (255, 215, 0) if entry.get('current_player', False) else WHITE
            
            rank_surface = self.small_font.render(f"{i+1}.", True, color)
            name_surface = self.small_font.render(entry['name'][:12], True, color)  # Limit name length
            score_surface = self.small_font.render(f"{entry['score']:,}", True, color)
            level_surface = self.small_font.render(str(entry['level']), True, color)
            
            self.screen.blit(rank_surface, (SCREEN_WIDTH//2 - 200, y_pos))
            self.screen.blit(name_surface, (SCREEN_WIDTH//2 - 100, y_pos))
            self.screen.blit(score_surface, (SCREEN_WIDTH//2 + 50, y_pos))
            self.screen.blit(level_surface, (SCREEN_WIDTH//2 + 150, y_pos))
    
    def draw_level_complete(self):
        complete_text = self.font.render("LEVEL COMPLETE!", True, GREEN)
        complete_rect = complete_text.get_rect(center=(SCREEN_WIDTH//2, 250))
        self.screen.blit(complete_text, complete_rect)
        
        # Show current score
        score_text = self.font.render(f"Score: {self.score:,}", True, WHITE)
        score_rect = score_text.get_rect(center=(SCREEN_WIDTH//2, 300))
        self.screen.blit(score_text, score_rect)
        
        # Show level bonus
        level_bonus = 100 * self.level + (self.deer_needed * 20)
        bonus_text = self.font.render(f"Level {self.level} Bonus: +{level_bonus:,}", True, (255, 215, 0))
        bonus_rect = bonus_text.get_rect(center=(SCREEN_WIDTH//2, 330))
        self.screen.blit(bonus_text, bonus_rect)
        
        next_text = self.font.render("Press SPACE for Next Level", True, WHITE)
        next_rect = next_text.get_rect(center=(SCREEN_WIDTH//2, 380))
        self.screen.blit(next_text, next_rect)
    
    def run(self):
        running = True
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                if event.type == pygame.KEYDOWN:
                    if self.state == GameState.MENU and event.key == pygame.K_SPACE:
                        self.state = GameState.PLAYING
                    elif self.state == GameState.GAME_OVER:
                        if self.entering_name:
                            # Handle name input
                            if event.key == pygame.K_RETURN:
                                # Submit name and score
                                if self.player_name.strip():
                                    self.add_to_leaderboard(self.player_name.strip(), self.score, self.level)
                                    # Mark this entry as current player
                                    for entry in self.leaderboard:
                                        if (entry['name'] == self.player_name.strip() and 
                                            entry['score'] == self.score):
                                            entry['current_player'] = True
                                            break
                                self.entering_name = False
                            elif event.key == pygame.K_BACKSPACE:
                                # Remove last character
                                self.player_name = self.player_name[:-1]
                            else:
                                # Add character (limit to 15 characters)
                                if len(self.player_name) < 15 and event.unicode.isprintable():
                                    self.player_name += event.unicode
                        elif event.key == pygame.K_r:
                            # Restart game
                            self.level = 1
                            self.score = 0
                            self.game_over_reason = ""  # Reset game over reason
                            self.entering_name = False
                            self.player_name = ""
                            # Clear current player markers
                            for entry in self.leaderboard:
                                entry.pop('current_player', None)
                            self.reset_level()
                            self.state = GameState.PLAYING
                    elif self.state == GameState.LEVEL_COMPLETE and event.key == pygame.K_SPACE:
                        self.level += 1
                        self.reset_level()
                        self.state = GameState.PLAYING
                    
                    # Handle step-by-step movement and firing
                    elif self.state == GameState.PLAYING:
                        if event.key == pygame.K_UP or event.key == pygame.K_w:
                            self.move_hunter(Direction.UP)
                        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                            self.move_hunter(Direction.DOWN)
                        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                            self.move_hunter(Direction.LEFT)
                        elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                            self.move_hunter(Direction.RIGHT)
                        elif event.key == pygame.K_SPACE:
                            # Fire the gun
                            self.hunter.fire_gun(self.maze)
            
            self.handle_input()
            self.update()
            
            # Draw everything
            self.screen.fill(BLACK)
            
            if self.state == GameState.PLAYING or self.state == GameState.LEVEL_COMPLETE:
                self.draw_maze()
                self.draw_items()
                self.hunter.draw(self.screen)
                for wolf in self.wolves:
                    wolf.draw(self.screen)
                self.draw_ui()
                
                if self.state == GameState.LEVEL_COMPLETE:
                    # Semi-transparent overlay
                    overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
                    overlay.set_alpha(128)
                    overlay.fill(BLACK)
                    self.screen.blit(overlay, (0, 0))
                    self.draw_level_complete()
            
            elif self.state == GameState.MENU:
                self.draw_menu()
            elif self.state == GameState.GAME_OVER:
                self.draw_game_over()
            
            pygame.display.flip()
            self.clock.tick(FPS)
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()
