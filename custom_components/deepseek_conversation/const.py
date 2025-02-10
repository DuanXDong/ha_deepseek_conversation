"""Constants for the OpenAI Conversation integration."""

import logging

DOMAIN = "deepseek_conversation"
LOGGER = logging.getLogger(__package__)

CONF_RECOMMENDED = "recommended"
CONF_PROMPT = "prompt"
CONF_CHAT_MODEL = "chat_model"
RECOMMENDED_CHAT_MODEL = "deepseek-chat"
CONF_MAX_TOKENS = "max_tokens"
RECOMMENDED_MAX_TOKENS = 4096
CONF_TOP_P = "top_p"
RECOMMENDED_TOP_P = 1.0
CONF_TEMPERATURE = "temperature"
RECOMMENDED_TEMPERATURE = 0.7
