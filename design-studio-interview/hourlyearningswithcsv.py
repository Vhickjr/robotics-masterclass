import csv 

number_of_employees = int(input("Enter the number of employees:"))
employee =[]


for _ in range(number_of_employees):
    name = input("Enter the name of the employee:")
    rate = int(input(f"Enter the rate of the employee {name}:"))
    hour = int(input(f"Enter the hour of the employee {name}:"))
    earning = rate * hour
    employee.append([name,rate,hour,earning])
    
csv_file= "hourly_earning.csv"

with open(csv_file, mode = "w" ,newline="") as file:
    
    writer = csv.writer(file)
    writer.writerow(["Name","Rate","Hour","Earning"])
    writer.writerows(employee)

print("The data has been written to the file successfully")