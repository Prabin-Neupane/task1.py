# bird = ['crows','pigeon','eagles','falcon','pigeon','falcon','falcon']
# Remove all the duplicates from the following list using while.
bird = ['crows','pigeon','eagles','falcon','pigeon','falcon','falcon']
new =[]
while bird:
    x = bird.pop()
    if x not in new:
        new.append(x)
print(new)

#Deli: Make a list called sandwich_orders and fill it with the names of various sandwiches.
#Then make an empty list called finished_sandwiches . Loop through the list of sandwich orders and print a message
#for each order, such as I made your tuna sandwich. As each sandwich is made, move it to the list of finished sandwiches.
# After all the sandwiches have been made, print a message listing each sandwich that was made.
sandwitch_orders=['every','night','in','my','dream','i','see','you']
finished_sandwitch = []
while sandwitch_orders:
    x = sandwitch_orders.pop()
    print("I am making your {} sandwitch".format(x))
    finished_sandwitch.append(x)
for items in finished_sandwitch:
    print(items + "sandwitch is made . Aaija khana xito aailey sakinxa")


# Dream Vacation: Write a program that polls users about their dream vacation.
# Write a prompt similar to If you could visit one place in the world, where would you go?
# Include a block of code that prints the results of the poll.
from collections import Counter
action = True
lists = []
x=0
while action:
    place = input("\nenter your dream vacation :")
    lists.append(place)
    again = input("\nany other dreams ? (Y/N)\n")
    if (again == "N"):
        action = False

print(lists)
duplicate_dict = {i:lists.count(i) for i in lists}
print(duplicate_dict)
poll = Counter(lists)
print(poll)


