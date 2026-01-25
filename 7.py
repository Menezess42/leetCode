

def reverse(x: int) -> int:
    x_str = str(x)
    print(f"x:{x}\nx_str:{x_str}")
    sign = ''
    if x_str[0] == '-':
        sign = x_str[0]
    print(f"sign:{sign}")
    x_str = x_str.replace('-','')
    x_str = x_str[::-1]
    x_str = sign+x_str
    x = int(x_str)
    if x not in range(-2**32,2**32):
        return 0
    return x


x = reverse(123)
print(x)
x = reverse(-123)
print(x)
x = reverse(120)
print(x)
