from os import getenv
from dotenv import load_dotenv
import disnake
from disnake.ext import commands

# Read discord bot settings
load_dotenv()
token = getenv("BOT_TOKEN")
test_guilds = getenv("DEVELOPER_GUILD_ID")
sync_commands = getenv("SYNC_COMMANDS")

# Defining the bot and settings
client = commands.InteractionBot(
    name = "Team Neptune FAQ Bot - v.2.0.0",
    sync_commands = sync_commands,
    #test_guilds = [test_guilds],
    intents = disnake.Intents.all()
)

# Load FAQ from JSON
FAQ_JSON = open("assets/faq.json")
FAQs = json.load(FAQ_JSON)

# Initialize the bot
for extention in os.listdir("./cogs"):
    if extention.endswith(".py"):
        try:
            client.load_extension("cogs." + extention[:-3])
        except Exception as error:
            print(f"Unable to load {extention} {error}.")

try:
    client.run(token)
except Exception as error:
    print(f"Error when logging in: {error}")
