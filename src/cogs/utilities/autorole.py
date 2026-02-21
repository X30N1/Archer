import fluxer
import os
from dotenv import load_dotenv

# Global values gathered from .env, do not modify.
GUILD_ID = int(os.getenv("GUILD_ID"))
ROLE_ID = int(os.getenv("AUTOROLE_ID"))
COG_ENABLED = os.getenv("AUTOROLECOG_DISABLE")

class AutoRoleCog(fluxer.Cog):
    def __init__(self, bot):
        super().__init__(bot)

    @fluxer.Cog.listener()
    async def on_member_join(self, data):
        print(f"[OK] Member has joined {GUILD_ID}, attempting to grant {ROLE_ID}")

        user_id = int(data["user"]["id"])

        guild = self.bot._guilds.get(GUILD_ID)
        if not guild:
            return
        
        member = await guild.fetch_member(user_id)
        await member.add_role(role_id=ROLE_ID, guild_id=GUILD_ID, reason="Auto-role upon join.")
        print(f"[OK] Added role '{ROLE_ID}' to {user_id} in {GUILD_ID}")

async def setup(bot):
    await bot.add_cog(AutoRoleCog(bot))