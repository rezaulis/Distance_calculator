speed = int(input("Enter the speed of the vehicle in mph: "))
hour = int(input("Enter the number of hours traveled: "))      

print("Hour             Distance Traveled")
print("----------------------------------")


def table(speed, hour):
    sum = 0
    for i in range(1, hour+1):       
        x = float((i) * speed)
        sum = sum + x
        print(i,"                  ",x)
    print("The accumalated distance traveled is: ", sum)

table(speed, hour)
