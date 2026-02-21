import fluxer
import os
from dotenv import load_dotenv

# Global values gathered from .env, do not modify.
GUILD_ID = int(os.getenv("GUILD_ID"))
DEBUG = int(os.getenv("BOT_DEBUG_MODE"))

class KickCog(fluxer.Cog):
    def __init__(self, bot):
        super().__init__(bot)

    reason = "No reason set."

    @fluxer.Cog.command(name="kick")
    async def kick(self, ctx, member_id: int, *, reason: str | None = None):
        guild = await self.bot.fetch_guild(ctx.guild_id)  

        if not guild:
            return await ctx.reply("This command hasn't been run in a guild, how are you using this bot?")
        await guild.kick(user_id=member_id, reason=reason)
        await ctx.reply(f"Kicked {member_id}.")

        if DEBUG == 1:
            print(f"[DEBUG] Kick command operated on {member_id}")
            
        
async def setup(bot):
    await bot.add_cog(KickCog(bot))