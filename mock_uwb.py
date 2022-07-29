from matplotlib.pyplot import draw
import pygame
import math
import statistics
import random

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
anchor1 = [200, 200]
anchor2 = [1160, 200]
anchor3 = [1160, 770]
anchor4 = [200, 770]

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
    
def extend_line(line):
    p1, p2 = line
    mul = 40
    x = p2[0]-p1[0]
    y = p2[1]-p1[1]
    p2[0] += 40*x
    p2[1] += 40*y
    p1[0] -= 40*x
    p1[1] -= 40*y
    return p1, p2

def lineLineIntersect(P0, P1, Q0, Q1):  
    d = (P1[0]-P0[0]) * (Q1[1]-Q0[1]) + (P1[1]-P0[1]) * (Q0[0]-Q1[0]) 
    if d == 0:
        return None
    t = ((Q0[0]-P0[0]) * (Q1[1]-Q0[1]) + (Q0[1]-P0[1]) * (Q0[0]-Q1[0])) / d
    u = ((Q0[0]-P0[0]) * (P1[1]-P0[1]) + (Q0[1]-P0[1]) * (P0[0]-P1[0])) / d
    if 0 <= t <= 1 and 0 <= u <= 1:
        return round(P1[0] * t + P0[0] * (1-t)), round(P1[1] * t + P0[1] * (1-t))
    return None

def draw_set_up():
    draw_dot(anchor1)
    draw_dot(anchor2)
    draw_dot(anchor3)
    draw_dot(anchor4)
    draw_line(anchor1, anchor2, black)
    draw_line(anchor2, anchor3, black)
    draw_line(anchor3, anchor4, black)
    draw_line(anchor4, anchor1, black)
    
# the main loop
def main(err = 25, show_debug = False): 
    run = True
    new_point = True
    d1 = d2 = d3 = d4 = 0
    count = 0
    diff = []
    tag = [random.randint(200, 1160), random.randint(200, 770)]
    
    while run:
        timer.tick(200)
        screen.fill(white)
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            elif event.type == pygame.KEYDOWN: # randomly generate a new tag position if the enter key is pressed
                if event.key == pygame.K_RETURN:
                    tag = [random.randint(200, 1160), random.randint(200, 770)]
                    new_point = True
                    
        # draw anchor spots and outer frame
        draw_set_up()
        draw_dot(tag)
    
        # calculate the distance and apply some deviation
        if new_point:
            d1 = random.randint(-err, err)
            d2 = random.randint(-err, err)
            d3 = random.randint(-err, err)
            d4 = random.randint(-err, err)
            
        r1 = get_distance( tag, anchor1) + d1
        r2 = get_distance( tag, anchor2) + d2
        r3 = get_distance( tag, anchor3) + d3
        r4 = get_distance( tag, anchor4) + d4
        
        p1, p2 = extend_line(get_cirlce_collision(r1, r2, anchor1, anchor2))
        p3, p4 = extend_line(get_cirlce_collision(r2, r3, anchor2, anchor3))
        p5, p6 = extend_line(get_cirlce_collision(r1, r3, anchor1, anchor3))
        p = lineLineIntersect(p1, p2, p3, p4)
        if p != None:
            draw_dot(p, dark_gray)
            pass
        else:
            new_point = True
            continue
        
    
        # draw the predicted tag position
        if new_point:
            min_x = p[0] - 50
            max_x = p[0] + 50
            min_y = p[1] - 100
            max_y = p[1] + 100
            if min_x < 200:
                min_x = 200
            if max_x > 1160:
                max_x = 1160
            if min_y < 200:
                min_y = 200
            if max_y > 770:
                max_y = 770   
            predicted_x = None
            predicted_y = None
            min_dis = None
            for i in range(min_x, max_x, 10):
                for j in range(min_y, max_y, 10):
                    temp = (get_distance((i, j), anchor1) - r1)**2 + (get_distance((i, j), anchor2) - r2)**2 + (get_distance((i, j), anchor3) -r3)**2 + (get_distance((i, j), anchor4) - r4)**2
                    if min_dis == None or temp <= min_dis:
                        min_dis = temp
                        predicted_x = i
                        predicted_y = j
        d = get_distance((predicted_x, predicted_y), tag)
        diff.append(d)
        draw_dot((predicted_x, predicted_y), gold)  
        
        if show_debug:
            draw_line(p1, p2, dark_gray)
            draw_line(p3, p4, dark_gray)
            draw_line(p5, p6, dark_gray)
            draw_circle(anchor1, r1, red)
            draw_circle(anchor2, r2, green)
            draw_circle(anchor3, r3, blue)
            
        pygame.display.flip()
        new_point = False
        # count += 1
        # if count == 100:
        #     break;
    return statistics.mean(diff)
    
if __name__ == "__main__":
    main()     
        

    
    
    
    
