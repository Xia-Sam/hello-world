coden=""
code = input("input the code:  ")

for i in range(0,len(code)):
    if code[i] == ' ':
        coden = coden + ' '
    
    elif ord(code[i])<=116:
        coden=coden+chr(ord(code[i])+6)
    else:
        coden=coden+chr(ord(code[i])-10)
print(coden)
