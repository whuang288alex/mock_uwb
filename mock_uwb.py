from matplotlib.pyplot import draw
import pygame
import math
import statistics
import random
import sys

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
def main(err = 30, show_debug = False, testing = False): 
    run = True
    new_point = True
    d1 = d2 = d3 = d4 = r1 = r2 = r3 = r4 = 0
    count = 0
    diff = []
    tag = [random.randint(200, 1160), random.randint(200, 770)]
    
    while run:
        timer.tick(200)
        screen.fill(white)
        
        if testing == False:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break
                elif event.type == pygame.KEYDOWN: # randomly generate a new tag position if the enter key is pressed
                    if event.key == pygame.K_RETURN:
                        tag = [random.randint(200, 1160), random.randint(200, 770)]
                        new_point = True
        else:
            pygame.event.get()

        # calculate the predicted points
        if new_point:
            r1 = get_distance( tag, anchor1) + random.randint(-err, err)
            r2 = get_distance( tag, anchor2) + random.randint(-err, err)
            r3 = get_distance( tag, anchor3) + random.randint(-err, err)
            r4 = get_distance( tag, anchor4) + random.randint(-err, err)

            # get the raw estimation
            temp_x = int(get_cirlce_collision(r1, r2, anchor1, anchor2)[0][0])
            temp_y = int(get_cirlce_collision(r2, r3, anchor2, anchor3)[0][1])

            # define the scope where the point is possibly at
            min_x = temp_x - 50 if temp_x - 50 > 200 else 200
            max_x = temp_x + 50 if temp_x + 50 < 1160 else  1160
            min_y = temp_y - 100 if temp_y - 100 > 200 else 200
            max_y = temp_y + 100 if temp_y + 100 < 770 else 770

            # calculate the predicted point
            predicted_x = predicted_y = min_dis = None
            for i in range(min_x, max_x, 10):
                for j in range(min_y, max_y, 10):
                    temp = (get_distance((i, j), anchor1) - r1)**2 + (get_distance((i, j), anchor2) - r2)**2 + (get_distance((i, j), anchor3) -r3)**2 + (get_distance((i, j), anchor4) - r4)**2
                    if min_dis == None or temp <= min_dis:
                        min_dis = temp
                        predicted_x = i
                        predicted_y = j

        # draw the results, show the lines for debug purpose if needed
        if show_debug:
            draw_line((temp_x, 0), (temp_x, 900), dark_gray)
            draw_line((0, temp_y), (1600,temp_y),  dark_gray)
            draw_circle(anchor1, r1, red)
            draw_circle(anchor2, r2, green)
            draw_circle(anchor3, r3, blue)
        draw_set_up()
        draw_dot(tag)
        draw_dot((temp_x,temp_y), dark_gray)
        draw_dot((predicted_x, predicted_y), gold)
        pygame.display.flip()
        
        
        if testing == True:
            # draw the predicted point and calculate the distance between it and the actual point
            d = get_distance((predicted_x, predicted_y), tag)
            diff.append(d)
            # reset the tag
            tag = [random.randint(200, 1160), random.randint(200, 770)]
            count += 1
            new_point = True
            if count == 100:
                break
        else:
            new_point = False
    return statistics.mean(diff)
    
if __name__ == "__main__":
    main()     
        

    
    
    
    
