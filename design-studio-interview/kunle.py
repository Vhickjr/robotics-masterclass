import csv
print("Welcome Kunle") 
number_of_tasks= int(input("Enter the number of tasks, Kunle: "))

start_time = float(input("Using 24 hour clock, Enter the start time in hours : "))
end_time = float(input("Using 24 hours clock, Enter the end time in hours:  "))
tasks= []


for _ in range(number_of_tasks): 
    taskName= str(input("Enter the name of the task: "))
    rate = 1500
    time = (end_time - start_time)
    total = rate*time
    tasks.append([taskName,rate,time,total])


csv_file = "kunle.csv"
with open(csv_file, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Rate","Time","Total"])
    writer.writerow([rate,time,total])
    
print(f"The data has been written to {csv_file} successfully")

''' If Kunle works from 11AM to 1:30 PM on Monday 23rd January. How did he make?

He will make: 1500*2.5 = 3750

'''