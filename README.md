# net-encoder-decoder
Encoder/Decoder for network communication - block Redundancy/CRC/Hamming Code

## Exemplos de uso
```
usage: index.py [-h] [-a algorithm] [-e ascii_string] [-d ascii_string]
                [-k key_polinom]

Encoder/Decoder for network communication - Block Redundancy/CRC/Hamming Code

optional arguments:
  -h, --help            show this help message and exit
  -a algorithm, --algorithm algorithm
                        Name of the algorithm to be used. Must be "redudancy",
                        "crc" or "hamming"
  -e ascii_string, --encode ascii_string
                        Encodes an ASCII string and returns the hexadecimal
                        code
  -d ascii_string, --decode ascii_string
                        Decodes an hexadecimal code and returns the ASCII
                        string
  -k key_polinom, --key key_polinom
                        Generator polinom
```

### Redundância de bloco (BCC)
A implementação deste algoritmo utiliza um bit de paridade no final de cada caractere (paridade horizontal) e no final da computação é adicionado um BCC (_Block Check Character_).

```bash
$ ./index.py -a redudancy -e redes
E4CAC9CAE7CA
```

```bash
$ ./index.py -a redudancy -d E4CAC9CAE7CA
redes
```

```bash
$ ./index.py -a redudancy -d E4CAC9CAE7CB
ERRO
```

### CRC
```bash
$ ./index.py -a crc -e redes -k 10101
72365964C659736
```

```bash
$ ./index.py -a crc -d 72365964C659736 -k 10101
redes
```

```bash
$ ./index.py -a crc -d 72365A64C659737 -k 10101
r_de_
ERRO nos caracteres: 2, 5
```

```bash
$ ./index.py -a crc -e pucrs -k 10011
70875763872E73D
```

```bash
$ ./index.py -a crc -d 70875763872E73D -k 10011
pucrs
```

```bash
$ ./index.py -a crc -d 70875663872E73D -k 10011
p_crs
ERRO nos caracteres: 2
```

### Código de Hamming
```bash
$ ./index.py -a hamming -e redes
79962C62B62C79E
```

```bash
$ ./index.py -a hamming -d 79962C62B62C79E
redes
```

```bash
$ ./index.py -a hamming -d 79961C62B62C69E
rbdes
ERRO no caractere 2 -> Correção: b
ERRO no caractere 5 -> Correção: s
```

