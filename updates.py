# Scheduling libraries
import schedule
import time

# Discord API Libraries
import discord
from discord.ext import commands

# Utilities
import utils


def main():
    discord_client = commands.Bot(command_prefix='.')

    @discord_client.event
    async def on_ready():

        # channels = [discord_client.get_channel(channel_id) for channel_id in channel_ids]
        await scheduler()

    print("Accessed Discord from updates.py")
    # discord_client.run(os.environ["CLIENT_TOKEN"])
    discord_client.run(
        "NzQyNjU3Nzc0NjUwOTE2OTM1.XzJT8w.aBwZUBd32urpqDDto7ZNhdgzYZk")

    discord_client.logout()
    exit(1000)


def check_mod_list():
    # opens the mod_list.txt file
    # "a" creates a file if it already does not exist
    with open("modlist.txt") as f:
        previous_mods = f.readlines()

        reddit = utils.reddit_access('updates.py')
        current_mods = reddit.subreddit('animemes').moderator()

        # f.truncate()

    # with open("mod_list.txt", "w")

    added_mods = list(set(current_mods) - set(previous_mods))
    removed_mods = list(set(previous_mods) - set(current_mods))

    for mod in added_mods:
        mod_account = reddit.redditor(mod.name)
        mod_account.friend()
        print('{} has been added as a moderator'.format(mod))

    for mod in removed_mods:
        mod_account = reddit.redditor(mod)
        print('{} has been removed as a moderator'.format(mod))
        mod_account.unfriend()


def send_mod_changes():
    pass


schedule.every(1).hours.do(check_mod_list)


def scheduler():
    check_mod_list()
    while True:
        schedule.run_pending()
        time.sleep(3600)


main()
