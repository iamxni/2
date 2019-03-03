import math

a=float(input('Введите A: '))
b=float(input('Введите B: '))
c=float(input('Введите C: '))

#Ax²+Bx+C=0

if a==0 and b!=0:
    x=(-c)/b
    print(x)
    
elif a!=0 and b==0:
    if c>0:
      print('Корней нет')
    else:
      x1=math.sqrt(-c/a)
      x2=-x1
    print('(%f; %f)'%(x1,x2))
    
elif a==0 and b==0:
    print('Корней нет')
    
elif a!=0 and b!=0:
    dis=(b**2)-(4*a*c)
    
    if dis==0:
      x=(-b)/(2*a)
      print(x)
      
    elif dis>0:
      d=math.sqrt(dis)
      x1=(-b+d)/(2*a)
      x2=(-b-d)/(2*a)
      print('(%f; %f)'%(x1,x2))

    else:
      print('Корней нет')
