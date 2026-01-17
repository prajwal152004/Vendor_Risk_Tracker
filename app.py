from services.vendor_service import load_vendors, assess_all_vendors, save_risks
from services.exception_handler import create_exception, apply_exception_logic
from dashboards.ciso_dashboard import show_ciso_dashboard
from dashboards.grc_dashboard import show_grc_dashboard

vendors = load_vendors()
risks = assess_all_vendors(vendors)
exceptions = []

# Scenario-based exception handling
for risk in risks:
    vid = risk["vendor_id"]

    if vid == "VND001":  # PayrollPro – active exception
        exc = create_exception(
            vendor_id=vid,
            justification="Business critical payroll processing",
            approved_by="CISO",
            expiry_date="2026-06-30"
        )
        risk, exc = apply_exception_logic(risk, exc)
        exceptions.append(exc)

    elif vid == "VND005":  # InfraOps – expired exception
        exc = create_exception(
            vendor_id=vid,
            justification="Infrastructure emergency access",
            approved_by="CISO",
            expiry_date="2024-12-31"
        )
        risk, exc = apply_exception_logic(risk, exc)
        exceptions.append(exc)

    elif risk["inherent_risk"] >= 70:
        # High risk but no exception approved
        risk["status"] = "Open"

save_risks(risks)

# Dashboards
show_ciso_dashboard(vendors, risks, exceptions)
show_grc_dashboard(risks, exceptions)
