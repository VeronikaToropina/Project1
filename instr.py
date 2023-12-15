win_x, win_y = 200, 100
win_heights = 600
win_width = 1000

#win1
txthello = 'Добро пожаловать в программу по определению состояния здоровья!'
txtinstruction = f'Данное приложение позволит вам с помощью теста Руфье провести первичную диагностику вашего здоровья.\n'
f'Проба Руфье представляет собой нагрузочный комплекс, предназначенный для оценки работоспособности сердца при физической нагрузке.\n'
f'У испытуемого, находящегося в положении лежа на спине в течение 5 мин, определяют частоту пульса за 15 секунд;\n'
f'затем в течение 45 секунд испытуемый выполняет 30 приседаний.\n'
f'После окончания нагрузки испытуемый ложится, и у него вновь подсчитывается число пульсаций за первые 15 секунд,\n'
f'а потом — за последние 15 секунд первой минуты периода восстановления.\n'
f'Важно! Если в процессе проведения испытания вы почувствуете себя плохо (появится головокружение, шум в\n'
f'ушах, сильная одышка и др.), то тест необходимо прервать и обратиться к врачу.'
butstart0 = 'Начать'


#win2
txtfio = 'Введите Ф.И.О.:'
txtage = 'Полных лет:'
txtresult1 = 'Лягте на спину и замерьте пульс за 15 секунд. Нажмите кнопку "Начать первый тест", чтобы запустить таймер.Результат запишите в соответствующее поле.'
txtstart = 'Выполните 30 приседаний за 45 секунд. Для этого нажмите кнопку "Начать делать приседания", чтобы запустить счетчик приседаний.'
txtresult2 = f'Лягте на спину и замерьте пульс сначала за первые 15 секунд минуты, затем за последние 15 секунд.\n'
f'Нажмите кнопку "Начать финальный тест", чтобы запустить таймер.\nЗелёным обозначены секунды, в течение которых необходимо \n'
f'проводить измерения, черным - секунды без замера пульсаций. Результаты запишите в соответствующие поля.'
txttime = ''
butstart1 = 'Начать первый тест'
butstartprised = 'Начать делать приседания'
butstart2 = 'Начать финальный тест'
butsendres = 'Отправить результаты'
linefio = 'Ф.И.О.'
lineage = '0'
linepuls0 = '0'
linepuls1 = '0'
linepuls2 = '0'

#win3
index_text_ = 'Индекс Руфье:'
result_text_ = 'Работоспособность сердца:'


final_window = 'Результаты'
second_window = 'Здоровье'


txt_res1 = "низкая. Срочно обратитесь к врачу!"
txt_res2 = "удовлетворительная. Обратитесь к врачу!"
txt_res3 = "средняя. Возможно, стоит дополнительно обследоваться у врача."
txt_res4 = "выше среднего"
txt_res5 = "высокая"