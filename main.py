bill = 0
height = int(input("What is your height in cm? "))

if height >= 120:
  print("Your height is tall enaugh to ride")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 7
    print("Pay 7k")
  elif age <=18:
    bill = 12
    print("pay 12k")
  else:
    bill = 18
    print("Pay 18k")

  poto = input("Do you want a photo taken? Y or N. ")
  if poto == "Y":
    bill += 10

  print(f"Your bill is : {bill}k")
else:
  print("You cant ride it")