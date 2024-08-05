from __future__ import annotations
from abc import ABC, abstractmethod
import os
from datetime import datetime, date, timedelta



class Command(ABC):

    @abstractmethod
    def execute(self) -> None:
        pass

class ComplexAddCategory(Command):
    def __init__(self, category: Category, a: str) -> None:
        self._category = category
        self._a = a

    def execute(self) -> None:
        self._category.add_Category_File(self._a)
        self._category.add_Category(self._a)
        return

class ComplexAddExpens(Command):
    def __init__(self, expense: Expense, a: str, b: str, c: float, d: object) -> None:
        self._expense = expense
        self._a = a
        self._b = b
        self._c = c
        self._d = d

    def execute(self) -> None:
        self._expense.save_Expense(self._a)
        self._expense.add_Expense(self._a, self._b, self._c, self._d)

class ComplexDeleteCategory(Command):
    def __init__(self, category: Category, a: str) -> None:
        self._category = category
        self._a = a

    def execute(self) -> None:
        self._category.del_Category(self._a)
        self._category.__str__()

class ComplexReportCategory(Command):
    def __init__(self, report: Report, a: str) -> None:
        self._report = report
        self._a = a

    def execute(self) -> None:
        self._report.show_Report_Category(self._a)

class ComplexReportExpens(Command):
    def __init__(self, report: Report, a: str, b: str) -> None:
        self._report = report
        self._a = a
        self._b = b

    def execute(self) -> None:
        self._report.show_Report_Expense(self._a, self._b)

class ComplexReportDate(Command):
    def __init__(self, report: Report, a: object) -> None:
        self._report = report
        self._a = a

    def execute(self) -> None:
        self._report.show_Date_Expense(self._a)

class ComplexCategoryMaxDate(Command):
    def __init__(self, report: Report, a: object, b: object) -> None:
        self._report = report
        self._a = a
        self._b = b

    def execute(self) -> None:
        self._report.max_Category_Date(self._a, self._b)

class ComplexCategoryMinDate(Command):
    def __init__(self, report: Report, a: object, b: object) -> None:
        self._report = report
        self._a = a
        self._b = b

    def execute(self) -> None:
        self._report.min_Category_Date(self._a, self._b)

class ComplexCategoryMax(Command):
    def __init__(self, report: Report) -> None:
        self._report = report
    def execute(self) -> None:
        self._report.category_Max()

class ComplexCategoryMin(Command):
    def __init__(self, report: Report) -> None:
        self._report = report
    def execute(self) -> None:
        self._report.category_Min()

class ComplexMaxInPeriod(Command):
    def __init__(self, report: Report, a: object, b: object) -> None:
        self._report = report
        self._a = a
        self._b = b

    def execute(self) -> None:
        self._report.max_In_Period(self._a, self._b)

class ComplexMinInPeriod(Command):
    def __init__(self, report: Report, a: object, b: object) -> None:
        self._report = report
        self._a = a
        self._b = b
    def execute(self) -> None:
        self._report.min_In_Period(self._a, self._b)



