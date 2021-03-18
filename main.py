#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: You might need to do some research in Google to figure out how to do this.
print("Welcome to the tip calculator")
bill = float(input("What was the total bill? "))
perc_share = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people_split = int(input("How many people to split the bill? "))
tip_calc = bill * (perc_share/100)
tot_bill = bill+tip_calc
each_share = round(tot_bill/people_split,2)
print(f"Each person should pay: ${each_share}")