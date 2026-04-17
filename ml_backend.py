import json
import random
import time
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# ==========================================
# CLAMP AI - MACHINE LEARNING FRAUD ENGINE
# Hackathon Implementation Backend
# ==========================================

def analyze_vocal_stress(audio_payload):
    """
    Mock function simulating a Deep Learning acoustic model.
    Analyzes micro-tremors in voice recording to detect deception.
    """
    # In a real environment, this would pass audio frames through a PyTorch/Tensorflow model.
    base_stress = random.uniform(5.0, 15.0)
    return round(base_stress, 2)

def audit_fake_bills(image_metadata):
    """
    Mock Computer Vision audit.
    Checks for Photoshop/editing software artifacts in receipt uploads.
    """
    # Simulate checking EXIF data and pixel-level noise discrepancies
    tamper_probability = random.uniform(0.1, 4.0)
    return round(tamper_probability, 2)

def check_historical_theft(user_id, asset_id):
    """
    Mock Blockchain/Ledger cross-check.
    Validates if the user's asset was previously reported stolen on old cards/policies.
    """
    historic_flag = False
    if asset_id == "KNOWN_FRAUD_ID_999":
         historic_flag = True
    return historic_flag

@app.route('/api/fraud_audit', methods=['POST'])
def run_fraud_audit():
    """
    Main API endpoint serving the Dashboard.
    Accepts JSON payloads of a claim and returns the full ML risk profile.
    """
    try:
        data = request.json
        user_id = data.get('user_id', 'UNKNOWN')
        asset_id = data.get('asset_id', 'UNKNOWN')
        
        # Run local ML analysis pipelines
        stress_level = analyze_vocal_stress(None)
        bill_tamper_risk = audit_fake_bills(None)
        is_historic_theft = check_historical_theft(user_id, asset_id)
        
        # Calculate compounded risk
        total_risk_score = stress_level + bill_tamper_risk
        if is_historic_theft:
            total_risk_score += 80.0
            
        status = "APPROVED" if total_risk_score < 30.0 else "FLAGGED FOR REVIEW"
        
        response = {
            "status": "SUCCESS",
            "ml_results": {
                "vocal_stress_index": stress_level,
                "fake_bill_probability": bill_tamper_risk,
                "historical_theft_match": is_historic_theft,
                "overall_fraud_score": round(total_risk_score, 2),
                "decision": status
            },
            "timestamp": time.time()
        }
        
        return jsonify(response), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    print("Initializing Clamp ML Zero-Trust Engine on Port 5000...")
    app.run(debug=True, port=5000)
