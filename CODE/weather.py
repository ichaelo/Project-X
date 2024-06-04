import asyncio  # Импортируем модуль для асинхронного программирования
import requests  # Импортируем модуль для выполнения HTTP-запросов
from aiogram import Bot, Dispatcher, types, F  # Импортируем необходимые классы из aiogram для создания телеграм-бота
from aiogram.filters.command import Command  # Импортируем фильтр для команд


# Задаем токены для телеграм-бота и для API погоды
TG_TOKEN = '6835958323:AAGzZgYsW1fP-XIY6RKwbDjitmNTu9XheBc'
WEATHER_TOKEN = 'ee7df615ccbb79fceec65c96e6392d88'

# Создаем экземпляр бота и диспетчера
bot = Bot(TG_TOKEN)
dp = Dispatcher()

# Список погодных условий, которые бот сможет распознать
weather_list = ('Clouds', 'Clear', 'Atmosphere', 'Snow', 'Rain', 'Drizzle', 'Thunderstorm')

# Обработчик команды /start
@dp.message(Command('start'))
async def start_command(message: types.Message):
    # Ответ бота на команду /start
    await message.answer('Привет! Для того чтобы получить информацию о погоде, напиши название города.')

# Обработчик текстовых сообщений
@dp.message(F.text)
async def get_weather(message: types.Message):
    city = message.text  # Извлекаем название города из сообщения
    try:
        # Формируем URL для запроса к API погоды
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=ru&appid={WEATHER_TOKEN}'
        weather_data = requests.get(url).json()  # Выполняем запрос и получаем данные в формате JSON

        # Извлекаем необходимые данные из ответа API
        temperature = weather_data['main']['temp']
        temperature_feels = weather_data['main']['feels_like']
        wind_speed = weather_data['wind']['speed']
        cloud_cover = weather_data['weather'][0]['description']
        humidity = weather_data['main']['humidity']

        # Проверяем погодное условие и отправляем соответствующее сообщение
        if weather_data['weather'][0]['main'] == 'Clouds':
            await message.answer(f'Город: {city} \n'
                                 f'Температура воздуха: {temperature}℃ 🌡\n'
                                 f'Ощущается как: {temperature_feels}℃ 🌡\n'
                                 f'Ветер: {wind_speed} м/с 💨\n'
                                 f'Облачность: {cloud_cover} 🌤\n'
                                 f'Влажность: {humidity}% 💧\n'
                                 f"\n"
                                 f'Вероятны осадки в виде тефтелей, задумайтесь о том чтобы взять зонтик! ☔️')

        elif weather_data['weather'][0]['main'] == 'Clear':
            await message.answer(f'Город: {city} \n'
                                 f'Температура воздуха: {temperature}℃ 🌡\n'
                                 f'Ощущается как: {temperature_feels}℃ \n'
                                 f'Ветер: {wind_speed} м/с 💨\n'
                                 f'Облачность: {cloud_cover} ☀️\n'
                                 f'Влажность: {humidity}% 💧\n'
                                 f"\n"
                                 f'Самое время выйти на прогулку 🧑🏻‍🦽')

        elif weather_data['weather'][0]['main'] == 'Atmosphere':
            await message.answer(f'Город: {city} \n'
                                 f'Температура воздуха: {temperature}℃ 🌡\n'
                                 f'Ощущается как: {temperature_feels}℃ 🌡\n'
                                 f'Ветер: {wind_speed} м/с 💨\n'
                                 f'Облачность: {cloud_cover} 🌪\n'
                                 f'Влажность: {humidity}% 💧\n'
                                 f"\n"
                                 f'Возможно стоит остаться дома, кто знает что тебя там ждет? 😶‍🌫️')

        elif weather_data['weather'][0]['main'] == 'Snow':
            await message.answer(f'Город: {city} \n'
                                 f'Температура воздуха: {temperature}℃ 🌡\n'
                                 f'Ощущается как: {temperature_feels}℃ 🌡\n'
                                 f'Ветер: {wind_speed} м/с 💨\n'
                                 f'Облачность: {cloud_cover} ❄️\n'
                                 f'Влажность: {humidity}% 💧\n'
                                 f"\n"
                                 f'Кажется на улице идет снег, пора пойти и слепить снеговика! ☃️')

        elif weather_data['weather'][0]['main'] == 'Rain':
            await message.answer(f'Город: {city} \n'
                                 f'Температура воздуха: {temperature}℃ 🌡\n'
                                 f'Ощущается как: {temperature_feels}℃ 🌡\n'
                                 f'Ветер: {wind_speed} м/с 💨\n'
                                 f'Облачность: {cloud_cover} 🌧\n'
                                 f'Влажность: {humidity}% 💧\n'
                                 f"\n"
                                 f'Кажется нас скоро затопит, пока не поздно запасайтесь припасами и покупайте лодку! 🤿')

        elif weather_data['weather'][0]['main'] == 'Drizzle':
            await message.answer(f'Город: {city} \n'
                                 f'Температура воздуха: {temperature}℃ 🌡\n'
                                 f'Ощущается как: {temperature_feels}℃ 🌡\n'
                                 f'Ветер: {wind_speed} м/с 💨\n'
                                 f'Облачность: {cloud_cover} 🌨\n'
                                 f'Влажность: {humidity}% 💧\n'
                                 f"\n"
                                 f'Пока не поздно, стоит купить дождевик! 🎈')

        elif weather_data['weather'][0]['main'] == 'Thunderstorm':
            await message.answer(f'Город: {city} \n'
                                 f'Температура воздуха: {temperature}℃ 🌡\n'
                                 f'Ощущается как: {temperature_feels}℃ 🌡\n'
                                 f'Ветер: {wind_speed} м/с 💨\n'
                                 f'Облачность: {cloud_cover} 🌨\n'
                                 f'Влажность: {humidity}% 💧\n'
                                 f"\n"
                                 f'Может ну его эти шоколадки из магазина, лучше оставайтесь дома и смотрите сериалы! 🍿📺')

        elif weather_data['weather'][0]['main'] not in weather_list:
            await message.answer(f'Город: {city} \n'
                                 f'Температура воздуха: {temperature}℃ 🌡\n'
                                 f'Ощущается как: {temperature_feels}℃ 🌡\n'
                                 f'Ветер: {wind_speed} м/с 💨\n'
                                 f'Облачность: {cloud_cover} ☀️\n'
                                 f'Влажность: {humidity}% 💧\n')

    except KeyError:
        # Отправляем сообщение об ошибке, если город не найден
        await message.answer(f'Не удалось определить город: {city}')

# Основная функция для запуска бота
async def main():
    await bot.delete_webhook(drop_pending_updates=True)  # Удаляем вебхук и обрабатываем накопившиеся обновления
    await dp.start_polling(bot)  # Запускаем опрос

if __name__ == '__main__':
    asyncio.run(main())  # Запускаем основную функцию