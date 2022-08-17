
import bet_types
import starting_details
import bet_strategy
import simulation


# Make a list of roulette outcomes ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
outcome_list = []

outcome_list.append({"num": 0, "o-e": "neither", "clr": "green", "set":"0-0"})
count = 1

# For each count till 36 
while count < 37:
  print("")
  # create a dict
  to_append = dict()
  
  to_append["num"] = count
  
  # if odd
  if count % 2 != 0:
    to_append["o-e"] = "odd"
    to_append["clr"] = "r"
    
  # if even
  else:
    to_append["o-e"] = "even"
    to_append["clr"] = "b"

  # add list items for numbers 1 to 18
  if count in range (1, 19):
    to_append["set"] = "1-18"
  
  # add list items for numbers 19 to 36
  if count in range(19, 37):
    to_append["set"] = "19-36"
  
  outcome_list.append(to_append)
  
  # add to count 
  count += 1
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

while True:
  balance = starting_details.starting_amount()

  unit = starting_details.get_unit(balance)

  strategy = bet_strategy.get_strategy()

  all_bets = bet_types.get_bet_types()

  sim_count = starting_details.get_sim_count()

  simulation.simulate(balance, unit, all_bets, outcome_list, strategy, sim_count)

# ASK TO REPEAT OR CLOSE

  repeat = input("press '1' to repeat simuation\npress '2' to exit " )
  
  while repeat not in ['1', '2']:
    print("")
    repeat = input("invalid input. '1' or '2' only " )
    
    
  if repeat == '1':
    print("")
    continue
  else:
    break 

print("\nScript finished.")
exit()