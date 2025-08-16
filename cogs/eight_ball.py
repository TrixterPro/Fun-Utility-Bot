import random
import discord
from discord.ext import commands
from discord import app_commands
import asyncio

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="8ball", description="Ask the magic 8-ball a question.")
    @app_commands.describe(question="The question you want to ask the magic 8-ball.")
    async def eight_ball(self, interaction: discord.Interaction, *, question: str):
        await interaction.response.defer(thinking=True)
        await asyncio.sleep(2)
        responses = [
            "Yes.", "No.", "Maybe.", "Definitely.", "Absolutely not.",
            "Ask again later.", "It is certain.", "Very doubtful.",
            "Without a doubt.", "Better not tell you now."
        ]
        answer = random.choice(responses)
        embed = discord.Embed(
            title="🎱 magic 8-Ball",
            color=discord.Color.blurple()
        )
        embed.add_field(name="🎱 Question", value=question, inline=False)
        embed.add_field(name="🎱 Answer", value=answer, inline=False)
        await interaction.followup.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Fun(bot))
