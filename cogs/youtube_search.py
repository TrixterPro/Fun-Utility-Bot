import discord
from discord.ext import commands
from discord import app_commands
import yt_dlp

class YoutubeSearchCog(commands.GroupCog, name="youtube"):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="search", description="Search for a YouTube video.")
    @app_commands.describe(query="The search query for YouTube.")
    async def search(self, interaction: discord.Interaction, query: str):
        await interaction.response.defer(thinking=True)
        ydl_opts = {
            'format': 'best',
            'quiet': True,
            'noplaylist': True,
            'default_search': 'ytsearch',
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            try:
                info = ydl.extract_info(query, download=False)
                if 'entries' in info:
                    video = info['entries'][0]
                else:
                    video = info
            except Exception as e:
                await interaction.followup.send(f"Error searching for video: {str(e)}", ephemeral=True)
                return

        embed = discord.Embed(
            title=video.get('title', 'No Title'),
            url=video.get('webpage_url', ''),
            description=video.get('description', 'No Description'),
            color=discord.Color.blurple()
        )
        embed.set_thumbnail(url=video.get('thumbnail', ''))
        embed.add_field(name="Duration", value=str(video.get('duration', 0)) + " seconds", inline=True)
        embed.add_field(name="Uploader", value=video.get('uploader', 'Unknown'), inline=True)

        await interaction.followup.send(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(YoutubeSearchCog(bot))