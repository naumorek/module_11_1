
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


summed_10_point = data_10_st.groupby('class_study')['point_study'].sum()   #Находим среднее значение баллов по классу
a=summed_10_point.loc [0:0]
print(summed_10_point,'summed_10_point',len(data_10_st))




img1=data_11_st['point_study'].plot.hist() # Построение гистограммы по колонке оценки в 11 классе
plt.title('Гистрограмма оценок в 11 классе')
plt.xlabel('Оценка')
plt.ylabel('Кол-во учащихся получивших оценку')
#plt.show()
img2=data_10_st['point_study'].plot.hist() # Построение гистограммы по колонке оценки в 11 классе
plt.title('Гистрограмма оценок в 10 классе')
plt.xlabel('Оценка')
plt.ylabel('Кол-во учащихся получивших оценку')

#plt.show()






