def get_country():
        print("""
        Countries to Change Money From
        1. U.S.
        2. Japan
        3. Australia
        4. Canada
        """)
        
        country = input("Choose a Number: ")

        if country == "1":#get the country based on user input and use it for other functions
            country = "U.S."
        elif country == "2":
            country = "Japan"
        elif country == "3":
            country = "Australia"
        elif country == "4":
            country = "Canada"
        else:
            print("Not a Country")
            get_country()

        return country