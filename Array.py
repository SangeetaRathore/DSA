# import numpy as np
# my1DArray = np.array([1,2,3,4,5,6])
# print(my1DArray)
# my2DArray = np.array([[1,2,3,4,5,6],[7,8,9,10,11,12]])
# print(my2DArray)
# print(my2DArray[1][2])
# my3DArray = np.array([[[1,2,3,4,5,6],[7,8,9,10,11,12]],[[101,102,103,104,105,106],[107,108,109,1010,1011,1012]]])
# print(my3DArray)
# print(my3DArray[1][0][0])
# 


# import numpy as np
# my1DArray = np.array([21,12,33,4,55,6])
# print(my1DArray[5])
# my1DArray[5] =100




# Sort the array in ascending order
# my1DArray.sort()
# my1DArray = [1,2,3,4,5,6]
# my1DArray.reverse()
# print(my1DArray)  # Output will be sorted array


# my2DArray=np.insert(my1DArray,0,200)
# print(my2DArray)

# my1DArray.insert(0,300)
# print(my1DArray)


# def ghj(listd):
#          # for i in listd:
#          #          print(i)
#          for i in range(len(listd)):
#                   print(listd[i])
                  
# ghj(myLIst)

# my1DArray = np.array([21,12,33,4,55,6])
# my1DArray = [1,2,3,4,5,6]
# my1DArray.shift()
# # my2DArray=np.insert(my1DArray,6,100)
# print(my1DArray)


#--------------------------------------- def fin(array,target):
#     for i in range(len(array)):
#         for j in range(i+1,len(array)):
#             if array[i]+array[j]==target:
#                 print(i,j)

# mylist = [3,3]
# fin(mylist,6)

# n= int(input("how many day's temperature = "))
# i=1
# count=0
# myList = []
# while i<=n:
#          p=int(input(f"Day {i}'s high temp:"))
#          myList.append(p)
#          # suma+=p
#          i+=1
# suma = sum(myList)
# average = suma/n
# for i in range(n):
#          if myList[i]>average:
#                   count+=1
# print(f"{count}day above average")

# 2. 
# def fin(array,target):
#     for i in range(len(array)):
#         for j in range(i+1,len(array)):
#             if array[i]+array[j]==target:
#                 print(i,j)

# mylist = [3,3]
# fin(mylist,6)
                  
# 3. 
# def findMaxProduct(arra):
#     maxa=0
#     for i in range(len(arra)):
#         for j in range(i+1,len(arra)):
#             p=arra[i]*arra[j]
#             if i==0 and j==1:
#                 maxa=p
#             else:
#                 if p>=maxa:
#                     maxa=p
#     return maxa
                  
                      
        

# arr = [1, 7, 3, 4, 9, 5] 
# print(findMaxProduct(arr))


# def max_product(arr):
#     # arr.sort(reverse=True)
#     # return arr[0]*arr[1]
#     arr.sort()
#     return arr[-1]*arr[-2]
# arr = [1, 7, 3, 4, 9, 5] 
# print(max_product(arr))



# mydic = dict(one = "ino",two = "sangeeta", three="rathore")
# print(mydic)
# # o/p={'one': 'ino', 'two': 'sangeeta', 'three': 'rathore'}

# mydic2 = {"one" : "ino","two" : "sangeeta", "three":"rathore"}
# print(mydic2)
# # o/p={'one': 'ino', 'two': 'sangeeta', 'three': 'rathore'}

# micd = [("one" , "ino"),("two" , "sangeeta"),("three","rathore")]
# mydic3 =dict(micd)
# print(mydic3)

# mydic2 = {"one" : "ino","two" : "sangeeta", "three":"rathore"}
# mydic2["two"] = "vishal"
# mydic2["address"] = "Agra"
# print(mydic2)
# o/p ={'one': 'ino', 'two': 'vishal', 'three': 'rathore', 'address': 'Agra'}

# mydic2 = {"one" : "ino","two" : "sangeeta", "three":"rathore"}
# def treverDic(dicti):
#          for key in dicti:
#                   print(key,dicti[key])

# treverDic(mydic2)


# mydic2 = {"one" : "ino","two" : "sangeeta", "three":"rathore","four":256}
# def treverDic(dicti, value):
#          for key in dicti:
#                   if dicti[key]==value:
#                            return key,value
#          return "this value does not exist"

# print(treverDic(mydic2,256))
# o/p= ('four', 256)

# mydic2 = {"one" : "ino","two" : "sangeeta", "three":"rathore","four":256}
# # it print the delet value
# remove_elemnt = mydic2.pop('two')
# # if we gave wrong key  and want  that its not show error so can give a default value
# print(remove_elemnt)
# print(mydic2)
# # remove_lemnt = mydic2.pop('ten',"wrong")
# # remove_lemnt = mydic2.pop('ten',None)
# print(remove_lemnt)


# mydic2 = {"one" : "ino","two" : "sangeeta", "three":"rathore","four":256}
# remove_elemnt = mydic2.pop('two')
# print(remove_elemnt)
# remove_lemnt = mydic2.popitem()
# # popitem is used to remove  last  key value it store key and value  
# print(remove_lemnt)


# mydic2 = {"one" : "ino","two" : "sangeeta", "three":"rathore","four":256}
# mydic2.clear()
# # clear is used all key value pair and gives empty dictionary
# print(mydic2)

# myNewdic = {}.fromkeys([1,2,3,4], 0)
# print(myNewdic)
# # o/p={1: 0, 2: 0, 3: 0, 4: 0}

# myNewdic = {}.fromkeys([1,2,3,4])
# print(myNewdic)
# # o/p={1: None, 2: None, 3: None, 4: None}


# myDic2 = {"name":"sangeeta", "class":"BCA","Address":"Agra","Age":28}
# # 1 case put the  only key and  wrong its gives answer acc. to key
# print(myDic2.get("Age",200))
# # o/p= 28
# print(myDic2.get("city","banglore"))
# # o/p=banglore
# print(myDic2.get("home"))
# # o/p= None

# myDic2 = {"name":"sangeeta", "class":"BCA","Address":"Agra","Age":28}
# print(myDic2.popitem())
# o/p= ('Age', 28)
# print(myDic2)
#  o/p= {'name': 'sangeeta', 'class': 'BCA', 'Address': 'Agra'}
# print(myDic2.items())

myDic2 = {
         "name":"sangeeta", 
         "class":"BCA",
         "Address":"Agra",
         "Age":28
         }


print("name" in myDic2)
# o/p true
print("Agra" in myDic2)
# o/p false
print("Agra" in myDic2.values())
# o/p true