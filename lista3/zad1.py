from warnings import warn
import filecmp

FLAG = "01111110"
GEN = "1001"


def minus_gen(x: str):
    res = ""
    for i in range(1, len(GEN)):
        if x[i] == GEN[i]:
            res += "0"
        else:
            res += "1"
    return res


def div_rem(data: str):
    next = len(GEN)
    rem = data[:next]
    while next <= len(data):
        if rem[0] == "1":
            rem = minus_gen(rem)
        else:
            rem = rem[1:]
        if next == len(data):
            break
        rem += data[next]
        next += 1
    return rem


def crc(data: str):
    data += "0" * (len(GEN) - 1)
    return div_rem(data)


def encode(data: str, max_datasize=32):
    frames = []
    i = 0
    ones = 0

    while i < len(data):
        cur = data[i : i + max_datasize]
        cur += crc(cur)
        cur_frame = ""
        ones = 0
        for c in cur:
            if ones == 5:
                ones = 0
                cur_frame += '0'
            if c == '1':
                ones += 1
            else:
                ones = 0
            cur_frame += c

        frames.append(FLAG + cur_frame + FLAG)
        i += max_datasize

    return "".join(frames)


def decode(data: str):
    frames = list(filter(None, data.split(FLAG)))
    decoded = []
    for frame in frames:
        current = ""
        i = 0
        ones = 0
        while i < len(frame):
            current += frame[i]
            if frame[i] == "1":
                ones += 1
                if ones == 5:
                    ones = 0
                    i += 1
            else:
                ones = 0
            i += 1

        if div_rem(current) != '0'*(len(GEN)-1):
            warn("Frame containing {} omitted.".format(frame))
        else:
            current = current[:-(len(GEN)-1)]
            decoded.append(current)

    return "".join(decoded)


def create_frames(source: str, target: str):
    try:
        with open(source) as src:
            lines = src.read().splitlines()
    except FileNotFoundError:
        print("Source file not found.")
        return

    coded_lines = [encode(line) + '\n' for line in lines]
    with open(target, 'w') as tgt:
        tgt.writelines(coded_lines)

def decode_frames(source: str, target: str):
    try:
        with open(source) as src:
            lines = src.read().splitlines()
    except FileNotFoundError:
        print("Source file not found.")
        return

    coded_lines = [decode(line) + '\n' for line in lines]
    with open(target, 'w') as tgt:
        tgt.writelines(coded_lines)

def test_decoding():
    create_frames("Z.txt", "W.txt")
    decode_frames("W.txt", "Z1.txt")
    with open("Z.txt") as f1, open("Z1.txt") as f2:
        for l1, l2 in zip(f1, f2):
            if l1 != l2:
                break
        else:
            print("Success!")
