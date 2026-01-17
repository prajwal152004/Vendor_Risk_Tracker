import streamlit as st
import json
from services.vendor_service import load_vendors, assess_all_vendors
from services.exception_handler import create_exception, apply_exception_logic

# -----------------------------
# Load Data
# -----------------------------
vendors = load_vendors()
risks = assess_all_vendors(vendors)
exceptions = []

# -----------------------------
# Scenario Logic (same as app.py)
# -----------------------------
for risk in risks:
    vid = risk["vendor_id"]

    if vid == "VND001":  # PayrollPro – Active Exception
        exc = create_exception(
            vendor_id=vid,
            justification="Business critical payroll processing",
            approved_by="CISO",
            expiry_date="2026-06-30"
        )
        risk, exc = apply_exception_logic(risk, exc)
        exceptions.append(exc)

    elif vid == "VND005":  # InfraOps – Expired Exception
        exc = create_exception(
            vendor_id=vid,
            justification="Emergency infrastructure access",
            approved_by="CISO",
            expiry_date="2024-12-31"
        )
        risk, exc = apply_exception_logic(risk, exc)
        exceptions.append(exc)

    elif risk["inherent_risk"] >= 70:
        risk["status"] = "Open"

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="Third Party Risk Dashboard", layout="wide")

st.title("🔐 Third Party Vendor Risk Management")

# Sidebar
view = st.sidebar.selectbox(
    "Select View",
    ["CISO Dashboard", "GRC Analyst Dashboard", "Vendor Details"]
)

# -----------------------------
# CISO DASHBOARD
# -----------------------------
if view == "CISO Dashboard":
    st.header("📊 CISO Dashboard")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Vendors", len(vendors))

    high_risk = [r for r in risks if r["residual_risk"] >= 70]
    col2.metric("High / Critical Risks", len(high_risk))

    accepted = [r for r in risks if r["status"] == "Risk Accepted"]
    col3.metric("Risks Accepted", len(accepted))

    expired = [e for e in exceptions if e["status"] == "Expired"]
    col4.metric("Expired Exceptions", len(expired))

    st.subheader("🔴 High Risk Vendors")
    st.table([
        {
            "Vendor ID": r["vendor_id"],
            "Risk": r["residual_risk"],
            "Status": r["status"]
        }
        for r in high_risk
    ])

# -----------------------------
# GRC ANALYST DASHBOARD
# -----------------------------
elif view == "GRC Analyst Dashboard":
    st.header("🧩 GRC Analyst Dashboard")

    open_risks = [r for r in risks if r["status"] == "Open"]
    st.metric("Open Risks", len(open_risks))

    st.subheader("📌 Risk Register")
    st.table(risks)

    st.subheader("⏰ Exceptions")
    st.table(exceptions)

# -----------------------------
# VENDOR DETAILS VIEW
# -----------------------------
elif view == "Vendor Details":
    st.header("🏢 Vendor Inventory")

    selected_vendor = st.selectbox(
        "Select Vendor",
        [v["vendor_name"] for v in vendors]
    )

    vendor = next(v for v in vendors if v["vendor_name"] == selected_vendor)
    vendor_risk = next(r for r in risks if r["vendor_id"] == vendor["vendor_id"])

    st.json(vendor)
    st.subheader("Associated Risk")
    st.json(vendor_risk)
