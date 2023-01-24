import pandas as pd
from pandas. tseries.offsets import DateOffset
from datetime import datetime, timedelta
from styleframe import StyleFrame, Styler, utils
import pygsheets
pd.options.mode.chained_assignment = None

from pygsheets import DataRange
from Price import price_count

#Гугл таблицы

gc = pygsheets.authorize(service_file=r"C:\Users\user\Desktop\stable-woods-374912-6149e61555af.json")
sh = gc.open_by_url('https://docs.google.com/spreadsheets/d/1uDJRJRoowdeSLKFlxa32a8fgiPYyMuq1hLSR6gu1gQo/edit#gid=0')
wks = sh[0]
#чтение файлов

df_service = pd.read_excel(r"C:\Users\user\Desktop\Сервис.xlsx")

df_finished = pd.read_excel(r"C:\Users\user\Desktop\Завершенные.xlsx")

df_vitya = wks.get_as_df()

#df_vitya = pd.read_excel(r"C:\Users\user\Desktop\Google_Disk\Сервис_Витя.xlsx")



# преобразование в дату

pd.to_datetime(df_service['Дата'])


#добавление стобца месяц и год
df_service['Месяц'] = df_service['Дата'].dt.to_period("M")


#получение сегодняшней даты и добавление столбца в ремонте

d = datetime.today()

df_service['В ремонте'] = (d - df_service['Дата']).dt.days

print(df_vitya['Запчасть'])
# обновление основного файла из Вити
df_service['Id'] = df_service['Id'].astype(int)
df_vitya['Id'] = df_vitya['Id'].astype(int)

df_vitya = df_vitya[['Id', 'Запчасть']]

df_service.set_index('Id', inplace=True)
df_vitya.set_index('Id', inplace=True)
#.drop(['Дата', 'Телефон клиента', 'ФИО Клиента', 'Серийный номер', 'Статус', 'Товар', 'В ремонте'], axis= 1 , inplace= True )


df_service.update(df_vitya)
df_service.reset_index(inplace=True)
df_vitya.reset_index(inplace=True)

print(df_service['Запчасть'])

#df_service.update(df_vitya)


#добавление списов с ценами

# byt_tekh_1 = ['Аэрогриль', 'Мультиварка', 'Хлебопечь'] #570
# byt_tekh_2 = ['Блендер', 'Миксер', 'Чоппер', 'Йогуртница', 'Шашлычница', 'Сэндвичница'
#               'Кофеварка', 'Электрочайник', 'Термокружка', 'Кофемолка', 'Сушилка'
#               'Плитка', 'Тостер', 'Плита', 'Электроплитка'] #370
# byt_tekh_3 = ['Бритва', 'Машинка для стрижки']  #340
# byt_tekh_4 = ['Вентилятор', 'Тепловентилятор', 'Фен', 'Утюг', 'Пылесос', 'Отпариватель'] #360
# byt_tekh_5 = ['Весы', 'Безмен'] #250
# byt_tekh_6 = ['Комбайн', 'Соковыжималка', 'Термопот'] #460
# byt_tekh_7 = ['Микроволновка', 'Мини-печь'] #500
# byt_tekh_out = ['Списано бт'] #200
#
# inst_1 = ['Аккумулятор'] #500
# inst_2 = [' Фен техн', 'Зарядное', 'Гравер'] #400
# inst_3 = ['Газонокосилка', 'Электропила', 'Высоторез электро', 'Воздуходув электро',
#           'Садовые ножницы']#600
# inst_4 = ['Бензопила', ' Воздуходув бензо', 'Бензотриммер'] #720
# inst_5 = ['Насос'] #470
# inst_out = ['Списано инстр'] #350

#подсчет суммы помесячно

