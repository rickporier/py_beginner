# General notes on things to remember for futre reference.
#---------------------------------------------------------

# Some how to recoginize the difference between.

# Lists - Lists are contained in brackets.

my_list=[1,2,3]

# Sets - Sets are in curly brackets.

my_set= {1,2,3}

# Tuples - Tuples are contained in parenthesis.

my_tuple=(1,2,3)

# Dictionaries - Contained in curly braces. 

my_dict={'key': 'value'}

#Dictionairy Example

my_dict={
    'name':'raj',
    'role': 'coder',
    'salary': '120000'
}
# Left column are KEYS (each must be unique). The right are values
#   and do not have to be unique. 

my_dict['age']=30  #this will add the KEY 'age' and the VALUE '30'

print(my_dict.get('age'))

print(my_dict.keys()) # This is called a 'View Object'.
        # Looks like a list when printed but not a list.

# all the things you can use as a VALUE in a dictionairy.
    # - Strings, intergers, floats, lists, booleans, tuple, 
        # a set, a dictionary (inside the dictionairy).

#EXAMPLE: Name as the KEY and a dictionairy as a VALUE.

my_emp={
    'Raj':{
        'role':'coder',
        'salary':'120000'
    },
    'Sam':{
        'role':'designer',
        'salary':'115000'

    }
}

my_emp['Raj']['salary']=135000 # Raj got a raise.

print(my_emp.get('Raj'))

