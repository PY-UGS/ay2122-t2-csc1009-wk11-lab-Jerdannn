class ClockTime:
    # Creates an instance that takes in
    # hours, minutes and seconds
    def __init__(self):
        self.hours = None
        self.minutes = None
        self.seconds = None

    def setHours(self, h):
        self.hours = h

    def setMinutes(self, m):
        self.minutes = m

    def setSeconds(self, sec):
        self.seconds = sec

    def setTime(self, h, m, sec):
        self.hours = h
        self.minutes = m
        self.seconds = sec

    def showTime(self):
        # Print out everything
        print("{}:{}:{}".format(self.hours,
                                self.minutes, self.seconds))


def checkTime(t, val, check):
    # Handle for minutes (1 to 59)
    if t == "minutes":
        if val >= 60:
            check = True
            return val, check
        else:
            check = False
            return val, check
    # Handle for seconds (1 to 59)
    else:
        if val >= 60:
            check = True
            return val, check
        else:
            check = False
            return val, check


def main():
    ct = ClockTime()
    minutes_add = 0
    hours_add = 0
    check = False

    user_hours = int(input("Please enter the hours: "))
    user_minutes = int(input("Please enter the minutes: "))
    user_seconds = int(input("Please enter the seconds: "))

    # Check should start from seconds
    user_seconds, check = checkTime("seconds",
                                    user_seconds, check)
    # Seconds exceeded 60
    if check:
        # Excess to be added to minutes
        minutes_add = int(user_seconds / 60)
        # Remainder to stay in seconds
        user_seconds = user_seconds % 60

    # Next check should be minutes
    user_minutes, check = checkTime("minutes",
                                    user_minutes + minutes_add
                                    , check)
    # Minutes exceeded 60
    if check:
        # Excess to be added to hours
        hours_add = int(user_minutes / 60)
        # Remainder to stay in minutes
        user_minutes = user_minutes % 60

    # For hours, no real carry over needed
    user_hours = (user_hours + hours_add) % 24

    ct.setTime(user_hours, user_minutes, user_seconds)
    ct.showTime()


if __name__ == "__main__":
    main()