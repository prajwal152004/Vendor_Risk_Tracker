def calculate_risk(access_level, data_sensitivity, criticality, security_rating):
    access_weight = {
        "Read": 1,
        "Read-Write": 2,
        "Admin": 3
    }

    data_weight = {
        "Public": 1,
        "PII": 3,
        "Financial": 4,
        "IP": 4
    }

    criticality_weight = {
        "Low": 1,
        "Medium": 2,
        "High": 3,
        "Critical": 4
    }

    score = (
        access_weight[access_level]
        * data_weight[data_sensitivity]
        * criticality_weight[criticality]
    ) * (5 - security_rating)

    return min(score * 5, 100)
