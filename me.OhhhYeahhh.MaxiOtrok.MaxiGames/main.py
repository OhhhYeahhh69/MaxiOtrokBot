import asyncio
from email import message
from itertools import cycle
from lib2to3.fixes.fix_input import context
from webbrowser import get

import discord
from discord import member
from discord.ext import commands, tasks

client = commands.Bot(command_prefix="+")
status = cycle(['mc.maxigames.cz Připoj se taky!', '@official_maxigames Budeme rádi za follow!', 'Užívej si hraní na MaxiGames!'])

@client.event
async def on_ready():
    change_status.start()
    print("Bot je Online!")

@client.command()
async def hlasuj(ctx):
    embed = discord.Embed(
    title="Hlasování",
    colour=discord.Colour.blue()

    )
    embed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/SLzDnUgLpLFLyzvFlFuw1RZthWqVovutluZapVcwBEI/https/media.discordapp.net/attachments/735562225594531990/818870517862891560/standard_7.gif")
    embed.add_field(name="Čím víc hlasů, tím víc borec!", value='------------------------------------------------------', inline=False)
    embed.add_field(name="Hlasuj zde:", value="https://czech-craft.eu/server/maxigames/vote/", inline=False)
    embed.set_footer(text="〈 mc.maxigames.cz 〉")
    # ctx.message.author.Permissions.administrator
    # ctx.member.avatar_url
    await ctx.send(embed=embed)


@client.command()
async def builder451145441543(ctx):
    embed = discord.Embed(
        title="Nábor - Builder/ka",
        colour=discord.Colour.blue()

    )
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/723499397404426270/834431098071154698/builder5121.png")
    embed.add_field(name="Máte zájem o pozici Builder/ka?!", value='----------------------------------------------------------------------------', inline=False)
    embed.add_field(name="Nábor zde:", value="https://docs.google.com/forms/d/e/1FAIpQLSd1X-t-hWrOB1ZX98Oquu7EpPVPTvA_XRH_tMGQd228CsrgjA/viewform", inline=False)
    await ctx.send(embed=embed)


@client.command()
async def helper54115445474(ctx):
    embed = discord.Embed(
        title="Nábor - Helper/ka",
        colour=discord.Colour.blue()

    )
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/723499397404426270/834431116844597279/helper515415.png")
    embed.add_field(name="Máte zájem o pozici Helper/ka?!", value='----------------------------------------------------------------------------', inline=False)
    embed.add_field(name="Nábor zde:", value="https://docs.google.com/forms/d/e/1FAIpQLSf5l_PxrsCFePRM_UhDQw94T0UIRiWAXQHBHY1LNytVv1HFgg/viewform", inline=False)
    await ctx.send(embed=embed)



@client.command()
async def server(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)

    owner = 'OhhhYeahhh'
    id = str(ctx.guild.id)
    region = str(ctx.guild.region)
    memberCount = str(ctx.guild.member_count)


    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(
        title=name + " Informace",
        color=discord.Color.blue()

    )
    embed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/SLzDnUgLpLFLyzvFlFuw1RZthWqVovutluZapVcwBEI/https/media.discordapp.net/attachments/735562225594531990/818870517862891560/standard_7.gif")
    embed.add_field(name="Server byl založen:", value=f"{ctx.guild.created_at}", inline=False)
    embed.add_field(name="Majitel serveru:", value=owner, inline=False)
    embed.add_field(name="Server ID:", value=id, inline=False)
    embed.add_field(name="Lokace:", value=region, inline=False)
    embed.add_field(name="Členů:", value=memberCount, inline=False)
    embed.set_footer(text="〈 mc.maxigames.cz 〉")
    await ctx.send(embed=embed)


