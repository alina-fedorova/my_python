#!/usr/bin/env python
# coding: utf-8

# In[5]:


film=input('Введите название фильма: "Пятница", "Чемпионы" или "Пернатая банда"\n')
date=input('Вы пойдете на фильм сегодня или завтра?\n')
people=int(input('Сколько билетов вам нужно?\n'))
if film=='Пятница' or 'пятница':
    time=int(input('Укажите время (цифрой): 12, 16 или 20 часов\n'))
    if date=='сегодня':
        if people>=20:
                if time==12:
                    print('Стоимость=',250*people*0.8,'руб')
                elif time==16:
                    print('Стоимость=',350*people*0.8,'руб')
                elif time==20:
                    print('Стоимость=',450*people*0.8,'руб')
                else:
                    print('Ошибка ввода')
        elif 0<=people<20:
                if time==12:
                    print('Стоимость=',250*people,'руб')
                elif time==16:
                    print('Стоимость=',350*people,'руб')
                elif time==20:
                    print('Стоимость=',450*people,'руб')
                else:
                    print('Ошибка ввода')
        else:
            print('Ошибка ввода')
    elif date=='завтра':
        if people>=20:
            if time==12:
                print('Стоимость=',250*people*0.95*0.8,'руб')
            elif time==16:
                print('Стоимость=',350*people*0.95*0.8,'руб')
            elif time==20:
                print('Стоимость=',450*people*0.95*0.8,'руб')
            else:
                    print('Ошибка ввода')
        elif 0<=people<20: 
            if time==12:
                print('Стоимость=',250*people*0.95,'руб')
            elif time==16:
                print('Стоимость=',350*people*0.95,'руб')
            elif time==20:
                print('Стоимость=',450*people*0.95,'руб')
            else:
                    print('Ошибка ввода')
        else:
            print('Ошибка ввода')
    else:
        print('Ошибка ввода')
elif film=='Чемпионы' or 'чемпионы':
    time1=int(input('Укажите время (цифрой): 10, 13 или 16 часов\n'))
    if date=='сегодня':
        if people>=20:
            if time1==10:
                print('Стоимость=',250*people*0.8,'руб')
            elif time1==13:
                print('Стоимость=',350*people*0.8,'руб')
            elif time1==16:
                print('Стоимость=',350*people*0.8,'руб')
            else:
                    print('Ошибка ввода')
        elif 0<=people<20: 
            if time1==10:
                  print('Стоимость=',250*people,'руб')
            elif time1==13:
                print('Стоимость=',350*people,'руб')
            elif time1==16:
                print('Стоимость=',350*people,'руб')
            else:
                    print('Ошибка ввода')
        else:
            print('Ошибка ввода')
    elif date=='завтра':
        if people>=20:
            if time1==10:
                print('Стоимость=',250*people*0.95*0.8,'руб')
            elif time1==13:
                print('Стоимость=',350*people*0.95*0.8,'руб')
            elif time1==16:
                print('Стоимость=',350*people*0.95*0.8,'руб')
            else:
                    print('Ошибка ввода')
        elif 0<=people<20: 
            if time1==10:
                print('Стоимость=',250*people*0.95,'руб')
            elif time1==13:
                print('Стоимость=',350*people*0.95,'руб')
            elif time1==16:
                print('Стоимость=',350*people*0.95,'руб')
            else:
                    print('Ошибка ввода')
        else:
            print('Ошибка ввода')
    else:
        print('Ошибка ввода')
elif film=='Пернатая банда' or 'пернатая банда':
    time2=int(input('Укажите время (цифрой): 10, 14 или 18 часов\n'))
    if date=='сегодня':
        if people>=20:
            if time2==10:
                print('Стоимость=',250*people*0.8,'руб')
            elif time2==14:
                print('Стоимость=',350*people*0.8,'руб')
            elif time2==18:
                print('Стоимость=',350*people*0.8,'руб')
            else:
                    print('Ошибка ввода')
        elif 0<=people<20: 
            if time2==10:
                print('Стоимость=',250*people,'руб')
            elif time2==14:
                print('Стоимость=',350*people,'руб')
            elif time2==18:
                print('Стоимость=',350*people,'руб')
            else:
                    print('Ошибка ввода')
        else:
            print('Ошибка ввода')
    elif date=='завтра':
        if people>=20:
            if time2==10:
                print('Стоимость=',250*people*0.95*0.8,'руб')
            elif time2==14:
                print('Стоимость=',350*people*0.95*0.8,'руб')
            elif time2==18:
                print('Стоимость=',350*people*0.95*0.8,'руб')
            else:
                    print('Ошибка ввода')
        elif 0<=people<20: 
            if time2==10:
                print('Стоимость=',250*people*0.95,'руб')
            elif time2==14:
                print('Стоимость=',350*people*0.95,'руб')
            elif time2==18:
                print('Стоимость=',350*people*0.95,'руб')
            else:
                    print('Ошибка ввода')
        else:
            print('Ошибка ввода')
    else:
        print('Ошибка ввода')
else:
    print('Ошибка ввода')


# In[ ]:




