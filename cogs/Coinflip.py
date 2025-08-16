import discord
from discord.ext import commands
from discord import app_commands
import random
import asyncio

class CoinFlipCog(commands.GroupCog, name='coin'):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="flip", description="Flip a coin and get heads or tails.")
    async def coinflip(self, interaction: discord.Interaction):
        
        await interaction.response.defer(thinking=True)
        await asyncio.sleep(1)
        result = random.choice(["Heads", "Tails"])
        embed = discord.Embed(
            title="Coin Flip Result",
            description=f"The coin landed on: **{result}**",
            color=discord.Color.gold()
        )
        await interaction.followup.send(embed=embed)
        
async def setup(bot: commands.Bot):
    await bot.add_cog(CoinFlipCog(bot))