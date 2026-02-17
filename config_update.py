#!/usr/bin/env python3
import json

# Load current config
with open('/root/.openclaw/openclaw.json', 'r') as f:
    d = json.load(f)

# Set primary model
d['agents']['defaults']['model']['primary'] = "zai/glm-4-flash"
d['agents']['defaults']['model']['fallbacks'] = ["zai/glm-5", "zai/glm-7"]

# Save
with open('/root/.openclaw/openclaw.json', 'w') as f:
    json.dump(d, f, indent=2)

print("Config updated: Primary model = zai/glm-4-flash")
print("Fallbacks: zai/glm-5, zai/glm-7")