for i in df_service['Id']:
    price_count(i, df=df_service)
    # item_index = df_service[df_service['Id'] == i].index[0]
    # item = df_service.at[item_index, 'Товар']
    # item_status = df_service.at[item_index, 'Статус']
    # if item in byt_tekh_1:
    #     if item_status != 'Списано':
    #         df_service.at[item_index, 'Цена'] = 570
    #     else:
    #         df_service.at[item_index, 'Цена'] = 200
    # elif item in byt_tekh_2:
    #     if item_status != 'Списано':
    #         df_service.at[item_index, 'Цена'] = 370
    #     else:
    #         df_service.at[item_index, 'Цена'] = 200
    # elif item in byt_tekh_3:
    #     if item_status != 'Списано':
    #         df_service.at[item_index, 'Цена'] = 340
    #     else:
    #         df_service.at[item_index, 'Цена'] = 200
    # elif item in byt_tekh_4:
    #     if item_status != 'Списано':
    #         df_service.at[item_index, 'Цена'] = 360
    #     else:
    #         df_service.at[item_index, 'Цена'] = 200
    # elif item in byt_tekh_5:
    #     if item_status != 'Списано':
    #         df_service.at[item_index, 'Цена'] = 250
    #     else:
    #         df_service.at[item_index, 'Цена'] = 200
    # elif item in byt_tekh_6:
    #     if item_status != 'Списано':
    #         df_service.at[item_index, 'Цена'] = 460
    #     else:
    #         df_service.at[item_index, 'Цена'] = 200
    # elif item in byt_tekh_7:
    #     if item_status != 'Списано':
    #         df_service.at[item_index, 'Цена'] = 500
    #     else:
    #         df_service.at[item_index, 'Цена'] = 200
    #
    #
    # elif item in inst_1:
    #     if item_status != 'Списано':
    #         df_service.at[item_index, 'Цена'] = 500
    #     else:
    #         df_service.at[item_index, 'Цена'] = 350
    # elif item in inst_2:
    #     if item_status != 'Списано':
    #         df_service.at[item_index, 'Цена'] = 400
    #     else:
    #         df_service.at[item_index, 'Цена'] = 350
    # elif item in inst_3:
    #     if item_status != 'Списано':
    #         df_service.at[item_index, 'Цена'] = 600
    #     else:
    #         df_service.at[item_index, 'Цена'] = 350
    # elif item in inst_4:
    #     if item_status != 'Списано':
    #         df_service.at[item_index, 'Цена'] = 720
    #     else:
    #         df_service.at[item_index, 'Цена'] = 350
    # elif item in inst_5:
    #     if item_status != 'Списано':
    #         df_service.at[item_index, 'Цена'] = 470
    #     else:
    #         df_service.at[item_index, 'Цена'] = 350
    #
    #
    # else:
    #     df_service.at[item_index, 'Цена'] = 0



#вычитание даты 2 месяца назад"

last_date = df_service['Дата'].iloc[-1]
last_date = last_date - DateOffset(months=2)
last_date = last_date.to_period("M")


#создание таблицы завершенные

names_to_del = ['Выдан', 'Списано']

finished = df_service[(df_service.Статус.isin(names_to_del)) & (df_service.Месяц < last_date)]
finished.drop('В ремонте', axis=1, inplace=True)
df_finished_final = pd.concat([df_finished, finished], ignore_index=True)
#df_finished_final.reset_index(inplace=True, drop=True)

#удаление старых данных выдан

delete_index = df_service.index[(df_service.Месяц < last_date) & (df_service.Статус.isin(names_to_del))].tolist()

if delete_index:
    df_service = df_service.drop(index=delete_index)
    df_service.reset_index(inplace=True) #drop=True, inplace=True


#удаление 00:00

df_service['Дата'] = df_service['Дата'].dt.date

#обновление таблицы Витя
print(df_vitya)
repair_status = ['Принят', 'Получено', 'Заказано', 'Диагностика', 'Списано']

df_vitya = df_service[(df_service.Механик == 'Витя') & (df_service.Статус.isin(repair_status))]
df_vitya.reset_index(inplace=True, drop=True)
print(df_vitya)
df_vitya['Запчасть'] = df_vitya['Запчасть']. fillna('-')

df_vitya.drop(['Механик', 'Месяц'], axis=1, inplace=True)
print(df_vitya)
#запись в xlsx

#df_service.to_excel(r"C:\Users\user\Desktop\Сервис.xlsx", index=False)
df_finished_final.to_excel(r"C:\Users\user\Desktop\Завершенные.xlsx", index=False)



#Вывод суммы по месяцам

