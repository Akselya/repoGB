t = int(input('duration = '))
d, h, m, s = t // 86400, t // 3600 % 24, t // 60 % 60, t % 60

print(f'{d} дней {h} час {m} мин {s} cек')


