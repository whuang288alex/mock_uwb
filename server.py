import socket
from datetime import datetime
import pygame
import math
import statistics
import random
import sys
import threading

pygame.init()
screen  = pygame.display.set_mode([1600, 900])
timer = pygame.time.Clock()
red = (255, 0, 0)
green = ( 0,255, 0)
black= ( 0, 0, 0)
white = (255,255,255) 
blue = (54, 166, 215)
gold = (212, 175, 55)
dark_gray = (150,150,150)

# anchor spots
anchor1 = [50, 50]
anchor2 = [850, 50]
anchor3 = [850, 850]
anchor4 = [50, 850]


HOST = '0.0.0.0'
PORT = 7000
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
x = y = 0
run = True


def get_distance(dot1, dot2):
    (x1, y1) = dot1
    (x2, y2) = dot2
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def get_cirlce_collision(r1, r2, center1, center2):
    d = get_distance(center1, center2)
    x1, y1  = center1
    x2, y2  = center2
    # a is the distance between the middle point and the center of circle 1
    a = (r1**2 -r2**2 + d**2) / (2*d)
    center_x = x1 + a/d * (x2 - x1) 
    center_y = y1 + a/d * (y2 - y1) 
    
    h = math.sqrt(abs(r1**2 - a**2))
    c1 = [round(center_x - (h/d) * (y2-y1), 2), round(center_y + (h/d) * (x2-x1), 2)]
    c2 = [round(center_x + (h/d) * (y2-y1), 2), round(center_y - (h/d)* (x2-x1), 2)]
    return c1, c2

def draw_dot(dot, color = blue):
    pygame.draw.circle(screen, color, dot, 5, 0)

def draw_circle(dot, r, color = blue):
    pygame.draw.circle(screen, color, dot, r, 2)

def draw_line(dot1, dot2, color = blue):
    pygame.draw.line(screen, color, dot1, dot2, 2)

def draw_set_up():
    draw_dot(anchor1)
    draw_dot(anchor2)
    draw_dot(anchor3)
    draw_dot(anchor4)
    draw_line(anchor1, anchor2, black)
    draw_line(anchor2, anchor3, black)
    draw_line(anchor3, anchor4, black)
    draw_line(anchor4, anchor1, black)
    
def read():
    global x, y, run
    r = [-1] * 4
    print('server start at: %s:%s' % (HOST, PORT))
    print('wait for connection...')
    pre = datetime.now()
    
    while True:
        indata, addr = s.recvfrom(1024)
        indata = indata.decode("utf-8")
        data = indata.split(" ")
        
        if data[0] == "0":
            index = int(data[1])
            distance = float(data[2])
            if distance != 0:
                r[index] = distance * 4
            
        if r[2] != -1 and r[1] != -1:
            curr = datetime.now()
            print((curr-pre).total_seconds())
            pre = curr
        
            c1 , c2 = get_cirlce_collision(r[1], r[2], anchor1, anchor2)
            if c1[1] > 50:
                x = c1[0]
                y = c1[1]
            else:
                x = c2[0]
                y = c2[1]
                
            r = [-1] * 4 
        
        print("receive: ", data[0], data[1], data[2])
        print("current r1: {}, r2: {}".format(r[1], r[2]))
        
        if run == False:
            break

def main():
    global x, y, run
    
    
    
    t = threading.Thread(target = read)
    t.start()
    while True:
        timer.tick(10)
        screen.fill(white)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
       
        if run == False:
            break

        draw_set_up()
        draw_dot((x, y), gold)
        pygame.display.flip()   
    t.join()

if __name__ == "__main__":
    main() 