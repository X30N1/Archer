import fluxer
import os
from dotenv import load_dotenv

# Global values gathered from .env, do not modify.
GUILD_ID = int(os.getenv("GUILD_ID"))

class TimeoutCog(fluxer.Cog):
    def __init__(self, bot):
        super().__init__(bot)

    @fluxer.Cog.command(name="timeout")
    async def timeout(self, ctx, member_id: int, reason: str, time: str):
        await ctx.reply(f"This feature is currently in development.")
        
async def setup(bot):
    await bot.add_cog(TimeoutCog(bot))