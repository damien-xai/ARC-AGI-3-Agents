#!/bin/bash
# Run the self-improving agent

# Activate venv
source .venv/bin/activate

# Run the agent
python3 main.py --agent selfimproving "$@"
