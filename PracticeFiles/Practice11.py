# Lists and Tuples

Vegetable = ["Cauliflower", "Ladyfinger", "Brinjal", "Tomato"]
print(type(Vegetable))
print(len(Vegetable))

Vegetable[2] = "Potato"
print(Vegetable)


Cars = ["BMW", "Lamborgini", "Skoda", "Toyota", "Hyundai"]
print(type(Cars))
print(len(Cars))


Fruits = ("Litchi", "Mango", "Apple")
print(type(Fruits))


Family = ("Mother", "Father", "Brother", "Sister", "Relatives")
print(type(Family))
print(len(Family))


# List Slicing

Name = ["Ram", "Lakshman", "Bharat", "Shatrughan", "Kartik", "Paro"]
print(Name[:3])

Numbers = [22, 12, 35, 80]
Numbers.append(99)
print(Numbers)

Boxes = [98, 35, 64, 83, 77]
Boxes.sort()
print(Boxes)

Height = [192, 162, 200, 175, 130]
Height.sort(reverse=True)
print(Height)

Weight = [90, 40, 62, 35, 67]
Weight.reverse()
print(Weight)

even = [2, 4, 6, 8, 10]
even.remove(4)
print(even)

odd = (1, 3, 5, 7, 9, 9, 11, 13)
print(odd.index(9))
