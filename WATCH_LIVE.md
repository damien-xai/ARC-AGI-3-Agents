# Watch ARC-AGI-3 Games Live! 🎮

## Quick Start - Watch Now

### 1. Run a Test
```bash
./scripts/arc-agi-3-grok-test.sh -l 1
```

### 2. Click the Scorecard URL

The script will show a **prominent, clickable URL**:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🌐 LIVE SCORECARD:

   https://three.arcprize.org/scorecards/a4d76322-d516-460f-b3a8-c5a78460ea82

   👆 Click above to watch games in real-time!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Just click it!** Your browser will open showing:
- 🎮 All games being played
- 📊 Current scores
- 🎯 Game states (playing, won, lost)
- ⏱️ Actions taken
- 🔄 Auto-refreshing updates

## After a Test - Get URLs Anytime

### Show All URLs & Recordings

```bash
./scripts/arc-agi-3-show-urls.sh
```

This displays:

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔗 ARC-AGI-3 URLs Finder
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🌐 LIVE SCORECARD (click to view):

   https://three.arcprize.org/scorecards/{card_id}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎬 AVAILABLE RECORDINGS:

   📼 ls20-fa137e247ce6 (644K)
      Replay: cd arc-prize/ARC-AGI-3 && uv run main.py --agent=ls20...jsonl

   📼 as66-821a4dcad9c2 (2.0M)
      Replay: cd arc-prize/ARC-AGI-3 && uv run main.py --agent=as66...jsonl
```

### What You Get

✅ **Scorecard URL** - Click to view final results  
✅ **Recording commands** - Copy-paste to replay games  
✅ **AgentOps URLs** - If configured (advanced monitoring)

## Three Ways to Watch

### 1. Web Scorecard (Built-in, Easiest) 🌐

**What:** Official ARC-AGI-3 web interface  
**Shows:** Live game progress, scores, states  
**Setup:** None needed - URL printed automatically  
**Click:** The prominent URL during or after test

**Features:**
- Real-time game states
- Current scores for all games
- Actions taken per game
- Win/loss statistics
- Auto-refreshing

### 2. Console Logs (Always Active) 📋

**What:** Real-time action logs in terminal  
**Shows:** Every action as it happens  
**Setup:** None needed - automatic

**Example:**
```
2025-10-05 14:13:01 | INFO | ls20 - ACTION2: count 6, score 150, avg fps 2.5
2025-10-05 14:13:04 | INFO | ls20 - ACTION4: count 7, score 200, avg fps 2.3
```

**Shows:**
- Game ID
- Action taken (ACTION1-7, RESET)
- Action count
- Current score
- Actions per second

### 3. AgentOps Dashboard (Most Powerful) ⭐

**What:** Professional monitoring platform  
**Shows:** Detailed analytics and visualizations  
**Setup:** One-time configuration required

**To Enable:**

1. Get free API key: https://app.agentops.ai
2. Add to `.env`:
   ```bash
   AGENTOPS_API_KEY=aos_your_key
   ```
3. Install:
   ```bash
   cd arc-prize/ARC-AGI-3
   uv sync --extra agentops
   ```

**Features:**
- Live action-by-action playback
- Visual game state
- Token usage tracking
- Cost monitoring
- Performance analytics
- Error debugging
- Beautiful dashboards

## Replay Recordings

Every game is automatically recorded!

### Find Recordings
```bash
./scripts/arc-agi-3-show-urls.sh
```

### Replay a Game
```bash
cd arc-prize/ARC-AGI-3
uv run main.py --agent=ls20-fa137e247ce6.grok4fast...recording.jsonl
```

Just copy-paste the command shown by `arc-agi-3-show-urls.sh`!

## Pro Tips

### Watch Multiple Games at Once

1. **Open 3 windows:**
   - Terminal (console logs)
   - Browser (scorecard)
   - Browser tab (AgentOps - if configured)

2. **Arrange side-by-side** for complete visibility

3. **See everything:**
   - Terminal: Raw action logs
   - Scorecard: Live scores/states
   - AgentOps: Deep analytics

### Quick Replay

After a test completes:
```bash
# Show URLs
./scripts/arc-agi-3-show-urls.sh

# Click scorecard to see final results
# Copy replay command for interesting games
```

### Monitor Long Runs

For tests with many games:
```bash
# Start test
./scripts/arc-agi-3-grok-test.sh --limit 10

# Open scorecard URL immediately
# Leave browser open - it auto-refreshes

# Check progress anytime
tail -f arc-prize/ARC-AGI-3/logs.log
```

## Troubleshooting

### Scorecard URL Not Showing

**Problem:** No URL in output  
**Solution:** 
```bash
# Check logs manually
grep "View your scorecard" arc-prize/ARC-AGI-3/logs.log

# Or use helper
./scripts/arc-agi-3-show-urls.sh
```

### Can't Click URL in Terminal

**Problem:** Terminal doesn't make URLs clickable  
**Solution:**
- Copy-paste the URL manually, or
- Use the helper script which shows it clearly

### Scorecard Not Updating

**Problem:** Scorecard shows old data  
**Solution:** Refresh the browser page

### No Recordings Found

**Problem:** No `.recording.jsonl` files  
**Solution:** 
- Test may still be running
- Check `arc-prize/ARC-AGI-3/recordings/` directory
- Run a new test

## Examples

### Quick Test & Watch
```bash
# Run 1 game
./scripts/arc-agi-3-grok-test.sh -l 1

# Click the prominent scorecard URL that appears
# Watch the game play live!
```

### After Test - Find Everything
```bash
# Get all URLs and commands
./scripts/arc-agi-3-show-urls.sh

# Click scorecard to see results
# Copy replay command for interesting games
```

### Replay Specific Game
```bash
# Show recordings
./scripts/arc-agi-3-show-urls.sh

# Copy the replay command
cd arc-prize/ARC-AGI-3
uv run main.py --agent=ls20-fa137e247ce6...recording.jsonl

# Watch it play again!
```

## Summary

✅ **URLs printed prominently** during test run  
✅ **Helper script** to find URLs anytime  
✅ **Copy-paste commands** for replays  
✅ **Three monitoring options** (scorecard, console, AgentOps)  
✅ **Automatic recordings** of every game

**Start watching:**
```bash
./scripts/arc-agi-3-grok-test.sh -l 1
```

Then click the scorecard URL! 🚀
