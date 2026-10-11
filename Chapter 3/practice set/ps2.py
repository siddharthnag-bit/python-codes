'''name=input()
date=input()
letter =f'''
'''Dear {name},
You are selected!
{date}
'''

'''print(letter)'''

name=input("Enter Your name:")
date=input("Enter the date:")
letter='''
Dear Name,
You are selected!
Date
'''
print(letter.replace("Name",name).replace("Date",date))
