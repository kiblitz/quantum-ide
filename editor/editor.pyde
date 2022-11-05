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
        self.string = ['']
        self.cursor = 0
        self.max_cursor = 0
        self.line = 0
        self.pos = Vector2D(x, y)

    def type(self, c):
        self.string[self.line] = self.string[self.line][:self.cursor] + c + self.string[self.line][self.cursor:]
        self.cursor += 1
        self.max_cursor += 1

    def left(self):
        self.cursor -= 1
        self.cursor = max(0, self.cursor)
        self.max_cursor = self.cursor
    
    def right(self):
        self.cursor += 1
        self.cursor = min(self.cursor, len(self.string[self.line]))
        self.max_cursor = self.cursor
        
    def down(self):
        if self.line < len(self.string) - 1:
            self.line += 1
            self.cursor = min(self.max_cursor, len(self.string[self.line]))
            
    def up(self):
        if self.line > 0:
            self.line -= 1
            self.cursor = min(self.max_cursor, len(self.string[self.line]))

    def enter(self):
        self.string = self.string[:self.line] + [self.string[self.line][:self.cursor]] + [self.string[self.line][self.cursor:]] + self.string[self.line+1:]
        self.line += 1
        self.cursor = 0
        self.max_cursor = self.cursor

    def backspace(self):
        if self.cursor > 0:
            self.string[self.line] = self.string[self.line][:self.cursor-1] + self.string[self.line][self.cursor:]
            self.cursor -= 1
        elif self.line > 0:
            self.cursor = len(self.string[self.line-1])
            self.string = self.string[:self.line-1] + [self.string[self.line-1] + self.string[self.line]] + self.string[self.line+1:]
            self.line -= 1
        self.max_cursor = self.cursor
    
    def space(self):
        self.type(' ')
    
    def draw(self):
        fill(0)
        for i, string_line in enumerate(self.string):
            if i == self.line:
                text("|" + str(i) + "|" + string_line[:self.cursor] + "|" + string_line[self.cursor:], self.pos.x, self.pos.y + i * FONT_SIZE)
            else:
                text("|" + str(i) + "|" + string_line, self.pos.x, self.pos.y + i * FONT_SIZE)
        
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
    elif key == ENTER:
        textbox.enter()
    elif key == ' ':
        textbox.space()

def keyPressed():
    if keyCode == LEFT:
        textbox.left()
    elif keyCode == RIGHT:
        textbox.right()
    elif keyCode == DOWN:
        textbox.down()
    elif keyCode == UP:
        textbox.up()