@client.command()
async def PravidlaTitle4535134545(ctx):
    embed=discord.Embed(
        title = "MaxiGames Pravidla",
        colour = discord.Colour.blue()

    )
    embed.set_image( url="https://images-ext-2.discordapp.net/external/wFRBdflwr3tv6kOfAK2FyXtMTHPXIncMPd4f1pprKpQ/https/media.discordapp.net/attachments/735562225594531990/823828721026727966/standard_2.gif")
    embed.add_field(name="Přečtěte si pravidla, připojením na server automaticky souhlasíte s pravidly.", value="----------------------------------------------------------------------------", inline=False)

    await ctx.send(embed=embed)



@client.command()
async def PravidlaDis5414154415(ctx):
    embed=discord.Embed(
        title = "Discord Pravidla",
        colour = discord.Colour.blue()

    )
    embed.set_thumbnail( url="https://images-ext-2.discordapp.net/external/SLzDnUgLpLFLyzvFlFuw1RZthWqVovutluZapVcwBEI/https/media.discordapp.net/attachments/735562225594531990/818870517862891560/standard_7.gif")
    embed.add_field(name="Pravidla.", value="----------------------------------------------------------------------------", inline=False)
    embed.add_field(name="1.) Členi musí dodržovat zákony České a Slovenské republiky.", value="----------------------------------------------------------------------------", inline=False)
    embed.add_field(name="2.) Zakázáno nadávat.", value="----------------------------------------------------------------------------", inline=False)
    embed.add_field(name="3.) Zakázáno spamovat.", value="----------------------------------------------------------------------------", inline=False)
    embed.add_field(name="4.) Zakázáno žebrat o role. ", value="----------------------------------------------------------------------------", inline=False)
    embed.add_field(name="5.) Zakázáno používat rasistický urážky.", value="----------------------------------------------------------------------------", inline=False)
    embed.add_field(name="6.) Zakázáno si dělat reklamu.", value="----------------------------------------------------------------------------", inline=False)
    embed.add_field(name="7.) Respektovat ostatní.", value="----------------------------------------------------------------------------", inline=False)
    embed.add_field(name="8.) Psát jen česky a Slovensky, někdy můžete i anglicky, ale ne furt.", value="----------------------------------------------------------------------------", inline=False)
    embed.add_field(name="9.) Zakázáno otravovat/provokovat členy serveru.", value="----------------------------------------------------------------------------", inline=False)
    embed.add_field(name="10.)  Zakázáno šířit údaje o ostatních bez jejich povolení např:  věk kde bydlí atd.", value="----------------------------------------------------------------------------", inline=False)
    embed.add_field(name="11.) Zakázáno posílat NSFW obsah.", value="----------------------------------------------------------------------------", inline=False)
    embed.add_field(name="12.) Zakázáno zbytečně označovat.", value="----------------------------------------------------------------------------", inline=False)
    embed.add_field(name="13.) Zakázáno se připojovat do roomek aby jste otravovali  ostatní hráče.", value="----------------------------------------------------------------------------", inline=False)
    embed.add_field(name="14.) Zakázáno spamovat do ticketů a posílat tam nesmysly. Porušení bude trestáno @🎫TICKET BAN🎫 ", value="----------------------------------------------------------------------------", inline=False)
    embed.add_field(name="15.) Zakázáno psát capslockem. Upozorní Vás Bot MEE6 pokud přesáhnete určitý počet varování dostanete dočasný mute do všech chatu (neplatí na tickety)", value="----------------------------------------------------------------------------", inline=False)
    embed.add_field(name="16.) Psát obsah do určitých roomek např: písničky do #songy.",value="----------------------------------------------------------------------------", inline=False)
    embed.add_field(name="17.) Zakázán Trolling.",value="----------------------------------------------------------------------------", inline=False)
    embed.add_field(name="18.) Room #📷│fotky│📷   slouží na sdílení věcí ze serveru. Pokud zde pošlete věci z jiného discordu bude to řešeno dočasným mutem. Pokud je to jen vtipná konverzace je to povolené, rádi se pobavíme.",value="----------------------------------------------------------------------------", inline=True)
    embed.add_field(name="19.) Vedení serveru si vyhrazuje právo na změnu pravidel.",value="----------------------------------------------------------------------------", inline=False)
    embed.add_field(name="20.) Vedení serveru má právo dát komukoliv jakýkoliv trest bez udaní důvodu.",value="----------------------------------------------------------------------------", inline=False)
    embed.set_footer(text="〈 mc.maxigames.cz 〉")

    await ctx.send(embed=embed)

