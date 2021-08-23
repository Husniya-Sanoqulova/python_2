print('Kvadrat tenglamani yechish: ')
a = float(input('a ning  qiymatini kiriting:  '))
b = float(input('b ning qiymatini kiriting:  '))
c = float(input('c ning qiymatini kiriting:  '))
d= b**2 - 4*a*c
print('Diskriminant= ' + str(d))
if d < 0:
   print('Ildizda manfiy son yuzaga keldi')
elif d == 0:
   x = -b / (2 * a)
   print('x = ' + str(x))
else:
   x1 = (-b+d ** 0.5)/(2 * a)
   x2 = (-b-d ** 0.5)/(2 * a)
   print('x₁ = ' + str(x1))
   print('x₂ = ' + str(x2))
