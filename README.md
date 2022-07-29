# mock_uwb

![image](https://user-images.githubusercontent.com/91099638/181670116-0d870530-a54e-4392-9e5b-d83de24648e2.png)

## Set Up

Randomly generate a dot in the frame and calculate the distance betwene the dot and three anchors. 
![image](https://user-images.githubusercontent.com/91099638/181673711-8d8d35b1-c9ef-448b-8af0-fa285b35cca6.png)
Randomly add some deviation on each of the three distances to simulate measurement errors in the real world. 
![image](https://user-images.githubusercontent.com/91099638/181674056-b9f50882-0779-447d-9622-069e73ba08bd.png)

## Method

In this project, two methods are used to estimate the position of the point.

# 1.
The first method is by using geometry methods to get an estimate point D according to the three circles we drawn previously.
![test](https://user-images.githubusercontent.com/91099638/181671346-c8d4b1ac-db48-4630-8b4b-4919b429e9cf.jpg)

Point D is the gray dot) in the pictures.
![image](https://user-images.githubusercontent.com/91099638/181676434-59ddbe8e-4d69-4801-b35c-2fae2b41bd75.png)
![image](https://user-images.githubusercontent.com/91099638/181676450-fb5af378-3ad9-45ea-b98b-713963a3e5e9.png)



# 2.
The second method is to define a loss function
![image](https://user-images.githubusercontent.com/91099638/181675281-761f8c40-1065-4ff7-afbb-602e83511c74.png)

and assume that x* .and y* in ![image](https://user-images.githubusercontent.com/91099638/181675239-a92e2f83-649d-4818-b5cb-e46fcd88000b.png) is the best point of estimation. 

(x*, y*) is the golden point in the pictures.

![image](https://user-images.githubusercontent.com/91099638/181676136-401e0b28-cb09-4a97-82ea-9bdd0da7349a.png)
![image](https://user-images.githubusercontent.com/91099638/181676165-d311f871-7723-4980-821b-a2f9a13641e9.png)
![image](https://user-images.githubusercontent.com/91099638/181676177-6e26fa9d-290f-43bc-b17c-86fa4ebbd54d.png)



