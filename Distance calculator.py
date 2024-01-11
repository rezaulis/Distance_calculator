v = int(input("Enter the speed of the vehicle in mph: "))
h = int(input("Enter the number of hours traveled: "))      

print("Hour             Distance Traveled")
print("----------------------------------")


def table(v, h):
    sum = 0
    for i in range(1, h+1):       
        x = float((i) * v)
        sum = sum + x
        print(i,"                  ",x)
    print("The accumalated distance traveled is: ", sum)

table(v, h)
