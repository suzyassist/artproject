#!/bin/bash
# Token Usage Tracker - Run every hour
# Logs token usage to /root/.openclaw/workspace/TOKEN_LOG.md

LOG_FILE="/root/.openclaw/workspace/TOKEN_LOG.md"
TIMESTAMP=$(date '+%Y-%m-%d %H:00')

# Get current hour
HOUR=$(date '+%H')
DATE=$(date '+%Y-%m-%d')

# Check if log file exists, create if not
if [ ! -f "$LOG_FILE" ]; then
    cat > "$LOG_FILE" << 'EOF'
# Token Usage Log (Hourly)

Tracking API token consumption per hour.

| Datum | Uur | Model | Input Est. | Output Est. | Totaal | Kosten | Taak |
|-------|-----|-------|------------|-------------|--------|--------|------|
EOF
fi

# Estimate tokens based on conversation (rough estimate)
# This is a manual entry - the actual API doesn't expose real-time token counts
# Users should update this manually or we integrate with API dashboard

echo ""
echo "=== Token Tracker ==="
echo "Tijd: $TIMESTAMP"
echo ""
echo "Gebruik: ./token_tracker.sh <input_tokens> <output_tokens> <taak>"
echo ""
echo "Voorbeeld:"
echo "  ./token_tracker.sh 50000 5000 'Kunstgeschiedenis updates'"
echo ""
echo "Huidige log:"
tail -5 "$LOG_FILE" 2>/dev/null || echo "Geen data yet"
