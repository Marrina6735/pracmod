import tkinter
import random
import canvas

WIDTH = 600 # Исходные данные
HEIGHT = 400
BG_COLOR = 'white' # Фоновый цвет
M_RADIUS = 30
M_COLOR = 'blue'
INIT_DX = 2
INIT_DY = 2
S_BALL = 20 # Скорость шаров
MAX_RADIUS = 30
MIN_RADIUS = 15
BAD_COLOR = 'red'
COLORS = ['orange', 'green', 'yellow', 'aqua', 'purple']
NUM_OF_BALLS = 5
RED_NUM_OF_BALLS = 3

class Balls(): # Класс шар
    def __init__(self, x, y, r, color, dx=0, dy=0): # Метод конструктора
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.dx = dx
        self.dy = dy
    def draw(self): # Рисует шар
        canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r,
                        fill=self.color, outline=BG_COLOR)
    def hide(self): # Функция очистки шара
        canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r,
                        fill=BG_COLOR, outline=BG_COLOR)
    def is_collision(self, ball): # Функция столкновения
        a = abs(self.x + self.dx - ball.x)
        b = abs(self.y + self.dy - ball.y)
        return (a*a + b*b)**0.5 <= self.r + ball.r
    def move(self): # Функция движения шара
        if (self.x + self.r + self.dx >= WIDTH) or (self.x - self.r + self.dx <= 0): # Столкновения со стеной
            self.dx = - self.dx
        if (self.y + self.r + self.dy >= HEIGHT) or (self.y - self.r + self.dy <= 0):
            self.dy = - self.dy
        for ball in balls: # Столкновения с шарами
            if self.is_collision(ball):
                if ball.color != BAD_COLOR:
                    ball.hide()
                    balls.remove(ball)
                    self.dx = - self.dx
                    self.dy = - self.dy
                else:
                    self.dx = self.dy = 0
        self.hide()
        self.x += self.dx
        self.y += self.dy
        self.draw()
    def red_move(self): # Опасные красные шары
        if (self.x + self.r + self.dx >= WIDTH) or (self.x - self.r + self.dx <= 0): # Столкновения со стеной
            self.dx = - self.dx
        if (self.y + self.r + self.dy >= HEIGHT) or (self.y - self.r + self.dy <= 0):
            self.dy = - self.dy
        for ball in balls: # Столкновения с шарами
            if ball != self:
                if self.is_collision(ball):
                    self.dx = - self.dx
                    self.dy = - self.dy
        self.hide()
        self.x += self.dx
        self.y += self.dy
        self.draw()

def mouse_click(event): # Функция клика мыши
    global main_ball
    if event.num == 1:
        if 'main_ball' not in globals():
            main_ball = Balls(event.x, event.y, M_RADIUS, M_COLOR, INIT_DX, INIT_DY)
            main_ball.draw()
        else: # Поворот налево
            if main_ball.dx * main_ball.dy > 0:
                main_ball.dy = - main_ball.dy
            else:
                main_ball.dx = - main_ball.dx
    elif event.num == 3: # Поворот направо
        if main_ball.dx * main_ball.dy > 0:
            main_ball.dx = - main_ball.dx
        else:
            main_ball.dy = - main_ball.dy

def create_list_of_balls(number, red_num): # Список шаров
    list = []
    while len(list) < number:
        next_ball = Balls(random.choice(range(MAX_RADIUS, WIDTH-MAX_RADIUS)),
                          random.choice(range(MIN_RADIUS, HEIGHT-MIN_RADIUS)),
                          random.choice(range(MIN_RADIUS, MAX_RADIUS)),
                          random.choice(COLORS))
        list.append(next_ball)
        next_ball.draw()
    while len(list) < number + red_num:
        next_ball = Balls(random.choice(range(MAX_RADIUS, WIDTH - MAX_RADIUS)),
                         random.choice(range(MIN_RADIUS, HEIGHT - MIN_RADIUS)),
                         random.choice(range(MIN_RADIUS, MAX_RADIUS)),
                         BAD_COLOR, 2, 2)
        list.append(next_ball)
        next_ball.draw()
    return list

def count_bad_balls(list_of_balls): #Функция подсчета опасных шаров
    result = 0
    for ball in list_of_balls:
        if ball.color == BAD_COLOR:
            result += 1
    return result

def main(): # Главная функция
    if 'main_ball' in globals():
        main_ball.move()
        for ball in balls:
            ball.red_move()
        if len(balls) - num_of_bad_balls == 0:
            canvas.create_text(WIDTH / 2, HEIGHT / 2, text='YOU WON', font='Arial 40', fill='green')
            main_ball.dx = main_ball.dy = 0
        elif main_ball.dx == 0:
            canvas.create_text(WIDTH / 2, HEIGHT / 2, text='YOU LOSE', font='Arial 40', fill='red')

    root.after(S_BALL, main)

root = tkinter.Tk() # Создаем окно игры
root.title('Balls')
canvas = tkinter.Canvas(root, width=WIDTH, height=HEIGHT, bg=BG_COLOR)
canvas.pack() # открываем экран
canvas.bind('<Button-1>', mouse_click) # Захват курсора
canvas.bind('<Button-3>', mouse_click, '+')
balls = create_list_of_balls(NUM_OF_BALLS, RED_NUM_OF_BALLS)
num_of_bad_balls = count_bad_balls(balls)
main()
root.mainloop() # закрываем экран