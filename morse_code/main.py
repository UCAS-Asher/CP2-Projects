#Asher Wangia, Simple Morse Code Translator
import string


english = list(string.ascii_lowercase)

morse_code = ["._","_...","_._.","_..",".",".._.","__.","....","..",".___","_._","._..","__","_.","___",".__.","__._","._.","...","_",".._","..._",".__","_.._","_.__","__.."]


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
        message_morse_code = input("What is your message in morse code: ")
    else:
        exit()
    

def trans_english(message):
    translation = []
    
    for letter in message:
        for x in english:
            if letter == x:
                translation.append()



while True:
    main()