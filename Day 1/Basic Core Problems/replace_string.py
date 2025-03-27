#Question 1: Replace Username with the given input

str1 = "Hello <<UserName>>"
name = input("Enter a name of length greater than 3: ")

# Method 1: Using the replace function 
# if len(name)>3:
#     str1 = str1.replace("<<UserName>>", name)

#Method 2: Without using the replace function
if len(name)>3:
    start = str1.find("<<UserName>>")
    end = start+len("<<UserName>>")
    str1 = str1[:start] + name + str1[end:]
    
print (str1+". How are you?")