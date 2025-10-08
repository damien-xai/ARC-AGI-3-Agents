# Real-Time Dashboard - Quick Start Guide

## 🎯 What You Get

A **live dashboard** that shows your agent's state in real-time:
- ✅ Current score, phase, status
- ✅ Rules learned
- ✅ Walls detected  
- ✅ Interactive objects found
- ✅ Recent actions
- ✅ Active hypotheses
- ✅ Updates every 3 seconds automatically

## 🚀 Quick Start (3 Steps)

### Step 1: Install Dependencies

```bash
cd /Users/damienmurphy/git/arc-agi-benchmarks/arc-prize/ARC-AGI-3

# Install Flask and SocketIO
uv sync
```

### Step 2: Run the Agent

```bash
# Set your API key
export XAI_API_KEY="your_xai_api_key"

# Run a game
uv run main.py --agent=grokharness --game=ls20
```

**You'll see**:
```
================================================================================
🌐 VISUALIZATION DASHBOARD RUNNING
================================================================================
  📊 Dashboard:  http://0.0.0.0:5000/
  🎮 Game View:  http://0.0.0.0:5000/game/ls20
  🛑 Will auto-stop when agent exits
================================================================================
```

### Step 3: Open the Dashboard

Open your browser to:
```
http://localhost:5000
```

**You should see**:
- Game name with action count
- Current score and phase
- Rules being learned in real-time
- Walls being detected
- Actions scrolling by
- Everything updating automatically!

## 🎮 What You'll See

### Active Games Section
```
🎮 Active Games
[Refresh]

as66    80 snapshots
Latest View
```

### Agent State Section
```
🤖 Agent State
[Refresh]

Phase: Exploration          ← Updates in real-time!
Score: 5                    ← Live score
Hypotheses: 3              ← Active hypotheses
Last Updated: 2025-10-06... ← Current timestamp
```

### Confirmed Rules
```
📋 Confirmed Rules
• ACTION1 = UP
• Color 4 = wall
• Score increases near Color 12
```

### Identified Walls
```
🧱 Identified Walls
🧱 Color: 4, Positions: 42
🧱 Color: 14, Positions: 8
```

### Recent Actions
```
📜 Recent Actions
#23: ACTION2 (Δscore=1, changed=True)
#22: ACTION1 (Δscore=0, changed=True)
#21: ACTION4 (Δscore=0, changed=True)
```

## 🔧 How It Works

### The Flow

```
Agent plays game
    ↓
Writes state to JSON file
(live_state/game_123.json)
    ↓
Server reads JSON file
    ↓
API returns data
    ↓
Browser refreshes every 3s
    ↓
Dashboard updates!
```

### Behind the Scenes

**Agent** (`choose_action`):
```python
self.live_state.update_state(
    game_id=self.game_id,
    score=5,
    phase="Exploration",
    rules=["ACTION1=UP"],
    walls=[{"color": 4, "count": 42}],
    ...
)
# Writes to: live_state/as66-821a4dcad9c2.json
```

**Server** (`/api/agent/state`):
```python
active_games = self.live_state.list_active_games()
return jsonify(active_games[0])  # Most recent
# Reads from: live_state/as66-821a4dcad9c2.json
```

**Browser** (JavaScript):
```javascript
setInterval(() => {
    fetch('/api/agent/state')
        .then(r => r.json())
        .then(data => updateDashboard(data));
}, 3000);  # Every 3 seconds
```

## 🐛 Troubleshooting

### Dashboard shows "No games yet"

**Problem**: Agent hasn't started or JSON files not being created

**Solution**:
```bash
# Check if live_state directory exists
ls -la arc-prize/ARC-AGI-3/live_state/

# Check if JSON files are being created
watch "ls -lh arc-prize/ARC-AGI-3/live_state/"

# View current state
cat arc-prize/ARC-AGI-3/live_state/*.json | jq
```

### Dashboard shows old data

**Problem**: Browser cache or state files not updating

**Solution**:
```bash
# Hard refresh browser
# Mac: Cmd+Shift+R
# Windows/Linux: Ctrl+Shift+R

# Or clear old state files
rm arc-prize/ARC-AGI-3/live_state/*.json

# Restart agent
```

### "Phase: unknown" still showing

**Problem**: Dependencies not installed or old code running

**Solution**:
```bash
# Reinstall dependencies
cd arc-prize/ARC-AGI-3
uv sync

# Make sure you're running latest code
# Stop agent and restart
```

## 📊 Advanced Usage

### View JSON State Directly

```bash
# Pretty print current state
cat arc-prize/ARC-AGI-3/live_state/*.json | jq

# Watch state updates in real-time
watch -n 1 "cat arc-prize/ARC-AGI-3/live_state/*.json | jq '.score, .phase, .action_count'"

# Count active games
ls arc-prize/ARC-AGI-3/live_state/*.json | wc -l
```

### Multiple Games

The system supports multiple concurrent games:
```bash
# Terminal 1
uv run main.py --agent=grokharness --game=ls20

# Terminal 2
uv run main.py --agent=grokharness --game=as66

# Dashboard shows both games!
```

### API Endpoints

```bash
# List all active games
curl http://localhost:5000/api/games | jq

# Get current agent state
curl http://localhost:5000/api/agent/state | jq

# Health check
curl http://localhost:5000/health | jq
```

## ✨ What's Different from Before

### Before (Broken)
- ❌ "Phase: unknown"
- ❌ "Last Updated: never"
- ❌ No data showing up
- ❌ Had to rely on terminal logs

### After (Working)
- ✅ Real-time phase updates
- ✅ Current timestamp
- ✅ All data visible
- ✅ Beautiful dashboard UI

## 🎉 Summary

**To see live agent state**:
```bash
# 1. Install
uv sync

# 2. Run agent
export XAI_API_KEY="..."
uv run main.py --agent=grokharness --game=ls20

# 3. Open browser
open http://localhost:5000
```

**That's it!** Dashboard updates automatically every 3 seconds with live game data! 🚀

---

## 📚 More Information

- **Implementation**: See `grok-harness/REAL-TIME-VISUALIZATION-COMPLETE.md`
- **Architecture**: See `grok-harness/REAL-TIME-VISUALIZATION-UPGRADE.md`
- **Hot Reload**: See `grok-harness/HOT-RELOAD-GUIDE.md`

