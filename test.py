import aiohttp
import asyncio
import json

# Function to obtain the authentication token
async def get_auth_token():
    async with aiohttp.ClientSession() as session:
        url = 'http://www.datairis.co/V1/auth/subscriber/'
        headers = {
            'SubscriberUsername': 'mintmediaapp',
            'SubscriberPassword': 'FNCcKWyi0bAXnoPAka8L',
            'SubscriberID': '224',
        }
        params = {
            'AccessToken': 'ad381-a59ec-4d7d',
        }
        async with session.get(url, headers=headers, params=params) as response:
            data = await response.json()
            return data['Response']['responseDetails']['TokenID']

# Function to add all search criteria
async def add_all_search_criteria(token_id, database_type, criteria):
    url = f"http://www.datairis.co/V1/criteria/search/addall/{database_type}"
    headers = {
        'TokenID': token_id,
        'Content-Type': 'application/json'
    }
    payload = json.dumps(criteria)  # Assuming 'criteria' is a dictionary of your compiled search criteria

    async with aiohttp.ClientSession() as session:
        async with session.put(url, headers=headers, data=payload) as response:
            response_data = await response.json()
            return response_data

# Main function to orchestrate the authentication and search criteria addition
async def main():
    # Obtain token ID
    token_id = await get_auth_token()
    
    # Specify the database type and criteria
    database_type = 'consumer'  
    criteria = {
        'First_Name': ['John', 'Jane'],
        'Last_Name': ['Doe', 'Smith'],
        'County': ['SomeCounty', 'AnotherCounty']
        # Add additional criteria as needed
    }
    
    # Add search criteria and print result
    result = await add_all_search_criteria(token_id, database_type, criteria)
    print(result)

if __name__ == '__main__':
    asyncio.run(main())
