from .helpers import byte_arr, bin_to_hex, flatten

def set_parity(bit_list):
    count = bit_list.count('1')
    if count % 2 == 0:
        bit_list.append('0')
    else:
        bit_list.append('1')

def encode(char_list):
    char_list = [list(c) for c in char_list]
    
    for c in char_list:
        set_parity(c)

    bcc = []
    for i in range(len(char_list[0])):
        listss = []
        for j in range(len(char_list)):
            listss.append(char_list[j][i])
        set_parity(listss)
        bcc.append(listss[-1])
   
    char_list.extend(bcc)
    bit_list = flatten(char_list)
    
    return bin_to_hex(bit_list)


def decode(string_b_arr):
    return string_b_arr

def redudancy(args):
    if args.decode != None:
        return decode(byte_arr(args.decode[0]))
    if args.encode != None:
        return encode(byte_arr(args.encode[0]))
