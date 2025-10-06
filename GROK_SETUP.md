# Running ARC-AGI-3 with Grok 4 Fast Reasoning

This guide explains how to run ARC-AGI-3 agents using Grok 4 Fast Reasoning via xAI's API.

## Setup

### 1. Environment Variables

Create a `.env` file in the `arc-prize/ARC-AGI-3/` directory with:

```bash
# Required for ARC-AGI-3 games API
ARC_API_KEY=your_arc_api_key_from_three.arcprize.org

# xAI API credentials (OpenAI SDK compatible)
OPENAI_API_KEY=your_xai_api_key
OPENAI_BASE_URL=https://api.x.ai
```

**Note**: The OpenAI SDK is used with a custom base URL to connect to xAI's API. You don't need an actual OpenAI API key.

### 2. Install Dependencies

Make sure you have `uv` installed:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Then sync dependencies:
```bash
cd arc-prize/ARC-AGI-3
uv sync
```

## Available Grok Agents

### `grok4fast`
Full reasoning agent with observation step (slower but more strategic)
- Uses Grok 4 Fast Reasoning model
- Observes game state before choosing action
- Better for complex games

### `grok4fastnoobserve`
Fast reasoning agent without observation (faster but less strategic)
- Uses Grok 4 Fast Reasoning model
- Directly chooses actions without observation step
- Better for simpler games or quick testing

## Running Tests

### Quick Test
```bash
# From project root

# Default: 2 games, 80 max actions per game
./scripts/arc-agi-3-grok-test.sh

# Custom game limit
./scripts/arc-agi-3-grok-test.sh --limit 5

# Single game with custom max actions
./scripts/arc-agi-3-grok-test.sh -l 1 -m 50

# Multiple games with higher action limit
./scripts/arc-agi-3-grok-test.sh --limit 3 --max-actions 100

# Help
./scripts/arc-agi-3-grok-test.sh --help
```

This script will:
1. Check your environment setup
2. Install dependencies
3. Run the `grok4fast` agent on specified number of games
4. Save results and recordings

### Manual Testing

```bash
cd arc-prize/ARC-AGI-3

# Test on specific game(s)
uv run main.py --agent=grok4fast --game=ls20

# Test on multiple games (comma-separated prefixes)
uv run main.py --agent=grok4fast --game=ls20,aa01

# Test on all available games
uv run main.py --agent=grok4fast

# Use the faster no-observe variant
uv run main.py --agent=grok4fastnoobserve --game=ls20
```

## Output Files

After running, you'll find:
- `logs.log` - Detailed execution logs
- `*.recording.jsonl` - Game recordings for each game played
- Scorecard results in the console output

## How It Works

The `Grok4Fast` and `Grok4FastNoObserve` agents are thin wrappers around the official `ReasoningLLM` class that:
1. Configure the model name to `grok-4-fast-reasoning`
2. Use the OpenAI SDK with `OPENAI_BASE_URL=https://api.x.ai/v1
3. Leverage all existing features (tool calling, reasoning tokens, etc.)

This means you get all the benefits of the official agent architecture while using Grok's reasoning capabilities.

## Troubleshooting

### "Connection refused" or API errors
- Make sure your `OPENAI_API_KEY` contains your xAI API key
- Verify `OPENAI_BASE_URL=https://api.x.ai/v1 is set
- Check that your ARC_API_KEY is valid

### "Agent not found"
- Make sure you've synced dependencies: `uv sync`
- Use lowercase agent names: `grok4fast` not `Grok4Fast`

### Model not responding
- Check your xAI API key has sufficient credits
- Verify the model name is correct: `grok-4-fast-reasoning`
- Check xAI API status at https://status.x.ai/

### ValidationError: "Input should be a valid integer"
**Symptom**: Error parsing tool arguments, shows XML-like strings in error message

**Cause**: Grok occasionally returns malformed tool arguments (XML format instead of JSON)

**Solution**: The agent now automatically handles this by:
1. Logging the malformed arguments for debugging
2. Using default coordinates (32, 32) for complex actions
3. Falling back to ACTION5 if parsing completely fails

The game will continue despite these errors. Check `logs.log` for details.

## Cost Tracking

The agent will track:
- Total tokens used
- Reasoning tokens (if available from the API)
- Actions taken per game
- Time per game

Check the logs for detailed cost information.
