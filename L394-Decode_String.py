# L394-Decode_String

def decodeString(s: str):
    decoded, current_num, current_str = [], [], []
    pointer = 0

    while pointer < len(s):
        if s[pointer].isnumeric():
            while s[pointer].isnumeric():
                current_num.append(s[pointer])
                pointer += 1
            decoded.append(''.join(current_str))
            decoded.append(int(''.join(current_num)))
            current_num, current_str = [], []
            pointer += 1
        elif s[pointer].isalpha():
            current_str.append(s[pointer])
            pointer += 1
        elif s[pointer] == ']':
            multiplier = decoded.pop()
            current_str = [multiplier * ''.join(current_str)]
            pointer += 1
    return ''.join(decoded)
    
decodeString("3[ac2[m]]2[b]")
