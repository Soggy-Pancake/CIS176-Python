"""
Write a program that will ask the user to enter the amount of a purchase. 
The program should then compute the state and county sales tax. 
Assume the state sales tax is 5 percent and the county sales tax is 2.5 percent. 
The program should display the amount of the purchase, the state sales tax, the county sales tax, the total sales tax, 
and the total of the sale (which is the sum of the amount of purchase plus the total sales tax).
"""

def assignmentName() -> str:
    return "Chapter 2: Sales Tax"

def main():
    while True:
        try:
            purchaseSubTotal = float(input("Purchase Amount: $"))
        except ValueError:
            print("Enter a number!")
            continue
        break
    stateTax = 0.05
    countyTax = 0.025
    totalTax = stateTax + countyTax

    totalWithTax = round(purchaseSubTotal * (1 + totalTax), 2)
    stateTaxAmount = round(purchaseSubTotal * stateTax, 2)
    countyTaxAmount = round(purchaseSubTotal * countyTax, 2)
    totalTaxAmount = round(purchaseSubTotal * totalTax, 2)

    print(f"State Tax: {stateTaxAmount}")
    print(f"County Tax: {countyTaxAmount}")
    print(f"Total Tax: {totalTaxAmount}")
    print(f"Purchase Total: {totalWithTax}")

    input("Enter to return to menu...")

if __name__ == "__main__":
    assignmentName() #just to give a warning when I copy paste this to other assignments
    main()