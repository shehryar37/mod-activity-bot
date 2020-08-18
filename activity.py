# Python Libraries
import os
import datetime

# Discord API Libraries
import discord
from discord.ext import commands

# Utilities
import utils


def main():
    discord_client = commands.Bot(command_prefix='.')

    @discord_client.event
    async def on_ready():

        channels = [discord_client.get_channel(
            channel_id) for channel_id in utils.channel_ids]
        await activity(channels)

    print("Accessed Discord from activity.py")
    discord_client.run(os.environ["CLIENT_TOKEN"])

    discord_client.logout()
    exit(1000)


async def activity(channels):
    # Tries getting access to the Reddit bot
    reddit = utils.reddit_access('activity.py')

    # All the mods have been added as friends on the account.
    # So it only has to access r/friends
    subreddit = reddit.subreddit('animemes')

    # pause_after=-1 tells the stream to make one API call and return None if there is no new activity
    comment_stream = subreddit.stream.comments(
        skip_existing=True, pause_after=-1)
    submission_stream = subreddit.stream.submissions(
        skip_existing=True, pause_after=-1)

    # Loops over every new comment and submission in r/friends
    while True:
        t = datetime.datetime.utcnow().timestamp()
        for comment in comment_stream:
            # Checks if the stream yielded anything or if the comment was posted in the past hour
            if comment is None or comment.created_utc <= (t - 3600):
                break

            message = "{} has just commented in {}: {}".format(
                comment.author.name, comment.subreddit_name_prefixed, comment.link_permalink + comment.id)
            print(message)

            for channel in channels:
                await channel.send(message)

            print("Messaged comment on Discord")

        for submission in submission_stream:
            # Checks if the stream yielded anything or if the submission was posted in the past hour
            if submission is None or submission.created_utc <= (t - 3600):
                break

            message = "{} has just submitted in {}: {}".format(
                submission.author.name, submission.subreddit_name_prefixed, submission.shortlink)
            print(message)

            for channel in channels:
                await channel.send(message)

            print("Messaged submission on Discord")

    return


main()
