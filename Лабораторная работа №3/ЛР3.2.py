# TODO Напишите функцию find_common_participants
def find_common_participants(str_1,str_2,sep=','):
   first_group = str_1.split(sep)
   second_group = str_2.split(sep)
   general = list(set(first_group).intersection(second_group))
   return general


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
sep_1 = '|'
result = find_common_participants(participants_first_group,participants_second_group,sep_1)
print(sorted(result))
# TODO Провеьте работу функции с разделителем отличным от запятой
