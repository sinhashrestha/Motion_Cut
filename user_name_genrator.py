import random
adjectives = ["Cool", "Epic", "Funky", "Swift", "Brave"]
nouns = ["Panda", "Wizard", "Gamer", "Ninja", "Dragon"]

def generate_username(format="Adjective_Noun", count=1):
    usernames = []
    for _ in range(count):
        adj = random.choice(adjectives)
        noun = random.choice(nouns)
        if format == "Adjective_Noun_Number":
            number = random.randint(100, 999)
            username = f"{adj}{noun}{number}"
        else:
            username = f"{adj}_{noun}"
        usernames.append(username)
    return usernames

def save_to_file(usernames, filename="usernames.txt"):
    with open(filename, "w") as file:
        for username in usernames:
            file.write(username + "\n")
    print(f"Usernames saved to {filename}.")

def main():
    print("Welcome to the Username Generator!")
    format = input("Choose format (Adjective_Noun or Adjective_Noun_Number): ")
    count = int(input("How many usernames do you want to generate? "))
    
    usernames = generate_username(format, count)
    print("\nGenerated Usernames:")
    for username in usernames:
        print(username)
    
    save_option = input("\nDo you want to save these usernames to a file? (yes/no): ").lower()
    if save_option == "yes":
        save_to_file(usernames)
    print("Thank you for using the Username Generator!")

if __name__== "_main_":
    main()