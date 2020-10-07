
def calc_new_height():
    width = int(input("Enter the current width:"))
    height = int(input("Enter the current height:"))
    aspect_ratio = width/height
    width = int(input("Enter the desired width:"))
    height = width/aspect_ratio
    print("The corresponding height is:",height)
    print(height)

calc_new_height()