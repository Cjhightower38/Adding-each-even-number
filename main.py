#Write your code below this row 👇
'''
Set a variable equal to 0 loop through each number starting at 0 (+=) mean to add each number to it's self and store the results back into the variable or accumulator and print to console.
'''
total = 0
for number in range(0, 101, 2):
  total += number
print(total)