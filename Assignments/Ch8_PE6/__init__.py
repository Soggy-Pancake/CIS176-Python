import os

def assignmentName() -> str:
    return "Chapter 8 (Average Number of Words)"

def main():

    if not os.path.exists("text.txt"): # make sure we are in assignment dir so it sees text.txt
        path = __file__[:__file__.rfind('\\')]
        os.chdir(path)

    with open("text.txt", "r") as textFile:
        text = textFile.readlines()

        totalChars = 0
        wordCount = 0

        for i in range(len(text)):
            line = text[i]
            totalChars += len(line)
            wordCount += len(line.split()) # Doesnt ignore numbers but whatever im not bothering filtering them out 

            print(f"Sentence {i + 1} is {len(line)} characters.")

        print("")
        print(f"The sum of all character is {totalChars} characters")
        print(f"The average of characters per line is {totalChars / len(text)}")
        print(f"Average word count: {wordCount / len(text)}")


if __name__ == "__main__":
    assignmentName() #just to give a warning when I copy paste this to other assignments
    main()