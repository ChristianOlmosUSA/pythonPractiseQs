# Your code here!!

var1 = "let it be, "
var2 = "whisper words of wisdom,"
var3 = "there will be an answer,"
countr=0

def sing(var1, countr):
    while (countr < 4):
        print (var1)
        countr = countr + 1
    
    print(var2, var1, var1)

    countr=0
    while (countr < 3):
        print (var1)
        countr = countr + 1
    var1 = var1[:-2]
    print(var3,var1)


sing(var1 ,0)



# DONE


