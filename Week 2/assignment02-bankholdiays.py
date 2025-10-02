# The objecive of this program is to print out the dates of the bank holidays that happen in northern Ireland.

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


# References:

# https://www.gov.uk/bank-holidays.json - For the live data on the UK's public holidays
# https://www.geeksforgeeks.org/python/json-dump-in-python/ - For getting the Json file in a readable format
# https://www.w3schools.com/python/ref_requests_get.asp - For the request command that allows me to get data from URLs.