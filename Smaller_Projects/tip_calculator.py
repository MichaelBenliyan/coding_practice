print("Welcome to the Tip Calculator!")
total_bill = int(input("What was the total bill? "))
tip_percentage = int(input("How much tip would you like to give? 10, 12, or 15? "))
num_people = int(input("How many people are splitting the bill? "))
per_person = (total_bill * (1 + tip_percentage/100)) / num_people
print("Each person should pay: ${}".format(per_person)) 
