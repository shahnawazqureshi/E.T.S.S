def firstLetterWord(str):
    result = ""

    # Traverse the string.
    v = True
    for i in range(len(str)):

        # If it is space, set v as true.
        if (str[i] == ' '):
            v = True

        # Else check if v is true or not.
        # If true, copy character in output
        # string and set v as false.
        elif (str[i] != ' ' and v == True):
            result += (str[i])
            v = False

    return result


def get_day(day):
    if day == 1:
        return "Monday"
    if day == 2:
        return "Tuesday"
    if day == 3:
        return "Wednesday"
    if day == 4:
        return "Thursday"
    if day == 5:
        return "Friday"


def get_day_and_slot(tup):
    print(get_day(tup[0]), end="")
    print(" Slot#", end="")
    print(tup[2], end="")