# Weather Bot
*Simple weather Discord bot created for [Codédex](https://www.codedex.io/home) final project!*

![](https://img.shields.io/github/license/pazurkota/weather_bot?style=for-the-badge)

---

### Cloning repo:
To clone repository, you can use Git client like GitKraken or Tower, or just simply type:
```commandline
git clone https://github.com/pazurkota/weather_bot.git
```

---

### Running bot:
Prerequisites:
- [Discord Bot Token](https://discord.com/developers/applications) with all intents
- [OpenWeather API](https://openweathermap.org/api) key

To run this bot: 
1. Make sure you are running `Python 3.8` or newer
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
  "api_key": "API KEY FROM https://openweathermap.org/"
}
```
4. Open project with PyCharm or any other IDE
5. Run the project

---

### Commands:
The bot prefix is `$`
- `weather <city>` - Get current weather for specified city
- `aqi <city>` - Get current air quality for specified city