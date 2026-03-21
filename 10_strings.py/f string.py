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

s2 = template.format(b,b1)
print(s2)