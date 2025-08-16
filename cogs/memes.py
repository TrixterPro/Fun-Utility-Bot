import discord
from discord.ext import commands
from discord import app_commands, ui
from utils.Handlers.RedditHandler import fetch_random_meme

class MemesCog(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot
        
    @app_commands.command(name='memes', description="Fetches a random meme from Reddit")
    async def memes(self, interaction: discord.Interaction):
        meme_data = await fetch_random_meme()
        if meme_data:
            embed = discord.Embed(title=meme_data["title"], color=discord.Color.random())
            embed.set_image(url=meme_data["image_url"])
            embed.set_footer(text="Source: r/Funnymemes", icon_url="https://www.redditinc.com/assets/images/site/reddit-logo.png")
            embed.url = meme_data["permalink"]
            
            if interaction.user.avatar:
                user_avatar = interaction.user.avatar.url
            else:
                user_avatar = interaction.user.default_avatar.url
            
            embed.set_author(name=interaction.user.display_name, icon_url=user_avatar)
            
            await interaction.response.send_message(embed=embed)
        
    
    
async def setup(bot):
    await bot.add_cog(MemesCog(bot))