import numpy as np 
'''Classes bundle data and functionality together. 
Creating a new class creates a new type of object, 
allowing new instances of that type to be made.'''

# class Vehicle:
    
#     def __init__(self, age, veh_type= None, brand=None):
#         self.age = age
#         self.veh_type = veh_type
#         self.brand = brand
        
# my_veh = Vehicle(10)
# print(my_veh.age)
# print(my_car)
# print(f"My vehichle is a{my_car.veh_type}, its brand is {my_car.brand}, it is {my_car.age}") 

'''We may want to modify the intormation that is printed when 
we print this object, let us create another special class method'''  

# class Vehicle:
    
#     def __init__(self,age, veh_type, brand):
#         self.age = age
#         self.veh_type = veh_type
#         self.brand = brand
#     def __str__(self): #we will see the output of this function when we print this object
#         return f"This vehicle is a {self.veh_type} its brand is {self.brand}, its age is {self.age} years"
#     def __repr__(self):# we will see the output of this function when we display this object
#         return self.__str__()
#     def production_year(self, current_year = 2023):
#         return current_year - self.age
    

# age = 5
# veh_type = "car"
# brand = "Maruti Suzuki"
# my_car = Vehicle(age, veh_type, brand)
        
# #display(my_car)
# #print(my_car)
# print(my_car.production_year())


# '''Class inheritence
# We may want to create another class what is based on the previous class
# and itherits its features. As our example was creating a class vehicle, 
# we know that there are different type of vehicles, it can be a bicycle, 
# car, motocycle or a truck. They all share some features, but are pretty different objects. 
# We intoruce class inheritance based on the vehicle example:
# '''
# class Car(Vehicle):
#     def __init__(self,age,brand,model):
#         # This allows to get the variables form the supeclass that we inherit from
#         super().__init__(age, "car", brand)
#         self.model = model
        
# age = 15
# brand = "Ford"
# model = "Focus"
# my_car = Car(age, brand, model)
# print(my_car)      
# print(my_car.production_year())
# print(my_car.veh_type)
# print(my_car.model)        
# '''We can override the methods '''

# class Car(Vehicle):
    
#     def __init__(self, age, brand, model):
#         super().__init__(age,"care", brand)
#         self.model = model 
    
#     def __str__(self):  # we will see the output of this function when we print this object
#         return f"The brand of this car is {self.brand}, the model is {self.model} and its age is {self.age} years"          
        
# age = 25
# brand = "Ford"
# model = "Focus"
# my_car = Car(age, brand, model)
# # print(my_car)      


# class polygon:
#     def __init__(self, name, side_lengths):
#         self.name = name
#         self.side_lengths = side_lengths
    
#     def __str__(self):
#         return f"This is polygon is a {self.name} and has the sides with legth {self.side_lengths}"
#     def num_of_sides(self):
#         return len(self.side_lengths)
#     def perimiter(self):
#         return sum(self.side_lengths)
    
# my_traingle = polygon("Triangle",[3,4,5])
# # print(my_traingle)
# # print(my_traingle.num_of_sides)
# # print(my_traingle.perimiter())  
    
# # class Triangle(polygon):
    
# #     def __init__(self, side_lenghts):
# #         self.name = "triangle"
# #         super().__init__(self.name, side_lenghts)    
    
# #     def area(self):
# #         s = self.perimiter()/2
# #         a,b,c = self.side_lengths
# #         return (s * (s-a) * (s-b) * (s-c)) ** 0.5    
    
# class Triangle(polygon):

#     def __init__(self, side_lengths):
#         self.name = "triangle"
#         super().__init__(self.name, side_lengths)

#     def area(self):
#         s = self.perimiter()/2
#         a, b, c = self.side_lengths
#         return (s*(s-a)*(s-b)*(s-c))**(1/2)

    
# my_trinagle = Triangle([1,2,2])
# # print(my_traingle)
# # print(my_traingle.area())    


import matplotlib.pyplot as plt

# data1 = [1,3,5,7,11,13,15]
# data2 = [0.5,0.9, 1.1, 1.3, 1.5, 1.7, 1.9]

# plt.plot(data1, data2)
# plt.show()

# plt.scatter(data1, data2)
# plt.show()

my_first_numpy = np.array([1,10,100, 1000, 10000])
# print(my_first_numpy[0])
# print(my_first_numpy[-1])
# print(my_first_numpy[4])