class Category:
    categoryList = []
    def __init__(self, nameCategory):
        self._nameCategory = nameCategory
        return

    def __str__(self):
        with open("Category List.txt", "a") as activity:
            activity = activity.writelines("")
        self.printList = []
        with open("Category List.txt", "r") as listCategory:
            listCategory = listCategory.readlines()
            for cat in listCategory:
                self.printList.append(cat[:-1])
        return self.printList

    def add_Category(self, addCategory):
        with open("Category List.txt", "r") as listCategory:
            listCategory = listCategory.readlines()
        for cat in listCategory:
            self.categoryList.append(cat[:-1])
        if addCategory not in self.categoryList:
            self._nameCategory = addCategory
            self.categoryList.append(self._nameCategory)
            with open("Category List.txt", "a") as listCategory:
                print(self._nameCategory, file=listCategory)
        return

    def add_Category_File(self, addCategory):
        with open("Category List.txt", "a") as activity:
            activity = activity.writelines("")
        with open("Category List.txt", "r") as listCategory:
            listCategory = listCategory.readlines()
        for cat in listCategory:
            self.categoryList.append(cat[:-1])
        if addCategory not in self.categoryList:
            self._nameCategory = addCategory
            with open(str(self._nameCategory) + ".txt", "a") as newCategory:
                newCategory = newCategory.writelines(f" \t\t\tКатегорія: {self._nameCategory}\n\n")
            with open(str(self._nameCategory) + ".txt", "r") as test:
                test.close()
            print("Категорію  >>>", self._nameCategory, "<<<  створено!")
        return

    def del_Category(self, del_Category):
        self.delCategoryList = []
        with open("Category List.txt", "r") as listCategory:
            listCategory = listCategory.readlines()
        for cat in listCategory:
            self.delCategoryList.append(cat[:-1])
        if del_Category in self.delCategoryList:
            os.remove(str(del_Category) + ".txt")
            os.remove("Category List.txt")
            self.delCategoryList.remove(del_Category)
            for cat in self.delCategoryList:
                with open("Category List.txt", "a") as newlistCategory:
                    print(cat, file=newlistCategory)
            return print("Категорія >>> {} <<<  ВИДАЛЕНА ! ... \n".format(del_Category))
        else:
            return print("Категорію  >>> {} <<<  не було створено раніше!...\n".format(del_Category))

class Expense:
    def __init__(self, nameCategory, nameExpense,  price, date):
        self._nameCategory = nameCategory
        self._nameExpense = nameExpense
        self._date = date
        self._price = price
        self.dictExpense = {}
        self.listCategory = []
        return

    def add_Expense(self, nameCategory, nameExpense, price, date):
        self.dictExpense[self._nameCategory] = self._nameExpense, self._price, self._date
        self._nameCategory = nameCategory
        self._nameExpense = nameExpense
        self._date = date
        self._price = price
        return

    def __str__(self):
        return f"Витрата створена: \t\t{self._nameExpense}, \t{self._price} грн, \t{self._date}"

    def save_Expense(self, addCategory):
        with open("Category List.txt", "r") as fileCategory:
            fileCategory = fileCategory.readlines()
            for category in fileCategory:
                self.listCategory.append(category[:-1])
        if addCategory not in self.listCategory:
            with open(str(addCategory) + ".txt", "a") as addCat:
                addCat = addCat.writelines(f"\t\t\t\tКатегорія :   {self._nameCategory}\n\n"
                                                    f"Витрата:\t\t{self._nameExpense},"
                                                    f"\t\t{self._price} грн,\t\t{self._date}\n")
        else:
            with open(str(addCategory) + ".txt", "a") as addCat:
                addCat = addCat.writelines(f"Витрата:\t\t{self._nameExpense},"
                                                    f"\t\t{self._price} грн,\t\t{self._date}\n")
        print("Витрата  >>", self._nameExpense, "<<  додана!")

