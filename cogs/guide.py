import discord
from discord.ext import commands
from discord import Option


# Re-region embed
region_emb = discord.Embed(
    title="🌍 REREGION (Change Region)\n",
    description="**How to Change a Save's Region (Reregion)**",
)
region_emb.add_field(
        name="**⚠️ STEP 1: SETUP (DO THIS FIRST)**",
        value="-  Click this link to go to the correct channel: https://discord.com/channels/1130158543237030049/1146892703028760696\n- Look at the **Members List** on the right side of the screen. Find a bot that has a green dot (Online).\n3. Create a **New Thread** with that bot, or go to a thread you already created with it.\n4. Do all the steps below inside that thread.\n",
        inline=False,
    )
region_emb.add_field(
        name="**Step 2: Start the Command**",
        value="• Type `/reregion` in the message box and press Enter.\n• A menu will pop up. In the **playstation_id** box, type your exact PSN Username.\n• You can completely ignore the `shared_gd_link` box. Just leave it empty.\n",
        inline=False,
    )
region_emb.add_field(
        name="**Step 3: Uploading Your Files**",
        value="• The bot will ask you to upload files two times.\n• **First Request:** It will ask for \"bin and non bin.\" Upload the save file that came **from your own console** (the one currently on your USB).\n• **Second Request:** After a moment, it will ask for files again. This time, upload the save file you got **from the internet** (the one you want to use).\n",
        inline=False,
    )
region_emb.add_field(
        name="**Step 4: Putting it on the Console**",
        value="• The bot will send you a download link or a file. Download it.\n• **Unzip** the file (Right-click > Extract All).\n• Inside, you will see a folder named `PS4`. Copy this folder.\n• Paste it onto the main screen (root) of your USB drive. If it asks to replace files, click **Yes**.\n• Plug the USB into your PlayStation.\n• Go to **Settings** -> **Application Saved Data Management** -> **Saved Data on USB Storage** -> **Copy to System Storage**.\n",
        inline=False,
    )
region_emb.add_field(
        name="Congratulations 🎉",
        value="You have successfully re-regioned a savefile!",
        inline=False,
    )
# Resign Embed
resign_emb = discord.Embed(
    title="✍️ RESIGN (Make a Save Work on Your Account)",
    description="**How to Resign a Save (Make it Yours)**\n",
)
resign_emb.add_field(
        name="**⚠️ STEP 1: SETUP (DO THIS FIRST)**",
        value="- Click this link to go to the correct channel: https://discord.com/channels/1130158543237030049/1146892703028760696\n2. Look at the **Members List** on the right side of the screen. Find a bot that has a green dot (Online).\n3. Create a **New Thread** with that bot, or go to a thread you already created with it.\n4. Do all the steps below inside that thread.\n",
        inline=False,
    )
resign_emb.add_field(
        name="**Step 2: Start the Command**",
        value="• Type `/resign` in the message box and press Enter.\n• In the **playstation_id** box, type your exact PSN Username.\n• You can ignore the `shared_gd_link` box.\n",
        inline=False,
    )
resign_emb.add_field(
        name="**Step 3: Uploading Your Files**",
        value="• The bot will say something like \"Upload bin and non bin.\"\n• Drag and drop the save files you want to fix (resign) into the chat and send them.\n",
        inline=False,
    )
resign_emb.add_field(
        name="**4. Putting it on the Console**",
        value="• The bot will send you a finished file. Download it.\n• **Unzip** the file (Right-click > Extract All).\n• Inside, you will see a folder named `PS4`. Copy this folder.\n• Paste it onto your USB drive. If it asks to replace/overwrite, say **Yes**.\n• **For PS4 Users:** Go to Settings -> Saved Data -> USB -> Copy to System.\n• **For PS5 Users:** Go to Settings -> Saved Data (PS4) -> USB Drive -> Copy to Console.\n",
        inline=False,
    )
resign_emb.add_field(
        name="Congratulation 🎉",
        value="You have successfully resigned a savefile!",
        inline=False,
    )
# Decrypt embed
decrypt_emb = discord.Embed(
    title="🔓 DECRYPT (Unlock Save for Cheating/Editing)",
    description="**How to Decrypt a Save (Open it for Editing)**",
)
decrypt_emb.add_field(
        name="**⚠️ STEP 1: SETUP (DO THIS FIRST)**",
        value="-  Click this link to go to the correct channel: https://discord.com/channels/1130158543237030049/1146892703028760696\n2. Look at the **Members List** on the right side of the screen. Find a bot that has a green dot (Online).\n3. Create a **New Thread** with that bot, or go to a thread you already created with it.\n4. Do all the steps below inside that thread.\n",
        inline=False,
    )
decrypt_emb.add_field(
        name="**Step 2: Start the Command**",
        value="• Type `/decrypt` and make sure you select the command for the specific bot you are using.\n• In the **sce_sys** box, select `False`.\n• Ignore the `shared_gd_link` box.\n",
        inline=False,
    )
