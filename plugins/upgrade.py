"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot,update):
	text = """**Fʀᴇᴇ Pʟᴀɴ Usᴇʀ**
	Dᴀɪʟʏ  Uᴘʟᴏᴀᴅ ʟɪᴍɪᴛ 𝟷.𝟸GB
	Pʀɪᴄᴇ : 𝟶
	
	**🪙 Sɪʟᴠᴇʀ Tɪᴇʀ 🪙** 
	Dᴀɪʟʏ  Uᴘʟᴏᴀᴅ  ʟɪᴍɪᴛ 𝟷𝟶GB
	Pʀɪᴄᴇ Rs 29  ɪɴᴅ /🌎 𝟶.𝟼$  ᴘᴇʀ Mᴏɴᴛʜ
	
	**💫 Gᴏʟᴅ Tɪᴇʀ 💫**
	Dᴀɪʟʏ Uᴘʟᴏᴀᴅ ʟɪᴍɪᴛ 𝟻𝟶GB
	Pʀɪᴄᴇ Rs 𝟺𝟿  ɪɴᴅ /🌎 𝟶.𝟿$  ᴘᴇʀ Mᴏɴᴛʜ
	
	**💎 Dɪᴀᴍᴏɴᴅ 💎**
	Dᴀɪʟʏ Uᴘʟᴏᴀᴅ ʟɪᴍɪᴛ 𝟷𝟶𝟶GB
	Pʀɪᴄᴇ Rs 𝟿𝟿  ɪɴᴅ /🌎 𝟷.𝟺$  ᴘᴇʀ Mᴏɴᴛʜ
	
	Aғᴛᴇʀ Pᴀʏᴍᴇɴᴛ Sᴇɴᴅ Sᴄʀᴇᴇɴsʜᴏᴛs Oғ 
	Pᴀʏᴍᴇɴᴛ Tᴏ Aᴅᴍɪɴ : @praxxsh"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("🔰 ADMIN 🔰",url = "https://t.me/Praxxsh")], 
        			[InlineKeyboardButton("🧧 Channel 🧧",url = "https://t.me/Doremon_Botz"),
        			InlineKeyboardButton("⚡Support Chat ⚡",url = "https://t.me/+5xScmjemXiI4Yjll")],[InlineKeyboardButton("❌ Cancel",callback_data = "cancel")  ]])
	await update.message.edit(text = text,reply_markup = keybord)
	

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
	text = """**Fʀᴇᴇ Pʟᴀɴ Usᴇʀ**
	Dᴀɪʟʏ  Uᴘʟᴏᴀᴅ ʟɪᴍɪᴛ 𝟷.𝟸GB
	Pʀɪᴄᴇ : 𝟶
	
	**🪙 Sɪʟᴠᴇʀ Tɪᴇʀ 🪙** 
	Dᴀɪʟʏ  Uᴘʟᴏᴀᴅ  ʟɪᴍɪᴛ 𝟷𝟶GB
	Pʀɪᴄᴇ Rs 29  ɪɴᴅ /🌎 𝟶.𝟼$  ᴘᴇʀ Mᴏɴᴛʜ
	
	**💫 Gᴏʟᴅ Tɪᴇʀ 💫**
	Dᴀɪʟʏ Uᴘʟᴏᴀᴅ ʟɪᴍɪᴛ 𝟻𝟶GB
	Pʀɪᴄᴇ Rs 𝟺𝟿  ɪɴᴅ /🌎 𝟶.𝟿$  ᴘᴇʀ Mᴏɴᴛʜ
	
	**💎 Dɪᴀᴍᴏɴᴅ 💎**
	Dᴀɪʟʏ Uᴘʟᴏᴀᴅ ʟɪᴍɪᴛ 𝟷𝟶𝟶GB
	Pʀɪᴄᴇ Rs 𝟿𝟿  ɪɴᴅ /🌎 𝟷.𝟺$  ᴘᴇʀ Mᴏɴᴛʜ
	
	Aғᴛᴇʀ Pᴀʏᴍᴇɴᴛ Sᴇɴᴅ Sᴄʀᴇᴇɴsʜᴏᴛs Oғ 
	Pᴀʏᴍᴇɴᴛ Tᴏ Aᴅᴍɪɴ : @praxxsh"""
	keybord = InlineKeyboardMarkup([[ 
        			InlineKeyboardButton("🔰 ADMIN 🔰",url = "https://t.me/Praxxsh")], 
        			[InlineKeyboardButton("🧧 Channel 🧧",url = "https://t.me/Doremon_Botz"),
        			InlineKeyboardButton("⚡ Support Chat ⚡",url = "https://t.me/+5xScmjemXiI4Yjll")],[InlineKeyboardButton("❌ Cancel",callback_data = "cancel")  ]])
	await message.reply_text(text = text,reply_markup = keybord)
