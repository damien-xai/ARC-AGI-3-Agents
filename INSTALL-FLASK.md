# Installing Flask for Visualization Server

## Issue

The visualization server requires Flask, but it wasn't installed in the ARC-AGI-3 environment.

```
Flask not installed. Run: pip install flask
WARNING | Failed to start visualization server: Flask is required for the visualization server
```

## Solution

Flask has been added to `pyproject.toml` dependencies. Install it:

```bash
cd /Users/damienmurphy/git/arc-agi-benchmarks/arc-prize/ARC-AGI-3

# Sync dependencies (installs Flask)
uv sync

# Or manually install Flask
uv pip install flask
```

## Verify Installation

```bash
# Check Flask is installed
uv run python -c "import flask; print(f'Flask {flask.__version__} installed!')"

# Should output: Flask 3.x.x installed!
```

## Run Agent with Visualization

```bash
cd /Users/damienmurphy/git/arc-agi-benchmarks/arc-prize/ARC-AGI-3

# Set API key
export XAI_API_KEY="your_xai_api_key"

# Run agent (visualization server will start automatically)
uv run main.py --agent=grokharness --game=ls20
```

**You should now see**:
```
================================================================================
🌐 VISUALIZATION DASHBOARD RUNNING
================================================================================
  📊 Dashboard:  http://0.0.0.0:5000/
  🎮 Game View:  http://0.0.0.0:5000/game/ls20
  🛑 Will auto-stop when agent exits
================================================================================
```

## What Was Changed

**File**: `arc-prize/ARC-AGI-3/pyproject.toml`

**Added**:
```toml
dependencies = [
    "dotenv>=0.9.9",
    "flask>=3.0.0",  # ← Added for visualization server
    "langchain[openai]>=0.3.27",
    ...
]
```

## Troubleshooting

### Still getting "Flask not installed"?

```bash
# Force reinstall
cd /Users/damienmurphy/git/arc-agi-benchmarks/arc-prize/ARC-AGI-3
uv pip install --force-reinstall flask

# Or recreate virtual environment
rm -rf .venv
uv sync
```

### Want to verify before running agent?

```bash
uv run python -c "
from grok_harness.visualization import VisualizationServer
print('✅ Visualization server can be imported!')
"
```

## Summary

- ✅ Added `flask>=3.0.0` to ARC-AGI-3 dependencies
- ✅ Run `uv sync` to install Flask
- ✅ Visualization server will now start automatically with agent
- ✅ Dashboard accessible at http://localhost:5000

