import discord
from discord.ext import commands
from discord import app_commands

class AvatarCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="avatar", description="Get the avatar of a user.")
    @app_commands.describe(user="The user whose avatar you want to see. Defaults to yourself.")
    async def avatar(self, interaction: discord.Interaction, user: discord.User = None):
        """Get the avatar of a user."""
        if user is None:
            user = interaction.user
        
        embed = discord.Embed(title=f"{user.name}'s Avatar", color=discord.Color.blue())
        embed.set_image(url=user.avatar.url if user.avatar else user.default_avatar.url)
        
        await interaction.response.send_message(embed=embed)
        
async def setup(bot: commands.Bot):
    await bot.add_cog(AvatarCog(bot))