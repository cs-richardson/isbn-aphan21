#This program determines if the set of numbers input by the user is a real ISBN.
#This program is created by Ann

total = 0

while True:
    isbn = str(input("Enter your isbn number: "))
    if len(isbn) < 9 or len(isbn) > 10:
        print("This is not an ISBN.")
    else:
        break
        
for i in range (len(isbn)):   
    next = (i+1)*(int(isbn[i]))
    total = total + next

if total % 11 == 0:
    print("This is a real ISBN.")
else:
    print("This is a fake ISBN.")
