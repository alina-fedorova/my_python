#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Екатеринбург-код 343, 15 руб/мин
# Омск-код 381, 18 руб/мин
# Воронеж-код 473, 13 руб/мин
# Ярославль-код 485, 11 руб/мин

code=int(input('Введите код города:\n'))
length=int(input('Введите длительность переговоров в минутах:\n'))
if code==343:
    print ('Стоимость переговоров:',length*15,'руб')
elif code==381:
    print ('Стоимость переговоров:',length*18,'руб')
elif code==473:
    print ('Стоимость переговоров:',length*13,'руб')
elif code==485:
    print ('Стоимость переговоров:',length*11,'руб')
else:
    print ('Позвоните в другой город :)')

