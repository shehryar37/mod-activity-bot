# Python Libraries
import os

# PRAW Libraries
import praw

# Discord API Libraries
import discord
from discord.ext import commands

channel_ids = [742799267294609448]  # add 743486931836338267


def main():
    discord_client = commands.Bot(command_prefix='.')

    @discord_client.event
    async def on_ready():

        channels = [discord_client.get_channel(
            channel_id) for channel_id in channel_ids]
        await activity(channels)

    print("Accessed Discord")
    discord_client.run(os.environ["CLIENT_TOKEN"])

    discord_client.logout()
    exit(self, 1000)


async def activity(channels):
    # Tries getting access to the Reddit bot
    reddit = reddit_access()

    # All the mods have been added as friends on the account.
    # So it only has to access r/friends
    subreddit = reddit.subreddit('friends')

    # pause_after=-1 tells the stream to make one API call and return None if there is no new activity
    comment_stream = subreddit.stream.comments(
        skip_existing=True, pause_after=-1)
    submission_stream = subreddit.stream.submissions(
        skip_existing=True, pause_after=-1)

    # Loops over every new comment and submission in r/friends
    while True:
        for comment in comment_stream:
            if comment is None:
                break

            message = "{} has just commented in {}: {}".format(
                comment.author.name, comment.subreddit_name_prefixed, comment.link_permalink + comment.id)
            print(message)

            for channel in channels:
                await channel.send(message)
                print("Messaged comment on Discord")

        for submission in submission_stream:
            if submission is None:
                break

            message = "{} has just submitted in {}: {}".format(
                submission.author.name, submission.subreddit_name_prefixed, submission.shortlink)
            print(message)

            for channel in channels:
                await channel.send(message)
                print("Messaged submission on Discord")

    return


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
