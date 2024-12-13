import re # importing regex synax which checks if a string matches a given regular expression

def valid_phone_number(user_phoneNumber): #function checks if a given phone number is valid according to the regex
   user_phoneNumber = re.sub(r'\D', '', user_phoneNumber) #removes non digit characters 
   
   pattern = r'^(?:\+44|0)7\d{9}$|^(?:\+44|0)1\d{10}$|^(?:+44|0)2\d{10}$' #regex pattern for Uk mobile or landline numbers which either start with +44 (country code) or 07 (01/02 for landlines) with 9 or 10 digits following
   if(re.search(pattern, user_phoneNumber)):
    return True #checks if the given user phonenumber matches one of the given patterns and returns True 
   else:
    return False #if not valid then retunrs false 

phone_numbers = [ # a list of phone numbers to check if valid 
  "07960513709" ,
  "+44 7983544900" ,
  "02032700054",
  "1234567890"
  

]

for number in phone_numbers: 
  print (f"{number}: {valid_phone_number(number)}") # a loop that goes through the list and check if each one matches one of the regex patterns and prints a list of the valid 