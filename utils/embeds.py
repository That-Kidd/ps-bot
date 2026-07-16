import discord
from enum import Enum
from utils.constants import VERSION, OTHER_TIMEOUT, BLACKLIST_MESSAGE

class Color(Enum):
    DEFAULT = 7475128
    GREEN = 0x22EA0D
    RED = 0xF42B00
    YELLOW = 0xD2D624

class Embed_t(Enum):
    DEFAULT_FOOTER = f"Hosted by That-Kidd. ({VERSION})"
    QR_FOOTER1 = "Respond with the number of your desired game, or type 'EXIT' to quit."
    QR_FOOTER2 = "Respond with the number of your desired save, or type 'BACK' to go to the game menu."

embUtimeout = discord.Embed(
    title="Upload alert: Error",
    description="Time's up! You didn't attach any files.",
    colour=Color.DEFAULT.value
)
embUtimeout.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

embhttp = discord.Embed(
    title="HttpError",
    description="Are you sure that you uploaded binary content?",
    colour=Color.DEFAULT.value
)
embhttp.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

embEncrypted1 = discord.Embed(
    title="Resigning Process: Upload Encrypted Saves",
    description="Please upload at least two encrypted save files (PS4 save). \nThis is the `.bin` and non bin `file`\n\n Or type `EXIT` to cancel the command.",
    image="https://cdn.discordapp.com/attachments/1381758125517836288/1381758592595529881/image.png?ex=6848ae78&is=68475cf8&hm=d41d012f35316c1dd822d2cbf673b78190f8b619f736dff9967c82b316b48ebe&",
    colour=Color.DEFAULT.value
)
embEncrypted1.add_field(
        name="Note:",
        value="- These files are usually located in a folder named: `CUSAXXXXX`\n- You can also supply the [Google Drive Link](<https://youtu.be/6wJDeWYuiFE?si=FtHvsQdfxids4lsK>) containing your files.\n- You can also supply multiple pairs of bin and files. Just make sure you have the matching pair.",
        inline=False,
    )
embEncrypted1.set_footer(text=Embed_t.DEFAULT_FOOTER.value)
embEncrypted1.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

embDecrypt1 = discord.Embed(
    title="Decrypt Process: Upload Encrypted Save",
    description="Please upload at least two encrypted save files (PS4 save). \nThis is the `.bin` and non bin `file`\n\n Or type `EXIT` to cancel the command.",
    image="https://cdn.discordapp.com/attachments/1381758125517836288/1381758592595529881/image.png?ex=6848ae78&is=68475cf8&hm=d41d012f35316c1dd822d2cbf673b78190f8b619f736dff9967c82b316b48ebe&",
    colour=Color.DEFAULT.value
)
embDecrypt1.add_field(
        name="Note:",
        value="- These files are usually located in a folder named: `CUSAXXXXX`\n- You can also supply the [Google Drive Link](<https://youtu.be/6wJDeWYuiFE?si=FtHvsQdfxids4lsK>) containing your files.\n- You can also supply multiple pairs of bin and files. Just make sure you have the matching pair.",
        inline=False,
    )
embDecrypt1.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

emb14 = discord.Embed(
    title="Decryption process: Provide Encrypted save for re-encryption ",
    description="Please upload at least two encrypted save files (PS4 save). \nThis is the `.bin` and non bin `file`\n\n Or type `EXIT` to cancel the command.",
    image="https://cdn.discordapp.com/attachments/1381758125517836288/1381758592595529881/image.png?ex=6848ae78&is=68475cf8&hm=d41d012f35316c1dd822d2cbf673b78190f8b619f736dff9967c82b316b48ebe&",colour=Color.DEFAULT.value
)
emb14.add_field(
        name="Note:",
        value="- These files are usually located in a folder named: `CUSAXXXXX`\n- You can also supply the [Google Drive Link](<https://youtu.be/6wJDeWYuiFE?si=FtHvsQdfxids4lsK>) containing your files.\n- You can also supply multiple pairs of bin and files. Just make sure you have the matching pair.",
        inline=False,
    )
emb14.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

