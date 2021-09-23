import random

if __name__ == "__main__":
    while True:
        min = input('Select a minimal value : ')
        max = input('Select a maximal value : ')
        if(not min.isdigit() or not max.isdigit()):
            print('Please enter digits only')
            continue
        else:
            secret = random.randint(int(min),int(max))
            while True:
                value = input('Select a number : ')
                if(value.isdigit()):
                    value = int(value)
                else:
                    print('Please enter digits only')
                    continue
                if(value == secret):
                    answer = input("GG, you found the secret number, want to play again ? (y/n)")
                    if answer == 'y':
                        break
                    else:
                        exit()
                elif(value > secret):
                    print("Secret is Lower")
                elif(value < secret):
                    print("Secret is Higher")