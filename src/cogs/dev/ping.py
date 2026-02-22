import fluxer
from fluxer.models import Embed

class PingCog(fluxer.Cog):
    def __init__(self, bot):
        super().__init__(bot)

    @fluxer.Cog.command()
    async def ping(self, ctx):
        pingEnded = Embed(
            title = "Pong!",
            color=0x65b7e6
        )

        print("[OK] Recieved ping command!")
        await ctx.reply(embed=pingEnded)
        print("[OK] Returned pong!")

async def setup(bot):
    await bot.add_cog(PingCog(bot))