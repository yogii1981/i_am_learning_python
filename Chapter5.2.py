####################
#
# Exercise 5.1
#
# Write a program which repeatedly reads numbers until the user enters "done". 
# Once "done" is entered, print out the total, count, and average of the numbers.
# If the user enters anything other than a number, detect their mistake
# using try and except and print and error message and skip to the next number.
#
# Enter a number: 4
# Enter a number: 5
# Enter a number: bad data
# Invalid input
# Enter a number: 7
# Enter a number: done
# 16 3 5,333333333333
#
#####################

total = 0
count = 0
average = 0
error_msg = "Error, please enter a valid number."
largest = None
print 'Before: ', largest
while True:
  line = raw_input('> ')
  if line == 'done':
    break
  try:
    if float(line):
      print 'input is valid, thanks!'
      total += float(line)
      count += 1
      itervar = float(line)
      if largest is None or itervar > largest :
        largest = itervar
      print 'Loop:', itervar, largest
  except:
      print error_msg
if count!=0:
  average = total / count
  print '##DONE!'
  print '##Total: ', total
  print '##Count: ', count
  print '##Average: ', average
  print '##Largest: ', largest
else:
  print 'You did not enter any values!'