def trapezoid_area(base1, base2, height):
    return 0.5 * (base1 + base2) * height

base1 = float(input("Enter the first base: "))
base2 = float(input("Enter the second base: "))
height = float(input("Enter the height: "))

area = trapezoid_area(base1, base2, height)
print(f"Area of the trapezoid: {area}")
