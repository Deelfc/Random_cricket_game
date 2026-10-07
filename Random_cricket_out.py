import random

out_types = ["Bowled", "Caught", "LBW", "Run out"]

user_total = 0
computer_total = 0

for ball in range(1, 7):
    user = int(input(f"Ball {ball} - your number (1-6): "))
    computer = random.randint(1, 6)

    print("Computer:", computer)

    
    if random.randint(1, 6) == 1:
        print("Out!", random.choice(out_types))
        break

    user_total += user
    computer_total += computer

print("Your total:", user_total)
print("Computer total:", computer_total)

if user_total > computer_total:
    print("You win!")
elif user_total < computer_total:
    print("Computer wins!")
else:
    print("Match tied!")
    
    