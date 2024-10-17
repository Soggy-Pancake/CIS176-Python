from random import randint

def assignmentName() -> str:
    return "Chapter 7, Lottery Number Generator"

def main():
    
    lotteryNum = []
    numberCount = 7

    for i in range(numberCount):
        lotteryNum.append(randint(0,9))

    for num in lotteryNum:
        print(num)

if __name__ == "__main__":
    assignmentName() #just to give a warning when I copy paste this to other assignments
    main()