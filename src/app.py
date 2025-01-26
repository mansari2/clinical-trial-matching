from flask import Flask, request, jsonify
from services.matching_service import MatchingService

app = Flask(__name__)
matching_service = MatchingService()

@app.route('/match', methods=['POST'])
def match():
    patient_data = request.json
    matched_trials = matching_service.match_patient_to_trial(patient_data)
    return jsonify(matched_trials)

if __name__ == '__main__':
    app.run(debug=True)