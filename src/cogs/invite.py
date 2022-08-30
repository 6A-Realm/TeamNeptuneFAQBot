# Public version: https://discord.com/api/oauth2/authorize?client_id=977012815607005225&permissions=0&scope=bot%20applications.commands
from disnake.ext import commands

class Invite(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Invite command
    @commands.slash_command(description = "Returns bot invite.")
    async def invite(self, ctx):
        bot_invite = f"https://discord.com/api/oauth2/authorize?client_id={self.client.user.id}&permissions=0&scope=bot%20applications.commands"
        await ctx.send(content = bot_invite, ephemeral  = True)

def setup(client):
    client.add_cog(Invite(client))
