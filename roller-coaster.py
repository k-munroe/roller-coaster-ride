#enforce what I've learned about logical operators
print("Check your height to see if you can access this ride.")
height = int(input("How tall are you(cm)?: "))
age = int(input("How old are you?: "))
ticket_cost = 0


if height > 120 and age < 56:
    print("You are eligible to ride.")
    if age >= 18 and age < 45:
        ticket_cost += 12
    elif age >= 45 and age <= 55:
        ticket_cost += 0
    elif age >= 12 and age < 18:
        ticket_cost += 7
    else:
        ticket_cost += 5
    
    
    photo_taken = input("Do you want photos taken of you while on the ride? Y or N: ")
    if photo_taken.upper() == "Y":
        ticket_cost += 3
    elif photo_taken.upper == "N":
        ticket_cost += 0
    else:
        print("Incorrect response.")
    print(f"Your ticket total comes out to ${ticket_cost}.")
elif height > 120 and age >= 56:
    print("Please have a note from your Physician permiting you to go on this ride. Thank you.") 
else:
    print("Sorry, you cannot go on the ride.")


