from .helpers import byte_arr, bin_to_hex, flatten, hex_to_bin, split_n

def set_parity(bit_list):
    count = bit_list.count('1')
    if count % 2 == 0:
        bit_list.append('0')
    else:
        bit_list.append('1')

def encode(byte_list):
    char_list = [list(c) for c in byte_list]
    
    for c in char_list:
        set_parity(c)

    bcc = []
    for i in range(len(char_list[0])):
        bits = []
        for j in range(len(char_list)):
            bits.append(char_list[j][i])
        set_parity(bits)
        bcc.append(bits[-1])
   
    char_list.extend(bcc)
    bit_list = flatten(char_list)
    
    return bin_to_hex(bit_list)

def check_hex(bit_list, bcc):
    for i in range(len(bit_list[0])):
        count = 0
        for j in range(len(bit_list)):
            if bit_list[j][i] == '1':
                count += 1
        if count % 2 == 0 and bcc[i] != '0':
            return 'ERROR'


def decode(hex_string):
    bit = hex_to_bin(hex_string)
    # quebra uma lista em pedacos de tamanho n
    bit_list = split_n(8, bit)
    
    bcc = list(bit_list[-1])
    bit_list_char = [list(c) for c in bit_list]

    check = check_hex(bit_list_char[:-1], bcc)
    if check == 'ERROR': return check

    string = []
    for i in range(len(bit_list)-1):
        string.append(chr(int(bit_list[i][:-1], 2)))

    return ''.join(string)

def redudancy(args):
    if args.decode != None:
        return decode(args.decode[0])
    if args.encode != None:
        return encode(byte_arr(args.encode[0]))
