
while True:
    work_hour_str=input("Pls input the number of hours one works in a month:  ")

    try:
        work_hour_int=int(work_hour_str)
        if work_hour_int<0:
            print("working hours need to be positive. Try again.")
            continue
        break
    except:
        print("You are not inputting number. Try again.")
if work_hour_int <= 160:
    grossPay=10*work_hour_int
    print("The gross pay is ", grossPay)
else:
    grossPay=15*(work_hour_int-160)+10*160
    print("The gross pay is ", grossPay)
if grossPay<=1000:
    tax=0.1*grossPay
elif 1000<grossPay<=1500:
    tax=100+0.2*(grossPay-1000)
else:
    tax=200+0.3*(grossPay-1500)
print("The tax is ", tax)
print("The net pay is ", grossPay-tax)