class Report:
    reportListDate = []
    def __init__(self, findNameCategory):
        self.reportListDate = []
        self._findNameCategory = findNameCategory

    def show_Report_Category(self, findNameCategory):
        self._findNameCategory = findNameCategory
        with open("Category List.txt", "r") as catList:
            catList = catList.readlines()
        for cat in catList:
            self.reportListDate.append(cat[:-1])
        if self._findNameCategory in self.reportListDate:
            print(self._findNameCategory)
            with open(str(self._findNameCategory) + ".txt", "r") as findFile:
                findFile = findFile.readlines()
        for elem in findFile:
            print(elem)

    def show_Report_Expense(self, findNameCategory, findNameExpense):
        self._findNameCategory = findNameCategory
        self._findNameExpense = findNameExpense
        with open("Category List.txt", "r") as catList:
            catList = catList.readlines()
        if self._findNameCategory + "\n" in catList:
            with open(str(self._findNameCategory) + ".txt", "r") as findCat:
                findCat = findCat.readlines()
            for elem in findCat:
                exp = elem.split(",")
                if exp[0] == "Витрата:\t\t" + self._findNameExpense:
                    print(elem)

    def show_Date_Expense(self, date):
        self._date = date
        self.charList = []
        self.word = ""
        with open("Category List.txt", "r") as catList:
            catList = catList.readlines()
        for cat in catList:
            with open(str(cat[:-1]) + ".txt", "r") as categ:
                categ = categ.readlines()
                for pos in categ[2::]:
                    possplit = pos.split(",")
                    if possplit[2] == "\t\t" + self._date.strftime("%Y-%m-%d") + "\n":
                        for elem in possplit:
                            for char in elem:
                                char.replace("\t", "   ")
                                self.word += char
        if self.word == "":
            print("\nВитрати в таку дату немає. ")
        else:
            print(self.word)

    def max_Category_Date(self, dateStart, dateFinish):
        self._dateStart = dateStart
        self._dateFinish = dateFinish
        delta = timedelta(days=1)
        period = []

        while self._dateStart <= self._dateFinish:
            period.append(self._dateStart.strftime('%Y-%m-%d'))
            self._dateStart += delta
        with open("Category List.txt", "r") as catList:
            catList = catList.readlines()
        for cat in catList:
            with open(str(cat[:-1]) + ".txt", "r") as categ:
                categ = categ.readlines()
                numExpense = []
                for date in period:
                    for pos in categ[2::]:
                        possplit = pos.split(",")
                        if possplit[2] == "\t\t" + date + "\n":
                            num = possplit[1]
                            n = float(num[2:-4])
                            numExpense.append(n)
                if numExpense != []:
                    maxExpense = max(numExpense)
                    print("\Категорія:\t", str(cat[:-1]), "\t", possplit[0], "\t\tМаксимальна сума витрати за цей період =  ",
                          maxExpense, "  грн")

    def min_Category_Date(self, dateStart, dateFinish):
        self._dateStart = dateStart
        self._dateFinish = dateFinish
        delta = timedelta(days=1)
        period = []

        while self._dateStart <= self._dateFinish:
            period.append(self._dateStart.strftime('%Y-%m-%d'))
            self._dateStart += delta
        with open("Category List.txt", "r") as catList:
            catList = catList.readlines()
        for cat in catList:
            with open(str(cat[:-1]) + ".txt", "r") as categ:
                categ = categ.readlines()
                numExpense = []
                for date in period:
                    for pos in categ[2::]:
                        possplit = pos.split(",")
                        if possplit[2] == "\t\t" + date + "\n":
                            num = possplit[1]
                            n = float(num[2:-4])
                            numExpense.append(n)
                if numExpense != []:
                    maxExpense = min(numExpense)
                    print("\nКатегорія:\t", str(cat[:-1]), "\t", possplit[0],
                          "\t\tМінімальна сума витрати за цей період =  ",
                          maxExpense, "  грн")

    def category_Max(self):
        with open("Category List.txt", "r") as catList:
            catList = catList.readlines()
        for cat in catList:
            with open(str(cat[:-1]) + ".txt", "r") as categ:
                categ = categ.readlines()
                numExpense = []
                for pos in categ[2::]:
                    possplit = pos.split(",")
                    num = possplit[1]
                    n = float(num[2:-4])
                    numExpense.append(n)
                if numExpense != []:
                    maxExpense = max(numExpense)
                    print("Категорія:\t", str(cat[:-1]), "\t\tМаксимальна сума витрати в категорії =  ",
                          maxExpense, "  грн",  "\t\t", possplit[0],)

    def category_Min(self):
        with open("Category List.txt", "r") as catList:
            catList = catList.readlines()
        for cat in catList:
            with open(str(cat[:-1]) + ".txt", "r") as categ:
                categ = categ.readlines()
                numExpense = []
                for pos in categ[2::]:
                    possplit = pos.split(",")
                    num = possplit[1]
                    n = float(num[2:-4])
                    numExpense.append(n)
                if numExpense != []:
                    minExpense = min(numExpense)
                    print("Категорія:\t", str(cat[:-1]), "\t\tМінімальна сума витрати в категорії =  ",
                          minExpense, "  грн",  "\t\t", possplit[0],)

    def max_In_Period(self, dateStart, dateFinish):
        self._dateStart = dateStart
        self._dateFinish = dateFinish
        delta = timedelta(days=1)
        period = []
        numExpense = []
        while self._dateStart <= self._dateFinish:
            period.append(self._dateStart.strftime('%Y-%m-%d'))
            self._dateStart += delta
        with open("Category List.txt", "r") as catList:
            catList = catList.readlines()
        for cat in catList:
            with open(str(cat[:-1]) + ".txt", "r") as categ:
                categ = categ.readlines()
                for date in period:
                    for pos in categ[2::]:
                        possplit = pos.split(",")
                        if possplit[2] == "\t\t" + date + "\n":
                            num = possplit[1]
                            n = float(num[2:-4])
                            numExpense.append(n)
                    if numExpense != []:
                        maxExpense = max(numExpense)
                        print("\n\tМаксимальна сума витрати за період ", dateStart, "-", dateFinish, " = ",
                              maxExpense, " грн", "\t___ ", possplit[0])

    def min_In_Period(self, dateStart, dateFinish):
        self._dateStart = dateStart
        self._dateFinish = dateFinish
        delta = timedelta(days=1)
        period = []
        numExpense = []
        while self._dateStart <= self._dateFinish:
            period.append(self._dateStart.strftime('%Y-%m-%d'))
            self._dateStart += delta
        with open("Category List.txt", "r") as catList:
            catList = catList.readlines()
        for cat in catList:
            with open(str(cat[:-1]) + ".txt", "r") as categ:
                categ = categ.readlines()
                for date in period:
                    for pos in categ[2::]:
                        possplit = pos.split(",")
                        if possplit[2] == "\t\t" + date + "\n":
                            exp = possplit[0].replace("\t", " ")
                            num = possplit[1]
                            n = float(num[2:-4])
                            numExpense.append(n)
                    if numExpense != []:
                        minExpense = min(numExpense)
                        print("\n\tМінімальна сума витрати за період ", dateStart, "-", dateFinish, " = ",
                              minExpense, " грн", "\t___ ", exp)

