def xor(a, b):
    """Perform XOR operation."""
    result = []
    for i in range(1, len(b)):
        result.append(str(int(a[i]) ^ int(b[i])))
    return ''.join(result)

def crc_calculate(message, generator):
    """Calculate CRC checksum."""
    # Convert message to binary (ASCII)
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    
    # Append zeros to the binary message (degree of generator - 1)
    appended_message = binary_message + '0' * (len(generator) - 1)
    
    # Perform binary division (modulo-2)
    dividend = appended_message[:len(generator)]
    for i in range(len(generator), len(appended_message) + 1):
        if dividend[0] == '1':
            # XOR with the generator
            dividend = xor(dividend, generator) + (appended_message[i] if i < len(appended_message) else '')
        else:
            # Shift the next bit
            dividend = dividend[1:] + (appended_message[i] if i < len(appended_message) else '')

    # The remainder is the CRC checksum
    checksum = dividend
    return checksum

def crc_append(message, generator):
    """Append CRC to the message."""
    checksum = crc_calculate(message, generator)
    # Append the checksum to the original message
    return message + '|' + checksum

# Example usage
message = "Algalon is dead"
generator = "1101"  # Example generator polynomial
crc_message = crc_append(message, generator)
print("Message with CRC:", crc_message)
