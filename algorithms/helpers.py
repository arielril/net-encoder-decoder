def byte_arr(string):
    return [format(ord(char), 'b').rjust(7, '0') for char in string]

def bin_to_hex(list):
    return hex(int(''.join(list), 2)).replace('0x', '', 1).upper()

def hex_to_bin(list):
    pass

def flatten(list_of_list):
    return [v for l1 in list_of_list for v in l1]