# two_dim_array = np.array([[1,2,3],[3,4,5]])
# print(two_dim_array.shape)  # 2 is height and 3 is width
# print(two_dim_array.size)  # total number of elements
# print(two_dim_array.ndim)   # To check the number of dimensions of an array we use ``ndim``. 

n =5
array_of_zeros = np.zeros(n)
# print(array_of_zeros)

ex_array = np.array([[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]])
# print(ex_array.shape)  # 2 is height and 3 is width
# print(ex_array.size)  # total number of elements
# print(ex_array.ndim)   # To check the number of dimensions of an array we use ``ndim``. 
# array_of_zeros = np.zeros(50)
# print(array_of_zeros)


r = 7 
value =2 
array_of_same_val = np.full(r, value)
# print(array_of_same_val) 

A=np.arange(0,100,2)
A=np.linspace(0,1, 100)
A = np.arange(1.0, 1.3, 0.1)
# print(A)
# print([10, 20, 13] + [0, 1, 2])
array1 = np.array([10, 20, 13])
array2 = np.arange(3)
# print(array2)

# print(array1 * array2)
# print(np.sin(np.linspace(0,1, 5)))
# print((np.linspace(0,10, 100)))
# print(np.cos(np.linspace(0,10, 100)))
# print(np.sum(np.cos(np.linspace(0,10, 100))))
# print(np.cos(np.linspace(0,10, 100)).sum())
# print(np.mean(np.cos(np.linspace(0,10, 100))))
# print(np.cos(np.linspace(0,10, 100)).std())

# print(np.ones(100).std())
# print(np.max(np.cos(np.linspace(0,10, 100))))
# print(np.array([3.14, 6.28, 12.56]))
# print(np.array([2.72, 6.81, 20.43]))
# print(np.arange([2.72, 6.81, 20.43]) *np.array(3.14, 6.28, 12,56]))
array_lots_decim = np.array([2.33333333333, 3.555555555, 6.88685756464])
n = 3
# print(f"Rounding to {n} decimal places")
# print(np.round(array_lots_decim, n))
# print(array_lots_decim.round(2))
# A= np.linspace(1,100,100)
# print(A)
# B = A[0:49]
# print(B)
# print(B[2:49:3])
# print(B[B>20])
# print(f"Rounding to {n} decimal places")
# print(np.round(A, n))
# print(A.round(3))
# array_with_some_numbers = np.random.randint(0, 100, size=100)
# print(array_with_some_numbers)
# print(array_with_some_numbers[(array_with_some_numbers > 40) & (array_with_some_numbers <= 90) ])
# print(array_with_some_numbers[(array_with_some_numbers > 40) | (array_with_some_numbers <= 90) ])
# cond_less = array_with_some_numbers < 10
# print(array_with_some_numbers[cond_less])
# two_dim_array =  np.random.uniform(0, 100, size = (5, 10))
# print((two_dim_array))
# print(np.sqrt(two_dim_array))
# print(np.sqrt(97.11219701))
# for element in two_dim_array.flat:
#     print("#########")
#     print(f"the element is {element}") 
    
    
# three_dim_array =  np.random.uniform(0, 10, size = (5, 4, 2))    
# print((three_dim_array))
# print(three_dim_array**2)
# for element in three_dim_array.flat:
#     print("#########")
#     print(f"the element is {element}") 
 
# array_unsorted = np.array([10, 5, 3, 13, 15, 1, 20])
# array_sorted = np.sort(array_unsorted)
# print(array_sorted, array_unsorted) 
# some_array = np.random.randint(0,10, size=20)
# some_array1 = np.sort(some_array)
# print(some_array, some_array1)

# array1 = np.array([2, 4, 7])
# array2 = np.array([3, 5, 8])
# concat_arrat = np.concatenate((array1, array2))
# print(concat_arrat)

# def padding(A, k):
#     B=np.zeros(k)
#     return np.concatenate((A,B))
# A= np.array([1, 2 ,3])
# B = padding(A, 3)
# print(padding(A, 3))
old_array = np.array([1, 4, 5])
new_array = np.append(old_array, 99)

print(f"The old array is {old_array}")
print(f"The new array is {new_array}")



A = np.array( [1, 2, 3])
B = np.array([5, 7])
a = 99.
new_array = np.append(A, a)
print(new_array)
new_array = np.concatenate(new_array,B)
print(new_array)
new_array = np.append(a)
print(new_array)
