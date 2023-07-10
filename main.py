year = int(input("Which year do you want to check? "))
leapYear = False

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      leapYear = True
  else:
    leapYear = True
  
if leapYear == True:
  print(f"{year} is a Leap Year.")
else:
  print(f"{year} is not a Leap Year.")