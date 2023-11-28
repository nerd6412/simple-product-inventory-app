import os

def save_product_record(file, productCode, productName, quantity):
    with open(file, "a") as f:
        f.write(f"{productCode},{productName},{quantity}\n")


def searchProduct(file, productCode):
    with open(file, 'r') as f:
        for line in f:
            record = line.strip().split(',')
            if record[0] == productCode:
                return record
    return None


def deleteProduct(file, productCode):
    lines = []
    deleted = False
    with open(file, "r") as f:
        for line in f:
            record = line.strip().split(',')
            if record[0] != productCode:
                lines.append(line)
            else:
                deleted = True

    if deleted:
        with open(file, 'w') as f:
            f.writelines(lines)
        print("The record is deleted.")
    else:
        print("Record not found.")


def editProduct(file, productCode):
    record = searchProduct(file, productCode)
    if record:
        print("Current List:")
        print(f"PRODUCT CODE: {record[0]}")
        print(f"PRODUCT NAME: {record[1]}")
        print(f"QUANTITY: {record[2]}")

        productName = input("Enter the PRODUCT NAME: ")
        quantity = input("Enter the QUANTITY: ")

        with open(file, 'r') as f:
            lines = f.readlines()

        with open(file, 'w') as f:
            for line in lines:
                rec = line.strip().split(',')
                if rec[0] == productCode:
                    f.write(f"{rec[0]},{productName},{quantity}\n")
                else:
                    f.write(line)

        print("The record was updated.")
    else:
        print("Record not found.")


def transactProduct(file, productCode):
    record = searchProduct(file, productCode)
    if record:
        print("Current List:")
        print(f"PRODUCT CODE: {record[0]}")
        print(f"PRODUCT NAME: {record[1]}")
        print(f"QUANTITY: {record[2]}")

        transactionCode = input("Enter the TRANSACTION CODE (P = Purchase, S = Sold): ")
        quantity = int(input("Enter the QUANTITY: "))

        if transactionCode == 'P':
            newQuantity = int(record[2]) + quantity
        elif transactionCode == 'S':
            if quantity > int(record[2]):
                print("Failed! Please try again.")
                return
            newQuantity = int(record[2]) - quantity
        else:
            print("Invalid transaction code!")
            return

        with open(file, 'r') as f:
            lines = f.readlines()

        with open(file, 'w') as f:
            for line in lines:
                rec = line.strip().split(',')
                if rec[0] == productCode:
                    f.write(f"{rec[0]},{rec[1]},{newQuantity}\n")
                else:
                    f.write(line)

        print("Successfully Transacted!")
    else:
        print("Record not found! Please try again.")


def displayFile(file):
    print("PRODUCT CODE\tPRODUCT NAME\tQUANTITY")
    with open(file, 'r') as f:
        lines = f.readlines()
        if len(lines) == 0:
            print("Record missing!")
        else:
            for line in lines:
                record = line.strip().split(',')
                print(f"{record[0]}\t\t{record[1]}\t\t{record[2]}")


def validateInput(prompt, choices):
    while True:
        userInput = input(prompt).strip().upper()
        if userInput in choices:
            return userInput
        print("\n\t\tInvalid input! Please try again.")


def main():
    file = "Products.txt"

    while True:
        print("PRODUCT LIST")
        print("Options:")
        print("A – ADD  D - DELETE  E – EDIT  T - TRANSACT  V - VIEW  X - EXIT")

        choice = validateInput("\nWHAT DO YOU WANT TO DO?\nPlease enter your choice: ", ['A', 'D', 'E', 'T', 'V', 'X'])

        if choice == "A":
            while True:
                productCode = input("\nPRODUCT CODE: ")
                productName = input("\nPRODUCT NAME: ")
                quantity = input("QUANTITY: ")

                save_product_record(file, productCode, productName, quantity)

                more = validateInput("\nEnter more? [Y/N]: ", ['Y', 'N'])

                if more == 'N':
                    break

        elif choice == 'D':
            productCode = input("\nPRODUCT CODE: ")
            record = searchProduct(file, productCode)
            if record:
                print("Record found: ")
                print(f"PRODUCT CODE: {record[0]}")
                print(f"PRODUCT NAME: {record[1]}")
                print(f"QUANTITY: {record[2]}")

                confirm = validateInput("\nDo you want to delete this record? [Y/N]: ", ['Y', 'N'])
                if confirm == 'Y':
                    deleteProduct(file, productCode)
            else:
                print("Record not found!")

        elif choice == 'E':
            productCode = input("PRODUCT CODE: ")
            editProduct(file, productCode)

        elif choice == 'T':
            productCode = input("PRODUCT CODE: ")
            transactProduct(file, productCode)

        elif choice == 'V':
            displayFile(file)

        elif choice == 'X':
            displayFile(file)
            print("\nEnd of program.")
            break


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("An error occurred:", str(e))