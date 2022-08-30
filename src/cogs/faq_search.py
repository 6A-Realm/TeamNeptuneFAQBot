from disnake.ext import commands
from main import FAQs

class FAQSearch(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Returns a list of questions that begin with the characters entered
    async def auto_fill(ctx: disnake.ApplicationCommandInteraction):
        return [faq for faq in FAQs.keys() if faq.startswith(ctx.value.capitalize())]

    # View FAQ command private
    @commands.slash_command(description = "View answers to Frequently Asked Questions privately")
    async def faq(self, ctx: disnake.ApplicationCommandInteraction, faq: str = commands.Param(autocomplete = auto_fill)):
        await ctx.send(content = faq,  ephemeral  = True)

    # View FAQ command public 
    @commands.slash_command(description = "Post answers to Frequently Asked Questions")
    async def post_faq(self, ctx: disnake.ApplicationCommandInteraction, faq: str = commands.Param(autocomplete = auto_fill)):
        await ctx.send(faq)

def setup(client):
    client.add_cog(FAQSearch(client))
