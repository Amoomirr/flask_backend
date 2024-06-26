
#Example of String Operators
X = 'Amir'
leng1 = len(X)
print(leng1)
leng1 = X.upper()
print(leng1)
leng1 = X.lower()
print(leng1)
leng1 = X.replace("ir",'oo')
print(leng1)
leng1 = X.find('mir')
print(leng1)
leng1 = X.split("i")
print(leng1)


#Example of DataTypes
#1 List
#List items are ordered, changeable, and allow duplicate values. List items are indexed, the first item has index [0], the second item has index [1] etc.
X=['A','M','I','R']#For List we use Square brackets
X[2]='O'
X[3]='O'#Mutable i.e Changeable
print(X)
if "M" in X: #If Else Loop
    print("M, is present")
else :
    print("M, is absent")
X.append('Amoo')#adding data to list
print(X)
del X[4]#deletion of data from the list of index 4 i.e Amoo
print(X)
X.sort()
print(X)

X = 'AMIR'
for i in X:
    print(X)

#2 Tuple
#Tuple items are ordered, unchangeable, and allow duplicate values. Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

X=(('A','M','I','R'))#For tuple we use parantheses
Y=list(X)#For changing data in tuple will have to convert it to list
Y[2]='O'#Changes
Y[3]='O'#Changes
X=tuple(Y) #We converted list back to tuple
print(X)

#3 Set 
#A set is a collection which is unordered, unchangeable, and unindexed.
X={"A","m","i","r"}
print(X)#it will print data iny any sequence as it does not have any index and it is unordered
Y=list(X)
Y[2]='O'
X=set(Y)
print(X)

#4 Dictionary
#Dictionaries are used to store data values in key:value pairs, A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

X={"brand":"Ford", "model":"mustang","year":"1965"}
print(X)
X={"brand":"Ford", "model":"mustang","year":"1965","model":"mustang gt"}#In output model will be overwridden by mustang gt as duplicates are not allowed
print(X["model"])
X = {
  "brand": "Ford",#str
  "electric": False,#boolean
  "year": 1964,#int
  "colors": ["red", "white", "blue"]#list   
}
print(X)