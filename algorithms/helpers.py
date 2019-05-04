def byte_arr(string):
    return [format(ord(char), 'b').rjust(7, '0') for char in string]

def bin_to_hex(blist):
    return hex(int(''.join(blist), 2)).replace('0x', '', 1).upper()

def hex_to_bin(string):
    return format(int(string, 16), 'b')

def flatten(list_of_list):
    return [v for l1 in list_of_list for v in l1]


def split_n(n, string):
    return [(string[i:i+n]) for i in range(0, len(string), n)]
