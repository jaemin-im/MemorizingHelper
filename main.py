import mhinfo
import sqlite3

print('Term Memorizing Program with Python: v{}'.format(mhinfo.version))
print('1. Add Term')
print('2. Modify Term')
print('3. Practice Term')
print('4. Test Term')
print('0. Exit')

select = int(input("Input the number:\n"))

if select == 1:
    pass # Add Term
elif select == 2:
    pass # Modify Term
elif select == 3:
    pass # Practice Term
elif select == 4:
    pass # Test Term
elif select == 0:
    print('Interrupting Program. Bye!')
    exit()
