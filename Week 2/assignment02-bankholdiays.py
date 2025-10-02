# The objecive of this program is to print out the dates of the bank holidays that happen in Northern Ireland.

# Author: Loic Bagnoud


# We first import the two packages we need.
import requests
import json

# This part gets us the URL which is live data and stores it in a variable called url.
url = "https://www.gov.uk/bank-holidays.json"

# We follow this up with the requests command to get the the data from that same variable.
response = requests.get(url)

# We get the data in a Json format.
data = response.json()

# We then basically format in a way that we can read. We use the "with" statement to open it and then use the dump function with an indentation
# at the 4th level.
with open("data", "w") as outfile:
    json.dump(data, outfile, indent=4)

# And then we just print out what we need. We start out with a quick print to make it look pretty, followed by
# a for loop that goes through the variable data and looks specifically at the Northern Ireland dictionary and its events.
print(f"These are the holidays and the dates for Northern Ireland\n")

for holiday in data["northern-ireland"]["events"]:
    print(f"{holiday['date']} – {holiday['title']}")

# This part was more complicated but ChatGPT had a good idea and I tried to follow it. 
# I had a problem when I used dates for the last for loop because I had multiple holidays in different days and it looked confusing,
# so I chose to sort it by title and used the break function to stop the loop

print(f"These are the holidays and the dates that are UNIQUE to Northern Ireland\n")

# I was having issues with duplicate holidays, so this helped me fix it. It's a little set that allows me to put duplicates tucked away. It looks cleaner.
printed = set()

# This for loop basically goes through the data and assumes that each value in that dictionary is unique.
# So we set that unique variable to TRUE.
for holiday in data["northern-ireland"]["events"]:
    unique = True  

# Afterwards, we check England to see if there are duplicates. If so, unique becomes FALSE. 
    for england_holiday in data["england-and-wales"]["events"]:
        if holiday["title"] == england_holiday["title"]:
            unique = False
            break

# We do the same for Scotland
    for scotland_holiday in data["scotland"]["events"]:
        if holiday["title"] == scotland_holiday["title"]:
            unique = False
            break

# And finally, if unique is still TRUE, we print out the holiday from the dictionary. Because this rests inside the for loop, it will go through 
# each holiday in the Northern Ireland section. It will also put duplicates inside the set we created above with the .add function.
    if unique and holiday["title"] not in printed:
        print(holiday["title"])
        printed.add(holiday["title"])


# References:

# https://www.gov.uk/bank-holidays.json - For the live data on the UK's public holidays
# https://www.geeksforgeeks.org/python/json-dump-in-python/ - For getting the Json file in a readable format
# https://www.w3schools.com/python/ref_requests_get.asp - For the request command that allows me to get data from URLs.
# https://docs.python.org/3/library/stdtypes.html#truth-value-testing - For reminding myself of Boolean Value logic.
# https://www.geeksforgeeks.org/python/python-break-statement/ - For the break statement.
# https://stackoverflow.com/questions/61596005/replace-set-to-keep-duplicates - This discussion had one user talk about how set() is used to remove duplicates and that led me to 
# the set statement.
# https://www.geeksforgeeks.org/python/python-set-function/ - Where I researched set() to store duplicates.

# ChatGPT - He gave the nifty idea about using TRUE and FALSE switches to check if an element is unique:
''' 
Instead of any(...) expressions, just use a plain loop and an if flag.

for holiday in data["northern-ireland"]["events"]:
    unique = True  # assume it's unique unless we find a match

    # check England/Wales
    for h in data["england-and-wales"]["events"]:
        if holiday["date"] == h["date"]:
            unique = False
This version just:

- Loops over NI holidays.
- Starts with unique = True.
- If the date shows up in the other regions, flip it to False.
- Print only if it stayed True.
'''