import uuid

def create_risk(vendor_id, category, description, inherent_risk):
    return {
        "risk_id": f"RISK-{uuid.uuid4().hex[:6]}",
        "vendor_id": vendor_id,
        "risk_category": category,
        "risk_description": description,
        "inherent_risk": inherent_risk,
        "residual_risk": inherent_risk,
        "mitigation": "Pending",
        "risk_owner": "GRC Team",
        "status": "Open"
    }
