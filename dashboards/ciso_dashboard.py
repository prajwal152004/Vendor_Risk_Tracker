def show_ciso_dashboard(vendors, risks, exceptions):
    print("\n=== CISO DASHBOARD ===")

    print(f"Total Vendors: {len(vendors)}")

    high_risk = [r for r in risks if r["residual_risk"] >= 70]
    print(f"High / Critical Risk Vendors: {len(high_risk)}")

    accepted = [r for r in risks if r["status"] == "Risk Accepted"]
    print(f"Risks Accepted by Exception: {len(accepted)}")

    expired = [e for e in exceptions if e["status"] == "Expired"]
    print(f"Expired Exceptions: {len(expired)}")
