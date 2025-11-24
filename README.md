# Programming-for-Data-Analytics-Assignments

All exercises are in their appropriate folder.

# Description of the Exercises

Week 2

For this exercise, I got the live bank holiday data from the GOV.UK URL, converted it from JSON into a Python dictionary, and then worked specifically with the Northern Ireland bank holidays. I decided to keep all available years instead of filtering just the current year to keep the assignment simple.

First, I print all the holidays (date and title) for Northern Ireland.
Then, I print only the holidays that are unique to Northern Ireland, meaning holidays whose title does not appear in England and Wales or Scotland.

For each Northern Ireland holiday, I start by assuming it is unique (unique = True). I then loop through the England and Wales holidays and the Scotland holidays; if I find a holiday with the same title, I set unique = False and stop checking. I also use a set called printed to keep track of titles I’ve already printed, so the same unique holiday title is not printed more than once.

If, after these checks, unique is still True and the title is not in printed, I print the holiday and add its title to the printed set.

Week 3

For this exercise, I continued from where we left off with the emails after they had all been sorted. The tricky part was making the pie chart look good. We started by counting all the values in the domain column and then adding their percentage values. The main issue came with the legend, but after checking Matplotlib’s documentation, .legend helped us customise the legend and put it where it needed to be.

Week 5

For this exercise, for Part 1, we followed from where we left off in class and organised the data. My main issue here was sorting the data. I was struggling a lot with groupby, so I eventually went with a simple for loop. I created a dictionary to store the values in. Then, I looked for unique values in the Sex column (in this case, male and female) and created a smaller dataframe that only contains rows where the Sex column matches that sex. Afterwards, we applied the NumPy function the same way we did to the Age column and appended those results to the dictionary.

For Part 2, we created a boolean mask that goes through the Single Year of Age column and marks ages between the chosen age minus 5 and plus 5. Afterwards, I followed the same logic as before with the dictionary, with the difference being that we summed up the results and then got the actual difference.

For Part 3, I had to be careful not to include Ireland, since by default it has the biggest population and it would skew the data. So, I went ahead and applied the same for loop logic (making sure I skipped Ireland), then summed everything up and calculated the difference. I wasn’t sure if we needed the absolute difference instead of the signed difference, so I included both.

Week 6

For this task, I started by cleaning the data. The issue was that the dataset had many missing values, meaning that the code took over a minute to execute. I found out later that this was because pandas was trying to iterate through each non-existent value and adjust accordingly. After finding out about the coerce option in to_datetime, I went ahead and applied that to reduce load time. I kept the original code anyway for posterity.

Afterwards, we moved on to the plotting. The code explanations are in the code itself, but the interesting thing here was that there were a lot of 0 values at both the beginning and the end of the dataset when it came to the wind speed. This led me to find out that it’s perfectly normal, since it just means the instruments are calibrating or powering down. I removed the initial 20 rows of data because they didn’t really add anything to the overall analysis and they made the plot look weird.