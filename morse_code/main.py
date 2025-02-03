#Asher Wangia, Simple Morse Code Translator
import string


english = list(string.ascii_lowercase)
english.append(" ")

morse_code = ["._","_...","_._.","_..",".",".._.","__.","....","..",".___","_._","._..","__","_.","___",".__.","__._","._.","...","_",".._","..._",".__","_.._","_.__","__..", " "]


def main():
    print("""
    What would you like to do?
        1. Translate English To Morse Code
        2. Translate Morse Code to English
        3. Exit
    """)
    
    choice = input("Choose a number: ")
    if choice == "1":
        trans_english(input("What is your message in english: ").lower())
    elif choice == "2":
        morse_code_message = []
        
        add_letters = True
        while add_letters == True:
            print("""
            Do you want to continue adding letters
            1. Yes
            2. No
            """)
            morse_code_choice = input("Choose a Number: ")
            if morse_code_choice == "1":
                morse_code_letter = input("What is your letter in morse code: ")
                morse_code_message.append(morse_code_letter)
            elif morse_code_choice == "2":
                trans_morse_code(morse_code_message)
                add_letters = False
                
    else:
        exit()
    

def trans_english(message):
    translation = []
    
    for letter in message:
        for x in english:
            if letter == x:
                morse_code_index = english.index(letter)

                translation.append(morse_code[morse_code_index])
    
    print("Your translated message is: ","".join(translation))



def trans_morse_code(message):
    translation = []

    for letter in message:
        for x in morse_code:
            if letter == x:
                english_index = morse_code.index(letter)
                translation.append(english[english_index])

    print("Your translated message is: ","".join(translation))


while True:
    main()