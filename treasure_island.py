print("Welcome to the treasure Island\n Choose your steps carefully in order to get to the treasure")
print("The game starts now!")
step1 = input("Where would you like to go? left or right")
if step1 == "left":
    print("You entered a cave")
elif step1 == "right":
    print('''A snake swalowed you
  /         \       /         \   
 /  /~~~~~\  \     /  /~~~~~\  \
 |  |     |  |     |  |     |  |
 |  |     |  |     |  |     |  |
 |  |     |  |     |  |     |  |         /
 |  |     |  |     |  |     |  |       //
(o  o)    \  \_____/  /     \  \_____/ /
 \__/      \         /       \        /
^''')
step2