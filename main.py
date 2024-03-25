'''def f(x, y, z, w):
    s1 = y <= z
    s2 = y or w
    s3 = z and x
    return int(s1 and (not (s2 <= s3)))


print("x y z w | f(x, y, z, w)")
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                if(f(x, y, z, w) == 1):
                    print(x, y, z, w, "|", f(x, y, z, w))
'''

'''def f(N):
    R = bin(N)[2:]
    if N % 4 == 0:
        R += R[len(R)-2:]
    else:
        ost = N % 4
        #ost *= 2
        ost = ost * 2
        R = bin(ost)[2:] + R
    return R

N = 12
R = f(N)
R_10 = int(R, 2)

#print(str(R) + " " + str(R_10))

max_N = 4
for N in range(4, 100):
    R = f(N)
    R_10 = int(R, 2)

    print(str(N) + ": " + str(R) + " " + str(R_10))
    if R_10 < 68:
        print(N)
        max_N = N

print(max_N)'''

# 1010  10  100
#  1100  00 -> 110000
#  1010  100  -> 100 + 1010 -> 1001010


def bit_ch(R):
    count = R.count('1')
    if count % 2 == 1:
        return '1'
    else:
        return '0'


def f(N):
    R = bin(N)[2:]
    R += R[len(R)-1:]
    R += bit_ch(R)
    R += bit_ch(R)

    return R


for N in range(4, 100):
    R = f(N)
    R_10 = int(R, 2)
    #print(str(N) + " "+ bin(N)[2:] + ": " + str(R) + " " + str(R_10))
    if R_10 > 144:
        print(R_10)
        break


R = bit_ch(R) + R + '00'
R = R + '11'