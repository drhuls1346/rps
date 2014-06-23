def compare():
    """This function decides who wins rock-paper-scisors"""
    count = 0
    while count <=2:
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
