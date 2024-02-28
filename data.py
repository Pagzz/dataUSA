import aiohttp
import asyncio

async def get_auth_token():
    async with aiohttp.ClientSession() as session:
        url = 'http://www.datairis.co/V1/auth/subscriber/'
        headers = {
            'SubscriberUsername': 'mintmediaapp',
            'SubscriberPassword': 'FNCcKWyi0bAXnoPAka8L',
            'AccountUsername': 'mintmediaacct',
            'AccountPassword': 'reference',
            'AccountDetailsRequired': 'true',
            'SubscriberID': '224',
        }
        params = {
            'AccessToken': 'ad381-a59ec-4d7d',
        }
        async with session.get(url, headers=headers, params=params) as response:
            data = await response.json()
            return data['Response']['responseDetails']['TokenID']

async def get_mapped_dbs(token_id):
    async with aiohttp.ClientSession() as session:
        url = 'http://www.datairis.co/V1/search/mapped/database'
        headers = {'TokenID': token_id}
        async with session.get(url, headers=headers) as response:
            data = await response.json()
            return data

async def main():
    token_id = await get_auth_token()
    mapped_dbs = await get_mapped_dbs(token_id)
    print(mapped_dbs)

if __name__ == '__main__':
    asyncio.run(main())
