import os

def assignmentName() -> str:
    return "Chapter 6 (Average of numbers)"

def removeEmpty(inputList : list):
    returnList = []
    for item in inputList:
        if item.strip() == "":
            continue
        returnList.append(item)

    return returnList

def main():

    filePath = __file__[:__file__.rfind("\\")] + "/numbers.txt" 
    print(filePath)

    if not os.path.exists(filePath):
        print("Numbers file not found! Exiting...")
        return

    with open(filePath, 'r') as numFile: # python auto closes using with
        nums = numFile.readlines()

        nums = removeEmpty(nums) # remove any extra empty lines since we are using array length for count
        
        total = 0

        for num in nums:
            total += float(num.strip()) # float as there's no garuntee it will be an int in testing

        print(f"Sum of Numbers: {total}")
        print(f"Count of Numbers: {len(nums)}")
        print(f"Average: {total/len(nums)}")


if __name__ == "__main__":
    assignmentName() #just to give a warning when I copy paste this to other assignments
    main()