emb20 = discord.Embed(
    title="Re-region process: Upload encrypted files from the FOREIGN region",
    description="Please upload at least two encrypted save files (PS4 save). \nThis is the `.bin` and non bin `file`\n\n Or type `EXIT` to cancel the command.",
    image="https://cdn.discordapp.com/attachments/1381758125517836288/1381758592595529881/image.png?ex=6848ae78&is=68475cf8&hm=d41d012f35316c1dd822d2cbf673b78190f8b619f736dff9967c82b316b48ebe&",
    colour=Color.DEFAULT.value
)
emb20.add_field(
        name="Note:",
        value="- These files are usually located in a folder named: `CUSAXXXXX`\n- You can also supply the [Google Drive Link](<https://youtu.be/6wJDeWYuiFE?si=FtHvsQdfxids4lsK>) containing your files.\n- You can also supply multiple pairs of bin and files. Just make sure you have the matching pair.",
        inline=False,
    )
emb20.add_field(name='THIS IS THE SAVE THAT YOU WANT TO CHANGE THE REGION OF!', value='This is the save you want to region change')
emb20.set_footer(text=Embed_t.DEFAULT_FOOTER.value)
emb21 = discord.Embed(
    title="Re-region process: Upload encrypted files from YOUR region",
    description="Please attach two encrypted savefiles that you want to upload (.bin and non bin). Or type 'EXIT' to cancel command.",
    colour=Color.DEFAULT.value
)
emb21.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

embpng = discord.Embed(
    title="PNG Process",
    description="Please attach at least two encrypted savefiles that you want to upload (.bin and non bin). Or type 'EXIT' to cancel command.",
    colour=Color.DEFAULT.value
)
embpng.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

emb8 = discord.Embed(
    title="Error: PSN username",
    description=f"{{msg}}. You have {OTHER_TIMEOUT} seconds to reply with your account ID instead.\nOr type 'EXIT' to cancel command.",
    colour=Color.YELLOW.value
)
emb8.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

embnt = discord.Embed(
    title="Error: Time limit reached",
    description="You did not send your account ID in time.",
    colour=Color.DEFAULT.value
)
embnt.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

embvalidpsn = discord.Embed(
    title="Obtained: PSN username",
    description="Your input was a valid PSN username.",
    colour=Color.DEFAULT.value
)
embvalidpsn.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

embinit = discord.Embed(
    title="Thread creator",
    description="Click button to get started!\nYou can also use old threads that you have created with the bot.",
    colour=Color.DEFAULT.value
)
embinit.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

embTitleChange = discord.Embed(
    title="Change title: Upload",
    description="Please attach at least two encrypted savefiles that you want to upload (.bin and non bin). Or type 'EXIT' to cancel command.",
    colour=Color.DEFAULT.value
)
embTitleChange.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

embTitleErr = discord.Embed(
    title="Change title: Error",
    description="Please select a maintitle or subtitle.",
    colour=Color.DEFAULT.value
)
embTitleErr.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

embTimedOut = discord.Embed(
    title="Timed out!",
    description="Sending file.",
    colour=Color.DEFAULT.value
)
embTimedOut.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

embDone_G = discord.Embed(
    title="Success",
    description=f"Please report any errors.",
    colour=Color.DEFAULT.value
)
embDone_G.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

emb_upl_savegame = discord.Embed(
    title="Upload files",
    description=f"Please attach at least 1 savefile, it must be fully decrypted. Or type 'EXIT' to cancel command.",
    colour=Color.DEFAULT.value
)
emb_upl_savegame.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

loadSFO_emb = discord.Embed(
    title="Initializing",
    description="Loading param.sfo...",
    color=Color.DEFAULT.value
)
loadSFO_emb.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

finished_emb = discord.Embed(title="Finished", color=Color.DEFAULT.value)
finished_emb.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

loadkeyset_emb = discord.Embed(
    title="Initializing",
    description="Obtaining keyset...",
    color=Color.DEFAULT.value
)
loadkeyset_emb.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

working_emb = discord.Embed(
    title="Working...",
    color=Color.DEFAULT.value
)
working_emb.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

retry_emb = discord.Embed(
    title="Please try again.",
    color=Color.DEFAULT.value
)
retry_emb.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

blacklist_emb = discord.Embed(
    title=BLACKLIST_MESSAGE,
    color=Color.RED.value
)
blacklist_emb.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

embChannelError = discord.Embed(
    title="Error",
    description="Invalid channel!",
    colour=Color.DEFAULT.value
)
embChannelError.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

