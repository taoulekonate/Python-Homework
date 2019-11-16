import os
import csv
udemy_csv = os.path.join("web_starter.csv")

# Lists to store data
title = []
price = []
subscribers = []
reviews = []
review_percent = []
length = []
courselist = []

# with open(udemy_csv, newline="", encoding='utf-8') as csvfile:
with open(udemy_csv, newline="", encoding="utf8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for row in csvreader:
        # Add title

        # YOUR CODE HERE()
        t = row[1].strip()


        # Add price
        # YOUR CODE HERE

        pr = row[4].strip()

        # Add number of subscribers
        # YOUR CODE HERE())
        sub = row[5].strip()
        # Add amount of reviews
        # YOUR CODE HERE
        revs = row[6].strip()

        # Determine percent of review left to 2 decimal places
        # YOUR CODE HERE

        # Get length of the course to just a number
        # YOUR CODE HERE
        lengthofcourse = row[7].strip()
        lengthofcourse = lengthofcourse.upper()
        lengthofcourse = lengthofcourse.replace("hOURS","")
        try :
            if pr == "Free":
                pr = 0.00
            else :
               pr = float(pr)
            sub = int(sub)
            revs = int(revs)
            lengthofcourse = int(lengthofcourse)
            revpers = revs / sub
            revpers =   int((revpers * 100) + 0.5) / 100.0
            round(revpers, 2)

        except Exception as ex:
            print(ex)
        else:
            title.append(t)
            price.append(pr)
            subscribers.append(sub)
            reviews.append(revs)
            review_percent.append(revpers)
            length.append(lengthofcourse)
           # courselist.append((title,price,subscribers,reviews,reviewpercentage,lengthofcourse))

# Zip lists together
# YOUR CODE HERE
lengthoffields = len(price)
courselist.append(("title,price,subscribers,reviews,review_percentage,length_of+_course"))
for i in range(lengthoffields):
    courselist.append((title[i],price[i],subscribers[i],reviews[i],review_percent[i],length[i]))

# Set variable for output file
output_file = os.path.join("web_final.csv")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Title", "Course Price", "Subscribers", "Reviews Left",
                     "Percent of Reviews", "Length of Course"])
    for z in courselist:
         writer.writerow([z[0],z[1],z[2],z[3],z[4],z[5]])
    # Write in zipped rows
    # YOUR CODE HERE

