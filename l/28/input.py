'''
input(<prompt>)
always returns a string
-> if we want to get a number, we need to cast the string to a number
int( input('Enter a number: ') ) # 123

'''
name = input('What is your name? ') #tom
print('Hello, ' + name)

# Nhập 3 số trên cùng một dòng, cách nhau bằng dấu cách
a, b, c = map(int, input("Nhập 3 số line 12: ").split())

# Tính tổng
tong = a + b + c

# In kết quả
print("Tổng =", tong)

"""
nhap ba tren 1 line
input trả về sâu ký tự  s= in = 1 2 3 -> s= '1 2 3'
s.slit() -> ['1', '2', '3']
x,y.z=map(int, s) anh xa
n1, n2, n3 = input('Enter three numbers: ').split() #
"""
# s= input("Enter three numbers line 27: ") # 1 2 3
# g=s.split()
# a,b,c=map(int, g)
# print('SUM IS HERE',a+b+c)

s1= input("Enter three numbers 999 : ") 
print('s1 :',s1) # '100 200 300'
g1=s1.split()      # '100' '200 ' '300'
print('g1',g1) # '100' '200 ' '300'
a,b,c=g1
print('message',a,b,c)


"""
 CONCLUSION
 """
x,y,z,t=map(int, input('nhap tren cung mot dong').split() )
print(x,y,z,t)