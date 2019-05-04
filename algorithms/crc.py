from .helpers import byte_arr, flatten, bin_to_hex, split_n

def append_zeros(string, n):
    return string + ('0' * n)

def reminder(padded_input_arr, input_len, key):
    key_size = len(key)
    while '1' in padded_input_arr[:input_len]:
        curr = padded_input_arr.index('1')

        for i in range(key_size):
            char_bit = padded_input_arr[curr + i]
            key_bit = key[i]
            padded_input_arr[curr + i] = str(int(char_bit != key_bit))

def encode(char_list, key):
    key_size = len(key)
    res = []
    for char in char_list:
        padded_input = append_zeros(char, key_size - 1)
        padded_input_arr = list(padded_input)
        char_len = len(char)

        reminder(padded_input_arr, char_len, key)

        rem = ''.join(padded_input_arr)[char_len:]
        val = hex(int(char + rem, 2)).lstrip('0x').upper()
        res.append(val)
        
    return ''.join(res)


def decode(hex_val, key):
    key_size = len(key)
    
    char_list = split_n(3, hex_val)
    char_list = [
        bin(int(val[:2], 16))[2:] + bin(int(val[2:], 16))[2:].zfill(4) 
        for val in char_list
    ]

    res = []

    for char in char_list:
        padded_input_arr = list(char)
        char_len = len(char) - 4

        reminder(padded_input_arr, char_len, key)
        rem = ''.join(padded_input_arr)[char_len:]
        res.append(
            chr(int(char[:char_len], 2))
                if '1' not in rem
                else '_'
        )

    str_res = ''.join(res)

    if '_' in res:
        wrongs = [
            str(i + 1) 
            for i, x in enumerate(res) 
            if x == '_'
        ]
        str_res += '\nERRO nos caracteres: ' + ', '.join(wrongs)

    return str_res


def crc(args):
    if args.key != None:
        key = args.key[0].lstrip('0')
        if args.decode != None:
            return decode(args.decode[0], key)
        if args.encode != None:
            return encode(byte_arr(args.encode[0]), key)