class Invoker:
    def __init__(self):  # Сброс команд
        self.reset_commands()

    def reset_commands(self):
        self._name_category = None
        self._add_expense = None
        self._del_category = None
        self._report_category = None
        self._report_expense = None
        self._report_date = None
        self._report_max_category_date = None
        self._report_min_category_date = None
        self._report_category_max = None
        self._report_category_min = None
        self._report_max_In_Period = None
        self._report_min_In_Period = None

    def set_name_category(self, command: Command):
        self._name_category = command
    def set_add_expense(self, command: Command):
        self._add_expense = command
    def set_del_category(self,command: Command):
        self._del_category = command
    def set_report_category(self, command: Command):
        self._report_category = command
    def set_report_expense(self, command: Command):
        self._report_expense = command
    def set_report_date(self, command: Command):
        self._report_date = command
    def set_report_max_date(self, command: Command):
        self._report_max_category_date = command
    def set_report_min_date(self, command: Command):
        self._report_min_category_date = command
    def set_report_category_max(self, command: Command):
        self._report_category_max = command
    def set_report_category_min(self, command: Command):
        self._report_category_min = command
    def set_report_max_In_Period(self, command: Command):
        self._report_max_In_Period = command
    def set_report_min_In_Period(self, command: Command):
        self._report_min_In_Period = command

    def do_something_important(self) -> None:

        if isinstance(self._name_category, Command):
            self._name_category.execute()
        if isinstance(self._add_expense, Command):
            self._add_expense.execute()
        if isinstance(self._del_category, Command):
            self._del_category.execute()
        if isinstance(self._report_category, Command):
            self._report_category.execute()
        if isinstance(self._report_expense, Command):
            self._report_expense.execute()
        if isinstance(self._report_date, Command):
            self._report_date.execute()
        if isinstance(self._report_max_category_date, Command):
            self._report_max_category_date.execute()
        if isinstance(self._report_min_category_date, Command):
            self._report_min_category_date.execute()
        if isinstance(self._report_category_max, Command):
            self._report_category_max.execute()
        if isinstance(self._report_category_min, Command):
            self._report_category_min.execute()
        if isinstance(self._report_max_In_Period, Command):
            self._report_max_In_Period.execute()
        if isinstance(self._report_min_In_Period, Command):
            self._report_min_In_Period.execute()

        return


