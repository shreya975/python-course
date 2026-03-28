# string formatting

template = "Dear {}, you are awesome. Take this {}$ bag"

a = "John"
a1 = 10000

b = "jack"
b1 = 1000

c = "Marrie"
c1 = 100

s1 = template.format(a,a1)
print(s1)

# s2 = template.format(b,b1)
# print(s2)

# s3 = template.format(c,c1)
# print(s3)

print(f"you are awesome {a}, take this {a1}$ bag")

print(f"you are awesome {b}, take this {b1}$ bag")

print(f"you are awesome {c}, take this {c1}$ bag")