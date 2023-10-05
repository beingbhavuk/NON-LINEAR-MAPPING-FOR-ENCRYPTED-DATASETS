def generate_all_binary_sets(num_digits):
    binary_sets = {}
    for i in range(1 << num_digits):
        binary_set = format(i, f'0{num_digits}b')
        binary_sets[binary_set] = 0
    return binary_sets

def count_duplicate_strings(input_string, substring_length, mp):
    substring_map = {}
    for i in range(0, len(input_string), substring_length):
        substring = input_string[i:i+substring_length]
        mp[substring] += 1

    with open("output.txt", "a") as output_file: 
        for key, value in mp.items():
            output_file.write(f"{value} ")
            mp[key] = 0
        output_file.write("\n")
        print("Output successfully stored in the file.")

def main():
    mp = {}
    num_digits = 8
    mp = generate_all_binary_sets(num_digits)

    with open("binary.txt", "r") as file:
        str_content = file.read()

    substring_length = 8
    size = len(str_content) // 1280

    for i in range(size):
        str1 = str_content[i * 1280: (i+1) * 1280]
        count_duplicate_strings(str1, substring_length, mp)
        for key in mp:
            mp[key] = 0

if __name__ == "__main__":
    main()