if __name__ == "__main__":
    invoker = Invoker()
    report = Report("")

    while True:
        print(f'''\n------------------------------------------------------
                            
                            ЗВІТ ВИТРАТ

                    ДОДАТИ КАТЕГОРІЮ ВИТРАТ -------------->  1
                    ВИДАЛИТИ КАТЕГОРІЮ ВИТРАТ  ----------->  2

                    ДОДАТИ ВИТРАТУ ----------------------->  3

                    ПОДИВИТИСЬ ЗВІТ: --------------------->  4  \n''')


        change = input("Введіть сюди номер обраного пункту (1-4): --->>>>  ")
        if not "0" < change < "5":
            print("\n\t\t\tВИ ВВЕЛИ НЕКОРЕКТНЕ ЗНАЧЕННЯ, СПРОБУЙТЕ ЩЕ РАЗ!!!")
        if change == "1":
            print("Ви обрали ДОДАВАННЯ КАТЕГОРІЇ.\n")
            invoker.reset_commands()
            new_Name_Category = input("Введіть назву нової категорії: ")
            category = Category(new_Name_Category)
            invoker.set_name_category(ComplexAddCategory(
                category, new_Name_Category))
            invoker.do_something_important()

        if change == "2":
            invoker.reset_commands()
            print("Ви обрали ВИДАЛЕННЯ КАТЕГОРІЇ.\n")
            category = Category(None)
            name_Del_Category = input("Введіть назву категорії для видалення: ")
            invoker.set_del_category(ComplexDeleteCategory(category, name_Del_Category))
            invoker.do_something_important()

        if change == "3":
            print("Ви обрали ДОДАВАННЯ ВИТРАТИ.\n")
            invoker.reset_commands()
            new_Name_Category = input("Введіть назву КАТЕГОРІЇ: ")
            new_Name_Expense = input("Введіть нову ВИТРАТУ: ")
            price = float(input("Введіть СУМУ витрати: "))
            day = int(input("ДЕНЬ витрати:  -->"))
            month = int(input("МІСЯЦЬ витрати:  -->"))
            year = int(input("РІК витрати:  -->"))
            date_Expense = datetime(year, month, day).date()
            expense = Expense(new_Name_Category, new_Name_Expense, price, date_Expense)
            category = Category(new_Name_Category)
            invoker.set_name_category(ComplexAddCategory(
                category, new_Name_Category))
            invoker.set_add_expense(ComplexAddExpens(
                expense, new_Name_Category, new_Name_Expense, price, date_Expense))
            invoker.do_something_important()
        if change == "4":
            print("\nРОЗДІЛ << ЗВІТ >>.\n")

            print(f'''            1 ---  ЗА ДАТОЮ      
            2 ---  ЗА НАЗВОЮ
            3 ---  ЗА КАТЕГОРІЄЮ
            4 ---  ВІДОБРАЖЕННЯ МАКСИМАЛЬНОЇ ВИТРАТИ В КОЖНІЙ КАТЕГОРІЇ
            5 ---  ВІДОБРАЖЕННЯ МАКСИМАЛЬНОЇ ВИТРАТИ У ВКАЗАНОМУ ПЕРІОДІ
            6 ---  ВІДОБРАЖЕННЯ МІНІМАЛЬНОЇ ВИТРАТИ В КОЖНІЙ КАТЕГОРІЇ
            7 ---  ВІДОБРАЖЕННЯ МІНІМАЛЬНОЇ ВИТРАТИ У ВКАЗАНОМУ ПЕРІОДІ \n''')

            choice = input("Введіть сюди номер обраного пункту (1-7): --->>>>  ")
            if not "0" < change < "8":
                print("\n\t\t\tВИ ВВЕЛИ НЕКОРЕКТНЕ ЗНАЧЕННЯ, СПРОБУЙТЕ ЩЕ РАЗ!!!")
            if choice == "1":
                print("Ви обрали ЗВІТ ЗА ДАТОЮ.\n")
                invoker.reset_commands()
                dayReport = int(input("ДЕНЬ звіту:  -->"))
                monthReprt = int(input("МІСЯЦЬ звіту:  -->"))
                yearReport = int(input("РІК звіту:  -->"))
                date_Expenseed = datetime(yearReport, monthReprt, dayReport).date()
                invoker.set_report_date(ComplexReportDate(report, date_Expenseed))
                invoker.do_something_important()
            if choice == "2":
                print("Ви обрали ЗВІТ ЗА НАЗВОЮ ВИТРАТИ.\n")
                invoker.reset_commands()
                findNameCategory = input("Введіть назву категорії для звіту:     ")
                findNameExpense = input("Введіть назву витрати для звіту:     ")
                invoker.set_report_expense(ComplexReportExpens(report, findNameCategory, findNameExpense ))
                invoker.do_something_important()
            if choice == "3":
                print("Ви обрали ЗВІТ ЗА КАТЕГОРІЄЮ.\n")
                invoker.reset_commands()
                findName = input(" Введіть назву витрати для звіту:   ")
                invoker.set_report_category(ComplexReportCategory(report, findName))
                invoker.do_something_important()
            if choice == "4":
                print("ВІДОБРАЖЕННЯ МАКСИМАЛЬНОЇ ВИТРАТИ В КОЖНІЙ КАТЕГОРІЇ\n")
                invoker.reset_commands()
                invoker.set_report_category_max(ComplexCategoryMax(report))
                invoker.do_something_important()
            if choice == "5":
                print("ВІДОБРАЖЕННЯ МАКСИМАЛЬНОЇ ВИТРАТИ У ВКАЗАНОМУ ПЕРІОДІ\n")
                invoker.reset_commands()
                day_Start_Expens = int(input("Введіть ДЕНЬ ПОЧАТКУ періоду звіту: "))
                month_Start_Expens = int(input("Введіть МІСЯЦЬ ПОЧАТКУ періоду звіту: "))
                year_Start_Expens = int(input("Введіть РІК ПОЧАТКУ періоду звіту: "))
                print()
                day_Finish_Expens = int(input("Введіть ДЕНЬ КІНЦЯ періоду звіту: "))
                month_Finish_Expens = int(input("Введіть МІСЯЦЬ КІНЦЯ періоду звіту: "))
                year_Finish_Expens = int(input("Введіть РІК КІНЦЯ періоду звіту: "))
                date_Expense_Start = datetime(year_Start_Expens, month_Start_Expens, day_Start_Expens).date()
                date_Expense_Finish = datetime(year_Finish_Expens, month_Finish_Expens, day_Finish_Expens).date()
                invoker.set_report_max_date(ComplexCategoryMaxDate(report, date_Expense_Start, date_Expense_Finish))
                invoker.do_something_important()
            if choice == "6":
                print("ВІДОБРАЖЕННЯ МІНІМАЛЬНОЇ ВИТРАТИ В КОЖНІЙ КАТЕГОРІЇ\n")
                invoker.reset_commands()
                invoker.set_report_category_min(ComplexCategoryMin(report))
                invoker.do_something_important()
            if choice == "7":
                print("ВІДОБРАЖЕННЯ МІНІМАЛЬНОЇ ВИТРАТИ У ВКАЗАНОМУ ПЕРІОДІ\n")
                invoker.reset_commands()
                day_Start_Expens = int(input("Введіть ДЕНЬ ПОЧАТКУ періоду звіту: "))
                month_Start_Expens = int(input("Введіть МІСЯЦЬ ПОЧАТКУ періоду звіту: "))
                year_Start_Expens = int(input("Введіть РІК ПОЧАТКУ періоду звіту: "))
                print()
                day_Finish_Expens = int(input("Введіть ДЕНЬ КІНЦЯ періоду звіту: "))
                month_Finish_Expens = int(input("Введіть МІСЯЦЬ КІНЦЯ періоду звіту: "))
                year_Finish_Expens = int(input("Введіть РІК КІНЦЯ  періоду звіту: "))
                date_Expense_Start = datetime(year_Start_Expens, month_Start_Expens, day_Start_Expens).date()
                date_Expense_Finish = datetime(year_Finish_Expens, month_Finish_Expens, day_Finish_Expens).date()
                invoker.set_report_min_date(ComplexCategoryMinDate(report, date_Expense_Start, date_Expense_Finish))
                invoker.do_something_important()









