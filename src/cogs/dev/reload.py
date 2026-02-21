import fluxer
import os
from dotenv import load_dotenv

# Global values gathered from .env, do not modify.
GUILD_ID = int(os.getenv("GUILD_ID"))
DEBUG = int(os.getenv("BOT_DEBUG_MODE"))

class ReloadCog(fluxer.Cog):
    def __init__(self, bot):
        super().__init__(bot)

    @fluxer.Cog.command()  
    async def reload(self, ctx):  
        for root, dirs, files in os.walk("./src/cogs"):  
            for filename in files:  
                if filename.endswith(".py") and not filename.startswith("_"):  
                    path = os.path.join(root, filename)  
                    cog = path.lstrip("./").replace(os.sep, ".")[:-3]  
                    cog = cog.removeprefix("src.")  
                    try:  
                        cog_name = cog.split(".")[-1].capitalize() + "Cog"  
                        if cog_name in self.bot.cogs:  
                            await self.bot.remove_cog(cog_name)  
                        await self.bot.unload_extension(cog)  
                        await self.bot.load_extension(cog)  
                        if DEBUG == 1:  
                            print(f"[DEBUG] Reloaded {cog}")  
                    except Exception as e:  
                        print(f"[ERROR] Failed to reload {cog}: {e}")

async def setup(bot):
    await bot.add_cog(ReloadCog(bot))