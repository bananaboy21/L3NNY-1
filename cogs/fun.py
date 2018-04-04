import discord
import sys
import os
import io
import asyncio
import aiohttp
import random
import json
from discord.ext import commands


class fun:
    def __init__(self, bot):
        self.bot = bot
        
        
        
        
        
        
    @commands.command()
    async def meme(self, ctx, user: discord.Member):
        """a meme animation"""
        msg = await ctx.send(f"i")
        await asyncio.sleep(2)
        await msg.edit(content="im")
        await asyncio.sleep(2)
        await msg.edit(content="im a")
        await asyncio.sleep(2)
        await msg.edit(content="im a M")
        await asyncio.sleep(2)
        await msg.edit(content="im a ME")
        await asyncio.sleep(2)
        await msg.edit(content="im a MEM")
        await asyncio.sleep(2)
        await msg.edit(content="im a MEME")
        await asyncio.sleep(2)
        await msg.edit(content="IM A MEME BOYZZZZ LMAOOOO XDDD")
        await asyncio.sleep(4)
        await msg.edit(content=f"lmao xd")   
            
    
    @commands.command()
    @commands.has_permissions(administrator = True)
    async def msg(self, ctx, user: discord.Member, *, msg: str):
        """Message someone as me!"""
        try:
            await user.send(msg)
            await ctx.message.delete()            
            await ctx.send("The message has been sent! hehehe....")
        except commands.MissingPermissions:
            await ctx.send("rip. you dont have enough perms. xd")
        except:
            await ctx.send(":x: Format: _msg (user tag) (messgae)")
    
    @commands.command()
    async def serverinfo(self, ctx):
        """bacically server info"""
        guild = ctx.guild 
        roles = [x.name for x in guild.roles] 
        role_length = len(roles)
        roles = ', '.join(roles)
        channels = len(guild.channels)
        time = str(guild.created_at.strftime("%b %m, %Y, %A, %I:%M %p")) 

        embed = discord.Embed(description="-", title='Server Info', colour=passcolor)
        if guild.icon_url:
            embed.set_thumbnail(url=guild.icon_url)
        else:
            embed.set_thumbnail(url="https://cdn.discordapp.com/embed/avatars/0.png")
        embed.add_field(name='__Server __', value=str(guild.name))
        embed.add_field(name='__Server ID__', value=str(guild.id))
        embed.add_field(name='__Owner__', value=str(guild.owner))
        embed.add_field(name='__Owner ID__', value=guild.owner_id) 
        embed.add_field(name='__Members__', value=str(guild.member_count))
        embed.add_field(name='__Text/Voice Channels__', value=str(channels))
        embed.add_field(name='__Region__', value='%s' % str(guild.region))
        embed.add_field(name='__ Total Roles__', value='%s' % str(role_length))
        embed.add_field(name='__Roles__', value='%s' % str(roles))
        embed.set_footer(text='Created - %s' % time)

        await ctx.send(embed=embed)
    
    
def setup(bot):
    bot.add_cog(fun(bot))
