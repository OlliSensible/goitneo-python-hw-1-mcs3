from birthdayreminder import BirthdayReminder
from models import users

if __name__ == "__main__":
    reminder = BirthdayReminder(users)
    reminder.calculate_birthdays()
    reminder.print_birthdays()
