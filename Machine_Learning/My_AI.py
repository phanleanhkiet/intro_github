# import ramdon 
# print ramdon.randint(1,10)


# from thanginramua import mua
# mua=(0)

# import math
# print(math.pi)

x=int(input('hay nhap so:'))
def bacgiaithua(x):
    if x==0:
        return 1
    return x*bacgiaithua(x-1)
print(bacgiaithua(x))




