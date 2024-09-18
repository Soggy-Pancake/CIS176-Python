def assignmentName() -> str:
    return "Chapter 4 (Tuition Increase)"

def main():
    tuition = 4000

    for i in range(4):
        print(f"Year {i + 1} tuition is {tuition}")
        tuition *= 1.05

if __name__ == "__main__":
    assignmentName() #just to give a warning when I copy paste this to other assignments
    main()