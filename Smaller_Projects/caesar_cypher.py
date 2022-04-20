alphabet = "abcdefghijklmnopqrstuvwxyz"
def user_choice():
    choice = input("Type 'yes' if you want to go again, otherwise type 'no: \n").lower().rstrip()
    satisfied = False
    while satisfied == False:    
        if choice == "yes":
            satisfied = True
            return True
        elif choice == "no":
            satisfied = True
            return False
        else: 
            print("\nTry Again.\n")

keep_going = True

while keep_going:
    operation = input("Type 'encode' to encrypt or 'decode' to decrypt: ").lower()
    correct_operation = False
    while correct_operation == False: 
        if operation !=  "encode" and operation != "decode": 
            print("\nTry again.\n")
        else: 
            correct_operation = True
    if operation == "encode": 
        user_message = [char for  char in input("Type your message: \n").lower()]
        shift = int(input("Type shift number: \n"))
        for index_message in range(len(user_message)): 
            char = user_message[index_message]
            if char in alphabet:
                index_alpha = alphabet.index(char)
                user_message[index_message] = alphabet[(index_alpha+shift) % 26]
        print("Encrypted Message: \n{}".format("".join(user_message)))
        keep_going = user_choice()
    elif operation == "decode":
        user_message = [char for  char in input("Type your message: \n").lower()]
        shift = int(input("Type shift number: \n"))
        for index_message in range(len(user_message)): 
            char = user_message[index_message]
            if char in alphabet:
                index_alpha = alphabet.index(char)
                user_message[index_message] = alphabet[(index_alpha-shift) % 26]
        print("Decrypted Message: \n{}".format("".join(user_message)))
        keep_going = user_choice()

        




