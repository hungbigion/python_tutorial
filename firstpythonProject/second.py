s = "Đại học Kinh Bắc"
# n = int(input("Nhập n: "))
# for i in range(1,n+1,1):
#     print(i, end=" ")
# for
# for i in s:
#     print(i, end="")
# i=0
# while i < len(s):
#     print(s[i], end="")
#     i +=1
# n = int(input("Nhập n: "))
# print(" số chẵn từ 0 -> ",n)
# for i in range(0,n+1,2):
#     print(i, end=" ")
# print()
# print(" số lẻ từ 0 -> ",n)
# for i in range(1,n+1,2):
#     print(i, end=" ")
# n = int(input("Nhập số lượng pt của mảng: "))
# a = []
# g = []
# h = []
# for i in range(1,n+1,1):
#     a.append(int(input("Nhập phần tử %d:" %i)))
# print("mảng a = ",a)
# print()
# for i in a:
#     if i%2 == 0:
#         print(i, end=" ")
#         g.append(i)
# print()
# print("Mảng chẵn được tạo từ a :",g)
# for i in a:
#     if i%2 != 0:
#         print(i, end=" ")
#         h.append(i)
# print()
# print("Mảng lẻ được tạo từ a :",h)

# sum=0
# sumc=0
# suml=0
# sumf=0
# for i in range(1,n+1,1):
#     print(i, end=" ")
#     sum=sum+i
#     if i%2==0:
#         sumc=sumc+i
#     else:
#         suml=suml+i
#     if i%10==0 :
#         sumf=sumf+i
# print("tổng các số từ 1 -> ",n," = ",sum)
# print("tổng các số chẵn số từ 1 -> ",n," = ",sumc)
# print("tổng các số lẻ số từ 1 -> ",n," = ",suml)
# print("tổng các số chẵn chia hết cho 5 số từ 1 -> ",n," = ",sumf)

# p =1
# s=0
# s1=0
# s2=0
# sle=0
# schan=0
# for i in range(1,n+1):
#     if i % 2 == 0:
#         schan = schan+i
#     else:
#         sle = sle+i
#     p=p*i
#     s=s+p
#
#     s2=s2+i
#     s1= s1 + 1/(s2)
# print(" giá trị đa thức 1 = ",(sle-schan))
# print(" giá trị đa thức 2 = ",s)
# print(" giá trị đa thức 3 = ",s1)
n = int(input("nhập n:"))
i =1
for i in range(1,n+1):
    print("*" * i)
