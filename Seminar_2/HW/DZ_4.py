# Задача4.Посчитайчужуюзарплату... Бухгалтерусталапостоянносчитатьвручнуюсреднегодовуюзарплату сотрудниковкомпаниии,
# чтобыоблегчитьсебежизнь,обратиласьк программисту. Напишитепрограмму,котораяпринимаетотпользователязарплатусотрудника 
# закаждыйиз12месяцевивыводитнаэкрансреднююзарплатузагод.
SumZP=0
for i in range(1,13):
  zp = float(input(f"Введите зарплату сотрудника за {i}-й месяц: "))
  SumZP+=zp
srZP=round(SumZP/12,2)
print(f"Средняя зарплата сотрудника за год будет равна = {srZP} ")