import random
import pygame
import sys

# global variables
WIDTH = 24
HEIGHT = 24
SIZE = 20
SCREEN_WIDTH = WIDTH * SIZE
SCREEN_HEIGHT = HEIGHT * SIZE

DIR = {
    'u' : (0, -1), # north is -y
    'd' : (0, 1),
    'l' : (-1,0),
    'r' : (1,0)
}

green = (0,255,0)
blue = (0,0,255)

class Snake(object):
    l = 1
    body = [(WIDTH // 2, HEIGHT // 2)]
    direction = 'r'
    dead = False
    change_length = False
    moving = False

    def __init__(self):
        pass
    
    def get_color(self, i):
        hc = (40,50,100)
        tc = (90,130,255)
        return tuple(map(lambda x,y: (x * (self.l - i) + y * i ) / self.l, hc, tc))

    def get_head(self):
        return self.body[0]

    def turn(self, dir):
        self.direction = dir

    def collision(self, x, y):
        if x < 0 or x > 23 or y < 0 or y > 23:
            return True
        if (x,y) in self.body[1:]:
            return True
        return False

    def get_body(self):
        return self.body
    
    def coyote_time(self):
        # TODO: See section 13, "coyote time".
        pass

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i] = self.body[i-1]

        self.body[0] = tuple(map(lambda i, j: i + j, self.body[0], DIR[self.direction]))

        if self.collision(self.body[0][0], self.body[0][1]):
            self.kill()
        
        tail = self.body[len(self.body) - 1]
        
        if self.change_length:
            self.change_length = False
            self.body.append(tail)


    def kill(self):
        # TODO: See section 11, "Try again!"
        self.dead = True

    def draw(self, surface):
        for i in range(len(self.body)):
            p = self.body[i]
            pos = (p[0] * SIZE, p[1] * SIZE)
            r = pygame.Rect(pos, (SIZE, SIZE))
            pygame.draw.rect(surface, self.get_color(i), r)

    def handle_keypress(self, k):
        if k == pygame.K_UP:
            self.turn('u')
        if k == pygame.K_DOWN:
            self.turn('d')
        if k == pygame.K_LEFT:
            self.turn('l')
        if k == pygame.K_RIGHT:
            self.turn('r')
    
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type != pygame.KEYDOWN:
                continue
            self.handle_keypress(event.key)
    
    def wait_for_key(self):
        #Implementing Feature 10
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    self.moving = True
                    return


# returns an integer between 0 and n, inclusive.
def rand_int(n):
    return random.randint(0, n)

class Apple(object):
    position = (10,10)
    color = (233, 70, 29)
    def __init__(self):
        self.place([])

    def place(self, snake):
        x_pos = rand_int(23)
        y_pos = rand_int(23)
        while (x_pos, y_pos) in snake:
            x_pos = rand_int(23)
            y_pos = rand_int(23)
        self.position = (x_pos, y_pos)

    def draw(self, surface):
        pos = (self.position[0] * SIZE, self.position[1] * SIZE)
        r = pygame.Rect(pos, (SIZE, SIZE))
        pygame.draw.rect(surface, self.color, r)

def draw_grid(surface):
    for y in range(0, HEIGHT):
        for x in range(0, WIDTH):
            r = pygame.Rect((x * SIZE, y * SIZE), (SIZE, SIZE))
            color = (169,215,81) if (x+y) % 2 == 0 else (162,208,73)
            pygame.draw.rect(surface, color, r)

def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    draw_grid(surface)
    

    snake = Snake()
    apple = Apple()

    score = 0
        
    snake.wait_for_key()
    #white = (255, 255, 255) 
    #green = (0, 255, 0) 
    #blue = (0, 0, 128)  
    #X = 40
    #Y = 40
    #display_surface = pygame.display.set_mode((X, Y )) 
    #pygame.display.set_caption('Show Text') 
    #font = pygame.font.Font('freesansbold.ttf', 32) 
    #text = font.render('Score: %d' % score, True, green, blue) 
    #textRect = text.get_rect()  
    #textRect.center = (X // 2, Y // 2) 
  

    while True:
        #Implements Feature 9
        length = len(snake.get_body())
        clock.tick(5 + int(0.1 * length))
        snake.check_events()
        draw_grid(surface)
        snake.move()

        snake.draw(surface)
        apple.draw(surface)
        if snake.get_head() == apple.position:
            print("Snake at an apple!")
            apple.place(snake.get_body())
            snake.change_length = True
            score += 1
        screen.blit(surface, (0,0))

        # TODO: see section 8, "Display the Score"
        
        #display_surface.fill(white) 
        #display_surface.blit(text, textRect)

        pygame.display.update()
        if snake.dead:
            print('You died. Score: %d' % score)
            pygame.quit()
            sys.exit(0)


if __name__ == "__main__":
    main()

