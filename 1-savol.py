import asyncio
import io
import httpx
from anyio.streams import file


class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = file

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()


async def a_data(url):
    async with httpx.AsyncClient() as client:
        response = await client.post(url)
        return response.text, response.status_code


async def main():
    url = "http://164.92.64.76/desc/"
    file_prefix = "Response_001.txt"
    
    data, status_code = await a_data(url)

    filename = f"{file_prefix}_{status_code}.txt"
    with FileManager(filename, "w") as f:
        f.write(data)


if __name__ == "__main__":
    asyncio.run(main())
