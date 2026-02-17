#!/usr/bin/env python3
"""
Configure OpenClaw model routing based on task complexity:
- Simple tasks (grep, file edits, quick responses) → glm-4-flash (fast, cheap)
- Medium tasks (HTML generation, standard coding) → glm-4.7 (balanced)
- Complex tasks (research, analysis, reasoning) → glm-5 (powerful)
"""
import json

# Load current config
with open('/root/.openclaw/openclaw.json', 'r') as f:
    d = json.load(f)

# Update primary model to flash for simple tasks
d['agents']['defaults']['model']['primary'] = "zai/glm-4-flash"

# Set fallbacks in order of complexity
d['agents']['defaults']['model']['fallbacks'] = [
    "zai/glm-4.7",      # Medium complexity
    "zai/glm-5",        # Complex tasks
    "moonshot/kimi-k2.5"  # Final fallback
]

# Add task-based routing hints
d['agents']['defaults']['model']['routing'] = {
    "simple": "zai/glm-4-flash",      # Quick responses, file edits, grep
    "medium": "zai/glm-4.7",          # HTML generation, standard coding
    "complex": "zai/glm-5"            # Research, analysis, reasoning
}

# Ensure all models are available in the providers list
if 'zai' in d['models']['providers']:
    models = d['models']['providers']['zai']['models']
    model_ids = [m['id'] for m in models]
    
    # Add glm-4-flash if not present
    if 'glm-4-flash' not in model_ids:
        models.append({
            "id": "glm-4-flash",
            "name": "GLM 4 Flash",
            "reasoning": False,
            "input": ["text"],
            "cost": {"input": 0, "output": 0, "cacheRead": 0, "cacheWrite": 0},
            "contextWindow": 128000,
            "maxTokens": 4096
        })

# Save updated config
with open('/root/.openclaw/openclaw.json', 'w') as f:
    json.dump(d, f, indent=2)

print("✅ Model routing configured:")
print(f"  Primary (simple): {d['agents']['defaults']['model']['primary']}")
print(f"  Fallbacks: {', '.join(d['agents']['defaults']['model']['fallbacks'])}")
print(f"  Routing: {d['agents']['defaults']['model'].get('routing', {})}")
