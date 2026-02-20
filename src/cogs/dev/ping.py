import fluxer

class PingCog(fluxer.Cog):
    def __init__(self, bot):
        super().__init__(bot)

    @fluxer.Cog.command()
    async def ping(self, ctx):
        await ctx.reply("Pong.")

async def setup(bot):
    await bot.add_cog(PingCog(bot))