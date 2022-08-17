def get_strategy():
  strat = []
  
  while True:
    print("\nSelect betting strategy:\n  (1) If loss, double up.        If win, reset to base.\n  (2) If loss, reset to base.    If win, double up.\n  (3) Custom: If win, reset to base. If loss, double up but limit to (x) number of losses in a row. When hit limit, reset bet to base unit.\n")
    user_input = input("Select strategy (enter digit between 1 to 3) ")

    # if is not integer digits 
    if user_input.isdigit() == False:
      print("enter digits only")
      continue
    
    else:
      user_input = int(user_input)
      
      # if input is 1 to 2
      if user_input in [1, 2]:
        strat.append( user_input )
        return strat
      
      # if input = 3, ask for limit
      elif user_input == 3:
        strat.append( user_input )
        
        print("Your desired strat is:  If loss, double up but limit to (x) number of losses in a row.  If win, reset to base.")
        
        while True:
          limit = input("\nenter value for (x) (min 2, max 4) ")
          
          if limit.isdigit() == False:
            print("enter digits only")
            continue
          else:
            limit = int(limit)
            
            if limit in range(2, 5):
              strat.append(limit)
              return strat
            
      else:
        print("Invalid input. Enter digts between 1 and 3.")
        continue