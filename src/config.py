"""Configuration for the AI Support Copilot"""
import os
from dotenv import load_dotenv
from anthropic import Anthropic

# Load .env file into os.environ
load_dotenv

# API key from environment
API_KEY = os.getenv("ANTHROPIC_API_KEY")

# Fail fast if the key is missing
if not API_KEY:
    raise ValueError("ANTHROPIC_API_KEY not found. Check your .env file.")

# Model settings
MODEL = "claude-opus-4-7"
DEFAULT_MAX_TOKENS = 1024
DEFAULT_TEMPERATURE = 0.3

# Shared Claude client - import this everywhere
client = Anthropic(api_key=API_KEY)

