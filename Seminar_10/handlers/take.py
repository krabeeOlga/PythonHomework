import random
from loader import dp
from aiogram.types import Message
import game


@dp.message_handler()
async def mes_help(message: Message):
    for duel in game.total:
        if message.from_user.id == duel[0]:
            if duel[2] == None:
                await check_set_max_count(message, duel)
                return
            count = message.text
            name = message.from_user.first_name
            if count.isdigit() and 0 < int(count) < 29:
                duel[2] -= int(count)
                if await check_win(message, 'Ты', duel):
                    return True
                await message.answer(f'{duel[1]} взял {count} конфет и на столе осталось {duel[2]}\n'
                                    f'Теперь ход бота...')
                bot_take = random.randint(1, 28) if duel[2] > 28 else duel[2]
                duel[2] -= bot_take
                if await check_win(message, 'Бот', duel):
                    return True
                await message.answer(f'Бот Виталий взял {bot_take} конфет и '
                                        f'на столе осталось {duel[2]}\n'
                                        f'Теперь твой ход...')
            else: 
                await message.answer(f'Введите число от 1 до 28')


async def check_win(message: Message, win: str, total: list):
    if total[2] <= 0:
        await message.answer(f'{win} победил! Поздравляю!')
        game.total.remove(total)
        return True
    return False

async def check_set_max_count(message: Message, total: list):
    if message.text.isdigit() == False:
        await message.answer('Чтобы начать тебе нужно установить макс кол-во конфет...')
        return False

    total[2] = int(message.text)
    await message.answer('Начинаем, теперь бери от 1 до 28...')
    return True


                
