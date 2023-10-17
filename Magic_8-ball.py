# A program to solve someones answers
# Just type in a yes or no question you want answered
import random
num = 0
Huh = True
while Huh:
  question = input("Ask the Magic 8 Ball a yes or no question: ")
  print("")
  num = random.randint(1, 10)
  if num == 1:
     print("Thats correct!")
  elif num == 2:
    print("...")
  elif num == 3:
    print("That might not be right")
  elif num == 4:
    print("Most definately yes!")
  elif num == 5:
    print("I dont know...")
  elif num == 6:
    print("The future seems a bit unclear")
  elif num == 7:
    print("come back again later")
  elif num == 8:
    print("I dont think so")
  elif num == 9:
    print("Who knows?")
  else:
    print("That doesn't matter.")
    
  print("")
  print("")
  print("-------------------")
  #Asking if they want to continue 
  while True:
    cont = input("Do you want to continue? (y/n): ")
    if cont in ["y", "yes", "Yes", "yeah", "Y", "Yeah", "YES", "Ye", "ye"]:
      Huh = True
      print("")
      break
    elif cont in ["n", "no", "No", "N", "nope", "Nope", "Nah", "NO", "nah"]:
      Huh = False
      print("(┬┬﹏┬┬)")
      break
    else:
      print("Thats not a valid answer.")
      print("")