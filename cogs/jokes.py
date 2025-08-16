import discord
from discord.ext import commands
from discord import app_commands
import pyjokes

class JokesCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @app_commands.command(name='joke', description="Tells a random joke!")
    async def joke(self, interaction: discord.Interaction):
        joke = pyjokes.get_joke()
        embed = discord.Embed(title="Here's a joke for you!",
                              description=joke,
                              color=discord.Color.blue())
        if interaction.user.avatar:
            user_avatar = interaction.user.avatar.url
        else:
            user_avatar = interaction.user.default_avatar.url
            
        if interaction.guild.icon:
            embed.set_thumbnail(url=interaction.guild.icon.url)
            
        embed.set_author(name=interaction.user.display_name, icon_url=user_avatar)
            
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(JokesCog(bot))