cancel_notify_emb = discord.Embed(
    title="Notice",
    description="You can 'EXIT' if you want to cancel while the files are uploading.",
    color=Color.DEFAULT.value
)
cancel_notify_emb.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

gd_upl_progress_emb = discord.Embed(
    title="Google Drive Upload",
    color=Color.DEFAULT.value
)
gd_upl_progress_emb.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

gd_maintenance_emb = discord.Embed(
    title="Google Drive maintenance",
    description="Please try again later.",
    colour=Color.YELLOW.value
)
gd_maintenance_emb.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

embpng1 = discord.Embed(
    title="PNG process: Initializng",
    description="Your save (**{savename}**) is being mounted, (save {j}/{savecount}, batch {i}/{batches}), please wait...\nSend 'EXIT' to cancel.",
    colour=Color.DEFAULT.value
)
embpng1.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

embpng2 = discord.Embed(
    title="PNG process: Initializng",
    description="Your save (**{savename}**) has mounted, (save {j}/{savecount}, batch {i}/{batches}), please wait...\nSend 'EXIT' to cancel.",
    colour=Color.DEFAULT.value
)
embpng2.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

embpngs = discord.Embed(
    title="PNG process: Successful",
    description="Altered the save png and resigned **{savename}** (save {j}/{savecount}, batch {i}/{batches}).",
    colour=Color.DEFAULT.value
)
embpngs.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

embPdone = discord.Embed(
    title="PNG process: Successful",
    description=(
        "Altered the save png of **{printed}** and resigned to **{id}** (batch {i}/{batches}).\n"
        "Uploading file...\n"
        "If file is being uploaded to Google Drive, you can send 'EXIT' to cancel."
    ),
    colour=Color.DEFAULT.value
)
embPdone.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

embTitleChange1 = discord.Embed(
    title="Title altering process: Initializng",
    description="Processing {savename} (save {j}/{savecount}, batch {i}/{batches}), please wait...\nSend 'EXIT' to attempt cancelling.",
    colour=Color.DEFAULT.value
)
embTitleChange1.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

embTitleSuccess = discord.Embed(
    title="Title altering process: Successful",
    description="Altered the save titles of **{savename}** (save {j}/{savecount}, batch {i}/{batches}).",
    colour=Color.DEFAULT.value
)
embTitleSuccess.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

embTdone = discord.Embed(
    title="Title altering process: Successful",
    description=(
        "Altered the save titles of **{printed}**, and resigned to **{id}** (batch {i}/{batches}).\n"
        "Uploading file...\n"
        "If file is being uploaded to Google Drive, you can send 'EXIT' to cancel."
    ),
    colour=Color.DEFAULT.value
)
embTdone.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

emb_conv_upl = discord.Embed(
    title="Conversion process: {game}",
    description="Please attach atleast 1 savefile. Or type 'EXIT' to cancel command.",
    colour=Color.DEFAULT.value
    )
emb_conv_upl.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

emb_conv_choice = discord.Embed(
    title="Converter: Choice ({basename})",
    description="Could not recognize the platform of the save, please choose what platform to convert the save to (file {j}/{count_entry}, batch {i}/{batches}).",
    colour=Color.DEFAULT.value
)
emb_conv_choice.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

embCDone1 = discord.Embed(
    title="TIMED OUT!",
    colour=Color.DEFAULT.value
)
embCDone1.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

embCDone2 = discord.Embed(
    title="ERROR!",
    description="Invalid save!",
    colour=Color.RED.value
)
embCDone2.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

embCDone3 = discord.Embed(
    title="Success",
    description="{result}\n**{basename}** (file {j}/{count_entry}, batch {i}/{batches}).",
    colour=Color.DEFAULT.value
)
embCDone3.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

embconvCompleted = discord.Embed(
    title="Success!",
    description=(
        "Converted **{finished_files}** (batch {i}/{batches}).\n"
        "Uploading file...\n"
        "If file is being uploaded to Google Drive, you can send 'EXIT' to cancel."
    ),
    colour=Color.DEFAULT.value
)
embconvCompleted.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

embSceSys = discord.Embed(
    title="Upload: sce_sys contents\n{savename}",
    description="Please attach the sce_sys files you want to upload. Or type 'EXIT' to cancel command.",
    colour=Color.DEFAULT.value
)
embSceSys.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

