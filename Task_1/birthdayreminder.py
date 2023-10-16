from datetime import datetime, timedelta

class BirthdayReminder:
    def __init__(self, users):
        self.users = users
        self.today = datetime.today().date()
        self.weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        self.birthday_dict = {day: [] for day in self.weekdays}
        self.next_week_birthday_dict = {day: [] for day in self.weekdays}

    def calculate_birthdays(self):
        for user in self.users:
            name = user.name
            birthday = user.birthday.date()
            birthday_this_year = birthday.replace(year=self.today.year)

            if birthday_this_year < self.today:
                birthday_this_year = birthday_this_year.replace(year=self.today.year + 1)

            delta_days = (birthday_this_year - self.today).days
            if delta_days < 7:
                day_of_week = self.weekdays[(self.today.weekday() + delta_days) % 7]
                if delta_days < 7:
                    self.birthday_dict[day_of_week].append((name, delta_days))
                else:
                    self.next_week_birthday_dict[day_of_week].append((name, delta_days))

    def print_birthdays(self):
        for day, names_and_days in self.birthday_dict.items():
            if names_and_days:
                names = [name for name, delta_days in names_and_days]
                if day == "Today (Monday)":
                    print(f"{day}: {', '.join(names)}")
                elif day == "Today":
                    print(f"Today ({self.weekdays[self.today.weekday()]}): {', '.join(names)}")
                elif day == "Saturday" or day == "Sunday":
                    print(f"Next Monday: {', '.join(names)}")
                else:
                    print(f"{day}: {', '.join(names)}")

        for day, names_and_days in self.next_week_birthday_dict.items():
            if names_and_days:
                names = [name for name, delta_days in names_and_days]
                print(f"Next {day}: {', '.join(names)}")
