import re

class Time:
    # Class attributes
    TIME_FORMATS = ("AM", "PM", "24 HOURS")
    time_count = 0

    def __init__(self):
        # Instance attributes
        self.hours = 0
        self.minutes = 0
        self.seconds = 0
        self.format = None
        Time.time_count += 1

    def __asign_format(self, pszFormat):
        pszFormat = pszFormat.upper()
        if pszFormat in Time.TIME_FORMATS:
            self.format = pszFormat
            return True
        return False

    def __is_24hour_format(self):
        if self.format == "24 HOURS":
            return True
        return False

    def _is_valid_time(self):
        if self.__is_24hour_format() == True:
            return 0 <= self.hours < 23 and 0 <= self.minutes < 59 and 0 <= self.seconds < 59
        else:
            return 1 <= self.hours <= 12 and 0 <= self.minutes < 59 and 0 <= self.seconds < 59

    def set_time(self, nHoras, nMinutos, nSegundos, pszFormato):
        if self.__asign_format(pszFormato):
            self.hours = nHoras
            self.minutes = nMinutos
            self.seconds = nSegundos
            if self._is_valid_time():
                return True
            else:
                print("Invalid time values.")
        else:
            print("Invalid format.")
        return False

    def get_time(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02} {self.format}"

    @classmethod
    def from_string(cls, time_string):
        pattern = r"(\d{2}):(\d{2}):(\d{2})\s?(AM|PM|24 HOURS)"
        match = re.match(pattern, time_string.upper())
        if match:
            hours, minutes, seconds, time_format = match.groups()
            hours, minutes, seconds = int(hours), int(minutes), int(seconds)
            new_time = cls()
            if new_time.set_time(hours, minutes, seconds, time_format):
                return new_time
        print("Invalid time string format.")
        return None

    @staticmethod
    def is_valid_format(time_format):
        return time_format.upper() in Time.TIME_FORMATS

    @classmethod
    def get_time_count(cls):
        return cls.time_count

def display_time(time_obj):
    if time_obj:
        print(f"The current time is: {time_obj.get_time()}")
    else:
        print("No time object to display.")

def main():
    current_time = None

    while True:
        print("\nMenu:")
        print("1. Introduce a new time")
        print("2. Display time")
        print("3. Create time from string (format HH:MM:SS FORMAT)")
        print("4. Exit")
        option = input("Select an option: ")

        if option == "1":
            try:
                nHoras = int(input("Enter hours: "))
                nMinutos = int(input("Enter minutes: "))
                nSegundos = int(input("Enter seconds: "))
                pszFormato = input("Enter format (AM, PM, 24 HOURS): ")
                if not Time.is_valid_format(pszFormato):
                    print("Invalid time format.")
                    continue

                current_time = Time()
                if not current_time.set_time(nHoras, nMinutos, nSegundos, pszFormato):
                    current_time = None
                else:
                    print("Time set successfully.")
            except ValueError:
                print("Invalid input. Please enter numerical values for time.")

        elif option == "2":
            display_time(current_time)

        elif option == "3":
            time_str = input("Enter time string (format HH:MM:SS FORMAT): ")
            current_time = Time.from_string(time_str)
            if current_time:
                print("Time created successfully.")
            else:
                print("Failed to create time.")

        elif option == "4":
            print("Exiting program.")
            break

        else:
            print("Invalid option. Please choose a valid one.")

if __name__ == "__main__":
    main()
