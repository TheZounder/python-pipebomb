import shutil
import os

currentDir = os.getcwd()

ans = input("Do you love me?(y/n)")

if ans == "n":

    x = 1

    while x < 5:
        dest = currentDir + "/pipebomb{0}.jpg".format(x+1)
        shutil.copy(currentDir + "/pipebomb.jpg", dest)
        x = x + 1 
        if x == 5:
            break
elif ans == "y":
    print("YAYAYAYAYAYAYAYAY")
        
