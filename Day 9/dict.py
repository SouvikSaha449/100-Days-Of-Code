programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again.",
    
}

# #retriving items from a dictonary
# print(programming_dictionary["Function"])

# adding new item to the dictionary 
programming_dictionary["Loop"] = "The action of doing something over and over"
print(programming_dictionary)

#wipe an entire dictionary
# programming_dictionary={}
# print(programming_dictionary)

#editing a key in a dictionary
programming_dictionary["Bug"] = "A moth on the computer"
print(programming_dictionary)

#looping through a dictionary

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key] + "\n")


##################################################################
    

#nesting a dicionary in a dictionary

travel_log={
    "France":{
    "cities_visited":["Paris","Little","Dijon"],
    "total_visits":12
    },
    "Germany":{
    "cities_visited":["Berlin","Hamburg","Stuttgart"] ,
    "total_visits":6
    },
}

#Nesting dictionary in a list

travel_log=[
    {
    "country":"France",
    "cities_visited":["Paris","Little","Dijon"],
    "total_visits":12
    },
    {
    "country":"Germany",
    "cities_visited":["Berlin","Hamburg","Stuttgart"] ,
    "total_visits":6
    },
]

for i in travel_log:
    print(i)