decrypt_emb.add_field(
        name="**Step 3: Uploading Your Files**",
        value="• When the bot asks for \"bin and non bin,\" upload the save files you want to mod.\n• **Important:** If the bot asks if you want the \"Second Layer\" decrypted, choose **Decrypted**. This is required if you want to use a Save Editor tool.\n",
        inline=False,
    )
decrypt_emb.add_field(
        name="**Step 4: Finish**",
        value="• The bot will give you a file. Download it.\n• You can now open this file in your Save Editor, Hex Editor, or Modding Tool.\n",
        inline=False,
    )
decrypt_emb.add_field(
        name="Congratulations 🎉",
        value="You have successfully decrypted your savefile!",
        inline=False,
    )
#Encrypt embed
encrypt_emb = discord.Embed(
    title="🔒 ENCRYPT (Lock Save After Editing)",
    description="**How to Encrypt (Lock the Save So It Works Again)**",
)
encrypt_emb.add_field(
        name="**⚠️ STEP 1: SETUP (DO THIS FIRST)**",
        value="- Click this link to go to the correct channel: https://discord.com/channels/1130158543237030049/1146892703028760696\n2. Look at the **Members List** on the right side of the screen. Find a bot that has a green dot (Online).\n3. Create a **New Thread** with that bot, or go to a thread you already created with it.\n4. Do all the steps below inside that thread.\n",
        inline=False,
    )
encrypt_emb.add_field(
        name="**Step 2: Start the Command**",
        value="• Type `/encrypt` and select the correct bot.\n• set **upload_individually** to `False`.\n• set **include_sce_sys** to `False`.\n• set **playstation_id** to your PSN Username.\n• Ignore the other boxes.\n",
        inline=False,
    )
encrypt_emb.add_field(
        name="**Step 3: Upload Step 1 (The Original)**",
        value="• The bot will ask for \"bin and non bin\" first.\n• Upload a normal, working save file from your USB (one you have NOT edited). This acts as a \"container\" for your cheats.",
        inline=False,
    )
encrypt_emb.add_field(
        name="**Step 4: Upload Step 2 (The Modded File)**",
        value="• The bot will now ask for the **decrypted** files.\n• **STOP AND READ:** Look at the filename the bot is asking for. You MUST rename your modded file to match that name exactly.\n• Once renamed, upload your modded file.",
        inline=False,
    )
encrypt_emb.add_field(
        name="**Step 5: Putting it on the Console**",
        value="• Download the file the bot gives you and **Unzip** it.\n• Copy the `PS4` folder to your USB drive. Overwrite if asked.\n• Plug the USB into your console and copy the save back to your System Storage.\n\n",
        inline=False,
    )
encrypt_emb.add_field(
        name="Congratulation 🎉",
        value="You have successfully encrypted your savefiles!",
        inline=False,
    )


# account id embed

accountid_embed = discord.Embed(
    title="🔢 Account Id Guide",
    description="This guide will show you how to manually get your account id for your psn account for use with the `/store_accountid` command.",
)
accountid_embed.set_image(url="https://github.com/That-Kidd/ps-resources/blob/main/crc/pics/accid_example.png?raw=true")
accountid_embed.set_footer(
        text="Made by That-Kidd",
    )
accountid_embed.add_field(
        name="Step 1. On your console",
        value="go to `Settings`>`Application Saved Data Management`>`Saved Data in System Storage`>`Copy to USB Storage Device`\n\nMake sure to copy any save game data to your usb device",
        inline=False,
    )
accountid_embed.add_field(
        name="Step 2. On your PC",
        value="Plug your USB into your computer. \nOn the root of your USB you should see a folder called `PS4`. \nOpen this folder",
        inline=False,
    )
accountid_embed.add_field(
        name="Step 3. On your PC",
        value="Now you should see a `SAVEDATA` folder\n\n you need to open this folder as well.",
        inline=False,
    )
accountid_embed.add_field(
        name="Step 4. On your PC",
        value="You should see a folder named `XXXXXXXXXXXXXXXX`\nIt should be 16-digit long. \nThis is the account id.",
        inline=False,
    )
accountid_embed.add_field(
        name="Example:",
        value="`2ec30469d34ff737` is the Account ID in the picture below!",
        inline=False,
    )

class guide(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot       
    @discord.slash_command(description="Guides on the bot")
    async def guide(self, ctx: discord.ApplicationContext, topic:Option(choices=['Resign', 'Decrypt', 'Encrypt', 'Reregion', 'Account ID'], description='Which guide do you want?')) -> None: # type: ignore
        if topic == 'Resign':
            embed = resign_emb
        elif topic == 'Decrypt':
            embed = decrypt_emb
        elif topic == 'Encrypt':
            embed = encrypt_emb
        elif topic == 'Reregion':
            embed = region_emb
        elif topic == 'Account ID':
            embed = accountid_embed
        else:
            pass #eventually put an error
        await ctx.respond(embed=embed)


def setup(bot: commands.Bot) -> None:
    bot.add_cog(guide(bot))