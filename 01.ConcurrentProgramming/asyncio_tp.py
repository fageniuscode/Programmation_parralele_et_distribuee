import asyncio

async def main():
    print("Hello world!")
    await asyncio.sleep(2)
    print("Goodbye world!")

asyncio.run(main())

# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())
# loop.close()