from .helpers import byte_arr, split_n

import math

# calcula quantos numeros de redundancia seram adicionados
def numOfRedundantBits(m):
    form = lambda r: math.pow(2, r) >= m + r + 1
    rn = 0
    while not form(rn):
        rn += 1
    return rn
    

# cria tabela com os valores binario das posicoes com bit 1
def getTable(pos_list, width):
    return [list(format(int(pos), 'b').rjust(width, '0')) for pos in pos_list]


# calcula o XOR da tabela criada
def computeXOR(table):
    x = []
    for i in range(len(table[0])):
        c = 0
        for j in range(len(table)):
            if table[j][i] == '1':
                c += 1
        if c % 2 != 0:
            x.append('1')
        else:
            x.append('0')
    return x


# preenche as lacunas da mensagem com o resultado do XOR
def fillBlanks(xor, char_bits):
    for v in xor:
        idx = char_bits.index('_')
        char_bits[idx] = v


# busca as posicoes com bit em 1
def getPositions(char_bits):
    return [
        str(i + 1)
        for i, x in enumerate(char_bits)
        if x == '1'
    ]


def encode(char_list):
    res = []
    for char in char_list:
        num_redundant = numOfRedundantBits(len(char))
        char_bits = list(char)
        # inverte a lista de bit para facilitar a manipulacao
        char_bits.reverse()
        for i in range(0, num_redundant):
            pos = int(math.pow(2, i))
            # adiciona placeholders para os bits de redundancia
            char_bits.insert(pos - 1, '_')
        pos_red = getPositions(char_bits)
        tb = getTable(pos_red, num_redundant)
        char_bits.reverse()
        xor = computeXOR(tb)
        # preenche as lacunas com o resultado calculado pelo XOR
        fillBlanks(xor, char_bits)
        res.append(hex(int(''.join(char_bits), 2)).lstrip('0x').upper())
    return ''.join(res)


def decode(hex_string):
    char_list = [format(int(c, 16), 'b') for c in split_n(3, hex_string)]
    res = []
    err = []
    for idx, char in enumerate(char_list):
        char_bits = list(char)
        char_bits.reverse()
        pos_one = getPositions(char_bits)
        tb = getTable(pos_one, 4)
        xor = computeXOR(tb)

        # caso o bit tenha erro, inverte seu valor
        if '1' in xor:
            err.append(idx)
            pos = int(''.join(xor), 2) - 1
            char_bits[pos] = '0' if char_bits[pos] == '1' else '1'
        
        # remove os bits de redundancia
        for i in range(0, 4):
            pos = int(math.pow(2, i))
            char_bits[pos - 1] = '_'
        while '_' in char_bits:
            char_bits.pop(char_bits.index('_'))
        char_bits.reverse()
        # adiciona a letra gerada pela mensagem
        res.append(''.join(char_bits))

    res_str = ''.join([ chr(int(c, 2)) for c in res ])
    error_str = ''
    for i in err:
        error_str += 'ERRO no caractere {} -> Correção: {}\n'.format(i + 1, res_str[i])

    return res_str + '\n' + error_str





def hamming(args):
    if args.decode != None:
        return decode(args.decode[0])
    if args.encode != None:
        return encode(byte_arr(args.encode[0]))
        
