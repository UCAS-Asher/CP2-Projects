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
        else:
            print("Not a Country")
            get_country()

        return country