import discord
import asyncio
from discord.ext import commands
from discord.ui import Button, View
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.voice_states = True
intents.members = True

bot = commands.Bot(command_prefix='-', intents=intents)

# شناسه‌های کانال‌ها
target_channel_id = 1271058331552714803  # شناسه کانال متنی هدف
target_voice_channel_id = 1271054783826100326  # شناسه کانال صوتی هدف
move_to_voice_channel_id = 1275923130308628532  # شناسه ویس برای انتقال

# View class for the Move button
class MoveButtonView(discord.ui.View):
    def __init__(self):
        super().__init__()

    @discord.ui.button(label='Move', style=discord.ButtonStyle.danger, custom_id='move_button')
    async def move_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        target_voice_channel = interaction.guild.get_channel(move_to_voice_channel_id)
        if interaction.user.voice and interaction.user.voice.channel:
            await interaction.user.move_to(target_voice_channel)
            await interaction.response.send_message(f'Moved to {target_voice_channel.name}!', ephemeral=True)
            
            # Remove the original message after the button interaction
            await interaction.message.delete()
        else:
            await interaction.response.send_message('You are not in a voice channel!', ephemeral=True)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_voice_state_update(member, before, after):
    # بررسی می‌کند که کاربر وارد کانال صوتی مشخص شده است یا خیر
    if after.channel and after.channel.id == target_voice_channel_id:
        await asyncio.sleep(120)  # صبر کردن به مدت 20 ثانیه

        # بررسی می‌کند که کاربر همچنان در کانال هدف باقی مانده است
        if member.voice and member.voice.channel and member.voice.channel.id == target_voice_channel_id:
            channel = bot.get_channel(target_channel_id)
            if channel:
                embed = discord.Embed(
                    description="Eternal Connect To Staff",
                    color=discord.Color.from_rgb(173, 216, 230)  # رنگ یخی
                )

                view = MoveButtonView()
                message = await channel.send(embed=embed, view=view, content=f'{member.mention}')

                # Delete the message after 20 seconds
                await asyncio.sleep(120)
                try:
                    await message.delete()
                except discord.NotFound:
                    pass  # Ignore errors if the message was already deleted

# کلاس برای دکمه Whitelist
class WhitelistView(View):
    def __init__(self):
        super().__init__()

    @discord.ui.button(label='Whitelist ✅', style=discord.ButtonStyle.secondary, custom_id='whitelist_button')
    async def whitelist_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(f'Click [here](https://discord.com/channels/1185690992783917066/1276631038986289243) to visit the channel!', ephemeral=True)

# رویداد هنگام ورود کاربر جدید
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1272193656970936340)  # آیدی کانال خوشامدگویی
    if channel is not None:
        embed = discord.Embed(
            description=f"Welcome {member.mention} to Eternal Community!",
            color=discord.Color.from_rgb(49, 143, 136)  # رنگ نوار کناری به شکل #318f88
        )
        embed.set_thumbnail(url=member.avatar_url_as(size=40))  # تغییر اندازه آواتار به 64x64 پیکسل
        view = WhitelistView()
        await channel.send(embed=embed, view=view)

# توکن بات را از متغیر محیطی بارگذاری کنید
TOKEN = os.getenv('DISCORD_TOKEN')
bot.run(TOKEN)

import discord
from discord.ext import commands
from discord.ui import Button, View

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix='-', intents=intents)

# کلاس برای دکمه Whitelist
class WhitelistView(View):
    def __init__(self):
        super().__init__()

    @discord.ui.button(label='Whitelist ✅', style=discord.ButtonStyle.secondary, custom_id='whitelist_button')
    async def whitelist_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(f'Click [here](https://discord.com/channels/1185690992783917066/1276631038986289243) to visit the channel!', ephemeral=True)

# رویداد هنگام ورود کاربر جدید
@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1272193656970936340)  # آیدی کانال خوشامدگویی
    if channel is not None:
        embed = discord.Embed(
            description=f"Welcome {member.mention} to Eternal Community!",
            color=discord.Color.from_rgb(49, 143, 136)  # رنگ نوار کناری به شکل #318f88
        )
        embed.set_thumbnail(url=member.avatar_url_as(size=40))  # تغییر اندازه آواتار به 64x64 پیکسل
        view = WhitelistView()
        await channel.send(embed=embed, view=view)

# توکن بات
TOKEN = 'MTI3Mzk4ODYzMTYxODY1MDE1Mw.Gazi6v.syTRlj4DQL-q3OfXU4Hfg15Kg7gFSYorMvxcH8'
bot.run(TOKEN)

# Ticket Script

import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True  # اضافه کردن intent اعضا

bot = commands.Bot(command_prefix='-', intents=intents)

