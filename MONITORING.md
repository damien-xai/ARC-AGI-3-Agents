# Monitoring ARC-AGI-3 Games in Real-Time

ARC-AGI-3 has several built-in options for monitoring games while they're being played!

## Option 1: Web Scorecard (Built-in) ✅

The official ARC-AGI-3 platform provides a web interface to view your games!

### How It Works

When your agent finishes playing, you'll see:
```
View your scorecard online: http://localhost:8001/scorecards/{card_id}
```

**Features:**
- View game results and scores
- See all games in the current session
- Compare different agent runs
- Access via browser while game is running

**To Access During Play:**
1. Start your agent
2. Note the `card_id` from the console output
3. Open: `http://localhost:8001/scorecards/{card_id}`
4. Refresh to see updates

**Default Server:** The API server at `localhost:8001` (or your configured HOST/PORT)

## Option 2: AgentOps Real-Time Monitoring (Recommended) ⭐

**AgentOps** provides real-time agent monitoring and debugging!

### Setup

1. **Install AgentOps** (optional dependency):
```bash
cd arc-prize/ARC-AGI-3
uv sync --extra agentops
```

2. **Get API Key:**
   - Visit https://app.agentops.ai
   - Create account and new project
   - Copy your API key

3. **Add to .env:**
```bash
AGENTOPS_API_KEY=aos_your_api_key_here
```

### What You Get

When you run your agent:
```bash
🖇 AgentOps: Session Replay for grok4fast: https://app.agentops.ai/sessions?trace_id=xxxxx
```

**Real-Time Features:**
- ✅ Live action-by-action playback
- ✅ Token usage tracking
- ✅ Cost monitoring
- ✅ Performance analytics
- ✅ Error tracking and debugging
- ✅ Compare multiple runs
- ✅ Beautiful web dashboard

**Perfect for:**
- Debugging agent behavior
- Optimizing strategies
- Cost analysis
- Performance tuning

## Option 3: Console Logs (Always Active) 📋

Real-time logs show every action:

```bash
2025-10-05 14:32:15 | INFO | ls20 - ACTION1: count 5, score 100, avg fps 2.5)
2025-10-05 14:32:16 | INFO | ls20 - ACTION4: count 6, score 150, avg fps 2.5)
```

**Shows:**
- Game ID
- Action taken
- Action count
- Current score
- Average actions per second (FPS)

**Enable Debug Mode** for more detail:
```bash
DEBUG=True uv run main.py --agent=grok4fast --game=ls20
```

## Option 4: Recording Files (Post-Game Analysis) 📹

Every game is recorded to `.recording.jsonl` files:

**Filename format:**
```
{game}.{agent}.{count}.{guid}.recording.jsonl
```

**Example:**
```
ls20.grok4fast.1.abc123.recording.jsonl
```

**Contains:**
- Every frame of the game
- All actions taken
- Scores and state changes
- Token usage
- Reasoning metadata (for Grok)

**Use recordings to:**
- Replay games exactly
- Analyze decision patterns
- Debug failures
- Compare strategies

**Replay a recording:**
```bash
uv run main.py --agent=ls20.grok4fast.1.abc123.recording.jsonl
```

## Comparison: Monitoring Options

| Feature | Web Scorecard | AgentOps | Console | Recordings |
|---------|--------------|----------|---------|------------|
| Real-time | ✅ | ✅ | ✅ | ❌ |
| Visual | ✅ | ✅ | ❌ | ❌ |
| Detailed | ⚠️ | ✅✅ | ⚠️ | ✅ |
| Setup Required | ❌ | ✅ | ❌ | ❌ |
| Post-Analysis | ✅ | ✅ | ❌ | ✅ |
| Cost Tracking | ⚠️ | ✅ | ✅ | ✅ |
| Replay | ❌ | ✅ | ❌ | ✅ |

## Recommended Setup for Grok Testing

### For Testing (Simple)
```bash
# Just use console logs + web scorecard
uv run main.py --agent=grok4fast --game=ls20

# Then visit: http://localhost:8001/scorecards/{card_id}
```

### For Development (Full Monitoring)
```bash
# Set up AgentOps in .env
AGENTOPS_API_KEY=aos_your_key

# Run with debug logging
DEBUG=True uv run main.py --agent=grok4fast --game=ls20

# Monitor at:
# - Console: Real-time actions
# - AgentOps: https://app.agentops.ai (live dashboard)
# - Scorecard: http://localhost:8001/scorecards/{card_id}
```

### For Analysis (Recordings)
```bash
# After game completes, analyze recording
ls *.recording.jsonl

# Replay it
uv run main.py --agent=ls20.grok4fast.1.*.recording.jsonl
```

## Monitoring Best Practices

1. **Start Simple**: Use console logs and web scorecard first
2. **Add AgentOps**: For deeper insights and cost tracking
3. **Save Recordings**: Always enabled by default
4. **Use Tags**: Add tags to organize runs
   ```bash
   uv run main.py --agent=grok4fast --game=ls20 --tags=test,v1.0
   ```

## Example: Full Monitoring Session

```bash
# 1. Start agent with AgentOps
cd arc-prize/ARC-AGI-3
uv run main.py --agent=grok4fast --game=ls20 --tags=grok-test

# 2. Console shows real-time actions:
# INFO | ls20 - ACTION1: count 1, score 0, avg fps 1.0

# 3. AgentOps link appears:
# 🖇 AgentOps: Session Replay: https://app.agentops.ai/sessions?trace_id=xxx

# 4. Note the card_id from early in the output

# 5. Open in browser:
# http://localhost:8001/scorecards/{card_id}

# 6. After completion, check recording:
# ls20.grok4fast.1.*.recording.jsonl
```

## Troubleshooting

**Can't access scorecard URL:**
- Check HOST and PORT in main.py (default: localhost:8001)
- Make sure ARC API server is running
- Verify your ARC_API_KEY is valid

**AgentOps not working:**
- Install extra: `uv sync --extra agentops`
- Check API key in .env
- Verify internet connection

**No recordings created:**
- Check file permissions in current directory
- Look for *.recording.jsonl files
- Recording is automatic, no flags needed

## Summary

You have **4 ways** to monitor your Grok agent:

1. ✅ **Web Scorecard** - Visit URL during/after game
2. ⭐ **AgentOps** - Professional real-time monitoring (recommended!)
3. 📋 **Console Logs** - Always active, simple
4. 📹 **Recordings** - Post-game analysis and replay

For your 2-game test, I recommend:
- Console logs (automatic)
- Web scorecard (open the URL shown)
- Consider AgentOps for full visibility
