#Importing libraries
import pygame
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from tkinter import messagebox

class pixel(object):
    def __init__(self, x, y, height, width):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = (255, 255,255)
        self.neighbours = []
        
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.x+self.width, self.y+self.height))
        
    def getNeighbours(self, g):
        j = self.x // 20
        i = self.y // 20
        rows = 28
        cols = 28
        
        #right neighbour
        if i < cols - 1:
            self.neighbours.append(g.pixels[i+1][j])
        #left neighbour
        if i > 0:
            self.neighbours.append(g.pixels[i-1][j])
        #top neighbour
        if j < rows - 1:
            self.neighbours.append(g.pixels[i][j+1])
        #bottom neighbour
        if j > 0:
            self.neighbours.append(g.pixels[i][j-1])
        # Diagonal neighbors
        # Top Left
        if j > 0 and i > 0:  
            self.neighbours.append(g.pixels[i - 1][j - 1])
        # Bottom Left
        if j + 1 < rows and i > -1 and i - 1 > 0:  
            self.neighbours.append(g.pixels[i - 1][j + 1])
        # Top Right
        if j - 1 < rows and i < cols - 1 and j - 1 > 0:  
            self.neighbours.append(g.pixels[i + 1][j - 1])
        # Bottom Right
        if j < rows - 1 and i < cols - 1:  
            self.neighbours.append(g.pixels[i + 1][j + 1])
            
class grid(object):
    pixels = []
    def __init__(self, row, col, height, width):
        self.rows = row
        self.cols = col
        self.length = row * col
        self.height = height
        self.width = width
        self.generatePixels()
        pass
    
    def draw(self, surface):
        for row in self.pixels:
            for col in row:
                col.draw(surface)
                
    def generatePixels(self):
        x_gap = self.width // self.cols
        y_gap = self.height // self.rows
        self.pixels = []
        
        for r in range(self.rows):
            self.pixels.append([])
            for c in range(self.cols):
                self.pixels[r].append(pixel(x_gap * c, y_gap * r, x_gap, y_gap))
                
        for r in range(self.rows):
            for c in range(self.cols):
                self.pixels[r][c].getNeighbours(self)
        
    def clicked(self, pos):
        t = pos[0]
        w = pos[1]
        g1 = int(t) // self.pixels[0][0].width
        g2 = int(w) // self.pixels[0][0].height
        
        return self.pixels[g2][g1]
    
    def convert_binary(self):
        li = self.pixels
        newMatrix = [[] for x in range(len(li))]

        for i in range(len(li)):
            for j in range(len(li[i])):
                if li[i][j].color == (255,255,255):
                    newMatrix[i].append(0)
                else:
                    newMatrix[i].append(1)

        mnist = tf.keras.datasets.mnist
        (x_train, y_train), (x_test, y_test) = mnist.load_data()
        x_test = tf.keras.utils.normalize(x_test, axis=1)
        for row in range(28):
            for x in range(28):
                x_test[0][row][x] = newMatrix[row][x]

        return x_test[:1]
        
    
def guess(li):
    model = tf.keras.models.load_model('mnist_model.h5')
    
    prediction = model.predict(np.expand_dims(li, axis=3))
    print(prediction[0])
    t = np.argmax(prediction[0])
    print('The model guessed the number is: ', t)
    window = Tk()
    window.withdraw()
    messagebox.showinfo('Prediction! The number predicted is: '+ str(t))
    window.destroy()
    
def main():
    run = True
    
    while run:
        for event in pygame.event.get():   
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                li = g.convert_binary()
                guess(li)
                g.generatePixels()
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                clicked = g.clicked(pos)
                clicked.color = (0,0,0)
                for n in clicked.neighbours:
                    n.color = (0,0,0)

            if pygame.mouse.get_pressed()[2]:
                pos = pygame.mouse.get_pos()
                clicked = g.clicked(pos)
                clicked.color = (255,255,255)
                
        g.draw(screen)
        pygame.display.update()


pygame.init()
height = width = 560
screen = pygame.display.set_mode((height, width))
pygame.display.set_caption("Number guesser")
g = grid(28, 28, height, width)
main()

pygame.quit()
quit()