# diy-driver-bot
 A simple Discord bot written in Python for SoundBytes PH. Searches the matching user's DIY earbud driver search query and sends the info of that search!

# Setup
Install requirements.txt `pip3 install -r requirements.txt`

Add your bot's `token` in `config.json`.

Configure your preferred prefix in `prefix` (yes still using prefix in 2023, f*ck slash commands) and status.

Add your preferred bot response channel in `channel_id`.

Put preferred bot response channel name in `channel_name`

Run `main.py`

That's it. test your bot on your server to see if it works. (Assuming your bot is already joined your server.)

# Contribution
This entire code is WIP, so some major changes can happen. Also i'm still noob at coding (specifically python), please spare me UwU

You can push a driver info in .json file if you want, just follow the `template.json` inside `driver-repo` folder.

Also, search result is based on file name, so be specific on that (add keywords that user might search, eg: `120ohm beryllium driver kaph white glue.json` something like that.)

# Credits
All driver database are fetched from and ported as json from [DIY Workroom](https://docs.google.com/spreadsheets/d/1PRXhXgAr8N-EiNk3K9Cuqd36LeS5JB7ZuFDAgJbTCm8/edit#gid=0), so huge thanks to this useful guide!

# Support
You can join my Discord Server for support and everything else as long as it's audio gear topic.

Normal URL:
https://discord.gg/mj2jbz3RWw

Vanity URL:
https://discord.gg/soundbytesph
