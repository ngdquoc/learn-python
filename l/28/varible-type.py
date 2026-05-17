""" 
dynamic typing in python

"""
#type()

ageMax=100
print('type of ageMax:',type(ageMax) ) 
a=1
A=2
print(a,A,   '\n'   ) #1 2

#nguyen | so thuc dau phay động | số phức
a=2
b=2.0
c=1+2j
print(type(a), type(b), type(c) ) 
#<class 'int'> <class 'float'> <class 'complex'>

# bloolan
isTrue=True
isFalse=False
print(type(isTrue), type(isFalse) )
#<class 'bool'> <class 'bool'>

# bool(1) #True
# bool(0) #False
# bool(-1) #True
# bool('') #False
# bool(' ') #True
# bool('False') #True
# bool([]) #False
# bool([1,2,3]) #True
console = 'python'
print('xbox : ',bool(console) )

# only has string and no character type in python
name='nguyen quoc swe'
paraphrase=""" đừng buồn đầu sầu lệ tràn trên
khoé mi
đừng buồn làm chi khi người ta đã bỏ đi
"""
print("buon" in paraphrase) #True

print(name,'\n' )
print(paraphrase )