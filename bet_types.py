
# CHECK BET AVAILABILITY ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def check_avail_bets(bet_list):
  list_avail = [{"type": "1", "print": "Bet type 1: even or odd", "input": "enter 'odd' or 'even'"}, {"type": "2", "print":"Bet type 2: red or black", "input": "enter 'r' or 'b'"}, {"type": "3", "print":"Bet type 3: 1 to 18 or 19 to 36", "input": "enter '1-18' or '19-36'"}]
  
  for i, item in enumerate(list_avail):
    if ('even' in bet_list) or ('odd' in bet_list):
      if list_avail[i]["type"] == "1":
        list_avail.pop(i)

    if ('r' in bet_list) or ('b' in bet_list):
      if list_avail[i]["type"] == "2":
        list_avail.pop(i)
    
    if ('1-18' in bet_list) or ('19-36' in bet_list):
      if list_avail[i]["type"] == "3":
        list_avail.pop(i) 
  
  return list_avail

# GET BET INPUT ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def bet_input(bet_list):
  
  # get list of avail bets ~~~~~~~~~~~~~~~~
  avail_bets = check_avail_bets(bet_list)
  possible_options = []
  # get list of possible inputs from avail_bets
  for i, item in enumerate(avail_bets):
    if item["type"] == "1":
      possible_options += ["odd", "even"]
    if item["type"] == "2":
      possible_options += ["r", "b"]
    if item["type"] == "3":
      possible_options += ["1-18", "19-36"]
  
  
  # Get input ~~~~~~~~~~~~~~~~
  while True:
    for item in avail_bets:
      print(f"  for bet type {item['type']}, {item['input']}")
      
    user_input = input("\nwhat do you want to bet on? ")
    # response validation
    if user_input not in possible_options:
      print("invalid input\n")
      continue

    # if response is valid and bet type not already entered
    else:
      return user_input


# loop to get all bets ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def get_bet_types():
  print("\nEnter your bet type")
  bets = []
  
  # get first bet
  bets.append(bet_input(bets))
  print(f"your bets: {bets}")
  
  
  while len(bets) < 3:
    print("")
    add_bet = input("add another bet type? (y/n) ")
    
    if add_bet == "n":
      break
    
    elif add_bet == "y":
      bets.append(bet_input(bets))
      
    else:
      print("invalid response. ('y' or 'n' only)")
      
    print(f"your bets: {bets}")
    
  
  # return formatted betlist
  formatted_bet_list = []
  
  for item in bets:
    if item in ["odd", "even"]:
      formatted_bet_list.append( { "type": "o-e", "bet": item, "amt": "", "prev": None, "l_loop": 0, "l_streak": 0, "w_streak": 0, "streak": 0} )
    if item in ["r", "b"]:
      formatted_bet_list.append( { "type": "clr", "bet": item, "amt": "", "prev": None, "l_loop": 0, "l_streak": 0, "w_streak": 0, "streak": 0} )
    if item in ["1-18", "19-36"]:
      formatted_bet_list.append( { "type": "set", "bet": item, "amt": "", "prev": None, "l_loop": 0, "l_streak": 0, "w_streak": 0, "streak": 0} )
      
    
      
  return formatted_bet_list