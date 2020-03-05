# This program will generate a list of 29 random numbers. It will then sort the list and find
# the mean, median, and total.
# Chris Blaylock
# 11/15/2019

# Import random module

import random

# Define the variable "total" to be used to find the total.
total = 0


# Use a loop to generate a list of 29 random numbers between 1 and 500. 
rand_list = [random.randint(1,500) for num in range(29)]

# Sort the random list that was generated. 
sort_list = sorted(rand_list)

# Finding the total: Use a loop to find the total of all the random numbers.
for num in rand_list:
    total = total + num

# Average: divide the total by 29 because there are 29 numbers that were generated.
avg = total / 29
# Median: Use the index 15 be that is the median of 29 which is how many numbers there are.  
medianNum = (sort_list[15]) 



# Output: Print the generated lists, the total, the average, and the median. 
print ("The numbers in the list are:\n",rand_list,'\n')
print ("The numbers in the sorted list are:\n",sort_list,'\n')
print ("Total: ", total)
print ("Average: ", format(avg,'.2f'))
print ("Median: ", medianNum)


