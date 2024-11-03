# TODO Напишите функцию find_common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

def find_common_participants(group1: str, group2: str, separator: str = ','):
    participants1 = set(group1.split(separator))
    participants2 = set(group2.split(separator))

    common_participants = participants1.intersection(participants2)

    return sorted(common_participants)


result = find_common_participants(participants_first_group, participants_second_group, '|')
print(result)
