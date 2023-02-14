from loader import dp, bot
from aiogram import types
from random import randint as RI

total = 150
limit = 28
player = None
game_over = False

@dp.message_handler(commands=['start'])
async def mes_start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.first_name}! '
                         f'Давненько тебя не видел')

@dp.message_handler(commands=['OOP','oop'])
async def mes_oop(message: types.Message):
    await message.answer('Да что вы говорите')


@dp.message_handler(commands=['game'])
async def mes_game(message: types.Message):
    global total
    global player
    global game_over
    game_over = False
    # count = message.text.split()[1]
    total = int(RI(150, 200))
    await message.answer(f'Для игры выдано {total} конфет.')

    player, msg = first_move()
    await message.answer(msg)
    if player == 'human':
        await message.answer(f'Первым ходит: {message.from_user.first_name}')
    else:
        await message.answer(f'Первым ходит: {player}')

    await bot_move(message)

@dp.message_handler(text = ['лох'])
async def mes_loh(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    await message.answer('Так у нас говорить нельзя')

@dp.message_handler()
async def mes_all(message: types.Message):
    global total
    global limit
    global player
    global game_over

    if game_over == True:
        return await bot.send_message(message.from_user.id, 'Чтобы начать новую игру введи команду: /game')

    if message.text.isdigit() == False:
        await message.answer(f'Гляди, че поймал - {message.text}')
        return await bot.send_message(message.from_user.id, 'Введи-ка ты число')
    
    num = int(message.text)
    if 0 >= num or num > limit:
        return await bot.send_message(message.from_user.id, f'Так нельзя, надо брать от 1 до {limit} конфет')
    
    await get_total(message, num)
    
    if limit >= total:
        game_over = True
        await bot.send_message(message.from_user.id, f'Игра окончена! Победил игрок {next_move(player)}!')
        return await bot.send_message(message.from_user.id, 'Сыграем еще раз?: /game')

    player = next_move(player)        
    await bot_move(message)


def first_move():
    a = ['human', 'bot']
    message = 'Решаем кто будет первым ходить...'
    return a[RI(0, 1)], message

def next_move(player):
    if player == 'human':
        player = 'bot'
    else:
        player = 'human'
    return player

async def bot_move(message):
    global player
    global total
    global limit
    if player == 'bot':
        num = total % (limit + 1)
        if num == 0:
            num = limit
        await bot.send_message(message.from_user.id, f'бот берет {num} конфет')        
        await get_total(message, num)

        player = next_move(player)
        await bot.send_message(message.from_user.id, f'Ваш ход, сколько конфет берете?')

async def get_total(message, num):    
    global total
    total -= num
    await bot.send_message(message.from_user.id, f'Конфет на столе осталось 'f'- {total}')
    