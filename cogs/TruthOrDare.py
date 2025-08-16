import discord
from discord.ext import commands
from discord import app_commands
import random

class TruthOrDareCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name='dare', description="Get a random dare!")
    async def dare(self, interaction: discord.Interaction):
        
        with open('utils/Data/dares.txt', 'r', encoding='utf-8') as file:
            dares = file.readlines()
            
        dare = random.choice(dares).strip()
        
        embed = discord.Embed(title='Dare', description=dare, color=discord.Color.green())
        
        if interaction.user.avatar:
            user_avatar = interaction.user.avatar.url
        if not interaction.user.avatar:
            user_avatar = interaction.user.default_avatar.url
            
        embed.set_author(name=interaction.user.display_name, icon_url=user_avatar)
        
        if interaction.guild.icon:
            embed.set_thumbnail(url=interaction.guild.icon.url)
            
        await interaction.response.send_message(embed=embed)
        
    @app_commands.command(name='truth', description="Get a random truth!")
    async def truth(self, interaction: discord.Interaction):
        with open('utils/Data/truths.txt', 'r', encoding='utf-8') as file:
            truths = file.readlines()
            
        truth = random.choice(truths).strip()
        
        embed = discord.Embed(title='Truth', description=truth, color=discord.Color.blue())
        
        if interaction.user.avatar:
            user_avatar = interaction.user.avatar.url
        if not interaction.user.avatar:
            user_avatar = interaction.user.default_avatar.url
            
        embed.set_author(name=interaction.user.display_name, icon_url=user_avatar)
        
        if interaction.guild.icon:
            embed.set_thumbnail(url=interaction.guild.icon.url)
            
        await interaction.response.send_message(embed=embed)
    
    
async def setup(bot):
    await bot.add_cog(TruthOrDareCog(bot))

    