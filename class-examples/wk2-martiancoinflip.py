import random

print("Welcome to the Martian Coin Toss Simulator!")
num_tosses = int(input("Enter the number of coin tosses: "))

if num_tosses <= 0:
    print("Please enter a valid number of coin tosses.")

heads_count = 0
tails_count = 0

for toss_number in range(num_tosses):
    toss_result = random.choice(["heads", "tails"])
    if toss_result == "heads":
        heads_count += 1
    else:
        tails_count += 1
    print(f"Toss result {toss_number + 1}: {toss_result}")

print("\nToss summary:")
print(f"Heads: {heads_count} ({(heads_count / num_tosses) * 100:.2f}%)")
print(f"Tails: {tails_count} ({(tails_count / num_tosses) * 100:.2f}%)")

