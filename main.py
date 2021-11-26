from discord.ext import commands
import discord

bot = commands.Bot(command_prefix = "!")

@bot.command()
async def 웹훅생성(ctx):
    if ctx.author.guild_permissions.administrator:
        webhook = await ctx.channel.create_webhook(name="hook bot")
        embed=discord.Embed(title="✅생성완료", description="성공적으로 생성되었습니다!")
        embed.add_field(name="웹훅링크", value=f"{webhook.url}", inline=False)
        await ctx.author.send(embed=embed)
        embed=discord.Embed(title="✅생성성공", description="개인메세지를 확인해주세요!")
        embed.set_footer(text="만약 오지않았다면 개인메시지를 허용해주세요!")
        await ctx.send(embed=embed)
    else:
        embed=discord.Embed(title="❎생성실패", description="당신은 권한이 없습니다!")
        await ctx.send(embed=embed)

bot.run("ㅌㅋㅌㅋ")
