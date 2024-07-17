# Weather Bot
*Simple weather Discord bot created for [Codédex](https://www.codedex.io/home) final project!*

### Cloning repo:
To clone repository, you can use Git client like GitKraken or Tower, or just simply type:
```commandline
git clone https://github.com/pazurkota/weather_bot.git
```

### Running bot:
To run this bot: 
1. Make sure you are running `Python 3.12`
2. You need both `requests` and `discord` packages installed:
```commandline
python -m pip install requests
```
```commandline
python -m pip install -U discord.py
```
3. Create `data.json` file in root directory (where `program.py` is localized) with following data:
```json
{
  "token": "DISCORD BOT TOKEN",
  "api_key": "API KEY FROM https://www.weatherapi.com/"
}
```
4. Open project with PyCharm or any other IDE
5. Press "run" or type into your terminal:
```commandline
python program.py
```
