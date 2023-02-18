"""
Exercise # 3

Congrats!  Variables and print outs are the bread and butter of coding

We are going to up the difficulty a little bit!

you don't need to create a f-print statement in order to print a variable.
We can just write:
    print(variable)
obviosuly exchange the word variable for whatever the name of the variable is


This exercise is going to introduce some other variable types.
lists. 

Think about this in the real world for a second.  Your mom wants to know what
is on the shopping list, but she can't remember what the 7th item on the list
was.  She might ask you "Can you tell me what the 7th item on the 
shopping list is?"  So you go to the list, and look for the 7th item on it.

This is similar to how computers work.  You need to tell it WHICH list to
look at, and WHAT item on the list

in terms of code, the above example would look like:
shopping_list[7]  # calls the 7th item inside the shopping list

python starts counting at 0.
so in this list
list_1 = [0, 1, 2, 3, ...] the numbers represent the position on the list

animal_list = ['monkey', 'skink', 'salamander']

the monkey is the zeroth position but the first item on the list
skink is the first position, and the second item
salamander is the second position, but the third item 

To create a new line inside of a print statment, you must call the
\ <-- slash operator and n for new line
this looks like:
\n
------------------------------------------------------
------------------------------------------------------

When this is executed properly, you can move to the next exercise!
"""
##############################################################################
##############################################################################
# DO NOT CHANGE THESE 

a = 7  # You can put comments after your code as well!
b = [6, 8, 9]  # This is a list of numbers
c = ['Orange', 'Doctor', 'Peeling', 'banana', 'bunches']

# To print an individual item from a list, you call the list[index_number]
print(F'\nThe variable a, is {a}  || This should be 7')

print(F'\nThe variable b, is {b}  || This should be 6, new line, 7, new line, 8')

print(F'\nWhy did the {c[0]} go to the {c[1]}')
print(F"Because it wasn't {c[2]} well!")

print(F'\nWhy dont {c[3]} ever feel lonely?')
print(F"Because they always hang out in  {c[4]}!")


##############################################################################
# INSERT YOUR CODE HERE

## 1. ----------------------------------
# Write a list of 10 unique numbers

# Print each of the numbers in the list  HINT: this can be done in one line

# Create a variable called my_sum and add all of the numbers in the list

# Print the variable my_sum


## 2. ----------------------------------
# Going to give less instructions on this one.
# I made 2 fruit based jokes above.  Follow that example and create your own! 

##############################################################################



print("\nPython Exercise #3 Complete!\n")