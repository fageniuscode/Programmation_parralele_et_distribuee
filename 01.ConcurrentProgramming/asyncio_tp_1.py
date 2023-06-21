import asyncio
import time

async def display_time():
    start_time = time.time()

    while True:
        dur = int(time.time() - start_time)

        if dur % 3 == 0:
            print("{} seconds have passed".format(dur))

        await asyncio.sleep(1)

async def print_nums():
    num = 1

    while True:
        print(num)
        num += 1
        await asyncio.sleep(0.1)

async def main():
    task1 = asyncio.create_task(display_time())  # Création de la tâche pour afficher le temps
    task2 = asyncio.create_task(print_nums())  # Création de la tâche pour afficher les nombres

    await asyncio.gather(task1, task2)  # Exécution des deux tâches en parallèle

# asyncio.run(main())  # Exécution de la fonction principale avec asyncio (version Python 3.7+)

loop = asyncio.get_event_loop()  # Obtention de la boucle d'événements asyncio
loop.run_until_complete(main())  # Exécution de la boucle jusqu'à la fin de la fonction principale
loop.close()  # Fermeture de la boucle d'événements
