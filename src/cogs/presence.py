import disnake
from disnake.ext import commands, tasks
import asyncio

class Presence(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.presence.start()

    # Presence Loop
    @tasks.loop()
    async def presence(self):
        await self.client.wait_until_ready()

        await self.client.change_presence(activity = disnake.Game(name = "Switch help"))
        await asyncio.sleep(45)

        await self.client.change_presence(activity = disnake.Activity(type = disnake.ActivityType.watching, name = "/faq"))
        await asyncio.sleep(45)

        await self.client.change_presence(activity = disnake.Game(name = "maintained by Team Neptune"))
        await asyncio.sleep(45)

        total_members = 0
        for guild in self.client.guilds:
            member_count = len([member for member in guild.members if not member.bot])
            total_members = total_members + member_count
        await self.client.change_presence(activity = disnake.Activity(type = disnake.ActivityType.watching, name = f"{total_members} members!"))
        await asyncio.sleep(45)

        total_guilds = len(self.client.guilds)
        await self.client.change_presence(activity = disnake.Activity(type = disnake.ActivityType.watching, name = f"{total_guilder} servers!"))
        await asyncio.sleep(45)

def setup(client):
    client.add_cog(Presence(client))
