import secrets
  
def print_strategy(strat):
  print("strategy:  ", end="")
  
  if strat[0] == 1:
    print("If loss, double up. If win, reset to base.")
  elif strat[0] == 2:
    print("If loss, reset to base. If win, double up.")
  else:
    print(f"If win, reset to base. If loss, double up but limit to {strat[1]} losses in a row. When hit limit, reset bet to base unit.")
    
def update_bets(all_bets, strat, base_unit):
  
  # (1) If loss, double up.       If win, reset to base.
  if strat[0] == 1:
    for bet in all_bets:
      if bet["prev"] == "win":
        bet["amt"] = base_unit
      else:
        bet["amt"] *= 2
        
  # (2) If loss, reset to base.   If win, double up.  
  elif strat[0] == 2:
    for bet in all_bets:
      if bet["prev"] == "win":
        bet["amt"] *= 2
      else:
        bet["amt"] = base_unit
  
  # (3) Custom: If win, reset to base.
  # If loss, double up but limit to (x) number of losses in a row. When hit limit, reset bet to base unit.
  else:
    for bet in all_bets:
      if bet["prev"] == "win":
        bet["amt"] = base_unit
      
      # if loss
      else:
        # if limit hit... 
        if (bet["prev"] == "loss") and (bet["l_loop"] == strat[1]):
          # reset bet amount to base
          bet["amt"] = base_unit
          # reset loop
          bet["l_loop"] = 0
          
        # if limit not hit
        else:
          bet["amt"] *= 2

     
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# MAIN SIMULATION ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def simulate(balance, base_unit, user_bets, outcome_list, strat, simulation_count):

  all_bets = user_bets
  cash = balance
  
  #for later use
  broke = False
  max_loss = 0
  max_profit = 0
  

  # set all bets to default (the other fields have been set)
  for bet in (user_bets):
    bet["amt"] = base_unit

  # make var to count simulation
  sim_count = 0

  # SIMULATE ROUNDS !! ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  for x in range (simulation_count):
    sim_count += 1
    
    # deduct cash
    for bet in all_bets:
      cash -= bet["amt"]
    
    # get an outcome from the roulette spin
    spin_outcome = secrets.choice(outcome_list)
    
    # Check bet to see if win/loss
      # for every bet type (is a dictionary).......
    for bet in all_bets:
      # get bet type
      bet_type = bet["type"]
      
      # if win ~~~~~~~~~~~~~
      if bet["bet"] == spin_outcome[bet_type]:
        
        #update cash
        cash += (bet["amt"] * 2)
        
        # update results in "prev" and streak count
        if bet["prev"] == "win":
          bet["streak"] += 1
        else:
          bet["streak"] = 1
          
        bet["prev"] = "win"
        
      # if loss ~~~~~~~~~~~~~
      else:
        if bet["prev"] == "loss":
          bet["streak"] += 1
        else:
          bet["streak"] = 1
        
        bet["l_loop"] += 1
        bet["prev"] = "loss"
        
      # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      
    update_bets(all_bets, strat, base_unit)

    # Find max loss
    if((cash - balance) < max_loss):
      max_loss = (cash - balance)
      round_max_loss = sim_count
    
    # Find max win
    if(cash - balance) > max_profit:
      max_profit = (cash - balance)
      round_max_win = sim_count
    
    # find max lose streak
    for bet in all_bets:
      if (bet["prev"] == "loss") and (bet["streak"] > bet["l_streak"]):
        bet["l_streak"] = bet["streak"]
      
      if (bet["prev"] == "win") and (bet["streak"] > bet["w_streak"]):
        bet["w_streak"] = bet["streak"]

    # find round broke
    if (cash <= 0) and (broke == False):
      round_broke = sim_count
      broke = True

    # END OF ROUND ~~~~~~~~~~~~~~~~~~~~~~~~
    #print(f"End of simulation round: {sim_count}")
      
  # END OF SIMULATION ~~~~~
  print("\n~~~~~~~~ Result at end of simulation ~~~~~~~~~~~~")
  print(f"\nStarting amount: ${balance}")
  print(f"Base unit amount: ${base_unit}")
  print_strategy(strat)
  #print("bets:")
  #for bet in all_bets:
  #  print("    ", bet['bet'])
  #print("")
  
  # ~~~~~~~~~~~~~~~~~
  
  print(f"balance: ${cash}")
  print(f"profit/loss: ${cash - balance}")
  print(f"max loss: ${max_loss}")
  print(f"max profit: ${max_profit}")
  if broke == True:
    print(f"broke at round: {round_broke}")
  for bet in all_bets:
      print(f"bet type: {bet['bet']}, longest loss streak: {bet['l_streak']}, longest win streak: {bet['w_streak']}\n")
  
  
