import discord
from discord.ext import commands
from discord import app_commands
import random
import asyncio

class DiceRollCog(commands.GroupCog, name="dice"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="roll", description="Roll a dice with a specified number of sides.")
    @app_commands.describe(sides="The number of sides on the dice (default is 6).")
    async def roll(self, interaction: discord.Interaction, sides: int = 6):
        """Roll a dice with a specified number of sides."""
        if sides < 1:
            await interaction.response.send_message("The number of sides must be at least 1.", ephemeral=True)
            return
        
        await interaction.response.defer(thinking=True)
        await asyncio.sleep(1)
        result = random.randint(1, sides)
        
        embed = discord.Embed(
            title="🎲 Dice Roll Result",
            description=f"You rolled a **{result}** on a {sides}-sided dice.",
            color=discord.Color.green()
        )
        await interaction.followup.send(embed=embed)
        
async def setup(bot: commands.Bot):
    await bot.add_cog(DiceRollCog(bot))
    