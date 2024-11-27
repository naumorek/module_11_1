import random



def dat_bas_rand(file_name,first_name_arr,second_name_arr,count_study):
    with open(f'{file_name}','a',encoding='utf-8') as file:
        list_study=[]
        for i in range(count_study):
            first=random.choice(first_name_arr)
            second=random.choice(second_name_arr)
            second_2=str(random.randint(1,13))
            clas_study=random.choice([10,11])
            sex=random.choice(['female','male'])
            if clas_study==10:
                point_study=random.choices([3,4,5,6,7,8,9,10],weights=[2, 3, 7,12,20,14,10,5])[0]
            else:
                point_study=random.choices([3,4,5,6,7,8,9,10],weights=[2, 4, 5,14,16,17,12,3])[0]


            study={'name':f'{first+second+second_2}','sex':sex,'class_study': clas_study,'point_study': point_study}

            file.write(f"{study}\n" )



first_name_arr=["Август","Августин","Авраам","Аврора","Агата","Агафон","Агнесса","Агния","Ада","Аделаида","Аделина","Адонис","Акайо","Акулина","Алан",\
"Алевтина","Александр","Александра","Алексей","Алена","Алина","Алиса","Алла","Алсу","Альберт","Альбина","Альфия","Альфред","Амалия","Амелия","Анастасий",\
                "Анастасия","Анатолий","Ангелина","Андрей","Анжела","Анжелика","Анисий","Анна","Антон","Антонина","Анфиса","Аполлинарий","Аполлон",\
                "Ариадна","Арина","Аристарх","Аркадий","Арсен","Арсений","Артем","Артемий","Артур","Архип","Ася"]
dat_bas_rand('study_arr.txt',first_name_arr,first_name_arr,2500)
