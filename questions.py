# sum of digit
'''
def sumOfDigit(n):
         assert n>=0 and int(n)==n,'the number should be positive integer' 
         if n==0:
                  return 0
         else:
                  return n%10 + sumOfDigit(n//10)
         
print(sumOfDigit(5678001))
# sangeeta

# hhuvybhhnm
'''

# fibonacci series
'''
def fibonacci(n):
         assert n>=0 and int(n)==n,'the number should be positive integer'
         if n in [0,1]:
                  return n
         else:
                  return fibonacci(n-1) +  fibonacci(n-2)
print(fibonacci(8))

'''

# sum of n number
'''
def sumOfNum(n):
         assert n>=0 and int(n)==n,'its not a positive integer'
         if n in [0,1]:
                  return n
         else:
                  return sumOfNum(n-1)+n
print(sumOfNum(500))

'''

# power
'''
def power(base,exponent):
         if exponent==0:
                  return 1
         elif exponent<0:
                  return 1/base * power(base,exponent+1)
         else:
                  return base * power(base,exponent-1)
print(power(2,-1))

'''   

# product of array
'''
def proOfArray(simple_array) :
            if not simple_array:
                     return 1
            else:
                     return  simple_array[0] * proOfArray(simple_array[1:])
            
arra1=[1,1,1,100]
print(proOfArray(arra1))

'''
# 
import numpy as np
my_array = np.array([[1,2,4],[11,12,14],[101,102,104]])
# print(my_array)
         
# new_column = np.array([[1],[2],[4],[5]])
# newMyArray = np.insert(my_array,0,[[10,20,30]],axis=1)  
newMyArray = np.append(my_array,[[10,20,30]],axis=0)       
# print(newMyArray)


my_array = np.array([[1,2,4],[11,12,14],[101,102,104]])
def accessElements(array, rowIndex,colIndex):
         if rowIndex >=len(array) or colIndex>=len(array[0]):
                  print('Incorrect index')
         else:
                  print(array[rowIndex][colIndex])
                  
                  
# accessElements(my_array,1,1)


# def traversalArray(array):
#          for i in range(len(array)):
#                   for j in range(len(array[0])):
#                            print(array[i][j])
                           
                           
# traversalArray(my_array)
# my1Darray=np.array([1,2,3,6,7,7])
# print(len(my1Darray))

# my1Darray=np.array([[1,2,3,6,7],[12,122,123,1234,13456],[211,311,4111,56,0]])
def searchElement(array1,target):
         for i in range(len(array1)):
                  for j in range(len(array1[0])):
                           if array1[i][j]==target:
                                    return 'yes'
         return 'no'

# print(searchElement(my1Darray,100))


# my1Darray=np.array([[1,2,3,6,7],[12,122,123,1234,13456],[211,311,4111,56,0]])
# print(my1Darray)
# myNewArray =np.delete(my1Darray,0,axis=1)
# print(myNewArray)


my_list = [1,2,3,4,5,6,7]
# for i in range(len(my_list)):
#         #  print(my_list[i])
# #  comment any one of these before run
# for i in my_list:
#         #  print(i)
         
         
# enumerate helps to get index with value in for loop
# def search(array,target):
#     for i,value in enumerate(array):
#         if value == target:
#             return i
#     return -1
    
# print(search(my_list,6))


# a=[0,1]
# b=a*4
# print(b)
# [0, 1, 0, 1, 0, 1, 0, 1] o/p


# a= [1,2,3,4,5,6,7,8,9]
# print(sum(a))
# 45 o/p

# a="sangeeta-rathore"
# b=a.split("-")
a="sangeetashivanshrathore"
# b="-"
delr = "#"
b=a.split(delr)
# print(b)
# b=a.split()
asa=delr.join(a)
# o/p ['sangeeta', 'rathore']
# print(type(asa))
# print(asa)



import numpy as np
myArray =np.array([1,2,3,4,5,6])
mtList =[1,2,3,4,5,6]
print(myArray/2)
#  o/p = [0.5 1.  1.5 2.  2.5 3. ]
print(mtList/2)
#   give error