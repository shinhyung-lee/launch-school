

def yes_no_response(sentence):
    
    while True:
        user_response = input(sentence)
        response = user_response.strip().lower()
        if response in ['y', 'yes']:
            print("Here we go again!")
            break
        elif response in ['n', 'no']:
            print("Okay. See you later.")
            break
        else:
            print("You goofed! That is not a valid answer.")

yes_no_response("Do you want to continue? (y/n)")
yes_no_response("Are you absolutely sure? (yes/no)")
print("All done.")