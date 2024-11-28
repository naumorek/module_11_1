
import ast
import pandas as pd
import matplotlib.pyplot as plt


with open('study_arr.txt','r', encoding='utf-8') as file:
    data_file=file.readlines()
    list_study=[]
    for line in data_file: #построчно читаем файл
        dict1=ast.literal_eval(line) #переводим строку в dict
        list_study.append(dict1)
    result_series = pd.DataFrame(list_study)  #переводим массив из dict в DataFrame
df=result_series


print(df.groupby(["sex", "class_study"])["sex"].count()) #выводим количество мальчиков и девочек по классам
data_11_st=df[lambda x: x['class_study'] == 11]
data_10_st=df[lambda x: x['class_study'] == 10]




mean_10_point = data_10_st.groupby('class_study')['point_study'].transform('mean')   #Находим среднее значение баллов по 10 классу
mean_11_point = data_11_st.groupby('class_study')['point_study'].transform('mean')   #Находим среднее значение баллов по 11 классу


print(mean_10_point[1].round(2), "Средний бал в 10 классе")
print(mean_11_point[0].round(2), "Средний бал в 11 классе")




img1=data_11_st['point_study'].plot.hist() # Построение гистограммы по колонке оценки в 11 классе
plt.title('Гистрограмма оценок в 11 классе')
plt.xlabel('Оценка')
plt.ylabel('Кол-во учащихся получивших оценку')
plt.show()
img2=data_10_st['point_study'].plot.hist() # Построение гистограммы по колонке оценки в 11 классе
plt.title('Гистрограмма оценок в 10 классе')
plt.xlabel('Оценка')
plt.ylabel('Кол-во учащихся получивших оценку')

plt.show()






