error_messages = {
    1: "Wrong Email 1: Email length should be at least 6 characters.",
    2: "Wrong Email 2: Email should start with an alphabet.",
    3: "Wrong Email 3: Email should contain exactly one '@'.",
    4: "Wrong Email 4: Email should end with a dot (either 3rd or 4th position from the end).",
    5: "Wrong Email 5: Email contains invalid characters, spaces, or uppercase letters."
}


email = input("Enter your Email : ")
k,j,d= 0,0,0
if len(email)>=6 :
    if email[0].isalpha():
        if ( "@" in email ) and (email.count("@")==1):
            if (email[-4]==".") ^ (email[-3]=="."):
                for element in email :
                    if element==element.isspace():
                        k = 1
                    elif element.isalpha():
                        if element == element.upper():
                            j = 1
                    elif element.isdigit():
                        continue
                    elif element == "_" or element == "." or element == "@":
                        continue
                    else:
                        d = 1
                if k == 1 or j == 1 or d == 1 :
                    print(error_messages[5])
                else:
                    print("Email is Correct.")
            else:
                print(error_messages[4])
        else:
            print(error_messages[3])
    else:
        print(error_messages[2])
else:
    print(error_messages[1])
