# discord-bot

## A Discord bot for use in some of my servers

You can run my bot locally or, for example, in an AWS EC2 instance, by doing either of:

1. Using my bash install script `run.sh`

    - Download the script

        ```bash
        curl -L https://raw.githubusercontent.com/nigeltroy/discord-bot/master/run.sh -o run.sh
        ```

    - Give the script executable permissions

        ```bash
        chmod +x run.sh
        ```

    - Run the script

        ```bash
        ./run.sh
        ```

2. Clone the repo and run `main.py` (make sure that Python 3 and pip are installed)

    - Clone the repository

        ```bash
        git clone https://github.com/nigeltroy/discord-bot.git
        ```

    - Navigate to the project directory

        ```bash
        cd discord-bot
        ```

    - Fill out `stub.env` file with the environment variables (replace `vim` with the text editor of your choice)

        ```bash
        vim stub.env
        ```

    - Copy `stub.env` to `.env`

        ```bash
        cp stub.env .env
        ```

    - Install Python requirements for the project

        ```bash
        pip3 install -r requirements.txt
        ```

    - Run the bot

        ```bash
        python3 main.py
        ```
