# ARC-AGI-3 with Grok - Quick Start

## 1. Setup (One-time)

Create `.env` in this directory:
```bash
ARC_API_KEY=your_arc_key
OPENAI_API_KEY=your_xai_key
OPENAI_BASE_URL=https://api.x.ai/v1
```

## 2. Run Test

From project root:
```bash
# Default: 2 games
./scripts/arc-agi-3-grok-test.sh

# Custom limit
./scripts/arc-agi-3-grok-test.sh --limit 5

# Single game
./scripts/arc-agi-3-grok-test.sh -l 1
```

## 3. Monitor Live

### Console (automatic)
Watch real-time actions:
```
INFO | ls20 - ACTION1: count 5, score 100, avg fps 2.5
```

### Web Scorecard (built-in)
1. Look for this in console output:
   ```
   View your scorecard online: http://localhost:8001/scorecards/{card_id}
   ```
2. Open URL in browser
3. Watch games live!

### AgentOps (optional, best)
1. Get key: https://app.agentops.ai
2. Add to `.env`: `AGENTOPS_API_KEY=aos_xxx`
3. Install: `uv sync --extra agentops`
4. Get live dashboard link when running

## 4. Manual Commands

```bash
cd arc-prize/ARC-AGI-3

# Single game
uv run main.py --agent=grok4fast --game=ls20

# Multiple games
uv run main.py --agent=grok4fast --game=ls20,aa01

# Faster variant (no observation)
uv run main.py --agent=grok4fastnoobserve --game=ls20

# All games
uv run main.py --agent=grok4fast
```

## 5. After Running

Check:
- **Console output** - Real-time actions and final scores
- **logs.log** - Detailed execution log
- **\*.recording.jsonl** - Game recordings for replay
- **Web scorecard** - Visual results and analytics

## Replay a Recording

```bash
uv run main.py --agent=ls20.grok4fast.1.*.recording.jsonl
```

## Guides

- **Full setup:** `GROK_SETUP.md`
- **Monitoring:** `MONITORING.md`
- **Project root:** `../../ARC-AGI-3-SETUP.md`
- **Summary:** `../../ARC-AGI-3-SUMMARY.md`

## Available Agents

- `grok4fast` - Full reasoning with observation (recommended)
- `grok4fastnoobserve` - Skip observation (faster)
- `random` - Random actions (baseline)
- `llm` - Generic LLM agent

## Cost Estimates

Per game (approximate):
- **Grok 4 Fast Reasoning**: $0.20-0.50
- **Time**: 2-5 minutes
- **Actions**: 20-80 per game

## Quick Troubleshooting

**Connection errors:**
- Check `OPENAI_BASE_URL=https://api.x.ai/v1 in `.env`
- Verify `OPENAI_API_KEY` is your xAI key (not OpenAI)

**No scorecard URL:**
- Check if API server is running (default: localhost:8001)
- Verify `ARC_API_KEY` is valid

**Agent not found:**
- Run `uv sync` first
- Use lowercase: `grok4fast` not `Grok4Fast`

## That's It!

You're ready to test Grok on ARC-AGI-3 games! 🚀
