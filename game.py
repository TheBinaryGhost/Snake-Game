import tkinter as tk
import random

class SnakeGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Snake Game")
        self.canvas = tk.Canvas(self.master, width=400, height=400, bg="black")
        self.canvas.pack()

        self.snake = [(200, 200), (210, 200), (220, 200)]
        self.food = self.create_food()
        self.direction = "Left"
        self.score = 0
        self.score_text = None

        self.bind_keys()
        self.draw_snake()
        self.draw_food()
        self.move_snake()

    def bind_keys(self):
        self.master.bind("<KeyPress-Up>", self.go_up)
        self.master.bind("<KeyPress-Down>", self.go_down)
        self.master.bind("<KeyPress-Left>", self.go_left)
        self.master.bind("<KeyPress-Right>", self.go_right)
        self.master.bind("<KeyPress-Escape>", self.quit_game)

    def draw_snake(self):
        self.canvas.delete("snake")
        for segment in self.snake:
            self.canvas.create_rectangle(segment[0], segment[1], segment[0]+10, segment[1]+10, fill="green", tags="snake")

    def draw_food(self):
        self.canvas.delete("food")
        self.food = self.create_food()
        self.canvas.create_oval(self.food[0], self.food[1], self.food[0]+10, self.food[1]+10, fill="red", tags="food")

    def create_food(self):
        while True:
            x = random.randint(0, 39) * 10
            y = random.randint(0, 39) * 10
            if (x, y) not in self.snake:
                return x, y

    def move_snake(self):
        head = self.snake[0]
        if self.direction == "Up":
            new_head = (head[0], head[1] - 10)
        elif self.direction == "Down":
            new_head = (head[0], head[1] + 10)
        elif self.direction == "Left":
            new_head = (head[0] - 10, head[1])
        elif self.direction == "Right":
            new_head = (head[0] + 10, head[1])

        if new_head == self.food:
            self.snake.insert(0, new_head)
            self.score += 1
            self.draw_food()
            self.move_snake()  # Continue moving the snake after eating food
        elif 0 <= new_head[0] < 400 and 0 <= new_head[1] < 400 and new_head not in self.snake[1:]:
            self.snake.insert(0, new_head)
            if new_head != self.food:
                self.snake.pop()
            self.draw_snake()
            self.master.after(100, self.move_snake)
        else:
            self.game_over()

    def game_over(self):
        self.score_text = self.canvas.create_text(200, 200, text=f"Game Over! Score: {self.score}", fill="white", font=("Helvetica", 20))
        self.master.bind("<KeyPress-Return>", self.restart_game)

    def restart_game(self, event):
        self.master.unbind("<KeyPress-Return>")
        if self.score_text:
            self.canvas.delete(self.score_text)
        self.snake = [(200, 200), (210, 200), (220, 200)]
        self.food = self.create_food()
        self.direction = "Left"
        self.score = 0
        self.draw_snake()
        self.draw_food()
        self.move_snake()

    def quit_game(self, event):
        self.master.destroy()

    def go_up(self, event):
        if self.direction != "Down":
            self.direction = "Up"

    def go_down(self, event):
        if self.direction != "Up":
            self.direction = "Down"

    def go_left(self, event):
        if self.direction != "Right":
            self.direction = "Left"

    def go_right(self, event):
        if self.direction != "Left":
            self.direction = "Right"

# Create the main window and start the game
if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()