@client.command()
async def PravidlaMc454512454(ctx):
    embed = discord.Embed(
        title="Minecraft Pravidla",
        colour=discord.Colour.blue()

    )
    embed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/SLzDnUgLpLFLyzvFlFuw1RZthWqVovutluZapVcwBEI/https/media.discordapp.net/attachments/735562225594531990/818870517862891560/standard_7.gif")
    embed.add_field(name="Pravidla.",value="----------------------------------------------------------------------------", inline=False)
    embed.add_field(name="1.) Členi musí dodržovat zákony České a Slovenské republiky.",value="----------------------------------------------------------------------------", inline=False)
    embed.add_field(name="2.) Zakázáno nadávat.",value="----------------------------------------------------------------------------", inline=False)
    embed.add_field(name="3.) Zakázáno spamovat.",value="----------------------------------------------------------------------------", inline=False)
    embed.add_field(name="4.) Zakázáno žebrat o op nebo rank.",value="----------------------------------------------------------------------------", inline=False)
    embed.add_field(name="5.) Zakázáno používat rasistický urážky.",value="----------------------------------------------------------------------------", inline=False)
    embed.add_field(name="6.) Zakázáno si dělat reklamu.",value="----------------------------------------------------------------------------", inline=False)
    embed.add_field(name="7.) Respektovat ostatní.",value="----------------------------------------------------------------------------", inline=False)
    embed.add_field(name="8.) Je povinnost psát jen česky slovensky, někdy můžete i anglicky, ale ne furt.",value="----------------------------------------------------------------------------", inline=False)
    embed.add_field(name="9.) Zakázáno otravovat/provokovat členy serveru.",value="----------------------------------------------------------------------------", inline=False)
    embed.add_field(name="10.) Zakázáno šířit údaje o ostatních bez jejich povolení např:  věk kde bydlí atd.",value="----------------------------------------------------------------------------", inline=False)
    embed.add_field(name="11.) Zakázáno poškozovat server např: Se ho snažit schválně shodit.",value="----------------------------------------------------------------------------", inline=False)
    embed.add_field(name="12.) Zakázáno používat nepovolené programy (cheaty, autoclicker, fly, x-ray, killaura a vše co spadá do cheatu) je povoleno: Minimapa, Optifine, Labymod, a další...",value="----------------------------------------------------------------------------", inline=False)
    embed.add_field(name="13.) Zakázáno dělat: velké redstone obvody, bugovat itemy, a snažit se shodit server!",value="----------------------------------------------------------------------------", inline=False)
    embed.add_field(name="14.) Zakázáno griefování kolem cizích rezidencí nebo staveb. Např: ničení krajiny, stavění zdí, pokládání TNT atd...  Neručíme za vaše residence, a neručíme za vaše věci, je pouze na vás koho si přidáte do residence!",value="----------------------------------------------------------------------------", inline=False)
    embed.add_field(name="15.) Zakázáno stavění nesmyslných staveb. Např: urážlivý stavby, znaky atd...",value="----------------------------------------------------------------------------", inline=False)
    embed.add_field(name="16.) Zakázán Trolling.",value="----------------------------------------------------------------------------", inline=False)
    embed.add_field(name="17.) Zakázáno mít nevhodný jméno nebo skin.",value="----------------------------------------------------------------------------", inline=False)
    embed.add_field(name="18.) Zakázáno obcházet bany, používat VPN nebo si vytvářet další účty.",value="----------------------------------------------------------------------------", inline=False)
    embed.add_field(name="19.) Zakázáno obcházet pravidla našeho serveru!",value="----------------------------------------------------------------------------", inline=False)
    embed.add_field(name="20.) Zakázáno utajovat bugy a zneužívat je pro svůj prospěch. Je vaší povinností bug nahlásit vedení serveru!",value="----------------------------------------------------------------------------", inline=False)
    embed.add_field(name="21.) Je povinnost psát jen česky slovensky, někdy můžete i anglicky, ale ne furt.",value="----------------------------------------------------------------------------", inline=False)
    embed.add_field(name="22.) Zakázáno se vydávat za YouTubera, Streamera, TikTokera nebo za nějakou slavnou nebo významnou osobnost.",value="----------------------------------------------------------------------------", inline=False)
    embed.add_field(name="23.) Vedení serveru si vyhrazuje právo na změnu pravidel.",value="----------------------------------------------------------------------------", inline=False)
    embed.add_field(name="24.) Vedení serveru má právo dát komukoliv jakýkoliv trest bez udaní důvodu.",value="----------------------------------------------------------------------------", inline=False)
    embed.set_footer(text="〈 mc.maxigames.cz 〉")

    await ctx.send(embed=embed)


