import requests
import time
import aiohttp
import asyncio
    
async def fetch_users(session):
    response = await session.get("https://jsonplaceholder.typicode.com/users")
    response_json = await response.json()
    
    
    return response_json


async def main():
    start_time = time.time()
    async with aiohttp.ClientSession() as session:
        
        lista_korutina = [fetch_users(session) for i in range(5)]
        rezultat = await asyncio.gather(*lista_korutina)
        
        for i in range(1):
            lista1 = [user["name"] for user in rezultat[i]]
            lista2 = [user["email"] for user in rezultat[i]]
            lista3 = [user["username"] for user in rezultat[i]]

            print (lista1, "\n")
            print (lista2, "\n")
            print (lista3, "\n")

        #print(rezultat)
        
        
asyncio.run(main())
    



