def no_of_x_in_y(x, y):  # Return 1 if x is present in y
    for i in y:
        if i == x:
            return 1

def if_email(case):
    index_at_the_rate = 0
    for i in range(0, len(case)):
        if case[i] == "@":
            index_at_the_rate = i # Position at which @ is present in the email id 
            break  # After break it will run if else statements and index_at_the_rate is updated
    if no_of_x_in_y(".", case[index_at_the_rate:len(case)]) == 0:  # If we don't have (.) after @ in the email id then it is not accepted
        return 0
        
    if(len(case[0:index_at_the_rate])==0): # If their is no charcter before @ then it is not accepted
        return 0

    if no_of_x_in_y("@", case) != 1: # If @!=1
        return 0
    else:
        return 1   # in all other casses it is accepted




given_text=str(input("Please Enter The Text To Extract Email's :"))


a = given_text.split() # Text to list
emails = []
for i in range(0, len(a)):
    present_case = a[i]
    if (if_email(present_case) == 1):
        emails.append(present_case)

for i in emails:
    print(i)
