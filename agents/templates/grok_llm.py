"""Grok-based LLM agents using the official ReasoningLLM with Grok 4 Fast Reasoning.

To use these agents, set the following environment variables in your .env file:
- OPENAI_API_KEY: Your xAI API key
- OPENAI_BASE_URL: https://api.x.ai

The OpenAI SDK will automatically use these settings to connect to xAI's API.
"""
import os
from typing import Any

from .llm_agents import ReasoningLLM, LLM


class Grok4Fast(ReasoningLLM):
    """Grok 4 Fast Reasoning agent using the official ReasoningLLM class.
    
    This is a minimal wrapper that configures ReasoningLLM to use Grok 4 Fast Reasoning.
    Make sure to set OPENAI_BASE_URL=https://api.x.ai/v1 in your .env file.
    
    You can override MAX_ACTIONS by setting the MAX_ACTIONS environment variable.
    """
    
    MAX_ACTIONS = int(os.getenv("MAX_ACTIONS", "80"))
    DO_OBSERVATION = True
    MODEL = "grok-4-fast-reasoning"
    MODEL_REQUIRES_TOOLS = True
    MESSAGE_LIMIT = 10

    @property
    def name(self) -> str:
        obs = "with-observe" if self.DO_OBSERVATION else "no-observe"
        name = f"{super(LLM, self).name}.grok-4-fast.{obs}"
        return name


class Grok4FastNoObserve(Grok4Fast):
    """Grok 4 Fast Reasoning without observation step (faster but less strategic).
    
    You can override MAX_ACTIONS by setting the MAX_ACTIONS environment variable.
    """
    
    MAX_ACTIONS = int(os.getenv("MAX_ACTIONS", "80"))
    DO_OBSERVATION = False
