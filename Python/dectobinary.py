# Prompt the user to enter a decimal number
decimal_num = int(input("Enter a decimal number: "))
# Initialize an empty string to store the binary representation
binary_num = ""
# Convert the decimal number to binary manually
while decimal_num > 0:
    # Extract the least significant bit
    bit = decimal_num % 2
    # Prepend the bit to the binary representation
    binary_num = str(bit) + binary_num
    # Shift the decimal number to the right (integer division by 2)
    decimal_num //= 2
# Print the binary representation
print("Binary representation:", binary_num)
