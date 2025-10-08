from typing import Type, cast
import sys
import os

from dotenv import load_dotenv

from .agent import Agent, Playback
from .recorder import Recorder
from .swarm import Swarm
from .templates.langgraph_functional_agent import LangGraphFunc, LangGraphTextOnly
from .templates.langgraph_random_agent import LangGraphRandom
from .templates.langgraph_thinking import LangGraphThinking
from .templates.llm_agents import LLM, FastLLM, GuidedLLM, ReasoningLLM
from .templates.random_agent import Random
from .templates.reasoning_agent import ReasoningAgent
from .templates.smolagents import SmolCodingAgent, SmolVisionAgent
from .templates.grok_llm import Grok4Fast, Grok4FastNoObserve

# Add grok-harness to path
grok_harness_path = os.path.join(os.path.dirname(__file__), "..", "..", "..", "grok-harness", "src")
if grok_harness_path not in sys.path:
    sys.path.insert(0, grok_harness_path)

# Import GrokHarnessAgent
try:
    from grok_harness.integration.arc_agi_adapter import GrokHarnessAgent
    GROK_HARNESS_AVAILABLE = True
except ImportError:
    GrokHarnessAgent = None  # type: ignore
    GROK_HARNESS_AVAILABLE = False

# Import SelfImprovingAgent
try:
    from src.integration.arc_adapter import ARCAdapter as SelfImprovingAgent
    SELFIMPROVING_AVAILABLE = True
except ImportError:
    SelfImprovingAgent = None  # type: ignore
    SELFIMPROVING_AVAILABLE = False

load_dotenv()

AVAILABLE_AGENTS: dict[str, Type[Agent]] = {
    cls.__name__.lower(): cast(Type[Agent], cls)
    for cls in Agent.__subclasses__()
    if cls.__name__ != "Playback"
}

# add all the recording files as valid agent names
for rec in Recorder.list():
    AVAILABLE_AGENTS[rec] = Playback

# update the agent dictionary to include subclasses of LLM class
AVAILABLE_AGENTS["reasoningagent"] = ReasoningAgent

# Add Grok agents
AVAILABLE_AGENTS["grok4fast"] = Grok4Fast
AVAILABLE_AGENTS["grok4fastnoobserve"] = Grok4FastNoObserve

# Add GrokHarnessAgent
if GROK_HARNESS_AVAILABLE and GrokHarnessAgent:
    AVAILABLE_AGENTS["grokharness"] = GrokHarnessAgent

# Add SelfImprovingAgent
if SELFIMPROVING_AVAILABLE and SelfImprovingAgent:
    AVAILABLE_AGENTS["selfimproving"] = SelfImprovingAgent

__all__ = [
    "Swarm",
    "Random",
    "LangGraphFunc",
    "LangGraphTextOnly",
    "LangGraphThinking",
    "LangGraphRandom",
    "LLM",
    "FastLLM",
    "ReasoningLLM",
    "GuidedLLM",
    "ReasoningAgent",
    "SmolCodingAgent",
    "SmolVisionAgent",
    "Grok4Fast",
    "Grok4FastNoObserve",
    "Agent",
    "Recorder",
    "Playback",
    "AVAILABLE_AGENTS",
]
