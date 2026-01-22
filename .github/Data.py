#different variable data types
a = 42
b = 43.675
c = "Hello world"
d = [1, 2, 3]
e = (4,5,7)
f = {6, 8, 9}
g = {"name": "Alive", "age": 24}
h = True

# printing data types
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))

'''
data types
<class 'int'>
<class 'float'>
<class 'str'>
<class 'list'>
<class 'tuple'>
<class 'set'>
<class 'dict'>
<class 'bool'>
'''

#Converting datatypes
num = 10
num_str = str(num) #converts int into string
print(num_str, type(num_str))

str_to_int = int("123") # convert string to int
print(str_to_int, type(str_to_int))

string_tolist = list("Python") #converts string to list
print(string_tolist), type(string_tolist)

'''
results
10 <class 'str'>
123 <class 'int'>
['P', 'y', 't', 'h', 'o', 'n']
'''

#Performing operations based on data types

#numeric operations
x = 15
y = 4
print("Addition:", x + y)
print("Division:", x / y)
print("Floor division:", x // y)

#strings
greeting = "Hello"
name = "Jeff"
print(greeting + ", " + name)

#list and set
my_list = [1, 2, 3]
my_list.append(4)
print("Modified list:", my_list)

my_set = {1, 2, 3}
my_set.add(4)
print("modified set", my_set)

'''
\Results
Addition: 19
Division: 3.75
Floor division: 3
Hello, Jeff
Modified list: [1, 2, 3, 4]
modified set {1, 2, 3, 4}
'''

#key value pairs in dictionaries
#creaating dictionary
person = {"name": "Joe", "age": 23, "city": "New York"}
print(person)

#access a value
print("Name:", person["name"])

#modify a value
person["age"] = 26
print("updated age:", person["age"])

#adding a value
person["profession"] = "engineer"
print("Updated disct", person)
#deleting value
del person["city"]
print("after deletion:", person)

'''
results
{'name': 'Joe', 'age': 23, 'city': 'New York'}
Name: Joe
updated age: 26
Updated disct {'name': 'Joe', 'age': 26, 'city': 'New York', 'profession': 'engineer'}
after deletion: {'name': 'Joe', 'age': 26, 'profession': 'engineer'}

'''

#boolean variables
is_active = True
is_logged_in = False

#logical operators
print("AND:", is_active and is_logged_in)
print("OR:", is_active and is_logged_in)
print("NOT:", not is_active)

#comparison operators
x = 10
y = 20
print("x > y:", x > y)
print("x == y:", x == y)

'''
results
AND: False
OR: False
NOT: False
x > y: False
x == y: False
'''

#collecting user data
name = input("Enter your name: ")
age = int(input("Enter your age: "))
hobbies = input("Enter your hobbies (comma-separated): ").split(",")

#storage in dictionary
user_data = {"name": name, "age": age, "hobbies": hobbies}

#display
print("\nUser info")
print(f"name: {user_data['name']}")
print(f"Hobbies: {', '.join(user_data['hobbies'])}")
                

'''
results
Enter your name: jeff
Enter your age: 23
Enter your hobbies (comma-separated): burning things

User info
name: jeff
Hobbies: burning things
'''
