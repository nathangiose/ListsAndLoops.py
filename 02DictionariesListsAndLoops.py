# Nathan John Giose
# I know people are going to be discouraged when they see dictionaries,
# I used to be in the same- so now I'm making it simpler by putting it the way
# I learnt it from David and Chuck's class
# I put in built in values (Boolean-True/False) as well


students = [{"name": "Nathan John", "location": "M/Plain", "Genius": True},
                 {"name": "Tashwill", "location": "M/Plain", "Genius": True},
                 {"name": "Uthmaan", "location": "M/Plain", "Genius": True},
                 {"name": "Abdul-Malik", "location": "M/Plain", "Genius": True},
                 {"name": "Mujaid", "location": "H/Park", "Genius": False},
                 {"name": "Gary", "location": "E/River", "Genius": False}]
# Please pay attention to the fact that I put the dictionary in the list


for student in students:
    print("The current student is ", student)
    # There's a simpler way to get the same printed information,
    # it is done in the by inserting an 'f'


    print(f"\nThe current student is {student}")
