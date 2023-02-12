import math

def paint_calc(height, width, cover):
    result = math.ceil(height * width / coverage)
    print(f"You\'ll need {result} cans of paint")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of the wall: "))
coverage = int(5)
paint_calc(height=test_h, width=test_w, cover=coverage)