@client.command()
async def návrh(ctx, *, args):
    await ctx.message.add_reaction("🗑️")
    channel1 = client.get_channel(833026950482100237)
    embed = discord.Embed(title = "Zareaguj ✅ nebo ❎", colour=discord.Colour.blue())
    embed.set_author(name = "Návrh od: " + ctx.author.name, icon_url = ctx.author.avatar_url)
    embed.add_field(name = "Text", value = "➡ " + args)
    embed.set_footer(text="Napadlo tě něco? Napiš +návrh <text>")
    msg = await channel1.send(embed = embed)
    await msg.add_reaction("✅")
    await msg.add_reaction("❎")

@client.command()
async def navrh(ctx, *, args):
    await ctx.message.add_reaction("🗑️")
    channel1 = client.get_channel(833026950482100237)
    embed = discord.Embed(title = "Zareaguj ✅ nebo ❎", colour=discord.Colour.blue())
    embed.set_author(name = "Návrh od: " + ctx.author.name, icon_url = ctx.author.avatar_url)
    embed.add_field(name = "Text", value = "➡ " + args)
    embed.set_footer(text="Napadlo tě něco? Napiš +návrh <text>")
    msg = await channel1.send(embed = embed)
    await msg.add_reaction("✅")
    await msg.add_reaction("❎")

@client.command()
async def napad(ctx, *, args):
    await ctx.message.add_reaction("🗑️")
    channel1 = client.get_channel(833026950482100237)
    embed = discord.Embed(title = "Zareaguj ✅ nebo ❎", colour=discord.Colour.blue())
    embed.set_author(name = "Návrh od: " + ctx.author.name, icon_url = ctx.author.avatar_url)
    embed.add_field(name = "Text", value = "➡ " + args)
    embed.set_footer(text="Napadlo tě něco? Napiš +návrh <text>")
    msg = await channel1.send(embed = embed)
    await msg.add_reaction("✅")
    await msg.add_reaction("❎")

@client.command()
async def nápad(ctx, *, args):
    await ctx.message.add_reaction("🗑️")
    channel1 = client.get_channel(833026950482100237)
    embed = discord.Embed(title = "Zareaguj ✅ nebo ❎", colour=discord.Colour.blue())
    embed.set_author(name = "Návrh od: " + ctx.author.name, icon_url = ctx.author.avatar_url)
    embed.add_field(name = "Text", value = "➡ " + args)
    embed.set_footer(text="Napadlo tě něco? Napiš +návrh <text>")
    msg = await channel1.send(embed = embed)
    await msg.add_reaction("✅")
    await msg.add_reaction("❎")
@tasks.loop(seconds =5)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

client.run("ODMzNDMxNDk2NjIxNTU1NzMy.YHyPkQ._NxVnDD5LxFP3Nogn40Sx0n0e_M")

