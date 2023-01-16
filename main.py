import pandas as pd
from pandas. tseries.offsets import DateOffset
from datetime import datetime, timedelta
from styleframe import StyleFrame, Styler, utils
#чтение файлов

df_service = pd.read_excel(r"C:\Users\user\Desktop\Сервис.xlsx")

df_finished = pd.read_excel(r"C:\Users\user\Desktop\Завершенные.xlsx")

df_vitya = pd.read_excel(r"C:\Users\user\Desktop\Google_Disk\Сервис_Витя.xlsx")

# преобразование в дату

pd.to_datetime(df_service['Дата'])


#добавление стобца месяц и год
df_service['Месяц'] = df_service['Дата'].dt.to_period("M")


#получение сегодняшней даты и добавление столбца в ремонте

d = datetime.today()

df_service['В ремонте'] = (d - df_service['Дата']).dt.days


# обновление основного файла из Вити
#df_service['Id'] = df_service['Id'].astype(int)
#df_vitya['Id'] = df_vitya['Id'].astype(int)
#df_service.set_index('Id')

df_service.set_index('Id')
df_service.update(df_vitya.set_index('Id', inplace=True))
df_service.reset_index()
#df_service.update(df_vitya)


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



#вычитание даты 2 месяца назад"

last_date = df_service['Дата'].iloc[-1]
last_date = last_date - DateOffset(months=2)
last_date = last_date.to_period("M")


#создание таблицы завершенные
finished = df_service[(df_service.Статус == 'Выдан') & (df_service.Месяц < last_date)]
#finished = df_service.index[(df_service.Статус != 'Выдан')].tolist()
#df_service_finished = df_service.drop(index=finished)
#df_finished.reset_index(drop=True, inplace=True)
df_finished_final = pd.concat([df_finished, finished])
df_finished_final.reset_index()

#удаление старых данных выдан

delete_index = df_service.index[(df_service.Месяц < last_date) & (df_service.Статус == 'Выдан')].tolist()

if delete_index:
    df_service = df_service.drop(index=delete_index)
    df_service.reset_index() #drop=True, inplace=True


#удаление 00:00

df_service['Дата'] = df_service['Дата'].dt.date

#обновление таблицы Витя

repair_status = ['Принят', 'Получено', 'Заказано', 'Диагностика']

df_vitya = df_service[(df_service.Механик == 'Витя') & (df_service.Статус.isin(repair_status))]
df_vitya.reset_index(drop=True, inplace=True)
print(df_service)
print(df_vitya)



#запись в xlsx

df_service.to_excel(r"C:\Users\user\Desktop\Сервис.xlsx", index=False)
df_finished_final.to_excel(r"C:\Users\user\Desktop\Завершенные.xlsx", index=False)

#Вывод суммы по месяцам

monthly_sum = df_service.groupby(df_service['Месяц'])['Цена'].sum()

vitya = df_service.groupby(['Механик', 'Месяц'], as_index=False)['Цена'].sum()

print(f' Заработок Вити за предыдущий месяц {vitya["Цена"].iloc[-2]}')

print(f' Стоимость ремонтов всего за предыдущий месяц {monthly_sum.iloc[-2]}')

#сохранение сервис Витя в style frame

default_style = Styler(font=utils.fonts.calibri, font_size=11, protection=True)
sf_vitya = StyleFrame(df_vitya, styler_obj=default_style)

header_style = Styler(bold=True, font_size=12, protection=True)
sf_vitya.apply_headers_style(styler_obj=header_style)

green_style = Styler(bold=True, bg_color=utils.colors.green, protection=True)
sf_vitya.apply_style_by_indexes(indexes_to_style=sf_vitya[sf_vitya['В ремонте'] <= 10],
cols_to_style='В ремонте', styler_obj=green_style, overwrite_default_style=False)

yellow_style = Styler(bold=True, bg_color=utils.colors.yellow, protection=True)
sf_vitya.apply_style_by_indexes(indexes_to_style=sf_vitya[(sf_vitya['В ремонте'] <= 30) & (sf_vitya['В ремонте'] > 10)],
cols_to_style='В ремонте', styler_obj=yellow_style, overwrite_default_style=False)

red_style = Styler(bold=True, bg_color=utils.colors.red, protection=True)
sf_vitya.apply_style_by_indexes(indexes_to_style=sf_vitya[(sf_vitya['В ремонте'] > 30)],
cols_to_style='В ремонте', styler_obj=red_style, overwrite_default_style=False)

protection_style = Styler(bold=True, font=utils.fonts.calibri, font_size=11, protection=False)
sf_vitya.apply_column_style(cols_to_style=['Запчасть'], styler_obj=protection_style, overwrite_default_style=True)

sf_vitya.set_column_width_dict(col_width_dict={'Id': 8,
'Дата': 10,
('Телефон клиента', 'ФИО Клиента', 'Товар', 'Артикул', 'Серийный номер', 'Механик', 'Поломка', 'Запчасть', 'В ремонте'): 15,
                                               ('Статус', 'Цена', 'Месяц'): 12})


sf_vitya.to_excel(r"C:\Users\user\Desktop\Google_Disk\Сервис_Витя.xlsx",
                  row_to_add_filters=0, columns_and_rows_to_freeze='A2', allow_protection=True).save()