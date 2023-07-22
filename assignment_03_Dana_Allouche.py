import json

def sum_tuples(tup1, tup2):
    return tuple(x + y for x, y in zip(tup1, tup2))

def export_to_json(data_dict, filename):
    with open(filename, 'w') as json_file:
        json.dump(data_dict, json_file, indent=4)

def import_from_json(filename):
    with open(filename, 'r') as json_file:
        data_list = json.load(json_file)
    return data_list

def display_menu():
    print("1. Sum Tuples")
    print("2. Export JSON")
    print("3. Import JSON")
    print("4. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter a choice: ")

        if choice == "1":
            tup1 = tuple(map(int, input("Enter elements of tuple 1 separated by spaces: ").split()))
            tup2 = tuple(map(int, input("Enter elements of tuple 2 separated by spaces: ").split()))

            if len(tup1) != len(tup2):
                print("Tuples must have same length.")
            else:
                result = sum_tuples(tup1, tup2)
                print("Result:", result)

        elif choice == "2":
            data_dict = {}
            num_entries = int(input("Enter the number of entries: "))
            for i in range(num_entries):
                key = input(f"Enter key for entry {i + 1}: ")
                value = input(f"Enter value for entry {i + 1}: ")
                data_dict[key] = value
            
            filename = input("Enter the filename for the JSON file: ")
            export_to_json(data_dict, filename)
            print("Data exported to JSON successfully.")

        elif choice == "3":
            filename = input("Enter the filename of the JSON file : ")
            data_list = import_from_json(filename)
            print("Data imported successfully.")
            print("List of dictionaries:", data_list)

        elif choice == "4":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

# Big O Notation:

# a. 1/6N + 8000N^3 + 24
# Big-O Notation: O(N^3)

# b. 1/6N^3
# Big-O Notation: O(N^3)

# c. 1/6N! + 200N^4
# Big-O Notation: O(N^4)

# d. NlogN + 1000
# Big-O Notation: O(NlogN)

# e. logN + N
# Big-O Notation: O(N)

# f. 1/2N(N-1)
# Big-O Notation: O(N^2)

# g. N^2 + 220NlogN + 3N + 9000
# Big-O Notation: O(N^2)

# h. N! + 3N + 2N + N^3 + N^2
# Big-O Notation: O(N!)
