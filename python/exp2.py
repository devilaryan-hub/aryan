import math

def calculate_circle_area():
    r = float(input("Enter the radius of the circle: "))
    area = math.pi * r * r
    print(f"The area of the circle is: {area:.2f}")

def calculate_rectangle_area():
    l = float(input("Enter the length of the rectangle: "))
    w = float(input("Enter the width of the rectangle: "))
    area = l * w
    print(f"The area of the rectangle is: {area:.2f}")

def calculate_triangle_area():
    b = float(input("Enter the base of the triangle: "))
    h = float(input("Enter the height of the triangle: "))
    area = 0.5 * b * h
    print(f"The area of the triangle is: {area:.2f}")

while True:
    print("\nChoose a geometric figure to calculate its area:")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Triangle")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        calculate_circle_area()
    elif choice == '2':
        calculate_rectangle_area()
    elif choice == '3':
        calculate_triangle_area()
    elif choice == '4':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
