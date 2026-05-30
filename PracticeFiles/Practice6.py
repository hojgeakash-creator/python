# Conditional Statements by using Single Line and Clever if

stationery = input("stationery : ")
(
    print("stationery")
    if stationery == "pencil" or stationery == "scale"
    else print("not stationery")
)

CPU = int(input("Enter CPU Usage : "))
print("High Alert" if CPU >= 80 else print("Everything is normal"))


Disk = int(input("Enter Disk Usage : "))
print("Maximum Disk Usage" if Disk >= 85 else print("Normal Disk Usage"))
