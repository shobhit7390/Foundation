# AsyncIO in Python
# It mainly helps in parallel execution of functions

import time
import asyncio

import requests

async def func1():
    url = 'https://images.unsplash.com/photo-1678937410711-7129616be1ba?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2070&q=80'
    r = requests.get(url, allow_redirects=True)
    open('img1.jpg', 'wb').write(r.content)
    print("Function 1")
    return "Hello User 1"

async def func2():
    url = 'https://images.unsplash.com/photo-1678931884462-312c820d3e67?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1931&q=80'
    r = requests.get(url, allow_redirects=True)
    open('img2.jpg', 'wb').write(r.content)
    print("Function 2")
    return "Hello User 2"

async def func3():
    url = 'https://images.unsplash.com/photo-1678954761791-7cb1a24e907e?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1886&q=80'
    r = requests.get(url, allow_redirects=True)
    open('img3.jpg', 'wb').write(r.content)
    print("Function 3")
    return "Hello User 3"


async def main():
    L=await asyncio.gather(func1(),func2(),func3())
    print(L)

    # task =asyncio.create_task(func1())
    # # await func1()
    # await func2()
    # await func3()

asyncio.run(main())


