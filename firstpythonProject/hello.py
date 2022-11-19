import math
a = int(input('Nhập a: '))
b = int(input('Nhập b: '))
c= int(input('Nhập c: '))
denta = b * b - 4 * a * c
# if(a==0):
#     if(b!=0):
#         print("PT: ",a,"x + ",b,' Vô nghiệm')
#     else:
#         print("PT: ", a, "x + ", b, ' Vô số nghiệm')
# elif (a!=0):
#     print("PT: ", a, "x + ", b, ' có nghiệm là ', (-b/a))
if(a==0):
    if(b==0):
        if(c!=0):
            print("PT: ",b,"x + ",c,' Vô nghiệm')
        else:
            print("PT: ", b, "x + ", c, ' Vô số nghiệm')
    elif (b!=0):
        print("PT: ", b, "x + ", c, ' có nghiệm là ', (-b/c))
else:
     if denta>0:
            print("PT có 2 nghiệm")
            print(" X1 = ", ((-b + math.sqrt(denta))/(2*a)))
            print(" X2 = ", ((-b - math.sqrt(denta)) / (2*a)))
     elif denta == 0:
        print("PT có 2 nghiệm kép X1 = X2 =",(-b/(2*a)))
     else:
        print("Phương trình vô nghiệm")