embgs = discord.Embed(
    title="Upload: Gamesaves\n{savename}",
    description=(
        "Please attach the gamesave files you want to upload.\n"
        "**FOLLOW THESE INSTRUCTIONS CAREFULLY**\n\n"
        "For **Discord uploads** rename the files according to the path they are going to have inside the savefile using the value '{splitvalue}'. For example the file 'savedata' inside the data directory would be called 'data{splitvalue}savedata'.\n\n"
        "For **Google Drive uploads** just create the directories on the drive and send the folder link from root, it will be recursively downloaded.\n\n"
        "*Or type 'EXIT' to cancel command.*"
    ),
    colour=Color.DEFAULT.value
)
embgs.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

embsl = discord.Embed(
    title="Gamesaves: Second layer\n{displaysave}",
    description="Checking for supported second layer encryption/compression...",
    colour=Color.DEFAULT.value
)
embsl.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

embc = discord.Embed(
    title="Processing",
    description="Creating {savename}...",
    colour=Color.DEFAULT.value
)
embc.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

embCRdone = discord.Embed(
    title="Creation process: Successful",
    description=(
        "**{savename}** created & resigned to **{id}**.\n"
        "Uploading file...\n"
        "If file is being uploaded to Google Drive, you can send 'EXIT' to cancel."
    ),
    colour=Color.DEFAULT.value
)
embCRdone.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

emb11 = discord.Embed(
    title="Decryption process: Initializing",
    description="Mounting {savename} (save {j}/{savecount}, batch {i}/{batches}), please wait...\nSend 'EXIT' to cancel.",
    colour=Color.DEFAULT.value
)
emb11.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

emb_dl = discord.Embed(
    title="Decryption process: Downloading",
    description="{savename} mounted (save {j}/{savecount}, batch {i}/{batches}), downloading decrypted savefile...\nSend 'EXIT' to cancel.",
    colour=Color.DEFAULT.value
)
emb_dl.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

emb13 = discord.Embed(
    title="Decryption process: Successful",
    description="Downloaded the decrypted save of **{savename}** (save {j}/{savecount}, batch {i}/{batches}).",
    colour=Color.DEFAULT.value
)
emb13.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

embDdone = discord.Embed(
    title="Decryption process: Successful",
    description=(
        "**{printed}** has been decrypted (batch {i}/{batches}).\n"
        "Uploading file...\n"
        "Send 'EXIT' to cancel."
    ),
    colour=Color.DEFAULT.value
)
embDdone.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

embmo = discord.Embed(
    title="Encryption process: Initializing",
    description="Mounting **{savename}**, (save {j}/{savecount}, batch {i}/{batches}), please wait...\nSend 'EXIT' to cancel.",
    colour=Color.DEFAULT.value
)
embmo.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

embmidComplete = discord.Embed(
    title="Encryption Processs: Successful",
    description="Encrypted **{dec_print}** into **{savename}** for **{id}** (save {j}/{savecount}, batch {i}/{batches}).",
    colour=Color.DEFAULT.value
)
embmidComplete.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

embencComplete = discord.Embed(
    title="Encryption process: Successful",
    description=(
        "Encrypted files into **{printed}** for **{id}** (batch {i}/{batches}).\n"
        "Uploading file...\n"
        "If file is being uploaded to Google Drive, you can send 'EXIT' to cancel."
    ),
    colour=Color.DEFAULT.value
)
embencComplete.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

keyset_emb = discord.Embed(
    title="Success",
    description="Keyset: {keyset}\nFW: {fw}",
    color=Color.DEFAULT.value
)
keyset_emb.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

embpingsuccess = discord.Embed(
    title=(
        "FTP: **{ftp_result}**\n"
        "CECIE: **{socket_result}**\n"
        "Active instances: **{instances_len}**/**{maximum_instances}**\n"
        "Latency: **{latency: .2f}** ms"
    ),
    colour=Color.GREEN.value)
embpingsuccess.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

embpingfail = discord.Embed(
    title=(
        "FTP: **{ftp_result}**\n"
        "CECIE: **{socket_result}**\n"
        "Active instances: **{instances_len}**/**{maximum_instances}**\n"
        "Latency: **{latency: .2f}** ms"
    ),
    colour=Color.RED.value)
embpingfail.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

embExit = discord.Embed(title="Exited.", colour=Color.DEFAULT.value)
embExit.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

