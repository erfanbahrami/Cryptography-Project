from tinyec import registry, ec
from sympy.ntheory.residue_ntheory import nthroot_mod
import os

##################################### question 1 part 1 ##################################### 
  ####################################################################################### 
print("##################################### question 1 part 1 #####################################")
curve = registry.get_curve('secp192r1')
a = curve.a
b = curve.b
print("decimal values:")
print("a: ", a)
print("b: ", b)

print("hex values:")
a = hex(curve.a)
b = hex(curve.b)
print("a: ", a)
print("b: ", b)

##################################### question 1 part 2 ##################################### 
  ####################################################################################### 
print("\n\n##################################### question 1 part 2 #####################################")
curve = registry.get_curve('secp192r1')

f = lambda x: nthroot_mod(x**3+curve.a*x+curve.b, 2, curve.field.p)

x = 401204921 
y = f(x)
assert y is not None

G = ec.Point(curve, x, y)
assert G.on_curve
print(G.on_curve)
print(G)

##################################### question 1 part 3 ##################################### 
  ####################################################################################### 
print("\n\n##################################### question 1 part 3 #####################################")

s=401204921
# Find 2G
R1 = G + G
print(R1.on_curve)
print(R1)

# Find s.G
R2 = s * G
print(R2.on_curve)
print(R2)
sG = R2

##################################### question 1 part 4 ##################################### 
  ####################################################################################### 
print("\n\n##################################### question 1 part 4 #####################################")
n = 0xffffffffffffffffffffffff99def836146bc9b1b4d22831
while True:
    k = os.urandom(24)
    k = int.from_bytes(k , 'big')
    r = os.urandom(24)
    r = int.from_bytes(r , 'big')
    if k>=1 and k<n and r>=1 and r<n:
        break

#encryption
kG = k * G 
C = r * G
C_prime = r * kG
cipher = (C , C_prime+sG)
D = C_prime+sG
print("cipher:\n" , cipher)


##################################### question 1 part 5 ##################################### 
  ####################################################################################### 
print("\n\n##################################### question 1 part 5 #####################################")

C_prime = k * C
plain = D - C_prime
print("plain:\n",plain)
