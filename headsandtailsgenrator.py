import random
def coin_toss():
    return random.choice(["Heads", "Tails"])
def multiple_tosses(num_flips):
    heads_count = 0
    tails_count = 0
    for _ in range(num_flips):
        result = coin_toss()
        if result == "Heads":
            heads_count += 1
        else:
            tails_count += 1
    return heads_count, tails_count
def coin_toss_simulation():
    while True:
        num_flips = int(input("Enter the number of times you want to flip the coin: "))
        heads_count, tails_count = multiple_tosses(num_flips)
        heads_percentage = (heads_count / num_flips) * 100
        tails_percentage = (tails_count / num_flips) * 100
        print(f"\nResults after {num_flips} flips:")
        print(f"Heads: {heads_count} ({heads_percentage:.2f}%)")
        print(f"Tails: {tails_count} ({tails_percentage:.2f}%)")
        repeat = input("\nDo you want to flip again? (yes/no): ").lower()
        if repeat != "yes":
            print("Exiting the program. Thank you!")
            break
coin_toss_simulation()