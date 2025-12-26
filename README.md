# GeminiBot - Personalized Telegram Bot

GeminiBot is a Telegram bot tailored to chat with Google's Gemini AI chatbot. Leveraging the official Gemini Bot on the Telegram platform, it engages users in dynamic conversations.

[Set-up Tutorial on Medium](https://medium.com/@alirezafathi/how-to-use-google-gemini-ai-in-your-personal-telegram-bot-on-your-own-server-b1f0b9de2bdd)

## Getting Started

### Prerequisites

Before deploying the bot, ensure you have the following:

- Python 3.10 installed on your system
- Obtain a [Telegram API token](https://core.telegram.org/bots) from BotFather
- Acquire a [Gemini API key](https://makersuite.google.com/app/apikey) from the Google Gemini website
- Get your Telegram Account id from [Show Json Bot](https://t.me/ShowJsonBot). Account id is different than Account username and you should set it in `.env` file to restrict GeminiBot to your account.

##


https://github.com/sudoAlireza/GeminiBot/assets/87416117/beeb0fd2-73c6-4631-baea-2e3e3eeb9319



### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/sudoAlireza/GeminiBot.git
   ```

2. Navigate to the project directory:

   ```bash
   cd GeminiBot
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Configuration

1. Create a file named `.env` in the project root and add your Telegram bot API token and Gemini API key:

   ```dotenv
   TELEGRAM_BOT_TOKEN=<Your Telegram Bot Token>
   GEMINI_API_TOKEN=<Your Gemini API key>
   GEMINI_MODEL=<Your Gemini Model (e.g., gemini-pro, gemini-1.5-flash)>
   AUTHORIZED_USER=<Your Telegram account ID number>
   ```

2. Update the `safety_settings.json` file with appropriate safety settings for Gemini policies.

### Usage

Run GeminiBot using:

```bash
python main.py
```

**Deployment with Docker**

You can also run GeminiBot using Docker and Docker Compose. This is the recommended way to deploy the bot in production.

**Data Persistence:**

The bot stores conversation data in the `data` directory. This directory is mounted as a volume in the Docker Compose configuration to ensure that your data is preserved even if the container is removed.

**Prerequisites:**

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

**Steps:**

1.  **Provide Environment Variables:** The bot requires environment variables to be set for configuration. You can provide them in one of the following ways:

    *   **Using a `.env` file (recommended):** Create a `.env` file in the project root as described in the "Configuration" section, and then run Docker Compose with the `--env-file` flag:

        ```bash
        docker-compose --env-file .env up -d --build
        ```

    *   **Setting variables in your shell:** You can set the environment variables directly in your shell before running Docker Compose:

        ```bash
        export TELEGRAM_BOT_TOKEN=<Your Telegram Bot Token>
        export GEMINI_API_TOKEN=<Your Gemini API key>
        export GEMINI_MODEL=<Your Gemini Model>
        export AUTHORIZED_USER=<Your Telegram account ID number>
        docker-compose up -d --build
        ```

    *   **Using `docker-compose run -e`:** You can pass the environment variables directly to the `run` command:

        ```bash
        docker-compose run -e TELEGRAM_BOT_TOKEN=<Your Telegram Bot Token> \
                             -e GEMINI_API_TOKEN=<Your Gemini API key> \
                             -e GEMINI_MODEL=<Your Gemini Model> \
                             -e AUTHORIZED_USER=<Your Telegram account ID number> \
                             geminibot
        ```

2.  **Build and Run:** Once you have provided the environment variables, build and run the bot using Docker Compose:

    ```bash
    docker-compose up -d --build
    ```

3.  The bot will now be running in the background. To view the logs, you can use the following command:

    ```bash
    docker-compose logs -f
    ```

4.  To stop the bot, use the following command:

    ```bash
    docker-compose down
    ```

## Features

- Engage in online conversations with Google's Gemini AI chatbot
- Maintain conversation history for continuing or initiating new discussions
- Send images with captions to receive responses based on the image content. For example, the bot can read text within images and convert it to text.


## To-Do

- [x] **Removing Specific Conversation from History**
- [ ] **Add Conversation Feature to Images Part**
- [ ] **Handle Long Responses in Multiple Messages**
- [ ] **Add Tests and Easy Deployment**


## Documentation

For detailed instructions on using Telegram bots, refer to the [Telegram Bots Documentation](https://core.telegram.org/bots).

To begin with Gemini, refer to the [Gemini API: Quickstart with Python](https://ai.google.dev/tutorials/python_quickstart).


## Security

Ensure the security of your API keys and sensitive information. Follow best practices for securing API keys and tokens.

## Contributing

Contributions to GeminiBot are encouraged. Feel free to submit issues and pull requests.
