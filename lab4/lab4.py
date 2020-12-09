import csv
import os.path
from prettytable import PrettyTable
from collections.abc import Iterable
from string import ascii_letters
class Old_base():
    """Родительский класс для класса Best_base
    """
    def __init__(self):
        """Конструктор класса Old_base
        """
        self.data_base = []
        self.my_iterator = 0
    @staticmethod
    def read_from_file(data_base):
        """Функция считывает данные для словаря из файла.
        param: data_base - словарь
        """
        with open('D://MyProgs/for_lab/base.csv') as File:
            reader = csv.DictReader(File, delimiter=';')
            for row in reader:
                data_base.append(row)

    @staticmethod
    def write_to_file(data_base):
        """Функция записывает данные из словаря в файл.
        param: data_base - словарь
        """
        with open('D://MyProgs/for_lab/base.csv', 'w', newline = '\n') as out_file:
                writer = csv.DictWriter(out_file, delimiter=';', fieldnames=('number_canteen', 'dish_name', 'quantity_in_grams', 'delivery_time', 'replacement_time', 'remainder'))
                writer.writeheader()
                for row in data_base:
                    writer.writerow(row)

class Best_base(Old_base):
    """ Этот класс создаёт словарь, а также методы для взаимодейстия со словарём. 

    """
    def __init__(self):
       """Конструктор класса Best_base
       """
       super().__init__()
        
    def output_data_base(self, num):
        """Функция выводит словарь в консоль.
        param: num - параметр для вывода строк
        """
        table = PrettyTable()
        table.field_names = self.data_base[0].keys()
        for i in range(len(self.data_base)):
                table.add_row(self.data_base[i].values())
        print(table)

    def using_iterator_and_generator(self,):
        """Функция создаёт итератор и генератор, а поотом совершает с ними работу.
        """
        print("Длина = ",len(self.data_base))
        my_list = []
        for i in range(len(self.data_base)):
            my_list .append(int(self.data_base[i]['number_canteen']))
        self.my_iterator = iter(my_list )
        print(next(self.my_iterator), next(self.my_iterator), next(self.my_iterator))
        #генератор
        print('Генератор:')
        my_generator = (int(x) * 2 for x in my_list)
        print(next(my_generator), next(my_generator), next(my_generator))


    def __repr__(self):
           """Функция возвращает определённое значение, когда в неё передаётся экзампляр класса. 
           """
           return  str(self.data_base[0]['dish_name'])

    def __getitem__(self, item):
           """Функция получает индекс элемента, а потом возвращает элемент списка под этим номером.  
           """
           return self.data_base[item]['number_canteen']

    def __setattr__(self, attr, value):
           """Вызывается при попытке присвоения полю экземпляра класса какого-либо значения. Производит проверку на тип данных.
           param: attr - имя атрибута
           param: value - значение, которое должно быть присвоено атрибуту
           """
           if isinstance(value, list):
               self.__dict__[attr] = value
           elif isinstance(value, Iterable):
               self.__dict__[attr] = value
           elif value > -1:
               self.__dict__[attr] = value
           else:
               raise (AttributeError, attr + ' not allowed')



def main():
    """Функция создаёт экземпляр класса Best_base. Записывает данные из файла в поля экзмепляра класса. 
    Производится взаимодействие с экзепляром класса. Вызываются  все необходимые методы. Данные записываются в файл.
    """
    base = Best_base()
    base.read_from_file(base.data_base)
    base.output_data_base(-1)
    base.using_iterator_and_generator()
    try:#Взаимодействие со словарём
        select_path = int(input("Введите (1), если хотите отсортировать словарь по строковому полю.\nВведите (2), если хотите отсортировать словарь по числовому полю.\nВведите (3), если хотите задать критерий для словаря.\nВведите (4), если хотите использовать getitem.\nВведите (5), если хотите использовать rerp.\nВвод: "))
    except ValueError as e:
        print("Вызвано исключение", e)
        return
    if(select_path == 1):
        base.data_base.sort(key=lambda i: i['dish_name'])
        base.output_data_base(base.data_base, -1)
    elif (select_path == 2):
        base.data_base.sort(key=lambda i: int(i['number_canteen']))
        base.output_data_base(-1)
    elif (select_path == 3):
        try:
            choice_criterion = int(input("Введите число. Будт показаны столовые, у которых номер большего этого числа.\nВвод: "))
        except ValueError as e:
            print("Вызвано исключение", e)
            return
            base.output_data_base(base.data_base,  choice_criterion)
    elif (select_path == 4):
        try:
            choice_item = int(input("Введите число. Будет выведен элемент под этим индексом.\nВвод:"))
        except ValueError as e:
            print("Вызвано исключение", e)
            return
        print("Использован getiem: ",base[choice_item])
    elif (select_path == 5):
        print("Использован repr: ", base)
    else:
        print("Введены некорректные данные!")
    try:#Запись изменённого словаря в файл
        select_save = int(input("Введите (1), если хотите сделать сохранение. Введите что-либо другое, если сохранение не требуется.\nВвод: "))
    except ValueError as e:
        print("Вызвано исключение", e)
        return
    if(select_save == 1):
        base.write_to_file(base.data_base)
    bespoleznaja = 5
    print("Конец программы!")

main()
    