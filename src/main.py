import discord 
import datetime
import asyncio
import os 
from dotenv import load_dotenv
from discord.ext import tasks

bot = discord.Bot()
load_dotenv()
TOKEN = os.getenv("TOKEN")

class ReminderView(discord.ui.View):
    def __init__(self, user):
        super().__init__()
        self.dismissed = False
        self.user = user

    @discord.ui.button(label="got it gurt", style=discord.ButtonStyle.primary, emoji="💊")
    async def dissmiss(self, button: discord.ui.Button, interaction: discord.Interaction):
        print(interaction.user.id)
        if interaction.user.id != self.user:
            await interaction.response.send_message("not for you gurtie buddy", ephemeral=True)
            return
        self.dismissed = True
        await interaction.response.send_message("ggs gurt", ephemeral=True)
        self.stop
        


notify_users = [{
    "name": "gixxix",
    "id": 328436117861040129,
    "meds": "frontin",
    "hour": 7,
},
{
    "name": "gixxix",
    "id": 328436117861040129,
    "meds": "frontin, paretin",
    "hour": 12,
},
{
    "name": "gixxix",
    "id": 328436117861040129,
    "meds": "frontin",
    "hour": 18,
},
{
    "name": "gixxix",
    "id": 328436117861040129,
    "meds": "bitinex, frontin",
    "hour": 23,
},
{
    "name": "freptical",
    "id": 312972801852309506,
    "meds": "bitinex, floxet",
    "hour": 22,
},
{
    "name": "kaoplo",
    "id": 221136608810893312,
    "meds": "magnezium",
    "hour": 23,
},
{
    "name": "kaoplo",
    "id": 221136608810893312,
    "meds": "c vitamin es q10",
    "hour": 7,
}

]


async def remind(channel, notifee):
    print("running scheduled task")
    button = ReminderView(notifee["id"])
    await channel.send(f"a1TAKE YOUR {notifee["meds"]} MED <@{notifee["id"]}>", view=button)

    number = 0
    while button.dismissed != True:
        if number > 4:
            await channel.send("no more reminders...")
            break
        await asyncio.sleep(3600)
        if button.dismissed != True:
            await channel.send(f"{number}:<@{notifee["id"]}> bro..")
            number += 1

@tasks.loop(minutes=1)
async def scheduler():
    print("running 1 minute scheduel")
    channel = bot.get_channel(1187467209174429776)
    now = datetime.datetime.now()
    for notify in notify_users:
        if notify["hour"] == now.hour and now.minute == 0:
            asyncio.create_task(remind(channel, notify))

    
@bot.event
async def on_ready():
    scheduler.start()
    print("bot started")


@bot.slash_command()
async def button(ctx):
    await ctx.respond("test")

bot.run(TOKEN)