import json
from services.risk_scoring import calculate_risk
from services.risk_register import create_risk

VENDOR_FILE = "data/vendors.json"
RISK_FILE = "data/risks.json"

def load_vendors():
    with open(VENDOR_FILE) as f:
        return json.load(f)

def load_risks():
    try:
        with open(RISK_FILE) as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_risks(risks):
    with open(RISK_FILE, "w") as f:
        json.dump(risks, f, indent=2)

def assess_all_vendors(vendors):
    risks = []

    for vendor in vendors:
        score = calculate_risk(
            vendor["access_level"],
            vendor["data_sensitivity"],
            vendor["criticality"],
            vendor["security_rating"]
        )

        risk = create_risk(
            vendor_id=vendor["vendor_id"],
            category="Third Party Risk",
            description=f"{vendor['vendor_name']} has access to {vendor['data_sensitivity']} data",
            inherent_risk=score
        )

        risks.append(risk)

    return risks
