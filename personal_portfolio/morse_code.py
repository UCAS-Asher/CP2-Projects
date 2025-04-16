#Asher Wangia, Simple Morse Code Translator
import string

def morse_code():

    english = list(string.ascii_lowercase)
    english.append(" ")

    morse_code_alphabet = ["._","_...","_._.","_..",".",".._.","__.","....","..",".___","_._","._..","__","_.","___",".__.","__._","._.","...","_",".._","..._",".__","_.._","_.__","__..", " "]


    def morse_code_main():# This function gets the message that is being translated
        print("""
        What would you like to do?
            1. Translate English To Morse Code
            2. Translate Morse Code to English
            3. Exit
        """)
        
        choice = input("Choose a number: ")
        
        if choice == "1":#This part runs the function that translates english to morse code and gets the message the user is translating
            trans_english(input("What is your message in english: ").lower())
        elif choice == "2": # This part gets the message in morsecode by adding each letter individually so they dont get mixed up and also runs the function to translate morse code into english
            morse_code_message = []
            get_morse_code_message(morse_code_message)
        else:
            print("Program Exit!")
           
      
    def get_morse_code_message(morse_code_message):
        
            
        print("""
        Do you want to continue adding letters
        1. Yes
        2. No
        """)
        
        morse_code_choice = input("Choose a Number: ")
                
        if morse_code_choice == "1":
            morse_code_letter = input("What is your letter in morse code: ")
            morse_code_message.append(morse_code_letter)
            get_morse_code_message(morse_code_message)
        else:
            trans_morse_code(morse_code_message)   

    def trans_english(message):#This function translates english to morse code by using the same indexes for each letter in both lists
        translation = []
        
        for letter in message:
            for x in english:
                if letter == x:
                    morse_code_index = english.index(letter)

                    translation.append(morse_code_alphabet[morse_code_index])
        
        print("Your translated message is: ","".join(translation))
        morse_code_main()



    def trans_morse_code(message):#This function translates morse code to english by using the same indexes for each letter in both lists
        translation = []

        for letter in message:
            for x in morse_code_alphabet:
                if letter == x:
                    english_index = morse_code_alphabet.index(letter)
                    translation.append(english[english_index])

        print("Your translated message is: ","".join(translation))
        morse_code_main()


    morse_code_main()
