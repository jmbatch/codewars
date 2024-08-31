def binary_to_string(binary):
    if not binary:
        return str(binary)
    else:
        binary = int(binary, 2)
        total_bytes = (binary.bit_length() + 7) // 8
        input_array = binary.to_bytes(total_bytes, "big")
        ascii_value = input_array.decode()
        return ascii_value