embresb = discord.Embed(
    title="Resigning process: Encrypted",
    description="Your save (**{savename}**) is being resigned ({i}/{savecount}), please wait...\nSend 'EXIT' to cancel.",
    colour=Color.DEFAULT.value
)
embresb.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

embresbs = discord.Embed(
    title="Resigning process (Encrypted): Successful",
    description="**{savename}** resigned to **{id}** ({i}/{savecount}).",
    colour=Color.DEFAULT.value
)
embresbs.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

embRdone = discord.Embed(
    title="Resigning process (Encrypted): Successful",
    description=(
        "**{printed}** resigned to **{id}**.\n"
        "Uploading file...\n"
        "If file is being uploaded to Google Drive, you can send 'EXIT' to cancel."
    ),
    colour=Color.DEFAULT.value
)
embRdone.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

embLoading = discord.Embed(
    title="Loading",
    description="Loading **{basename}**... (file {j}/{count_entry}, batch {i}/{batches}).",
    colour=Color.DEFAULT.value
)
embLoading.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

embApplied = discord.Embed(
    title="Success!",
    description="Quick codes applied to **{basename}** (file {j}/{count_entry}, batch {i}/{batches}).",
    colour=Color.DEFAULT.value
)
embApplied.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

embqcCompleted = discord.Embed(
    title="Success!",
    description=(
        "Quick codes applied to **{finished_files}** ({i}/{batches}).\n"
        "Uploading file...\n"
        "If file is being uploaded to Google Drive, you can send 'EXIT' to cancel."
    ),
    colour=Color.DEFAULT.value
)
embqcCompleted.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

embchLoading = discord.Embed(
    title="Loading",
    description="Loading cheats process for **{game}**...",
    colour=Color.DEFAULT.value
)
embchLoading.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

embkstone1 = discord.Embed(
    title="Obtain process: Keystone",
    description="Obtaining keystone from file: **{savename}**, please wait...\nSend 'EXIT' to cancel.",
    colour=Color.DEFAULT.value
)
embkstone1.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

embkstone2 = discord.Embed(
    title="Obtain process: Keystone",
    description="Keystone from **{target_titleid}** obtained.",
    colour=Color.DEFAULT.value
)
embkstone2.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

embrrp = discord.Embed(
    title="Re-regioning process: Encrypted",
    description="Your save (**{savename}**) is being re-regioned & resigned, (save {j}/{savecount}, batch {i}/{batches}), please wait...\nSend 'EXIT' to cancel.",
    colour=Color.DEFAULT.value
)
embrrp.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

embrrps = discord.Embed(
    title="Re-regioning (Encrypted): Successful",
    description="**{savename}** re-regioned & resigned to **{id}** (**{target_titleid}**), (save {j}/{savecount}, batch {i}/{batches}).",
    colour=Color.DEFAULT.value
)
embrrps.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

embrrdone = discord.Embed(
    title="Re-region: Successful",
    description=(
        "**{printed}** re-regioned & resigned to **{id}** (**{target_titleid}**), (batch {i}/{batches}).\n"
        "Uploading file...\n"
        "If file is being uploaded to Google Drive, you can send 'EXIT' to cancel."
    ),
    colour=Color.DEFAULT.value
)
embrrdone.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

embres = discord.Embed(
    title="Resigning process: Encrypted",
    description="Your save (**{savename}**) is being resigned, (save {j}/{savecount}, batch {i}/{batches}), please wait...\nSend 'EXIT' to cancel.",
    colour=Color.DEFAULT.value
)
embres.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

embress = discord.Embed(
    title="Resigning process (Encrypted): Successful",
    description="**{savename}** resigned to **{id}** (save {j}/{savecount}, batch {i}/{batches}).",
    colour=Color.DEFAULT.value
)
embress.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

embRbdone = discord.Embed(
    title="Resigning process (Encrypted): Successful",
    description=(
        "**{printed}** resigned to **{id}** (batch {i}/{batches}).\n"
        "Uploading file...\n"
        "If file is being uploaded to Google Drive, you can send 'EXIT' to cancel."
    ),
    colour=Color.DEFAULT.value)
embRbdone.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

embLoad = discord.Embed(
    title="Loading",
    description="Loading {filename}...",
    colour=Color.DEFAULT.value
)
embLoad.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

embdec = discord.Embed(
    title="Finished",
    description="Successfully decrypted {filename}.",
    colour=Color.DEFAULT.value
)
embdec.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