# لیست رنک‌هایی که اجازه استفاده از دستور دارند
allowed_ranks = ["━━ ≀ Management", "━━ ≀ Developer", "━━ ≀ Administrator", "━━ ≀ Controller", "━━ ≀ Helper"]

# لیست نام کتگوری‌ها (۹ کتگوری)
category_names = [
    "Management",
    "Refund Iteam",
    "Report Player",
    "Faction Report",
    "Gang Request",
    "Ped Request",
    "3D Request",
    "Police Department",
    "Question"
]

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def p(ctx, suffix: str):
    """دستور برای اضافه کردن suffix به نام کانال در صورتی که کانال در کتگوری مجاز باشد"""
    member = ctx.author
    channel = ctx.channel

    # چک کردن اینکه کاربر یکی از رنک‌های مجاز را دارد یا خیر
    user_roles = [role.name for role in member.roles]
    if not any(rank in user_roles for rank in allowed_ranks):
        await ctx.send("شما رنک مورد نیاز برای استفاده از این دستور را ندارید.")
        return

    if not suffix:
        await ctx.send("لطفاً یک suffix وارد کنید.")
        return

    # چک کردن اینکه کانال در کتگوری مجاز قرار دارد یا خیر
    if channel.category and channel.category.name in category_names:
        # تغییر نام کانال
        new_name = f"{channel.name}-{suffix}"
        await channel.edit(name=new_name)
        await ctx.send(f'نام کانال به {new_name} تغییر یافت.')
    else:
        await ctx.send("این دستور فقط در کانال‌های کتگوری‌های مجاز قابل استفاده است.")

bot.run(os.getenv('DISCORD_TOKEN'))


import discord
from discord.ext import commands
from discord.ui import Select, View
import json
import aiofiles
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configurations
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

bot = commands.Bot(command_prefix='+', intents=intents)

categories = {
    "Refund Item": 1272169803557240833,
    "Report Player": 1272170004447760455,
    "Faction Report": 1272170095682261032,
    "Gang Request": 1272170246492655708,
    "Ped Request": 1272170330995298366,
    "3D Request": 1272170396749398037,
    "Police Departement": 1272170686571479111,
    "Management": 1274761639140261949,
    "Question": 1274762825864314890,
    "Owner": 1276876273532010599,
    "Manage": 1276876382911074418
}

roles_for_tickets = {
    "Refund Item": [1186222063925612584, 1186222322647048192, 1186222388258558014, 1271744567393386540, 1186222128601780405],
    "Report Player": [1186222063925612584, 1186222322647048192, 1186222388258558014, 1271744567393386540, 1186222128601780405],
    "Faction Report": [1186222063925612584, 1186222322647048192, 1186222388258558014, 1271744567393386540, 1186222128601780405],
    "Gang Request": [1186222063925612584, 1186222322647048192, 1186222388258558014, 1271744567393386540, 1186222128601780405],
    "Ped Request": [1186222063925612584, 1186222322647048192, 1186222388258558014, 1271744567393386540, 1186222128601780405],
    "3D Request": [1274770007651422336, 1274770015671809410, 1274770025691393025, 1274770034672345477, 1274770045622464001],
    "Police Departement": [1186222063925612584, 1186222322647048192, 1186222388258558014, 1271744567393386540, 1186222128601780405],
    "Management": [1186222063925612584],
    "Question": [1186222063925612584, 1186222322647048192, 1186222388258558014, 1271744567393386540, 1186222128601780405],
    "Owner": [1186222063925612584],  # Example roles for owner
    "Manage": [1186222063925612584, 1186222322647048192]  # Example roles for manage
}

allowed_roles = ["━━ ≀ Owner", "━━ ≀ Management", "━━ ≀ Administrator"]
ticket_categories = [1272169803557240833, 1272170004447760455, 1272170095682261032, 1272170246492655708, 1272170330995298366, 1272170396749398037, 1272170686571479111, 1274761639140261949, 1274762825864314890]

channel_id = 1186031537209221250
ticket_data_file = 'ticket_data.json'

# Async file operations
async def save_ticket_data(data):
    async with aiofiles.open(ticket_data_file, 'w') as file:
        await file.write(json.dumps(data, indent=4))

async def load_ticket_data():
    try:
        async with aiofiles.open(ticket_data_file, 'r') as file:
            content = await file.read()
            return json.loads(content)
    except FileNotFoundError:
        return {}

