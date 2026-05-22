""" if bool_condition: 
           statement1

    elif bool_condition2:
           statement2       
        else:
             statement2
"""
if 1<2 : 
    print('1 is less than 2')

    print('This is still in the if block')
print('This is outside the if block','\n')



age = 20
license = True
if age>18 and license==True:
    print('You can drive')


''' Check if a number belong to [18, 60]'''
a = 22
if a>=18 and a<= 60 :
    print("a belong to [18, 60] (", a ,")",sep='')
    """ELSE"""
else:
    print("a does not belong to [18, 60]")

""" Elif"""
# choose talent engineer
age = 24
ivyleague = True
qExperience = 2

if  age<=22 and ivyleague==True:
    print('You are a talent grad')  

elif bool(qExperience):
        print('CV passed',type(qExperience) )

else:    print('Not qualified enough')
    
""""short hand if
age = 20
if age>18: print('You can drive') """
ez = True
learn='python' if ez else 'java'
print(learn)