paramEmb = discord.Embed(
    colour=Color.DEFAULT.value
)
paramEmb.set_footer(
    text=Embed_t.DEFAULT_FOOTER.value
)

embchErr = discord.Embed(
    title="ERROR!",
    description="Could not add cheat: {error}.",
    colour=Color.RED.value
)
embchErr.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

embErrconv = discord.Embed(
    title="ERROR!",
    description="Could not convert: {error}.",
    colour=Color.RED.value
)
embErrconv.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

embErrdec = discord.Embed(
    title="ERROR!",
    description="Could not convert: {error}.",
    colour=Color.RED.value
)
embErrdec.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

embchgtav = discord.Embed(
    title="Save loaded: GTA V",
    description=(
        "Platform: **{platform}**\n"
        "Franklin money: **{franklin_cash: ,}**\n"
        "Michael money: **{michael_cash: ,}**\n"
        "Trevor money: **{trevor_cash: ,}**"
    ),
    colour=Color.DEFAULT.value
)
embchgtav.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

embchrdr2 = discord.Embed(
    title="Save loaded: RDR 2",
    description=(
        "Platform: **{platform}**\n"
        "Money: **{money}**"
    ),
    colour=Color.DEFAULT.value
)
embchrdr2.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

embgddone = discord.Embed(
    title="Google drive upload: Retrieved file",
    description="{filename} has been uploaded and saved ({i}/{filecount}).",
    colour=Color.DEFAULT.value
)
embgddone.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

embuplSuccess = discord.Embed(
    title="Upload alert: Successful",
    description="File '{filename}' has been successfully uploaded and saved ({i}/{filecount}).",
    colour=Color.DEFAULT.value
)
embuplSuccess.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

embe = discord.Embed(
    title="Error",
    description="{error}",
    colour=Color.RED.value
)
embe.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

embuplSuccess1 = discord.Embed(
    title="Upload alert: Successful",
    description="File '{filename}' has been successfully uploaded and saved.",
    colour=Color.DEFAULT.value
)
embuplSuccess1.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

embencupl = discord.Embed(
    title="Current save: {savename}",
    description="Please attach a decrypted savefile that you want to upload, MUST be equivalent to {filename} (can be any name). Or type 'EXIT' to cancel command.",
    colour=Color.DEFAULT.value
)
embencupl.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

embenc_out = discord.Embed(
    title="Current save: {savename}",
    colour=Color.DEFAULT.value
)
embenc_out.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

embencinst = discord.Embed(
    title="Current save: {savename}",
    description=(
        "**FOLLOW THESE INSTRUCTIONS CAREFULLY**\n\n"
        "FOR **DISCORD ATTACHMENT UPLOAD**:\n"
        "Please attach at least one of these files and make sure its the same name, including path in the name if that is the case. Instead of '/' use '{splitvalue}'.\n"
        "\nFOR **GOOGLE DRIVE LINK UPLOAD**:\n"
        "UPLOAD WITH ANY FOLDER STRUCTURE!\n\n"
        "*Or type 'EXIT' to cancel command*."
        "\n\nHere are the contents:"),
    colour=Color.DEFAULT.value
)
embencinst.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

embgdout = discord.Embed(
    title="Google Drive: Upload complete",
    description="[Download]({url})\n{extra_msg}",
    colour=Color.DEFAULT.value
)
embgdout.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

embgames = discord.Embed(
    title="All available games",
    colour=Color.DEFAULT.value
)
embgames.set_footer(text=Embed_t.QR_FOOTER1.value)

embgame = discord.Embed(
    colour=Color.DEFAULT.value
)
embgame.set_footer(text=Embed_t.QR_FOOTER2.value)

emb_il = discord.Embed(
    title="Too many users at the moment!",
    description="{error}",
    colour=Color.YELLOW.value
)
emb_il.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

embdecTimeout = discord.Embed(
        title="Timeout Error:",
        description="You took too long, sending the file with the format: 'Encrypted'",
        colour=Color.DEFAULT.value)
embdecTimeout.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

embdecFormat = discord.Embed(
    title="Current save: {savename}",
    description="Choose if you want second layer removed ('Decrypted') or just Sony PFS layer ('Encrypted').",
    colour=Color.DEFAULT.value)
embdecFormat.set_footer(text="If you want to use the file in a save editor, choose 'Decrypted'!")

