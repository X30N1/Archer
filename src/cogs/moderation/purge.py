import fluxer
import os
from dotenv import load_dotenv
from fluxer.models import Embed

# Global values gathered from .env, do not modify.
GUILD_ID = int(os.getenv("GUILD_ID"))
DEBUG = int(os.getenv("BOT_DEBUG_MODE"))
MOD_ROLE = int(os.getenv("MOD_ROLE"))

class PurgeCog(fluxer.Cog):
    def __init__(self, bot):
        super().__init__(bot)

    @fluxer.Cog.command(name="purge")  
    async def purge(self, ctx, purge_count: int):  
        channel = await self.bot.fetch_channel(ctx.channel_id)  

        # Permission gating, only mods can use this command.
        author_id = getattr(ctx.author, "user", ctx.author).id  
        guild = await self.bot.fetch_guild(ctx.guild_id)  

        member = await guild.fetch_member(author_id)  
        if not member or not member.has_role(MOD_ROLE):  
            await ctx.reply("Oops! You do not have permission to use that command.")  
            print("[WARNING] Someone without the mod role tried to use the purge command!")  
            return  

        if not channel:  
            return await ctx.reply("Could not resolve this channel.")  
    
        messages_data = await self.bot._http.get_messages(  
            channel.id, limit=purge_count  
        )  
        from fluxer.models.message import Message  
        messages = [Message.from_data(m, self.bot._http) for m in messages_data]  
    
        # Delete each message  
        for msg in messages:  
            if msg.id != ctx.id:
                await msg.delete()          
        await ctx.reply(f"Purged {len(messages)} message(s).")

        if DEBUG == 1:
            print(f"[DEBUG] Purge command operated, deleting {purge_count} messages.")
            
async def setup(bot):
    await bot.add_cog(PurgeCog(bot))