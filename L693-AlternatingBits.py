#  693 Binary Number with Alternating Bits

def alternating_bits(num):
    binary = []
    while num > 0:
        if num % 2 == 0:
            binary.append(0)
        else:
            binary.append(1)
        num //= 2
    idx = 0 
    for idx, bit in enumerate(binary[:-1]):
        if bit == binary[idx+1]:
            return False
    return True

print(alternating_bits(11))


