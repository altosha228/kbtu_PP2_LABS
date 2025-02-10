def parallelogram_area(base, height):
    return base * height

base = float(input("Enter the base length: "))
height = float(input("Enter the height: "))

area = parallelogram_area(base, height)
print(f"Area of the parallelogram: {area}")
