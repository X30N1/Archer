import fluxer

class AutoRoleCog(fluxer.Cog):
    def __init__(self, bot):
        super().__init__(bot)

    @fluxer.Cog.listener()
    async def on_member_join(self, member):
        try:
            user_id = member['id']
        except KeyError:
            print(f"[FAIL] Member join event did not include 'id': {member}")
            return

        guild_id = 1473331137336340540
        role_id = 1473337450582138986

        await self.bot.rest.add_guild_member_role(
            guild_id=guild_id,
            user_id=user_id,
            role_id=role_id,
            reason="Joined."
        )

        print(f"Added role {role_id} to user {user_id}.")


async def setup(bot):
    await bot.add_cog(AutoRoleCog(bot))