times = 0

print("Hello, World!")
name = input("What is your name? ")

while True:
    times_input = input("How many times should I say hello (q to quit)? ")
    if times_input == 'q':
        break
    elif times_input == '':
        continue
    times = int(times_input)

    if times > 100:
        print("Yikes, that's too many!")
    else:
        for x in range(1,times+1):
            print(str(x) + ": Hello, " + name + "!")

print("Thank you for playing the hello game!")