import fluxer
import os
from dotenv import load_dotenv
from fluxer.models import Embed

# Global values gathered from .env, do not modify.
GUILD_ID = int(os.getenv("GUILD_ID"))
DEBUG = int(os.getenv("BOT_DEBUG_MODE"))

class BanCog(fluxer.Cog):
    def __init__(self, bot):
        super().__init__(bot)

    @fluxer.Cog.command(name="ban")
    async def ban(self, ctx, member_id: int, reason: str):
        guild = await self.bot.fetch_guild(ctx.guild_id)  

        if not guild:
            return await ctx.reply("This command hasn't been run in a guild, how are you using this bot?")
        await guild.ban(user_id=member_id, reason=reason)

        bannedEmbed = Embed(
            title = f"Banned {member_id}",
            description = f"This member hass been banned for: {reason}",
            color=0x65b7e6
        )

        await ctx.reply(embed=bannedEmbed)

        if DEBUG == 1:
            print(f"[DEBUG] Kick command operated on {member_id}")
        
async def setup(bot):
    await bot.add_cog(BanCog(bot))