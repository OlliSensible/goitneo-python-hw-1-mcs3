class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone):
        self.contacts[name] = phone
        return "Contact added."

    def change_contact(self, name, new_phone):
        if name in self.contacts:
            self.contacts[name] = new_phone
            return "Contact updated."
        else:
            return "Contact not found."

    def show_phone(self, name):
        if name in self.contacts:
            return self.contacts[name]
        else:
            return "Contact not found."

    def show_all(self):
        if not self.contacts:
            return "No contacts found."
        result = "\n".join([f"{name}: {phone}" for name, phone in self.contacts.items()])
        return result

    def handle_input(self, user_input):
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()

        if cmd == "hello":
            return "How can I help you?"
        elif cmd == "add" and len(args) == 2:
            return self.add_contact(args[0], args[1])
        elif cmd == "change" and len(args) == 2:
            return self.change_contact(args[0], args[1])
        elif cmd == "phone" and len(args) == 1:
            return self.show_phone(args[0])
        elif cmd == "all" and not args:
            return self.show_all()
        elif cmd in ["close", "exit"]:
            return "Good bye!"
        else:
            return "Invalid command."