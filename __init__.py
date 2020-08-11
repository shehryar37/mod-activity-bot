import praw


def main():
    reddit = login()

    # Makes a Redditor object out of all the mods
    subreddit = reddit.subreddit('friends')

    for comment in subreddit.stream.comments(skip_existing=True):
        print("{} has just commented in {}: {}".format(
            comment.author.name, comment.subreddit_name_prefixed, comment.link_permalink + comment.id))


def login():
    try:
        reddit = praw.Reddit(username="SauceCommentBot",
                             password="@Reddit123",
                             client_id="wQULoIPX2p5vkg",
                             client_secret="f_smlHjE0zrvozuV9VYGooUJ4Kg",
                             user_agent="SauceCommentBot by u/wizardhecate"
                             )

        # reddit = praw.Reddit(username=os.environ["USERNAME"],
        #                      password=os.environ["PASSWORD"],
        #                      client_id=os.environ["CLIENT_ID"],
        #                      client_secret=os.environ["CLIENT_SECRET"],
        #                      user_agent=os.environ["USER_AGENT"]
        #                      )

        print("Logged in")

        return reddit
    except:
        print("Failed to log in")


main()
