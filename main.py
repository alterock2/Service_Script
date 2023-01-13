import pandas as pd
from pandas. tseries.offsets import DateOffset
#чтение файла

df_service = pd.read_excel(r"C:\Users\user\Desktop\Сервис.xlsx")

df_finished = pd.read_excel(r"C:\Users\user\Desktop\Завершенные.xlsx")

# преобразование в дату

pd.to_datetime(df_service['Дата'])


#добавление стобца месяц и год
df_service['Месяц'] = df_service['Дата'].dt.to_period("M")

#удаление 00:00

df_service['Дата'] = df_service['Дата'].dt.date

#добавление списов с ценами

byt_tekh_1 = ['Аэрогриль', 'Мультиварка', 'Хлебопечь'] #570
byt_tekh_2 = ['Блендер', 'Миксер', 'Чоппер', 'Йогуртница', 'Шашлычница', 'Сэндвичница'
              'Кофеварка', 'Электрочайник', 'Термокружка', 'Кофемолка', 'Сушилка'
              'плитка'] #370
byt_tekh_3 = ['Бритва', 'Машинка для стрижки']  #340
byt_tekh_4 = ['Вентилятор', 'Тепловентилятор', 'Фен', 'Утюг', 'Пылесос', 'Отпариватель'] #360
byt_tekh_5 = ['Весы', 'Безмен'] #250
byt_tekh_6 = ['Комбайн', 'Соковыжималка', 'Термопот'] #460
byt_tekh_7 = ['Микроволновка', 'Мини-печь'] #500
byt_tekh_out = ['Списано бт'] #200

inst_1 = ['Аккумулятор'] #500
inst_2 = [' Фен техн', 'Зарядное', 'Гравер'] #400
inst_3 = ['Газонокосилка', 'Электропила', 'Высоторез электро', 'Воздуходув электро',
          'Садовые ножницы']#600
inst_4 = ['Бензопила', ' Воздуходув бензо', 'Бензотриммер'] #720
inst_out = ['Списано инстр'] #350

#подсчет суммы помесячно

#vitya = df_service.index[(df_service.Механик != 'Витя')].tolist()
#df_service_vitya = df_service.drop(index =vitya)

#df_service_vitya.reset_index(drop=True, inplace=True)

for i in df_service['Id']:
    item_index = df_service[df_service['Id'] == i].index[0]
    item = df_service.at[item_index, 'Товар']
    if item in byt_tekh_1:
        df_service.at[item_index, 'Цена'] = 570
    elif item in byt_tekh_2:
        df_service.at[item_index, 'Цена'] = 370
    elif item in byt_tekh_3:
        df_service.at[item_index, 'Цена'] = 340
    elif item in byt_tekh_4:
        df_service.at[item_index, 'Цена'] = 360
    elif item in byt_tekh_5:
        df_service.at[item_index, 'Цена'] = 250
    elif item in byt_tekh_6:
        df_service.at[item_index, 'Цена'] = 460
    elif item in byt_tekh_7:
        df_service.at[item_index, 'Цена'] = 500
    elif item in byt_tekh_out:
        df_service.at[item_index, 'Цена'] = 200
    elif item in inst_1:
        df_service.at[item_index, 'Цена'] = 500
    elif item in inst_2:
        df_service.at[item_index, 'Цена'] = 400
    elif item in inst_3:
        df_service.at[item_index, 'Цена'] = 600
    elif item in inst_4:
        df_service.at[item_index, 'Цена'] = 720
    elif item in inst_out:
        df_service.at[item_index, 'Цена'] = 350

    else:
        df_service.at[item_index, 'Цена'] = 0

#создание таблицы завершенные

finished = df_service.index[(df_service.Статус != 'Выдан')].tolist()
df_service_finished = df_service.drop(index=finished)
df_service_finished.reset_index(drop=True, inplace=True)
df_finished_final = pd.concat([df_finished, df_service_finished])

#удаление из основной таблицы старых данных "выдан"

last_date = df_service['Дата'].iloc[-1]
last_date = last_date - DateOffset(months=2)
last_date = last_date.to_period("M")


delete_index = df_service.index[(df_service.Месяц < last_date) & (df_service.Статус == 'Выдан')].tolist()
if delete_index:
    df_service = df_service.drop(index=delete_index)
    df_service.reset_index(drop=True, inplace=True)

#запись в xlsx

#df_service.to_excel(r"C:\Users\user\Desktop\Сервис.xlsx", index=False)
#df_finished_final.to_excel(r"C:\Users\user\Desktop\Завершенные.xlsx", index=False)

#Вывод суммы по месяцам

monthly_sum = df_service.groupby(df_service['Месяц'])['Цена'].sum()

vitya = df_service.groupby(['Механик', 'Месяц'], as_index=False)['Цена'].sum()

print(f' Заработок Вити за предыдущий месяц {vitya["Цена"].iloc[-2]}')

print(f' Стоимость ремонтов всего за предыдущий месяц {monthly_sum.iloc[-2]}')