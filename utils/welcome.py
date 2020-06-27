import random


def get_welcome_message(username):
    # Thanks to user macdja38: https://gist.github.com/macdja38/12dff2a6a496cd2d9185fec43c01d77b
    welcome_messages = [
        f"{username} just joined. Everyone, look busy!",
        f"{username} just joined. Can I get a heal?",
        f"{username} joined your party.",
        f"{username} joined. You must construct additional pylons.",
        f"Ermagherd. {username} is here.",
        f"Welcome, {username}. Stay awhile and listen.",
        f"Welcome, {username}. We were expecting you ( ͡° ͜ʖ ͡°)",
        f"Welcome, {username}. We hope you brought pizza.",
        f"Welcome {username}. Leave your weapons by the door.",
        f"A wild {username} appeared.",
        f"Swoooosh. {username} just landed.",
        f"Brace yourselves. {username} just joined the server.",
        f"{username} just joined. Hide your bananas.",
        f"{username} just arrived. Seems OP - please nerf.",
        f"{username} just slid into the server.",
        f"A {username} has spawned in the server.",
        f"Big {username} showed up!",
        f"Where’s {username}? In the server!",
        f"{username} hopped into the server. Kangaroo!!",
        f"{username} just showed up. Hold my beer.",
        f"{username} just joined the server - glhf!",
    ]

    message = random.choice(welcome_messages)
    return message
