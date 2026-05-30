# Conditional Statement

marks = int(input("marks : "))
if marks >= 90:
    print("grade A")
elif marks < 90 and marks >= 80:
    print("grade B")
elif marks < 80 and marks >= 70:
    print("grade C")
else:
    print("grade D")

country = input("Enter the country : ")
if country == "Australia":
    print("Australia are 5 time World Champoins")
elif country == "India":
    print("India are 2 time World Champions")
elif country == "West Indies":
    [print("West Indies are 2 time World Champions")]
else:
    print("Rest countries have won atleast once or none")

# Conditonal Statement using Logical Operator

CPU_Usage = int(input("Enter CPU Usage : "))
if CPU_Usage >= 90:
    print("Critical Alert")
elif CPU_Usage >= 80 and CPU_Usage < 90:
    print("High Alert")
elif CPU_Usage >= 70 and CPU_Usage < 80:
    print("Warning Alert")
else:
    print("Services are running fine")

disk_usage = int(input("Enter disk usage : "))
if disk_usage >= 95:
    print("Max Usage Alert")
elif disk_usage >= 80 and disk_usage < 90:
    print("High Usage Alert")
elif disk_usage >= 70 and disk_usage < 80:
    print("Warning Usage Alert")
else:
    print("Disk Usage is Normal")
