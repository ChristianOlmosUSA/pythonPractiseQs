

x = 99

var2 = f"{x} bottles of milk on the wall,"
var3 = f"{x} bottles of milk."
var4 = f"Take one down and pass it around, {x-1} bottles of milk on the wall."
var5 = "Take one down and pass it around, no more bottles of milk on the wall."
var6 = "No more bottles of milk on the wall, no more bottles of milk. \nGo to the store and buy some more, 99 bottles of milk on the wall."

def number_of_bottles():
    x=99
    for x in range(99, 1, -1):
        print(f"{x} bottles of milk on the wall, {x} bottles of milk.")
        if x == 2:
            print("1 bottle of milk on the wall, 1 bottle of milk.")
            print("Take one down and pass it around, no more bottles of milk on the wall.")
            print(" ")
            print(var6)


number_of_bottles()