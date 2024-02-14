from NIM_enigine import put_stones, get_bunches, take_from_bunch, is_game_over
from termcolor import cprint, colored


put_stones()
user_number = 1
while True:
    cprint('Текущая позиция', color='green')
    cprint(get_bunches(), color='green')
    
    user_color = "blue" if user_number == 1 else 'yellow'
    cprint(f'Ход игрока {user_number}', color=user_color)
    pos = int(input(colored('Откуда берем?', color=user_color)))
    qua = int(input(colored('Сколько берем?', color=user_color)))
    if qua > get_bunches()[pos-1]:
        print('Здесь нет столько камней')
        continue
    take_from_bunch(position=pos,quantity=qua)
    if is_game_over():
        break
    user_number = 2 if user_number == 1 else 1

cprint(f'Выйграл игрок номер {user_number}')