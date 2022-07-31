# mock_uwb

This project simulates the "three-point fix" method that is widely used to locate a tag's location. 
In theory, by using measured distances between tags and anchor points, we will get only one possible result.

![image](https://user-images.githubusercontent.com/91099638/181723429-83da4c1a-bd42-45ab-8751-2c0dccc3e411.png)

However, in reality, measurment errors might result in three circles having no intersection or many intersections. Therefore, this project aims to solve this problem by finding a best estimated point even if the measured distances results in obscure results.

## Set Up

Randomly generate a dot in the frame and calculate the distance betwene the dot and three anchors. 
![image](https://user-images.githubusercontent.com/91099638/181673711-8d8d35b1-c9ef-448b-8af0-fa285b35cca6.png)
Randomly add some deviations to each of the three distances to simulate measurement errors in the real world. 
![image](https://user-images.githubusercontent.com/91099638/181674056-b9f50882-0779-447d-9622-069e73ba08bd.png)

## Method

In this project, two methods are used to estimate the position of the tag.

### 1.

The first method is by using geometry methods to get an estimate point D according to the three circles we drew previously.
![test](https://user-images.githubusercontent.com/91099638/181671346-c8d4b1ac-db48-4630-8b4b-4919b429e9cf.jpg)

![image](https://user-images.githubusercontent.com/91099638/181676434-59ddbe8e-4d69-4801-b35c-2fae2b41bd75.png)
![image](https://user-images.githubusercontent.com/91099638/181676450-fb5af378-3ad9-45ea-b98b-713963a3e5e9.png)

### 2.

The second method is to define a loss function $\sum\limits_{i=1}^{3} {(\sqrt{(x-x_i)^2 + (y-y_i)^2} -r_i)}^2$, and assume that $x^\prime$ and  $y^\prime$  in $x^\prime,  \ y^\prime =  argmin_{x,\ y} \sum\limits_{i=1}^{3} {(\sqrt{(x-x_i)^2 + (y-y_i)^2} -r_i)}^2$ is the best point of estimation.

![image](https://user-images.githubusercontent.com/91099638/181676165-d311f871-7723-4980-821b-a2f9a13641e9.png)
![image](https://user-images.githubusercontent.com/91099638/181676177-6e26fa9d-290f-43bc-b17c-86fa4ebbd54d.png)

## Result

The average execution time for executing method 1 a hundred times is around 0.55 second, and the average distance between the calculated point and the actual point is around 23 pixel.

![image](https://user-images.githubusercontent.com/91099638/182017072-9b92b7a2-aabd-41d4-b1cf-d2fad066ac21.png)
(https://github.com/whuang288alex/mock_uwb/blob/main/test_results/method1_test_result.txt)

The average execution time for executing method 2 a hundre times is around 4 seconds, and the average distance between the calculated point and the actual point is around 14 pixel.

![image](https://user-images.githubusercontent.com/91099638/182017052-66874637-c04c-4afa-8bf1-4081f0f6e056.png)
(https://github.com/whuang288alex/mock_uwb/blob/main/test_results/method2_10_test_result.txt)


(A clip that showcases the testing process: https://www.youtube.com/watch?v=7AVO-l16kf0)

## Discussion

As we can clearly see from the results, the points we get from using method 2 is on average much closer to those that we get from method 1. However, the time it takes is also much longer. Therefore, I decided to use method 1 to narrow the scope of possible points and then use method 2 to get the most accurate result.

## Conclusion

The improvement is substantial, as by using this hybrid approach, the average execution time for executing this method 100 times is very closed to that of method 1 (around 0.58 second), and the average distance between the calculated point and the actual point is very closed to that of method (around 14 pixels).

![image](https://user-images.githubusercontent.com/91099638/182016998-07a4044f-3aae-4f90-b2f3-039162d65f51.png)
(https://github.com/whuang288alex/mock_uwb/blob/main/test_results/method3_10_test_result.txt)



