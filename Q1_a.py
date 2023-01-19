from tinyec import registry

curve = registry.get_curve('secp192r1')

# Extract the 'a' and 'b' parameters from the curve object
a = curve.a
b = curve.b
print("---------------------------------decimal values-----------------------------------")
print("a: ", a)
print("b: ", b)

print("-----------------------------------hex values-------------------------------------")
a = hex(curve.a)
b = hex(curve.b)
print("a: ", a)
print("b: ", b)

