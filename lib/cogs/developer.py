import discord
from discord import Cog, Embed

from lib.utils import checks


class Developer(Cog, name="developer"):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(
        name="shutdown",
        description="Make the bot shutdown.",
    )
    @checks.is_developer()
    async def shutdown(self, ctx):
        embed = Embed(
            description="Shutting down. Bye! 👋🏼",
            color=0xd62728  # tab:red matplotlib
        )

        channel_announce_id = int(self.bot.config["channel_ids"]["announce"])
        await ctx.respond("Got it! Going to announce this on your announcement channel.")
        await ctx.guild.get_channel(channel_announce_id).send(embed=embed)
        await self.bot.close()


def setup(bot):
    bot.add_cog(Developer(bot))
