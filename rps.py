def compare():
    """This function decides who wins rock-paper-scisors"""
    count = 0
    rounds = int(raw_input("Enter number of rounds: "))
    while count <=rounds - 1:
        choice1 = raw_input("Enter choice 1: ")
        choice2 = raw_input("Enter choice 2: ")
        if choice1.lower() == choice2.lower():
            print("It's a tie!")
        elif choice1.lower() == 'rock':
            if choice2.lower() == 'scissors':
                print('Rock wins!')
            elif choice2.lower() == 'paper':
                print ('Paper wins!')
        elif choice1.lower() == 'scissors':
            if choice2.lower() == 'rock':
                print('Rock wins!')
            elif choice2.lower() == 'paper':
                print ('Scissors wins!')
        elif choice1.lower() == 'paper':
            if choice2.lower() == 'rock':
                print('Paper wins!')
            elif choice2.lower() == 'scissors':
                print ('Scissors wins!')
        count += 1

    player1_name = raw_input("Enter player one name: ")
    player2_name = raw_input("Enter player two name: ")
    print("{} and {} thanks for playing!".format(player1_name, player2_name))
      
