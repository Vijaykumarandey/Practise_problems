'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
def parse_encoded_string(encoded):
    parts = encoded.split('0')  # Split on all zeros
    clean_parts = [part for part in parts if part]  # Remove empty strings
    return {
        "first_name": clean_parts[0],
        "last_name": clean_parts[1],
        "id": clean_parts[2]
    }

input = "Robert000Smith000123"
print(parse_encoded_string(input))

