# This code is licensed under the GPLv2, feel free to tweak, redistribute or do whatever you want really.
# See license.md for more information :)

from dotenv import load_dotenv
import fluxer
import os

# Initialise .env > You bot token should be in this virtual environment.
load_dotenv()

bot = fluxer.Bot(command_prefix="$", intents=fluxer.Intents.default())

@bot.event
async def on_ready():
    await load_extensions()
    print(f"Logged in, and ready as {bot.user.username}")

async def load_extensions():
    for root, dirs, files in os.walk("./src/cogs"):
        for filename in files:
            if filename.endswith(".py") and not filename.startswith("_"):
                path = os.path.join(root, filename)
                cog = path.lstrip("./").replace(os.sep, ".")[:-3]
                cog = cog.removeprefix("src.")
                try:
                    await bot.load_extension(cog)
                    print(f"[*] Loaded {cog}")
                except Exception as e:
                    print(f"[X] Failed to load {cog}: {e}")

if __name__ == "__main__":
    # !!! SECURITY WARNING!!!
    # NEVER, EVER, EVER UNDER ANY CIRCUMSTANCES PUT YOUR TOKEN HERE.
    # PUT YOUR TOKEN IN .ENV IN THE PROJECT ROOT.
    # THANK YOU.
    TOKEN = os.getenv('FLUXER_BOT_TOKEN')
    bot.run(TOKEN)