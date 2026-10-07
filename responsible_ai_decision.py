import datetime
import json

def make_ai_decision(applicant_data: dict) -> dict:
    """
    Simulates an AI system making a decision (e.g., loan approval)
    while incorporating elements of responsible AI management.
    """
    decision_log = {
        "timestamp": datetime.datetime.now().isoformat(),
        "applicant_id": applicant_data.get("id"),
        "input_data": applicant_data,
        "decision": "",
        "reason": [],
        "fairness_check_status": "N/A"
    }

    # --- Core AI Decision Logic (simplified) ---
    # This represents the 'AI system' making a judgment based on rules/model
    score = 0
    if applicant_data.get("credit_score", 0) >= 700:
        score += 3
        decision_log["reason"].append("High credit score.")
    elif applicant_data.get("credit_score", 0) >= 600:
        score += 1
        decision_log["reason"].append("Moderate credit score.")
    else:
        decision_log["reason"].append("Low credit score.")

    if applicant_data.get("income_usd_per_year", 0) >= 50000:
        score += 2
        decision_log["reason"].append("Stable income.")
    else:
        decision_log["reason"].append("Lower income.")

    if applicant_data.get("has_criminal_record", False):
        score -= 5 # Significant penalty for a sensitive attribute
        decision_log["reason"].append("Applicant has a criminal record.")

    if score >= 4:
        decision_log["decision"] = "APPROVED"
        decision_log["reason"].append("Overall score met approval criteria.")
    else:
        decision_log["decision"] = "REJECTED"
        decision_log["reason"].append("Overall score did not meet approval criteria.")

    # --- ISO 42001 Aligned Practices ---

    # 1. Transparency/Explainability: Log the reasons for the decision.
    #    The 'reason' field above directly supports this.

    # 2. Accountability/Auditability: Log all input data and the final decision.
    #    The 'decision_log' object serves as an audit trail.

    # 3. Basic Fairness Check (simplified): Check for potential bias based on a sensitive attribute.
    #    ISO 42001 emphasizes identifying and mitigating risks like discrimination.
    if applicant_data.get("has_criminal_record", False) and decision_log["decision"] == "REJECTED":
        decision_log["fairness_check_status"] = "Potential bias risk: Criminal record heavily influenced rejection. Requires human review."
    elif applicant_data.get("age", 0) < 25 and decision_log["decision"] == "REJECTED" and applicant_data.get("credit_score", 0) >= 650:
        decision_log["fairness_check_status"] = "Potential age bias risk: Young applicant with decent credit rejected. Requires human review."
    else:
        decision_log["fairness_check_status"] = "No immediate fairness concern detected for this decision."

    return decision_log


if __name__ == "__main__":
    applicants = [
        {
            "id": "A001",
            "credit_score": 720,
            "income_usd_per_year": 60000,
            "age": 35,
            "has_criminal_record": False
        },
        {
            "id": "A002",
            "credit_score": 610,
            "income_usd_per_year": 40000,
            "age": 22,
            "has_criminal_record": False
        },
        {
            "id": "A003",
            "credit_score": 750,
            "income_usd_per_year": 80000,
            "age": 45,
            "has_criminal_record": True # This applicant has a record
        },
        {
            "id": "A004",
            "credit_score": 680,
            "income_usd_per_year": 55000,
            "age": 24,
            "has_criminal_record": False
        }
    ]

    print("--- Simulating AI Decisions with Responsible AI Practices ---")
    for i, applicant in enumerate(applicants):
        print(f"\nProcessing Applicant {applicant['id']}...")
        result = make_ai_decision(applicant)
        print(json.dumps(result, indent=2, ensure_ascii=False))
        print("--------------------------------------------------------")

    print("\nThis simulation demonstrates how an AI system can incorporate logging, transparency, and basic fairness checks, aligning with principles of ISO 42001 for responsible AI management.")
