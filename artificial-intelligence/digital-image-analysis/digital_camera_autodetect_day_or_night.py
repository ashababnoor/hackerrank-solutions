'''
Digital Camera Autodetect: Day or Night
Link: https://www.hackerrank.com/challenges/digital-camera-day-or-night/problem 
'''

# Enter your code here. Read input from STDIN. Print output to STDOUT

def string_to_list(string: str) -> list:
    return list(map(int, string.split(",")))

img = list(map(string_to_list, input().split()))

# Converting the image to a single channel black and white image
black_and_white_img = [sum(pixel)/3 for pixel in img]

avg_pixel_value = sum(black_and_white_img)/len(black_and_white_img)

if avg_pixel_value > 90:
    print("day")
else:
    print("night")