# Exercise 1:
def calculate_factorial(n):
  if n < 0:
    return "Factorial is undefined for negative numbers."
  elif n == 0 or n == 1:
    return 1
  else:
    factorial = 1
    for i in range(2, n + 1):
      factorial *= i
    return factorial


num = int(input("Enter a non-negative integer: "))
result = calculate_factorial(num)
print("Factorial of", num, "is:", result)


# Exercise 2:
def find_divisors(n):
  divisors = []
  for i in range(1, n + 1):
    if n % i == 0:
      divisors.append(i)
  return divisors


num = int(input("Enter a positive integer: "))
result = find_divisors(num)
print("Divisors of", num, "are:", result)


#Exercise 3:
def reverseString(input_string):
  reversed_string = ""
  for i in range(len(input_string) - 1, -1, -1):
    reversed_string += input_string[i]
  return reversed_string


user_input = input("Enter a string: ")
result = reverseString(user_input)
print("Reversed string:", result)


#Exercise 4:
def get_even_numbers(input_list):
  even_numbers = []
  for num in input_list:
    if num % 2 == 0:
      even_numbers.append(num)
  return even_numbers


user_input = input("Enter a list of integers: ")
input_list = [int(num) for num in user_input.split(",")]
result = get_even_numbers(input_list)
print("Even numbers:", result)


#Exercise 5:
def check_password_strength(password):
  # Check length
  if len(password) < 8:
    return "Weak password"

  # Check uppercase, lowercase, digit, and special character
  has_uppercase = False
  has_lowercase = False
  has_digit = False
  has_special_character = False
  special_characters = "#?!$"

  for char in password:
    if char.isupper():
      has_uppercase = True
    elif char.islower():
      has_lowercase = True
    elif char.isdigit():
      has_digit = True
    elif char in special_characters:
      has_special_character = True

  if has_uppercase and has_lowercase and has_digit and has_special_character:
    return "Strong password"
  else:
    return "Weak password"


user_input = input("Enter a password: ")
result = check_password_strength(user_input)
print("Password strength:", result)


#Exercise 6:
def check_ipv4_address(ip_address):
  octets = ip_address.split(".")

  # Check if the address has exactly four octets
  if len(octets) != 4:
    return "Invalid IPv4 address"

  for octet in octets:
    # Check if each octet is a valid integer
    if not octet.isdigit():
      return "Invalid IPv4 address"

    # Check if each octet is between 0 and 255
    octet_value = int(octet)
    if octet_value < 0 or octet_value > 255:
      return "Invalid IPv4 address"

    # Check for leading zeros in each octet
    if len(octet) > 1 and octet[0] == '0':
      return "Invalid IPv4 address"

  return "Valid IPv4 address"


user_input = input("Enter an IPv4 address: ")
result = check_ipv4_address(user_input)
print("IPv4 address validity:", result)


