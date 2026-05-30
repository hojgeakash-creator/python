# Nesting Condition

# age = int(input("Enter the age : "))

if age >= 18:
    if age >= 75:
        print("Eligible for Senior Citizens Fixed Deposit Benefits")
    else:
        print("Senior Citizens Benefits not Eligible")
else:
    print("Not eligible for Fixed Deposit Benefits")


cpu_usage = int(input("Enter the cpu_usage : "))

service_running = True

if service_running:
    if cpu_usage > 90:
        print("High CPU usage Alert")
    else:
        print("Warning alert for high cpu usage")
else:
    print("CPU usage is healthy")

bank = input("Enter the bank : ")

if bank == "Bank of India":
    loan_type = input("Enter loan type : ")

    if loan_type == "Home Loan":
        print("Bank of India is giving less ROI for home loans")
    else:
        print("Different loan policy applies")

elif bank == "Bank of Maharashtra":
    print("Bank of Maharashtra is giving less ROI for home loans")

else:
    print("Rest other banks are giving high ROI for home loans")
