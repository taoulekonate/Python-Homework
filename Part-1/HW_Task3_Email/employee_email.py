import os
import csv

#filepath = os.path.join("Resources", "employees.csv")
filepath = os.path.join("Resources", "employees.csv")
new_employee_data = []

# Read data into dictionary and create a new email field
with open(filepath,encoding="utf8",newline = "" ) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)
        # YOUR CODE HERE
        firstn = row["first_name"]
        lastn = row["last_name"]
        ssn =row["ssn"]
        email = firstn + lastn + "@example.com"
        empdict = {}
        if ssn  not in empdict.keys():
            empdict[ssn] = (firstn,lastn,email)
        new_employee_data.append(empdict)


    print(new_employee_data)


        # Hint: You can use csv.DictReader
        # This will require a little bit of independent research (by design)
        # In the real world, you will encounter situations like this

# Grab the filename from the original path
_, filename = os.path.split(filepath)

# Write updated data to csv file
#csvpath = os.path.join("output", filename)
csvpath = os.path.join("output", filename)

with open(csvpath, "w") as csvfile:
    # YOUR CODE HERE
    # Hint: You can use csv.DictWriter
    fieldnames = ['first_name', 'last_name', 'SSN', "Email"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for newemps in new_employee_data:
        for key in newemps.keys():
            empdata = newemps[key]
            writer.writerow({'first_name': empdata[0], 'last_name': empdata[1],"SSN":key,"Email":empdata[2]})
    pass