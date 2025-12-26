import json
import os
import google.generativeai as genai
import logging

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


class GeminiChat:

    def __init__(
        self, gemini_token: str, image=None, chat_history: list = None
    ) -> None:
        self.image = image
        self.chat_history = chat_history
        self.GOOGLE_API_KEY = gemini_token

        genai.configure(api_key=self.GOOGLE_API_KEY)

        with open("./safety_settings.json", "r") as fp:
            self.safety_settings = json.load(fp)

        logging.info("Initiated new chat model")

    def _get_model(self, generative_model: str = "gemini-1.5-flash") -> genai.GenerativeModel:
        """Gets a generative model instance."""
        try:
            model_name = os.getenv("GEMINI_MODEL", generative_model)
            logging.info(f"Trying to get generative model: {model_name}")
            return genai.GenerativeModel(
                model_name, safety_settings=self.safety_settings
            )
        except Exception as e:
            logging.warning(f"Failed to get model: {e}")
            raise ValueError(f"Failed to get model: {e}")

    def send_image(self, message_text: str | None = None) -> str:
        """Sends an image and message to the model and generates a response."""
        message_text = message_text or "Please describe this photo"
        try:
            model = self._get_model("gemini-pro-vision")
            response = model.generate_content([message_text, self.image])
            logging.info("Recieved response from Gemini")
            return response.text
        except Exception as e:
            logging.warning(f"Failed to send image: {e}")
            return "Couldn't reach out to Google Gemini. Try Again..."

    def start_chat(self) -> None:
        """Starts a new chat session."""
        try:
            model = self._get_model("gemini-1.5-flash")
            self.chat = model.start_chat(history=self.chat_history)
            logging.info("Start new conversation")
        except Exception as e:
            logging.warning(f"Failed to start chat: {e}")

    def send_message(self, message_text: str) -> str:
        """Sends a message to the chat session and returns the response."""
        try:
            response = self.chat.send_message(message_text)
            logging.info("Recieved response from Gemini")
            return response.text
        except Exception as e:
            logging.warning(f"Failed to send message: {e}")
            return "Couldn't reach out to Google Gemini. Try Again..."

    def get_chat_title(self) -> str:
        """Gets a short title for the conversation."""
        try:
            return self.send_message(
                "Write a one-line short title up to 10 words for this conversation in plain text."
            )
        except Exception as e:
            logging.warning(f"Failed to get chat title: {e}")

    def get_chat_history(self):
        """Gets the chat history."""
        try:
            return self.chat.history
        except Exception as e:
            logging.warning(f"Failed to get chat history: {e}")

    def close(self) -> None:
        """Closes the chat and cleans history."""
        logging.info("Closed model instance")
        self.chat = None
        self.chat_history = []
