# 2024 project

import customtkinter as ctk

class ColoredMovingPixel:
    def __init__(self, rt):
        self.rt=rt
        # width and height
        self.w=400
        self.h=400
        # x and y coordinates
        self.x=0
        self.y=0
        # Black background
        self.canvas = ctk.CTkCanvas(rt, width=self.w, height=self.h, bg='black')
        self.canvas.pack()
        # Sqaure objects
        self.square = self.canvas.create_rectangle(self.x, self.y, self.x+200, self.y+200, fill='red')
        # Moving position
        self.position = [(0,0), (0,200), (200, 200), (200,0)]
        self.index = 0
        self.move_square()
        
    def move_square(self):
        # Go to position
        xx, yy = self.position[self.index]
        dx = xx - self.x
        dy = yy - self.y
        # Move
        self.canvas.move(self.square, dx, dy)
        # Reassign
        self.x = xx
        self.y = yy
        self.color_pixel()   
        # Remainder
        self.index = (self.index + 1) % len(self.position)
        # Animation and speed
        self.rt.after(50, self.move_square)
        
    # Different colors
    def color_pixel(self):
        if self.x == 0 and self.y == 0:
            self.canvas.itemconfig(self.square, fill='pink')
            
        if self.x == 0 and self.y == 200:
            self.canvas.itemconfig(self.square, fill='green')
            
        if self.x == 200 and self.y == 200:
            self.canvas.itemconfig(self.square, fill='blue')
    
        if self.x == 200 and self.y == 0:
            self.canvas.itemconfig(self.square, fill='orange')
        
        
root = ctk.CTk()
sample = ColoredMovingPixel(root)
root.mainloop()