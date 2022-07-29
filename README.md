# mock_uwb

This project simulate three-point fix method that is widely used to locate a tags' location. 
In theory, by using measured distances between tags and anchor points, we will get only one possible result.

![image](https://user-images.githubusercontent.com/91099638/181723429-83da4c1a-bd42-45ab-8751-2c0dccc3e411.png)

However, in reality, measurment errors might result in three circles having no intersection or many intersections. Therefore, this project aims to solve this problem by finding a best estimated point even if the measured distances results in obscure result.

## Set Up

Randomly generate a dot in the frame and calculate the distance betwene the dot and three anchors. 
![image](https://user-images.githubusercontent.com/91099638/181673711-8d8d35b1-c9ef-448b-8af0-fa285b35cca6.png)
Randomly add some deviation on each of the three distances to simulate measurement errors in the real world. 
![image](https://user-images.githubusercontent.com/91099638/181674056-b9f50882-0779-447d-9622-069e73ba08bd.png)

## Method

In this project, two methods are used to estimate the position of the point.

### 1.
The first method is by using geometry methods to get an estimate point D according to the three circles we drew previously.
![test](https://user-images.githubusercontent.com/91099638/181671346-c8d4b1ac-db48-4630-8b4b-4919b429e9cf.jpg)

![image](https://user-images.githubusercontent.com/91099638/181676434-59ddbe8e-4d69-4801-b35c-2fae2b41bd75.png)
![image](https://user-images.githubusercontent.com/91099638/181676450-fb5af378-3ad9-45ea-b98b-713963a3e5e9.png)



### 2.
The second method is to define a loss function and assume that x* and y* in $ \sum_{k=1}^n \sqrt{{(x-x_i)^2 + (y-y_i)^2}-r_i} $ is the best point of estimation.


![image](https://user-images.githubusercontent.com/91099638/181678668-8d3e6383-a654-463e-9f7d-368bde5fd532.png)



![image](https://user-images.githubusercontent.com/91099638/181678303-ae47d3a3-c7f2-4e1b-a4d8-e58ecb6a0a1f.png) 

 
 


![image](https://user-images.githubusercontent.com/91099638/181676136-401e0b28-cb09-4a97-82ea-9bdd0da7349a.png)
![image](https://user-images.githubusercontent.com/91099638/181676165-d311f871-7723-4980-821b-a2f9a13641e9.png)
![image](https://user-images.githubusercontent.com/91099638/181676177-6e26fa9d-290f-43bc-b17c-86fa4ebbd54d.png)



