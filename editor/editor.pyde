WIDTH = 1800
HEIGHT = 1200
FONT_SIZE = 22

BACKGROUND = color(255, 255, 255)

class Vector2D():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class TextBox():
    def __init__(self, x, y):
        self.string = ''
        self.cursor = 0
        self.pos = Vector2D(x, y)

    def type(self, c):
        self.string = self.string[:self.cursor] + c + self.string[self.cursor:]
        self.cursor += 1

    def left(self):
        self.cursor -= 1
        self.cursor = max(0, self.cursor)
    
    def right(self):
        self.cursor += 1
        self.cursor = min(self.cursor, len(self.string))

    def backspace(self):
        if len(self.string) > 0:
            self.string = self.string[:len(self.string)-1]
    
    def space(self):
        self.type(' ')
    
    def draw(self):
        fill(0)
        text("|1|" + self.string[:self.cursor] + "|" + self.string[self.cursor:], self.pos.x, self.pos.y)
        
textbox = TextBox(0, FONT_SIZE)

def setup():
    size(WIDTH, HEIGHT)
    textAlign(LEFT)
    textSize(FONT_SIZE)

def draw():
    background(BACKGROUND)
    textbox.draw()

def keyTyped():
    if (key >= 'A' and key <= 'Z') or (key >= 'a' and key <= 'z') or (key >= '0' and key <= '9') or key in [':']:
        textbox.type(str(key))
    elif key == BACKSPACE:
        textbox.backspace()
    elif key == ' ':
        textbox.space()

def keyPressed():
    if keyCode == LEFT:
        textbox.left()
    elif keyCode == RIGHT:
        textbox.right()
