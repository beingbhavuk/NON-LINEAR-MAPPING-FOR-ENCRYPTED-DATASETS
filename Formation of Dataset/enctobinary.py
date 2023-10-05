def text_to_binary_from_file(file_path):
    binary_string = ""
    with open(file_path, 'r', encoding='latin-1') as file:
        for line in file:
            for char in line:
                ascii_value = ord(char)
                binary_value = bin(ascii_value)[2:]
                padded_value = binary_value.zfill(8)
                binary_string += padded_value
    
    return binary_string

# Example usage
file_path = 'new.txt.enc'
binary = text_to_binary_from_file(file_path)
print(binary)
with open("binary.txt","w")as file:
    file.write(binary) 