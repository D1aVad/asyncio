import asyncio
from random import randint

# Функция для имитации поднятия шара
async def lift_ball(name, power, ball_number):
    print(f'Силач {name} поднял {ball_number} шар')
    await asyncio.sleep(randint(1, 10) / power)  # Задержка обратно пропорциональна силе

# Асинхронная функция для начала соревнований силача
async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования')
    for ball_number in range(1, 6):
        await lift_ball(name, power, ball_number)
    print(f'Силач {name} закончил соревнования')

# Асинхронная функция для запуска турнира
async def start_tournament():
    names = ['Pasha', 'Denis', 'Apollon']
    powers = [3, 4, 5]
    tasks = []
    for name, power in zip(names, powers):
        task = asyncio.create_task(start_strongman(name, power))
        tasks.append(task)
    await asyncio.gather(*tasks)

# Запуск турнира
asyncio.run(start_tournament())