import discord
from discord.ext import commands
from discord import app_commands
import qrcode
import random
import string
import os

class QRCodeCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @app_commands.command(name="qr", description="Generate a QR code from the provided text.")
    @app_commands.describe(text="The text or URL to encode in the QR code.")
    async def qr_code(self, interaction: discord.Interaction, text: str):
        """Generate a QR code from the provided text."""
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(text)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        
        imgname = f"qrcode-{random.choices(string.ascii_letters, k=6)}.png"
        img.save(imgname)

        await interaction.response.send_message(file=discord.File(imgname))
        os.remove(imgname)
        
async def setup(bot: commands.Bot):
    await bot.add_cog(QRCodeCog(bot))