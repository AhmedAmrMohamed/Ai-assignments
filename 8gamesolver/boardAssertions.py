from constants import BOARD_NUM_COUNT

def checkInputNumbers(numbers):
    if len(numbers) != BOARD_NUM_COUNT:
        raise ValueError(f"input must consist of {BOARD_NUM_COUNT} numbers")

    if checkAllNumbersExistOnce(numbers) == False:
        raise ValueError(f"input must contain all the numbers between 0 and {BOARD_NUM_COUNT-1}.")

def checkAllNumbersExistOnce(numbers):
    for idx in range(BOARD_NUM_COUNT):
        if not idx in numbers:
            return False
    return True

