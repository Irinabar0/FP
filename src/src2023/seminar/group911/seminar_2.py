#print('hello')
#print('is this working?')
""""

Manage a list of circles
    1. Add a circle from console
    2. Add a random circle
    3. Display all circles
    4. Sort circle by radius
    5. Exit the program

"""

print('Hello world')

#a circlus is represented by center (x,y) and radius (r) -- all integers, r > 0

#circle center (1,2), radius 3 => {"x":1, "y":2, "r":3}

#Decouple the circle's representation from the prgogram
#the program should not know that the circle is a dict
#Circle functions

d = {1: "Alice", 2: "Bob", 3: [1,2,3]}
#d[3] = "Xavier"
#print(d, type (d))
#print(d.keys(), d.values())

def create_circle(x : int, y : int, radius : int) -> dict:
    """
    Create a circle represented as a dictionary
    
    :param x: X coordinate of center 
    :param y: Y coordinate of center
    :param radius: circle radius
    :return:  the newly created circle
    
    """
    return {"x": x, "y": y, "r": radius}


#Program funtionalitiess
c1 = {"x": 1, "y": 2, "r": 3}
c2 = {"x": 3, "y": 4, "r": 5}
# print([c1,c2])


# str - Python string data type
# str() builtin function to convert its argument to a Pyhton string.

def to_str(circle : dict) -> str:
    # TODO Write specification for this method
    #pass
    return "circle center (" + str(circle["x"]) +","+ str(circle["y"])+ ")), radius=" + str(circle["r"])

data = [create_circle(3,4, 2), create_circle(1,2,3)]
#print(data)

for circle in data:
    print(to_str(circle))

for i in range(0, len(data)):
    print(to_str(data[i]))

while True:
    print("1. Add a circle")
    print("2. Display all circles")
    print("0. Exit the program")
    option = input(">")

    if option == "1": #C switch statement
         #add a circle
         pass
    elif option == "2":
         #display circles
         pass
    elif option == "0":
         break
    else:
        print("Invalid Option")












