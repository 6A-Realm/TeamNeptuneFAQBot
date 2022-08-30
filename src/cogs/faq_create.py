from disnake.ext import commands

class FAQCreate(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Suggest new FAQ to bot owner
    @bot.slash_command(description = "Learn how you can contribute to the responses of this bot")
    async def contribute(self, ctx):
        await ctx.send(content = "You can contribute by going to https://github.com/Team-Neptune/TeamNeptuneFAQBot", ephemeral = True)

def setup(client):
    client.add_cog(FAQCreate(client))
