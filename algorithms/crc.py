from .helpers import byte_arr


def encode(string_b_arr):
    pass


def decode(string_b_arr):
    pass


def crc(args):
    if args.decode != None:
        return decode(byte_arr(args.decode[0]))
    if args.encode != None:
        return encode(byte_arr(args.encode[0]))
