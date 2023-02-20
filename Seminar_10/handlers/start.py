from loader import dp
from aiogram.types import Message
import game


@dp.message_handler(commands=['start'])
async def mes_start(message: Message):
    for duel in game.total:
        if message.from_user.id == duel[0]:
            await message.answer('Ты уже начал игру! Играй давай!')
            break
    else:
        await message.answer(f'Привет, {message.from_user.full_name}')
        await message.answer(f'Мы будем играть в конфеты, тебе нужно установить макс кол-во конфет...')
        my_game = [message.from_user.id, message.from_user.first_name, None]
        game.total.append(my_game)

