import os

class Config():
  #Get it from @botfather
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "5640837043:AAHSBVIgYeVUdhlFtAP3QOth8pPUb-ht8-U")
  # Your bot updates channel username without @ or leave empty
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "redxbotlist")
  # Heroku postgres DB URL
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://aman:aman@cluster0.chnpche.mongodb.net/?retryWrites=true&w=majority")
  # get it from my.telegram.org
  APP_ID = os.environ.get("APP_ID", "9411723")
  API_HASH = os.environ.get("API_HASH", "30fa091455c0548d77dc254f0bb705b0")
  # Sudo users( goto @LaylaRobot and send /id to get your id)
  SUDO_USERS = list(set(int(x) for x in os.environ.get("SUDO_USERS", "875770605").split()))
  SUDO_USERS.append(797768146)
  SUDO_USERS = list(set(SUDO_USERS))

class Messages():
      HELP_MSG = [
        ".",

        "**Force Subscribe**\n__Force group members to join a specific channel before sending messages in the group.\nI will mute members if they not joined your channel and tell them to join the channel and unmute themself by pressing a button.__",
        
        "**Setup**\n__First of all add me in the group as admin with ban users permission and in the channel as admin.\nNote: Only creator of the group can setup me and i will leave the chat if i am not an admin in the chat.__",
        
        "**Commmands**\n__/ForceSubscribe - To get the current settings.\n/ForceSubscribe no/off/disable - To turn of ForceSubscribe.\n/ForceSubscribe {channel username or channel ID} - To turn on and setup the channel.\n/ForceSubscribe clear - To unmute all members who muted by me.\n/source_code - To get bot source code😍\n\nNote: /FSub is an alias of /ForceSubscribe__",
        
       "**Developer @HEROGAMERS1 \nDevloped By @LaylaList \nSupport Group @AwesomeSupport**"
      ]
      SC_MSG = "**Hey [{}](tg://user?id={})**\n click on below👇 button to get my source code, for more help ask in my support group👇👇 "

      START_MSG = "**Hey [{}](tg://user?id={})**\n__I can force members to join a specific channel before writing messages in the group.\nLearn more at /help__"
