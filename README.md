# Telegram Group User Diff
Returns a list of members in one group that are not present in another group.

## Requirements
 * Python 3.7
 * Python `pip`
 * A Telegram API ID and Hash ([generate one here](https://my.telegram.org/apps))

## Setup
 1. Run `pip3 install -r requirements.txt`
 2. Configure the application as outlined in the "Configuration" section
 3. Run the application for the first time (`python3 tg_user_diff.py`). Enter your Telegram phone number (including country code) and the authentication code returned in your Telegram client to create your session.

## Configuration
First, rename `config.example.json` to `config.json`. Then, fill in the following values:

 * **api_id**: The API ID assigned by Telegram
 * **api_hash**: The API Hash assigned by Telegram
 * **main_group_id**: Some identifier for the main group you wish to scan. [Look here](https://telethon.readthedocs.io/en/stable/extra/basic/entities.html#getting-entities) for information on what kind of identifiers you can use.
 * **second_group_id**: An identifier for the group against which to check differences. Users present in this group but not present in the main group will be displayed.
