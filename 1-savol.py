import asyncio
import os
import httpx



class FayilOqish:
    def __init__(self, path, mode):
        self.path = path
        self.mode = mode

    def __enter__(self):
        file = open(file=self.path, mode=self.mode)
        self.file = file
        return file

    def __exit__(self, *args, **kwargs):
        self.file.close()



def get_url_response():
    url = 'http://164.92.64.76/desc/'
    response = httpx.post(url)
    return response.status_code


async def RaiderFilePath():
    path = 'descriptions'
    status_code = str(get_url_response())
    file_name = os.listdir(path)
    for i in file_name:
        
        with FayilOqish(path +'/'+ i, 'r') as f:
            split_data = f.read().split('\n')
            name = split_data[0]
            price = split_data[1]
            text = split_data[2]

        with FayilOqish("Response.txt", 'a+') as w:
            w.write(str(i + ' ' + status_code + '\n'))

        print(name, price, text)

            
async def main():
    await asyncio.create_task(RaiderFilePath())
    await asyncio.create_task(get_url_response())

if __name__=='__main__':
    asyncio.run(RaiderFilePath())
    
