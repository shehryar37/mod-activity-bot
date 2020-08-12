import praw
import os

import discord
from discord.ext import commands


def main():
    discord_client = commands.Bot(command_prefix='.')

    @discord_client.event
    async def on_ready():
        channel = discord_client.get_channel(742799267294609448)
        await fetch_comments(channel)

    print("Accessed Discord")
    discord_client.run(os.environ["CLIENT_TOKEN"])


async def fetch_comments(channel):
    # Tries getting access to the Reddit bot
    reddit_client = reddit_access()

    # All the mods have been added as friends on the account.
    # So it only has to access r/friends
    subreddit = reddit_client.subreddit('friends')

    # Loops over every new comment in r/friends
    for comment in subreddit.stream.comments(skip_existing=True):
        message = "{} has just commented in {}: {}".format(
            comment.author.name, comment.subreddit_name_prefixed, comment.link_permalink + comment.id)
        print(message)
        await channel.send(message)
        print("Messaged comment on Discord.")


def reddit_access():
    try:
        reddit = praw.Reddit(username=os.environ["USERNAME"],
                             password=os.environ["PASSWORD"],
                             client_id=os.environ["CLIENT_ID"],
                             client_secret=os.environ["CLIENT_SECRET"],
                             user_agent=os.environ["USER_AGENT"]
                             )

        print("Accessed Reddit")

        return reddit

    except Exception as e:
        print(e)
        exit(self, 1)


main()
