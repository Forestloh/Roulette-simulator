


def starting_amount():
  while True:
    amt = input("Starting amount? (enter between 100 and 1mil) ")

    # if is not integer digits
    if amt.isdigit() == False:
      print("enter positive digits only")
      continue
      
    else:
      amt = int(amt)
      
      if amt not in range (100, 1000001):
        print("starting amount must be between 100 and 1,000,000")
        continue
      
      else:
        return amt

def get_unit(start_amount): 
  while True:
    print("")
    unit = input("Enter bet unit (min 1) ")

    # if is not integer digits
    if unit.isdigit() == False:
      print("enter positive digits only")
      continue
      
    else:
      unit = int(unit)
      
      # if unit is less than 0
      if unit == 0:
        print("unit bet amount cannot be less than 0")
        continue
      
      # if unit more than starting amount 
      elif(unit > start_amount):
        print("unit bet amount cannot be more than starting amount")
        continue
      
      else:
        return unit

def get_sim_count():
  while True:
    print("")
    sim_count = input("Number of times to simulate? (enter between 1 and 1,000,000) ")

    # if is not integer digits
    if sim_count.isdigit() == False:
      print("enter positive digits only")
      continue
      
    else:
      sim_count = int(sim_count)
      
      # if unit is less than 0
      if sim_count == 0:
        print("number of times to simulate cannot be less than 0")
        continue
      
      elif sim_count > 1000000:
        print("max number of simulations is 1,000,000")
        continue
      
      else:
        return sim_count
