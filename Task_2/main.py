from contact_manager import ContactManager

def main():
    print("Welcome to the assistant bot!")
    contact_manager = ContactManager()

    while True:
        user_input = input("Enter a command: ")
        result = contact_manager.handle_input(user_input)
        print(result)

if __name__ == "__main__":
    main()