monthly_sum = df_service.groupby(df_service['Месяц'])['Цена'].sum()

vitya = df_service.groupby(['Механик', 'Месяц'], as_index=False)['Цена'].sum()
vitya = vitya[(vitya.Механик == 'Витя')]

print(f' Заработок Вити за предыдущий месяц {vitya["Цена"].iloc[-2]}')

print(f' Стоимость ремонтов всего за предыдущий месяц {monthly_sum.iloc[-2]}')

#сохранение сервис в style frame

default_style = Styler(font=utils.fonts.calibri, font_size=11)
sf_service = StyleFrame(df_service, styler_obj=default_style)

header_style = Styler(bold=True, font_size=12)
sf_service.apply_headers_style(styler_obj=header_style)

green_style = Styler(bold=True, bg_color=utils.colors.green)
sf_service.apply_style_by_indexes(indexes_to_style=sf_service[sf_service['В ремонте'] <= 10],
cols_to_style='В ремонте', styler_obj=green_style, overwrite_default_style=False)

yellow_style = Styler(bold=True, bg_color=utils.colors.yellow)
sf_service.apply_style_by_indexes(indexes_to_style=sf_service[(sf_service['В ремонте'] <= 30) & (sf_service['В ремонте'] > 10)],
cols_to_style='В ремонте', styler_obj=yellow_style, overwrite_default_style=False)

red_style = Styler(bold=True, bg_color=utils.colors.red)
sf_service.apply_style_by_indexes(indexes_to_style=sf_service[(sf_service['В ремонте'] > 30)],
cols_to_style='В ремонте', styler_obj=red_style, overwrite_default_style=False)

#protection_style = Styler(bold=True, font=utils.fonts.calibri, font_size=11, protection=False)
#sf_vitya.apply_column_style(cols_to_style=['Запчасть'], styler_obj=protection_style, overwrite_default_style=True)

sf_service.set_column_width_dict(col_width_dict={'Id': 8,
'Дата': 10,
('Телефон клиента', 'ФИО Клиента', 'Товар', 'Артикул', 'Серийный номер', 'Механик', 'Поломка', 'Запчасть', 'В ремонте'): 15,
 ('Статус', 'Цена', 'Месяц'): 12})


sf_service.to_excel(r"C:\Users\user\Desktop\Сервис.xlsx", row_to_add_filters=0, columns_and_rows_to_freeze='A2').save()

#запись в Гугл таблицы

wks.clear()
wks.set_dataframe(df_vitya, (1, 1), copy_index=False)

#Форматирование Гугл Таблицы Витя

model_cell = wks.cell('A1')
model_cell.set_text_format('bold', True)
model_cell.text_format['fontSize'] = 11
model_cell.color = (255/255, 132/255, 0, 1)
model_cell.wrap_strategy = 'WRAP'
model_cell.borders = {
    "bottom": {'style': 'SOLID_THICK', "width": 1,"color": {'red': 0, 'green': 0, 'blue': 0}},
    "right": {'style': 'SOLID_THICK', "width": 1,"color": {'red': 0, 'green': 0, 'blue': 0}}
}



wrap_cell = wks.cell('A1')
wrap_cell.wrap_strategy = 'WRAP'

date_cell = wks.cell('A1')
date_cell.set_number_format(format_type= pygsheets.FormatType.DATE)

DataRange('C', 'L', worksheet=wks).apply_format(wrap_cell)
DataRange('A1','L1', worksheet=wks).apply_format(model_cell)



wks.add_conditional_formatting('L', 'L', 'NUMBER_GREATER_THAN_EQ', {'backgroundColor': {'red': 0.8},
                                'textFormat': {'bold': True}}, ['30'])

wks.add_conditional_formatting('L', 'L', 'NUMBER_BETWEEN', {'backgroundColor':
{"red": 250/255, "green": 77/255, "blue": 77/255, "alpha": 1}}, ['14', '30'])

wks.add_conditional_formatting('L', 'L', 'NUMBER_LESS_THAN_EQ', {'backgroundColor':
{"red": 255/255, "green": 158/255, "blue": 158/255, "alpha": 1}}, ['14'])

DataRange('B2','B8', worksheet=wks).apply_format(date_cell)

