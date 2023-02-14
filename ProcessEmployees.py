'''
The Customer Service Represetatives (CSRs) in the marketing department with a security clearance of 'TS' were able
to thwart an attack on the server and for that management has decided to reward them with a 10% increase in their salary. 
To evaluate the impact on the budget, you have been asked to run a report on the employee file and display the results 
of BEFORE AND AFTER the salary increase. Also calculate the total difference between the old salary and the new
salary (as shown in the image).

You will create a dictionary that has the full employee name as the key and only their NEW salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as shown in the image)
'''

import csv

#open the file

with open ("employee_data.csv", 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    header = next(csv_reader)


#create an empty dictionary

    employee_dict = {}


#use a loop to iterate through the csv file
    for row in csv_reader:
        

    #check if the employee fits the search criteria
        if row[3] == "Marketing" and row[4] == "CSR" and row [9] == 'TS':
            employee_name = row[1] + ' ' + row[2]
            old_salary = int(row[5])
            new_salary = int(old_salary * 1.1)
            employee_dict[employee_name] = (old_salary, new_salary)

    
    for employee, salary in employee_dict.items():
       print(f"Employee Name : {employee} Current Salary : ${salary[0]}")

    

print()
print('=========================================')
print()

#iternate through the dictionary and print out the key and value as per image

for employee, salary in employee_dict.items():
    print(f"Employee Name : {employee} New Salary : ${salary[1]}")


          

print()
print('=========================================')
print()

#print out the total difference between the old salary and the new salary as per image.
for salary in employee_dict.values():
    total_difference = sum([salary[1] - salary[0]])
    
print(f"Total increase in salary: ${total_difference}")
    
