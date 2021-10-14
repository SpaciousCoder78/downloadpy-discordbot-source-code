import discord
import logging
import asyncio
client=discord.Client()


@client.event
async def on_message(message):
    ...
    if message.content == "!botinfo":
        embed = discord.Embed(title="downloadpy info", description="A bot that gives you links to python installers")
        embed.add_field(name="Programming Language", value="Python")
        embed.add_field(name="Developed by", value="a random python learner")
        embed.add_field(name="Version", value="1.0")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!python":
        embed = discord.Embed(title="Versions of python", description="Use the right command to head to download pages")
        embed.add_field(name="Python 1.6", value="https://www.python.org/download/releases/1.6.1/")
        embed.add_field(name="Python 2", value="!python-2")
        embed.add_field(name="Python 3", value="!python-3")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!python-2":
        embed = discord.Embed(title="Python 2 Downloads", description="Use the links to download/commands to get the links")
        embed.add_field(name="Python 2.0.1", value="https://www.python.org/downloads/release/python-201/")
        embed.add_field(name="Python 2.1.3", value="https://www.python.org/downloads/release/python-213/")
        embed.add_field(name="Python 2.2", value="!python-2.2")
        embed.add_field(name="Python 2.3", value="!python-2.3")
        embed.add_field(name="Python 2.4", value="!python-2.4")
        embed.add_field(name="Python 2.5", value="!python-2.5")
        embed.add_field(name="Python 2.6", value="!python-2.6")
        embed.add_field(name="Python 2.7", value="!python-2.7")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!python-3":
        embed = discord.Embed(title="Python 3 Downloads", description="Use the links to download/commands to get the links")
        embed.add_field(name="Python 3.0", value="https://www.python.org/downloads/release/python-30/")
        embed.add_field(name="Python 3.0.1", value="https://www.python.org/downloads/release/python-301/")
        embed.add_field(name="Python 3.1", value="!python-3.1")
        embed.add_field(name="Python 3.2", value="!python-3.2")
        embed.add_field(name="Python 3.3", value="!python-3.3")
        embed.add_field(name="Python 3.4", value="!python-3.4")
        embed.add_field(name="Python 3.5", value="!python-3.5")
        embed.add_field(name="Python 3.6", value="!python-3.6")
        embed.add_field(name="Python 3.7",value="!python-3.7")
        embed.add_field(name="Python 3.8", value="!python-3.8")
        embed.add_field(name="Python 3.9",value="!python-3.9")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!python-2.2":
        embed = discord.Embed(title="Python 2.2 Downloads", description="Use the links to download/commands to get the links")
        embed.add_field(name="Python 2.2.0", value="https://www.python.org/downloads/release/python-220/")
        embed.add_field(name="Python 2.2.1", value="https://www.python.org/downloads/release/python-221/")
        embed.add_field(name="Python 2.2.2", value="https://www.python.org/downloads/release/python-222/")
        embed.add_field(name="Python 2.2.3", value="https://www.python.org/downloads/release/python-223/")
        await message.channel.send(content=None, embed=embed)
    ...
    ...
    if message.content == "!python-2.3":
        embed = discord.Embed(title="Python 2.3 Downloads", description="Use the links to download/commands to get the links")
        embed.add_field(name="Python 2.3.0", value="https://www.python.org/downloads/release/python-230/")
        embed.add_field(name="Python 2.3.1", value="https://www.python.org/downloads/release/python-231/")
        embed.add_field(name="Python 2.3.2", value="https://www.python.org/downloads/release/python-232/")
        embed.add_field(name="Python 2.3.3", value="https://www.python.org/downloads/release/python-233/")
        embed.add_field(name="Python 2.3.4", value="https://www.python.org/downloads/release/python-234/")
        embed.add_field(name="Python 2.3.5", value="https://www.python.org/downloads/release/python-235/")
        embed.add_field(name="Python 2.3.6", value="https://www.python.org/downloads/release/python-236/")
        embed.add_field(name="Python 2.3.7", value="https://www.python.org/downloads/release/python-237/")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!python-2.4":
        embed = discord.Embed(title="Python 2.4 Downloads", description="Use the links to download/commands to get the links")
        embed.add_field(name="Python 2.4.0", value="https://www.python.org/downloads/release/python-240/")
        embed.add_field(name="Python 2.4.1", value="https://www.python.org/downloads/release/python-241/")
        embed.add_field(name="Python 2.4.2", value="https://www.python.org/downloads/release/python-242/")
        embed.add_field(name="Python 2.4.3", value="https://www.python.org/downloads/release/python-243/")
        embed.add_field(name="Python 2.4.4", value="https://www.python.org/downloads/release/python-244/")
        embed.add_field(name="Python 2.4.5", value="https://www.python.org/downloads/release/python-245/")
        embed.add_field(name="Python 2.4.6", value="https://www.python.org/downloads/release/python-246/")
        await message.channel.send(content=None, embed=embed)
    ...
    ...
    if message.content == "!python-2.5":
        embed = discord.Embed(title="Python 2.5 Downloads", description="Use the links to download/commands to get the links")
        embed.add_field(name="Python 2.5.0", value="https://www.python.org/downloads/release/python-250/")
        embed.add_field(name="Python 2.5.1", value="https://www.python.org/downloads/release/python-251/")
        embed.add_field(name="Python 2.5.2", value="https://www.python.org/downloads/release/python-252/")
        embed.add_field(name="Python 2.5.3", value="https://www.python.org/downloads/release/python-253/")
        embed.add_field(name="Python 2.5.4", value="https://www.python.org/downloads/release/python-254/")
        embed.add_field(name="Python 2.5.5", value="https://www.python.org/downloads/release/python-255/")
        embed.add_field(name="Python 2.5.6", value="https://www.python.org/downloads/release/python-256/")
        await message.channel.send(content=None, embed=embed)
    ...
    ...
    if message.content == "!python-2.6":
        embed = discord.Embed(title="Python 2.6 Downloads", description="Use the links to download/commands to get the links")
        embed.add_field(name="Python 2.6.0", value="https://www.python.org/downloads/release/python-260/")
        embed.add_field(name="Python 2.6.1", value="https://www.python.org/downloads/release/python-261/")
        embed.add_field(name="Python 2.6.2", value="https://www.python.org/downloads/release/python-262/")
        embed.add_field(name="Python 2.6.3", value="https://www.python.org/downloads/release/python-263/")
        embed.add_field(name="Python 2.6.4", value="https://www.python.org/downloads/release/python-264/")
        embed.add_field(name="Python 2.6.5", value="https://www.python.org/downloads/release/python-265/")
        embed.add_field(name="Python 2.6.6", value="https://www.python.org/downloads/release/python-266/")
        embed.add_field(name="Python 2.6.7", value="https://www.python.org/downloads/release/python-267/")
        embed.add_field(name="Python 2.6.8", value="https://www.python.org/downloads/release/python-268/")
        embed.add_field(name="Python 2.6.9", value="https://www.python.org/downloads/release/python-269/")
        await message.channel.send(content=None, embed=embed)
    ...
    ...
    if message.content == "!python-2.7":
        embed = discord.Embed(title="Python 2.7 Downloads", description="Use the links to download/commands to get the links")
        embed.add_field(name="Python 2.7.0", value="https://www.python.org/downloads/release/python-270/")
        embed.add_field(name="Python 2.7.1", value="https://www.python.org/downloads/release/python-271/")
        embed.add_field(name="Python 2.7.2", value="https://www.python.org/downloads/release/python-272/")
        embed.add_field(name="Python 2.7.3", value="https://www.python.org/downloads/release/python-273/")
        embed.add_field(name="Python 2.7.4", value="https://www.python.org/downloads/release/python-274/")
        embed.add_field(name="Python 2.7.5", value="https://www.python.org/downloads/release/python-275/")
        embed.add_field(name="Python 2.7.6", value="https://www.python.org/downloads/release/python-276/")
        embed.add_field(name="Python 2.7.7", value="https://www.python.org/downloads/release/python-277/")
        embed.add_field(name="Python 2.7.8", value="https://www.python.org/downloads/release/python-278/")
        embed.add_field(name="Python 2.7.9", value="https://www.python.org/downloads/release/python-279/")
        embed.add_field(name="Python 2.7.10", value="https://www.python.org/downloads/release/python-2710/")
        embed.add_field(name="Python 2.7.11", value="https://www.python.org/downloads/release/python-2711/")
        embed.add_field(name="Python 2.7.12", value="https://www.python.org/downloads/release/python-2712/")
        embed.add_field(name="Python 2.7.13", value="https://www.python.org/downloads/release/python-2713/")
        embed.add_field(name="Python 2.7.14", value="https://www.python.org/downloads/release/python-2714/")
        embed.add_field(name="Python 2.7.15", value="https://www.python.org/downloads/release/python-2715/")
        embed.add_field(name="Python 2.7.16", value="https://www.python.org/downloads/release/python-2716/")
        embed.add_field(name="Python 2.7.17", value="https://www.python.org/downloads/release/python-2717/")
        embed.add_field(name="Python 2.7.18", value="https://www.python.org/downloads/release/python-2718/")
        await message.channel.send(content=None, embed=embed)
    ...
    
    ...
    if message.content == "!python-3.1":
        embed = discord.Embed(title="Python 3.1 Downloads", description="Use the links to download/commands to get the links")
        embed.add_field(name="Python 3.1.0", value="https://www.python.org/downloads/release/python-31/")
        embed.add_field(name="Python 3.1.1", value="https://www.python.org/downloads/release/python-311/")
        embed.add_field(name="Python 3.1.2", value="https://www.python.org/downloads/release/python-312/")
        embed.add_field(name="Python 3.1.3", value="https://www.python.org/downloads/release/python-313/")
        embed.add_field(name="Python 3.1.4", value="https://www.python.org/downloads/release/python-314/")
        embed.add_field(name="Python 3.1.5", value="https://www.python.org/downloads/release/python-315/")
        await message.channel.send(content=None, embed=embed)
    ...
    
    ...
    if message.content == "!python-3.2":
        embed = discord.Embed(title="Python 3.2 Downloads", description="Click the links to download")
        embed.add_field(name="Python 3.2.0", value="https://www.python.org/downloads/release/python-32/")
        embed.add_field(name="Python 3.2.1", value="https://www.python.org/downloads/release/python-321/")
        embed.add_field(name="Python 3.2.2", value="https://www.python.org/downloads/release/python-322/")
        embed.add_field(name="Python 3.2.3", value="https://www.python.org/downloads/release/python-323/")
        embed.add_field(name="Python 3.2.4", value="https://www.python.org/downloads/release/python-324/")
        embed.add_field(name="Python 3.2.5", value="https://www.python.org/downloads/release/python-325/")
        embed.add_field(name="Python 3.2.6", value="https://www.python.org/downloads/release/python-326/")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!python-3.3":
        embed = discord.Embed(title="Python 3.3 Downloads", description="Click the links to download")
        embed.add_field(name="Python 3.3.0", value="https://www.python.org/downloads/release/python-33/")
        embed.add_field(name="Python 3.3.1", value="https://www.python.org/downloads/release/python-331/")
        embed.add_field(name="Python 3.3.2", value="https://www.python.org/downloads/release/python-332/")
        embed.add_field(name="Python 3.3.3", value="https://www.python.org/downloads/release/python-333/")
        embed.add_field(name="Python 3.3.4", value="https://www.python.org/downloads/release/python-334/")
        embed.add_field(name="Python 3.3.5", value="https://www.python.org/downloads/release/python-335/")
        embed.add_field(name="Python 3.3.6", value="https://www.python.org/downloads/release/python-336/")
        embed.add_field(name="Python 3.3.7", value="https://www.python.org/downloads/release/python-337/")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!python-3.4":
        embed = discord.Embed(title="Python 3.4 Downloads", description="Click the links to download")
        embed.add_field(name="Python 3.4.0", value="https://www.python.org/downloads/release/python-34/")
        embed.add_field(name="Python 3.4.1", value="https://www.python.org/downloads/release/python-341/")
        embed.add_field(name="Python 3.4.2", value="https://www.python.org/downloads/release/python-342/")
        embed.add_field(name="Python 3.4.3", value="https://www.python.org/downloads/release/python-343/")
        embed.add_field(name="Python 3.4.4", value="https://www.python.org/downloads/release/python-344/")
        embed.add_field(name="Python 3.4.5", value="https://www.python.org/downloads/release/python-345/")
        embed.add_field(name="Python 3.4.6", value="https://www.python.org/downloads/release/python-346/")
        embed.add_field(name="Python 3.4.7", value="https://www.python.org/downloads/release/python-347/")
        embed.add_field(name="Python 3.4.8", value="https://www.python.org/downloads/release/python-348/")
        embed.add_field(name="Python 3.4.9", value="https://www.python.org/downloads/release/python-349/")
        embed.add_field(name="Python 3.4.10", value="https://www.python.org/downloads/release/python-3410/")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!python-3.5":
        embed = discord.Embed(title="Python 3.5 Downloads", description="Click the links to download")
        embed.add_field(name="Python 3.5.0", value="https://www.python.org/downloads/release/python-35/")
        embed.add_field(name="Python 3.5.1", value="https://www.python.org/downloads/release/python-351/")
        embed.add_field(name="Python 3.5.2", value="https://www.python.org/downloads/release/python-352/")
        embed.add_field(name="Python 3.5.3", value="https://www.python.org/downloads/release/python-353/")
        embed.add_field(name="Python 3.5.4", value="https://www.python.org/downloads/release/python-354/")
        embed.add_field(name="Python 3.5.5", value="https://www.python.org/downloads/release/python-355/")
        embed.add_field(name="Python 3.5.6", value="https://www.python.org/downloads/release/python-356/")
        embed.add_field(name="Python 3.5.7", value="https://www.python.org/downloads/release/python-357/")
        embed.add_field(name="Python 3.5.8", value="https://www.python.org/downloads/release/python-358/")
        embed.add_field(name="Python 3.5.9", value="https://www.python.org/downloads/release/python-359/")
        embed.add_field(name="Python 3.5.10", value="https://www.python.org/downloads/release/python-3510/")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!python-3.6":
        embed = discord.Embed(title="Python 3.6 Downloads", description="Click the links to download")
        embed.add_field(name="Python 3.6.0", value="https://www.python.org/downloads/release/python-36/")
        embed.add_field(name="Python 3.6.1", value="https://www.python.org/downloads/release/python-361/")
        embed.add_field(name="Python 3.6.2", value="https://www.python.org/downloads/release/python-362/")
        embed.add_field(name="Python 3.6.3", value="https://www.python.org/downloads/release/python-363/")
        embed.add_field(name="Python 3.6.4", value="https://www.python.org/downloads/release/python-364/")
        embed.add_field(name="Python 3.6.5", value="https://www.python.org/downloads/release/python-365/")
        embed.add_field(name="Python 3.6.6", value="https://www.python.org/downloads/release/python-366/")
        embed.add_field(name="Python 3.6.7", value="https://www.python.org/downloads/release/python-367/")
        embed.add_field(name="Python 3.6.8", value="https://www.python.org/downloads/release/python-368/")
        embed.add_field(name="Python 3.6.9", value="https://www.python.org/downloads/release/python-369/")
        embed.add_field(name="Python 3.6.10", value="https://www.python.org/downloads/release/python-3610/")
        embed.add_field(name="Python 3.6.11", value="https://www.python.org/downloads/release/python-3611/")
        embed.add_field(name="Python 3.6.12", value="https://www.python.org/downloads/release/python-3612/")
        embed.add_field(name="Python 3.6.13", value="https://www.python.org/downloads/release/python-3613/")
        embed.add_field(name="Python 3.6.14", value="https://www.python.org/downloads/release/python-3614/")
        embed.add_field(name="Python 3.6.15", value="https://www.python.org/downloads/release/python-3615/")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!python-3.7":
        embed = discord.Embed(title="Python 3.7 Downloads", description="Click the links to download")
        embed.add_field(name="Python 3.7.0", value="https://www.python.org/downloads/release/python-37/")
        embed.add_field(name="Python 3.7.1", value="https://www.python.org/downloads/release/python-371/")
        embed.add_field(name="Python 3.7.2", value="https://www.python.org/downloads/release/python-372/")
        embed.add_field(name="Python 3.7.3", value="https://www.python.org/downloads/release/python-373/")
        embed.add_field(name="Python 3.7.4", value="https://www.python.org/downloads/release/python-374/")
        embed.add_field(name="Python 3.7.5", value="https://www.python.org/downloads/release/python-375/")
        embed.add_field(name="Python 3.7.6", value="https://www.python.org/downloads/release/python-376/")
        embed.add_field(name="Python 3.7.7", value="https://www.python.org/downloads/release/python-377/")
        embed.add_field(name="Python 3.7.8", value="https://www.python.org/downloads/release/python-378/")
        embed.add_field(name="Python 3.7.9", value="https://www.python.org/downloads/release/python-379/")
        embed.add_field(name="Python 3.7.10", value="https://www.python.org/downloads/release/python-3710/")
        embed.add_field(name="Python 3.7.11", value="https://www.python.org/downloads/release/python-3711/")
        embed.add_field(name="Python 3.7.12", value="https://www.python.org/downloads/release/python-3712/")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!python-3.8":
        embed = discord.Embed(title="Python 3.8 Downloads", description="Click the links to download")
        embed.add_field(name="Python 3.8.0", value="https://www.python.org/downloads/release/python-38/")
        embed.add_field(name="Python 3.8.1", value="https://www.python.org/downloads/release/python-381/")
        embed.add_field(name="Python 3.8.2", value="https://www.python.org/downloads/release/python-382/")
        embed.add_field(name="Python 3.8.3", value="https://www.python.org/downloads/release/python-383/")
        embed.add_field(name="Python 3.8.4", value="https://www.python.org/downloads/release/python-384/")
        embed.add_field(name="Python 3.8.5", value="https://www.python.org/downloads/release/python-385/")
        embed.add_field(name="Python 3.8.6", value="https://www.python.org/downloads/release/python-386/")
        embed.add_field(name="Python 3.8.7", value="https://www.python.org/downloads/release/python-387/")
        embed.add_field(name="Python 3.8.8", value="https://www.python.org/downloads/release/python-388/")
        embed.add_field(name="Python 3.8.9", value="https://www.python.org/downloads/release/python-389/")
        embed.add_field(name="Python 3.8.10", value="https://www.python.org/downloads/release/python-3810/")
        embed.add_field(name="Python 3.8.11", value="https://www.python.org/downloads/release/python-3811/")
        embed.add_field(name="Python 3.8.12", value="https://www.python.org/downloads/release/python-3812/")
        await message.channel.send(content=None, embed=embed)
    ...

    ...
    if message.content == "!python-3.9":
        embed = discord.Embed(title="Python 3.9 Downloads", description="Click the links to download")
        embed.add_field(name="Python 3.9.0", value="https://www.python.org/downloads/release/python-39/")
        embed.add_field(name="Python 3.9.1", value="https://www.python.org/downloads/release/python-391/")
        embed.add_field(name="Python 3.9.2", value="https://www.python.org/downloads/release/python-392/")
        embed.add_field(name="Python 3.9.3", value="https://www.python.org/downloads/release/python-393/")
        embed.add_field(name="Python 3.9.4", value="https://www.python.org/downloads/release/python-394/")
        embed.add_field(name="Python 3.9.5", value="https://www.python.org/downloads/release/python-395/")
        embed.add_field(name="Python 3.9.6", value="https://www.python.org/downloads/release/python-396/")
        embed.add_field(name="Python 3.9.7", value="https://www.python.org/downloads/release/python-397/")
        await message.channel.send(content=None, embed=embed)
    ...
client.run('token')