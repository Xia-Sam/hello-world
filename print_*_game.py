while True:
    width_str = input("Pls input an integer: ")
    try:
        width=int(width_str)
        if width<=0:
            print("Your integer must be larger than 0. Try again.")
            continue
        break
    except:
        print("You are not inputting an integer. Try again.")
for i in range(2*width):
    if i<=width:
        for j in range(i):
            print("*", end='')
    else:
        for x in range(2 * width - i):
            print("*", end='')
    print()
