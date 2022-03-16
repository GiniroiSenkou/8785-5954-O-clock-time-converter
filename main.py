from datetime import datetime
import time

bwithminutes = 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19, 21, 22, 23, 24, 26, 27, 28, 29
pwithminutes = 31, 32, 33, 34, 36, 37, 38, 39, 41, 42, 43, 44, 46, 47, 48, 49, 51, 52, 53, 54, 56, 57, 58
bwithoutminutes = 5, 10, 20, 25
pwithoutminutes = 35, 40, 50, 55

time_in_words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty', 'twenty-one', 'twenty-two', 'twenty-three', 'twenty-four', 'twenty-five', 'twenty-six', 'twenty-seven', 'twenty-eight', 'twenty-nine']

def time_converter():
    Chour = int(datetime.now().strftime("%I"))
    Cminute = int(datetime.now().minute)

    if Cminute == 1:
        var = f"{time_in_words[Cminute]} minute past {time_in_words[Chour]}"
    elif Cminute == 15:
        var = f"a quarter past {time_in_words[Chour]}"
    elif Cminute in bwithminutes:
        var = f"{time_in_words[Cminute]} minutes past {time_in_words[Chour]}"
    elif Cminute in bwithoutminutes:
        var = f"{time_in_words[Cminute]} past {time_in_words[Chour]}"
    elif Cminute == 30:
        var = f"half past {time_in_words[Chour]}"
    elif Cminute in pwithminutes:
        var = f"{time_in_words[60 - Cminute]} minutes to {time_in_words[Chour + 1]}"
    elif Cminute in pwithoutminutes:
        var = f"{time_in_words[60 - Cminute]} to {time_in_words[Chour + 1]}"
    elif Cminute == 45:
        var = f"a quarter to {time_in_words[Chour + 1]}"
    elif Cminute == 59:
        var = f"a minute to {time_in_words[Chour + 1]}"
    else:
        var = f"{time_in_words[Chour]} o\'clock"
    var = f"It's {var}."
    return var

while True:
    print(time_converter())
    time.sleep(1)