class TicketDropdown(Select):
    def __init__(self):
        options = [
            discord.SelectOption(label=name, description=f"Create a {name} ticket")
            for name in categories if name not in ["Owner", "Manage"]
        ]
        super().__init__(placeholder="Select the type of ticket...", min_values=1, max_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        selected_category = self.values[0]
        await create_ticket(interaction, selected_category)

class TicketView(View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(TicketDropdown())

class CloseTicketView(View):
    def __init__(self):
        super().__init__(timeout=None)
        close_button = discord.ui.Button(label="Close", style=discord.ButtonStyle.red)
        close_button.callback = self.close_ticket
        self.add_item(close_button)

    async def close_ticket(self, interaction: discord.Interaction):
        confirm_view = ConfirmCloseTicketView()
        embed = discord.Embed(title="Are you sure?", color=discord.Color.red())
        await interaction.response.send_message(embed=embed, view=confirm_view)

class ConfirmCloseTicketView(View):
    def __init__(self):
        super().__init__(timeout=None)
        yes_button = discord.ui.Button(label="Yes", style=discord.ButtonStyle.green)
        yes_button.callback = self.confirm_close
        self.add_item(yes_button)

        no_button = discord.ui.Button(label="No", style=discord.ButtonStyle.red)
        no_button.callback = self.cancel_close
        self.add_item(no_button)

    async def cancel_close(self, interaction: discord.Interaction):
        await interaction.message.delete()

    async def confirm_close(self, interaction: discord.Interaction):
        ticket_data = await load_ticket_data()
        user_tickets = ticket_data.get(str(interaction.user.id), {})
        for ticket_type, channel_id in user_tickets.items():
            if channel_id == str(interaction.channel.id):
                del user_tickets[ticket_type]
                break
        ticket_data[str(interaction.user.id)] = user_tickets
        await save_ticket_data(ticket_data)
        await interaction.channel.delete()

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

    channel = bot.get_channel(channel_id)
    if channel:
        async for msg in channel.history(limit=100):
            if msg.embeds:
                if msg.embeds[0].title == "Select Ticket Type":
                    print("Ticket embed already exists.")
                    return

        embed = discord.Embed(title="Select Ticket Type", description="Choose a category below to create a ticket.", color=discord.Color.dark_gray())
        view = TicketView()
        await channel.send(embed=embed, view=view)
    else:
        print(f"Channel with ID {channel_id} not found.")

    # Ensure to handle previously created ticket channels
    ticket_data = await load_ticket_data()
    for user_id, user_tickets in ticket_data.items():
        for ticket_type, channel_id_str in user_tickets.items():
            channel = bot.get_channel(int(channel_id_str))
            if channel:
                embed = discord.Embed(title="Close Ticket", description="Click the button below to close the ticket.", color=discord.Color.yellow())
                view = CloseTicketView()
                await channel.send(embed=embed, view=view)

async def create_ticket(interaction: discord.Interaction, ticket_type: str):
    user_id = str(interaction.user.id)
    ticket_data = await load_ticket_data()
    user_tickets = ticket_data.get(user_id, {})

    if ticket_type in user_tickets:
        await interaction.response.send_message("You already have an open ticket of this type!", ephemeral=True)
        return

    guild = interaction.guild
    category_id = categories[ticket_type]
    category = guild.get_channel(category_id)

    if category is None:
        await interaction.response.send_message(f"Category with ID {category_id} not found!", ephemeral=True)
        return

    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),
        interaction.user: discord.PermissionOverwrite(read_messages=True, send_messages=True),
        guild.me: discord.PermissionOverwrite(read_messages=True, send_messages=True)
    }

    for role_id in roles_for_tickets.get(ticket_type, []):
        role = guild.get_role(role_id)
        if role is None:
            continue
        overwrites[role] = discord.PermissionOverwrite(read_messages=True, send_messages=True)

    ticket_channel = await category.create_text_channel(f"{ticket_type}-{interaction.user.name}", overwrites=overwrites)
    user_tickets[ticket_type] = str(ticket_channel.id)
    ticket_data[user_id] = user_tickets
    await save_ticket_data(ticket_data)

    embed = discord.Embed(title="Ticket Created", description="Use the button below to close the ticket when done.", color=discord.Color.green())
    view = CloseTicketView()
    await ticket_channel.send(embed=embed, view=view)

    await interaction.response.send_message(f"{ticket_type} ticket created: {ticket_channel.mention}", ephemeral=True)

