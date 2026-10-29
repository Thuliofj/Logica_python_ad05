import datetime
import calendar
from babel.dates import format_date



meses = [
    "Janeiro",
    "Fevereiro",
    "Março",
    "Abril",
    "Maio",
    "Junho",
    "Julho",
    "Agosto",
    "Setembro",
    "Outubro",
    "Novembro",
    "Dezembro"
]

#21/12/2024
data = datetime.date(2024, 12, 21)

print (data)

dias_semana =  [
    "segunda-feira", 
    "terça-feira", 
    "quarta-feira", 
    "quinta-feira",
    "sexta-feira", 
    "sábado", 
    "domingo"
    ]

hoje = datetime.date.today()

print(hoje)
print(hoje.strftime("%d/%m/%Y"))
print(f"São Paulo, {dias_semana[hoje.weekday()]}, {hoje.day} de {meses[hoje.month - 1]} de {hoje.year}")

data_extenso = format_date(hoje, format='long', locale='pt_br')
print(data_extenso)

print(f"2027 é bissexto?: {calendar.isleap(2027)}")

print(f"é o ultimo dia do mês? {calendar.monthrange(2026, 10)[1]}")