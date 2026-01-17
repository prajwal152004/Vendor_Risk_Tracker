def show_grc_dashboard(risks, exceptions):
    print("\n=== GRC ANALYST DASHBOARD ===")

    open_risks = [r for r in risks if r["status"] == "Open"]
    print(f"Open Risks: {len(open_risks)}")

    pending_mitigation = [r for r in risks if r["mitigation"] == "Pending"]
    print(f"Risks Pending Mitigation: {len(pending_mitigation)}")

    expired = [e for e in exceptions if e["status"] == "Expired"]
    print(f"Expired Exceptions: {len(expired)}")
