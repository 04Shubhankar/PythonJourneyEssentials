import random

# This line imports the random module, which is used to generate random choices.

when = ['A few years ago', 'Yesterday', 'Last night', 'A long time ago', 'On 20th Jan']

# This line creates a list of time phrases.

who = ['a rabbit', 'an elephant', 'a mouse', 'a turtle', 'a cat']

# This line creates a list of animals.

name = ['Ali', 'raj', 'daniel', 'Hoouk', 'Starwalker']

# This line creates a list of names.

residence = ['Barcelona', 'India', 'Germany', 'Venice', 'England']

# This line creates a list of places.

went = ['cinema', 'university', 'seminar', 'school', 'laundry']

# This line creates a list of activities.

happened = ['made a lot of friends', 'Eats a burger', 'found a secret key', 'solved']

# This line creates a list of events.

# This line randomly selects an element from each list and concatenates them into a sentence using string formatting.
print(random.choice(when) + ', ' + random.choice(who) + ' that lived in ' + random.choice(residence) + ', went to the ' + random.choice(went) + ' and ' + random.choice(happened))
