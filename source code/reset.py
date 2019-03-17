def resetit():
    for x in range(1, 12+1):
        f = open("cand{}.txt".format(x), mode = 'w')
        f.write("0")
        f.close()
        del f

    for x in range(1, 12+1):
        f = open("cand{}.txt".format(x), mode = 'r')
        print(str(f.read()))
        f.close()
        del f

try:
    resetit()
    print("It is succesfully done.")
    x = input()
    
except:
    print("There is an error.")