embwlcom = discord.Embed(
    title="Welcome",
    description="Hello **{user}**.",
    colour=Color.DEFAULT.value
)
embwlcom.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

#Kidds welcome msg 
embwlcom1 = discord.Embed(
        color=7475128,
        title="Welcome to PS Bot!",
        description="This bot is designed to allow editing of ps4 saves!\n Such as resigning others saves, converting saves to pc or vice versa, and customizing your saves! This is a free alternative to Save Wizard; The bot uses a jailbroken PS4 to handle the modifaction of PS4 saves.\n",
        thumbnail="https://media.discordapp.net/attachments/1381758125517836288/1381758459669909636/image.png?ex=68568618&is=68553498&hm=a18899a34382b9cbdc417053e1a8b1a5b37ccbf32f894c95cca480b34020aa47&=&format=webp&quality=lossless"
    )
embwlcom2 = discord.Embed(
        color=7475128,
        title="PS Bot Command List",
        description="To get started using the bot, here is a list of available commands you can use!\n\n### Main Commands: \n`/resign` - Use other people’s saves on your account \n`/decrypt` - exports the raw contents of your save to use in save editors and or hex editors. \n`/encrypt` - imports raw data into your supplied save file \n`/reregion` - change the region of saves to work on your version of games\n\n### Miscellaneous Commands \n`/psn` - allows you to search users on psn\n`/store_accountid` - allows you to set the resign id. The bot will remember who to resign to\n`/quick resign` - allows you to resign saves that <@285251932505767936> have provided. The bot has a decent selection \n`/quick codes` - allows you to input SaveWizard hex quick codes into your save\n`/change title` - allows you customize the title and sub title of a save file\n`/change picture` - allows you to upload a custom image for you save file\n\n### Advanced Commands\n`/convert` - convert supported games from ps4 to pc or vice versa \n`/createsave` - create a ps4 save from scratch using raw files\n`/sfo read` - obtain the param.sfo \n`/sfo write` - patch the parameters in the param.sfo\n`/sealed_key decrypt` - decrypted the sealed key of a save file (.bin file)",     
)
embwlcom3 = discord.Embed(
        color=7475128,
        title="Important Notes:",
        description="\nif the bot says application didn’t respond: it means the bot is **OFFLINE**!\n\n`/ping` to see the status of the bot\n`/help` to get more detailed information on each command\ncheck out our [Video Guides](<https://youtube.com/playlist?list=PLxevmZH4AJusnb9VnOpRojfe8fQndy1Js&si=uZn3tYo0mFweknvQ>) on the bot \nIf you wish to see the video tutorials again use `/tutorial`\n\nIf you need further help please ask in <#1212821931707858984> or <#1195354790339821639>!",
        image="https://media.discordapp.net/attachments/1381758125517836288/1381758318191575151/4k-Playstation-Buttons-Background-4K-Wallpaper.png?ex=685685f6&is=68553476&hm=ec83e66312a59ff748d00bc664eac6b7a1728935339d6b8593397b9c80a45378&=&format=webp&quality=lossless&width=550&height=200"
)
embwlcom3.set_footer(
    text="Hosted by That_Kidd | Help from Owwlz",
    icon_url="https://cdn.discordapp.com/attachments/1381758125517836288/1385727626097852416/pfp.png?ex=68571eeb&is=6855cd6b&hm=0736f514d6895836a4d46641992ac9520ecc5a4d2660743741695ee1077cc448&"
)
embzip1 = discord.Embed(
    title="Upload folder",
    description="Please attach one or more ZIP files each containing a sufficient folder to produce a valid savefile.",
    colour=Color.DEFAULT.value
)
embzip1.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

embc_bulk = discord.Embed(
    title="Processing",
    description="Creating **{savename}**, (save {j}/{savecount}, batch {i}/{batches}), please wait...\nSend 'EXIT' to cancel.",
    colour=Color.DEFAULT.value
)
embc_bulk.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

embCRdone_bulk = discord.Embed(
    title="Creation process: Successful",
    description=(
        "**{printed}** resigned to **{id}** (batch {i}/{batches}).\n"
        "Uploading file...\n"
        "If file is being uploaded to Google Drive, you can send 'EXIT' to cancel."
    ),
    colour=Color.DEFAULT.value
)
embCRdone_bulk.set_footer(text=Embed_t.DEFAULT_FOOTER.value)

