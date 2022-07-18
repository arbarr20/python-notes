import asyncio
import logging
logging.basicConfig(level=logging.DEBUG, format='%(threadName)s: %(message)s',)

def func(x, y):
    logging.info(f"func x{x}+y{y}")
    return x + y

@asyncio.coroutine
def do_func(x, y):
    logging.info(f"do_func x{x},y{y}")
    yield from asyncio.sleep(1)
    logging.info(f"Ddo_func x{x},y{y}")
    return func(x, y)

loop = asyncio.get_event_loop()
result = loop.run_until_complete(do_func(2,3))
logging.info(f"result {result}")

