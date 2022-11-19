import matplotlib.pyplot as plt
# Tạo dữ liệu
riding = ((17, 18, 19, 20, 21, 22, 23, 24), (18, 19, 20, 21, 22, 23, 24, 25))
swimming = ((19, 20, 21, 22, 23, 24, 25, 26), (19, 20, 21, 22, 23, 24, 25, 26))
sailing = ((12, 14, 10, 25, 21, 20, 19, 18), (13, 25, 24, 26, 29, 28, 24, 23))
# Canh chỉnh toạ độ
plt.plot(riding[0], riding[1], 'ro', label='riding')
plt.plot(swimming[0], swimming[1], 'g^', label='swimming')
plt.plot(sailing[0], sailing[1], 'b*', label='sailing')
# Cấu tạo lại đồ thị
plt.xlabel('Age')
plt.ylabel('Hours')
plt.title('Activities Scatter Graph')
plt.legend()
# Hiển thị lên đồ thị
plt.show()