@bot.command()
@commands.has_any_role("━━ ≀ Owner", "━━ ≀ Management", "━━ ≀ Administrator")
async def p(ctx, target: str):
    # Load ticket data
    ticket_data = await load_ticket_data()
    user_id = str(ctx.author.id)
    user_tickets = ticket_data.get(user_id, {})

    # Check if user has an open ticket
    if not user_tickets:
        await ctx.send("You don't have any open tickets!")
        return

    # Find the open ticket channel
    ticket_channel_id = None
    for ticket_type, channel_id_str in user_tickets.items():
        ticket_channel_id = int(channel_id_str)
        break

    if ticket_channel_id is None:
        await ctx.send("Unable to find your open ticket!")
        return

    ticket_channel = bot.get_channel(ticket_channel_id)

    if target == "owner":
        # Move the ticket to the 'Owner' category
        category_id = 1276876273532010599  # Owner category ID
        overwrites = {
            ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
            ctx.author: discord.PermissionOverwrite(read_messages=True, send_messages=True),
            ctx.guild.me: discord.PermissionOverwrite(read_messages=True, send_messages=True)
        }
    elif target == "manage":
        # Move the ticket to the 'Manage' category
        category_id = 1276876273532010599  # Manage category ID
        overwrites = {
            ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
            ctx.author: discord.PermissionOverwrite(read_messages=True, send_messages=True),
            ctx.guild.me: discord.PermissionOverwrite(read_messages=True, send_messages=True),
            ctx.guild.get_role(1186222063925612584): discord.PermissionOverwrite(read_messages=True, send_messages=True)
        }
    elif target == "admin":
        # Move the ticket to the 'Admin' category
        category_id = 1277029706998349877  # Admin category ID
        overwrites = {
            ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
            ctx.author: discord.PermissionOverwrite(read_messages=True, send_messages=True),
            ctx.guild.me: discord.PermissionOverwrite(read_messages=True, send_messages=True),
            ctx.guild.get_role(1186222322647048192): discord.PermissionOverwrite(read_messages=True, send_messages=True),  # Example role 1
            ctx.guild.get_role(1186222322647048192): discord.PermissionOverwrite(read_messages=True, send_messages=True)   # Example role 2
        }
    else:
        await ctx.send("Invalid command! Use either +p owner, +p manage, or +p admin.")
        return

    category = bot.get_channel(category_id)
    if category is None:
        await ctx.send(f"Category with ID {category_id} not found!")
        return

    await ticket_channel.edit(category=category, overwrites=overwrites)
    await ctx.send(f"Ticket moved to {category.name} and permissions updated!")

@bot.command()
@commands.has_any_role("━━ ≀ Owner", "━━ ≀ Management", "━━ ≀ Administrator", "━━ ≀ Controller")
async def adduser(ctx, member: discord.Member):
    # Check if command is used in a ticket channel
    if ctx.channel.category_id not in ticket_categories:
        await ctx.send("This command can only be used in a ticket channel.")
        return

    # Add the user to the ticket channel
    await ctx.channel.set_permissions(member, read_messages=True, send_messages=True)
    await ctx.send(f"{member.mention} has been added to the ticket.")

@bot.command()
@commands.has_any_role("━━ ≀ Owner", "━━ ≀ Management", "━━ ≀ Administrator", "━━ ≀ Controller")
async def reuser(ctx, member: discord.Member):
    # Check if command is used in a ticket channel
    if ctx.channel.category_id not in ticket_categories:
        await ctx.send("This command can only be used in a ticket channel.")
        return

    # Remove the user from the ticket channel
    await ctx.channel.set_permissions(member, overwrite=None)
    await ctx.send(f"{member.mention} has been removed from the ticket.")


bot.run(os.getenv('DISCORD_TOKEN'))


import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

bot = commands.Bot(command_prefix='-', intents=intents)

# List of rank names that are allowed to use the command
allowed_ranks = ["━━ ≀ Management", "━━ ≀ Developer", "━━ ≀ Administrator", "━━ ≀ Controller", "━━ ≀ Helper"]

# List of category names (9 categories)
category_names = [
    "Management",
    "Refund Iteam",
    "Report Player",
    "Faction Report",
    "Gang Request",
    "Ped Request",
    "3D Request",
    "Police Department",
    "Question"
]

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def p(ctx, suffix: str, category_name: str = None):
    """Command to append a suffix to the name of the channel and optionally move it to a specified category"""
    member = ctx.author
    guild = ctx.guild
    channel = ctx.channel

    # Check if the user has one of the allowed ranks
    user_roles = [role.name for role in member.roles]
    if not any(rank in user_roles for rank in allowed_ranks):
        await ctx.send("You do not have the required rank to use this command.")
        return

    if not suffix:
        await ctx.send("Please provide a suffix to append.")
        return

    # Change the channel name
    new_name = f"{channel.name}-{suffix}"
    await channel.edit(name=new_name)
    await ctx.send(f'Channel name changed to: {new_name}')

    # Move the channel to the specified category if provided
    if category_name:
        category = discord.utils.get(guild.categories, name=category_name)
        if category:
            await channel.edit(category=category)
            await ctx.send(f'Channel moved to category "{category_name}".')
        else:
            await ctx.send(f'Category "{category_name}" not found.')

# Load the token from the .env file
TOKEN = os.getenv('DISCORD_TOKEN')

bot.run(TOKEN)
