import disnake
from disnake.ext import commands, tasks
from aiohttp_requests import requests
from aiofiles import open

class Github(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.refresh.start()

    # Github refresh Loop every 12 hours
    @tasks.loop(hours = 12)
    async def refresh(self):
        await self.client.wait_until_ready()

        # Async http get request
        resp = await requests.get("https://raw.githubusercontent.com/Team-Neptune/TeamNeptuneFAQBot/main/faq.json")
        response = await resp.json(content_type = "text/plain")
        
        async with aiofiles.open(f"assets/faq.json", mode = "w") as outfile:
            await outfile.write(json.dumps(response, indent = 4))

def setup(client):
    client.add_cog(Github(client))
