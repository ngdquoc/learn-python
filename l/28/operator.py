#assignment  arithmetic comparison 
a=1000
b=a # b=1000

a,b,c=1,2,3
print(a,b,c) #1 2 3

x,y=10,'twenty'
print(x,y) # 10 twenty

#hoan vi
a,b=b,a
print(a,b) # twenty 10
"""
  + - * / 
  //(chia  nguyên)
  %(lấy dư ) 
  **(lũy thừa) 
"""

print("This is my theory:",10!=20) 

#logical operator 
''' AND OR NOT'''
print("Logical AND:", 5 > 3 and 10 < 20)
print("Logical OR:", 5 > 3 or 10 > 20)
print("Logical NOT:", not (5 > 3))  

# bitwise operator identity operator 
'''
==, !=, >, <, >=, <=
'''
# membership operator    
name='nguyen quoc swe'
print('quoc' in name) #True
print('quoc' not in name) #False

ar1=[1,2,3]
ar2=ar1
print(ar1 is ar2) #True
ar2=[1,2,3]
print(ar1 is ar2) #False