def get_country():
        print("""
        Countries to Change Money From
        1. America
        2. Japan
        3. Australia
        4. Canada
        """)
        
        country = input("Choose a Number: ")

        if country == "1":
            country = "America"
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