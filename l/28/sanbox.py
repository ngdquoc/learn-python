# # sep end TESTING
# print('hellnah','botch',sep='--',end='\n')
# print('newline')
# """
# hellnah--botch
# newline
# """
# Nhập 3 số trên cùng một dòng, cách nhau bằng dấu cách

a = input("Nhập 3 số: ")
g=a.split()
a,b,c=map(int, g)
# Tính tổng
tong = a + b + c

# In kết quả
print("Tổng =", tong)