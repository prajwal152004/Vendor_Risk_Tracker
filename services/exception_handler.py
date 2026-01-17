from datetime import datetime

def create_exception(vendor_id, justification, approved_by, expiry_date):
    return {
        "exception_id": f"EXC-{vendor_id}",
        "vendor_id": vendor_id,
        "justification": justification,
        "approved_by": approved_by,
        "expiry_date": expiry_date,
        "status": "Approved"
    }

def is_exception_expired(expiry_date):
    today = datetime.now().date()
    return today > datetime.strptime(expiry_date, "%Y-%m-%d").date()

def apply_exception_logic(risk, exception):
    if is_exception_expired(exception["expiry_date"]):
        risk["residual_risk"] = risk["inherent_risk"]
        risk["status"] = "Exception Expired"
        exception["status"] = "Expired"
    else:
        risk["residual_risk"] = int(risk["inherent_risk"] * 0.7)
        risk["status"] = "Risk Accepted"

    return risk, exception
