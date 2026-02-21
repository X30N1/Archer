import fluxer
import os
from dotenv import load_dotenv

# Global values gathered from .env, do not modify.
GUILD_ID = int(os.getenv("GUILD_ID"))

class BanCog(fluxer.Cog):
    def __init__(self, bot):
        super().__init__(bot)

    @fluxer.Cog.command(name="ban")
    async def ban(self, ctx, member_id: int, reason: str, time: str, hack: bool):
        await ctx.reply(f"This feature is currently in development.")
        
async def setup(bot):
    await bot.add_cog(BanCog(bot))