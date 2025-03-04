from datetime import datetime
date = input("Enter a date: DD-MM-YYYY: ")
converted_date = datetime.strptime(date,"%d-%m-%Y")
current_date = datetime.now()

difference = current_date.year - converted_date.year

if converted_date.month > current_date.month:
    difference -= 1


print(f"Difference in age is {difference}")