import os , math

######################## compute private key
def gcdExtended(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = gcdExtended(b % a, a)
        return (g, x - (b // a) * y, y)
 
def modInverse(a, m):
    g, x, y = gcdExtended(a, m)
    if g != 1:
        raise Exception("Inverse doesn't exist")
    else:
        return x % m

for i in range(1, 4):
    file = open(os.getcwd() + '\\Desktop\\ErfanBahrami_401204921_project\\sig' + str(i) + '.txt', 'r')
    lines = file.readlines()
    for count, line in enumerate(lines):
        lines[count] = line.strip()

    n = int(lines[0][2:])  
    e = int(lines[1][2:])  
    m = int(lines[2][2:])  
    sig = int(lines[3][4:])  
    message = pow(sig, e, n)

    if m != message:
        print("\nThe sig(" + str(i) + ") signature has error\n")
        # raveshe tozih dade shode dar maghale
        q = math.gcd(n, pow((pow(sig, e, n) - m),1,n))
        p = n // q
        phi = (p-1)*(q-1)
        # d is private key
        d = modInverse(e, phi)



######################## check the private key
file = open(os.getcwd() + '\\Desktop\\ErfanBahrami_401204921_project\\sig1.txt', 'r')
lines = file.readlines()
for count, line in enumerate(lines):
    lines[count] = line.strip()

n = int(lines[0][2:])  
e = int(lines[1][2:])  
m = int(lines[2][2:])  
sig = int(lines[3][4:])
s = pow(m, d, n)

if s == sig:
    print("The private key(d) is calculated correctly\n")
    print("d=",d)
