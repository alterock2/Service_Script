def price_count(str, df):
    byt_tekh_1 = ['Аэрогриль', 'Мультиварка', 'Хлебопечь']  # 570
    byt_tekh_2 = ['Блендер', 'Миксер', 'Чоппер', 'Йогуртница', 'Шашлычница', 'Сэндвичница',
                  'Кофеварка', 'Электрочайник', 'Термокружка', 'Кофемолка', 'Сушилка',
                  'Плитка', 'Тостер', 'Плита', 'Электроплитка']  # 370
    byt_tekh_3 = ['Бритва', 'Машинка для стрижки']  # 340
    byt_tekh_4 = ['Вентилятор', 'Тепловентилятор', 'Фен', 'Утюг', 'Пылесос', 'Отпариватель']  # 360
    byt_tekh_5 = ['Весы', 'Безмен']  # 250
    byt_tekh_6 = ['Комбайн', 'Соковыжималка', 'Термопот']  # 460
    byt_tekh_7 = ['Микроволновка', 'Мини-печь']  # 500

    inst_1 = ['Аккумулятор', 'Аккумуляторный', 'Аккумуляторная']  # 500
    inst_2 = [' Фен техн', 'Зарядное', 'Гравер', 'Опрыскиватель аккумуляторный']  # 400
    inst_3 = ['Газонокосилка', 'Электропила', 'Высоторез электро', 'Воздуходув электро',
              'Садовые ножницы']  # 600
    inst_4 = ['Бензопила', ' Воздуходув бензо', 'Бензотриммер']  # 720
    inst_5 = ['Насос', 'Электротриммер']  # 470

    other_price = ['Списано', 'Не гарантия']

    item_index = df[df['Id'] == str].index[0]
    item = df.at[item_index, 'Товар']
    item_status = df.at[item_index, 'Статус']
    if item in byt_tekh_1:
        if item_status not in other_price:
            df.at[item_index, 'Цена'] = 570
        elif item_status == 'Не гарантия':
            df.at[item_index, 'Цена'] = 0
        elif item_status == 'Списано':
            df.at[item_index, 'Цена'] = 200
    elif item in byt_tekh_2:
        if item_status not in other_price:
            df.at[item_index, 'Цена'] = 370
        elif item_status == 'Не гарантия':
            df.at[item_index, 'Цена'] = 0
        elif item_status == 'Списано':
            df.at[item_index, 'Цена'] = 200
    elif item in byt_tekh_3:
        if item_status not in other_price:
            df.at[item_index, 'Цена'] = 340
        elif item_status == 'Не гарантия':
            df.at[item_index, 'Цена'] = 0
        elif item_status == 'Списано':
            df.at[item_index, 'Цена'] = 200
    elif item in byt_tekh_4:
        if item_status not in other_price:
            df.at[item_index, 'Цена'] = 360
        elif item_status == 'Не гарантия':
            df.at[item_index, 'Цена'] = 0
        elif item_status == 'Списано':
            df.at[item_index, 'Цена'] = 200
    elif item in byt_tekh_5:
        if item_status not in other_price:
            df.at[item_index, 'Цена'] = 250
        elif item_status == 'Не гарантия':
            df.at[item_index, 'Цена'] = 0
        elif item_status == 'Списано':
            df.at[item_index, 'Цена'] = 200
    elif item in byt_tekh_6:
        if item_status not in other_price:
            df.at[item_index, 'Цена'] = 460
        elif item_status == 'Не гарантия':
            df.at[item_index, 'Цена'] = 0
        elif item_status == 'Списано':
            df.at[item_index, 'Цена'] = 200
    elif item in byt_tekh_7:
        if item_status not in other_price:
            df.at[item_index, 'Цена'] = 500
        elif item_status == 'Не гарантия':
            df.at[item_index, 'Цена'] = 0
        elif item_status == 'Списано':
            df.at[item_index, 'Цена'] = 200

    elif item in inst_1:
        if item_status not in other_price:
            df.at[item_index, 'Цена'] = 500
        elif item_status == 'Не гарантия':
            df.at[item_index, 'Цена'] = 0
        elif item_status == 'Списано':
            df.at[item_index, 'Цена'] = 350
    elif item in inst_2:
        if item_status not in other_price:
            df.at[item_index, 'Цена'] = 400
        elif item_status == 'Не гарантия':
            df.at[item_index, 'Цена'] = 0
        elif item_status == 'Списано':
            df.at[item_index, 'Цена'] = 350
    elif item in inst_3:
        if item_status not in other_price:
            df.at[item_index, 'Цена'] = 600
        elif item_status == 'Не гарантия':
            df.at[item_index, 'Цена'] = 0
        elif item_status == 'Списано':
            df.at[item_index, 'Цена'] = 350
    elif item in inst_4:
        if item_status not in other_price:
            df.at[item_index, 'Цена'] = 720
        elif item_status == 'Не гарантия':
            df.at[item_index, 'Цена'] = 0
        elif item_status == 'Списано':
            df.at[item_index, 'Цена'] = 350
    elif item in inst_5:
        if item_status not in other_price:
            df.at[item_index, 'Цена'] = 470
        elif item_status == 'Не гарантия':
            df.at[item_index, 'Цена'] = 0
        elif item_status == 'Списано':
            df.at[item_index, 'Цена'] = 350

    else:
        df.at[item_index, 'Цена'] = 0
