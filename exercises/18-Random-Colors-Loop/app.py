import random

def get_color(color_number):
    # making sure is a number and not a string
    color_number = int(color_number)

    switcher={
                  0:'red',
                  1:'yellow',
                  2:'blue',
                  3:'green',
                  4:'black',
                  5:'yellow',
                  6:'white',
                  7:'orange',
                  8:'copper',
                  9:'green'
              }

    return switcher.get(color_number,"Invalid Color Number")

students_array = []

def get_allStudentColors():

    example_color = 1
    students_array = []
    #your loop here
    for x in range(0, 9):
        color_number=random.randint(0,9)
        students_array.append(color_number)


print(*students_array)