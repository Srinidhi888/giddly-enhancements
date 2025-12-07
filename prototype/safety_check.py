import re

SUSPICIOUS_KEYWORDS = [
    "guaranteed returns",
    "double your money",
    "earn money fast",
    "investment scheme",
    "crypto profit",
]

def rule_based_risk(title, description, organizer_behavior):
    text = (title + " " + description).lower()
    score = 0.0

    # keyword detection
    for kw in SUSPICIOUS_KEYWORDS:
        if kw in text:
            score += 0.4

    # very short description
    if len(description.split()) < 10:
        score += 0.2

    # spammy formatting
    if re.search(r"[A-Z]{5,}", description):
        score += 0.1

    # suspicious organizer patterns
    if organizer_behavior["events_last_24h"] > 5:
        score += 0.2
    if organizer_behavior["account_age_days"] < 3:
        score += 0.1

    return min(score, 1.0)

def label(score):
    if score >= 0.7:
        return "high_risk"
    elif score >= 0.4:
        return "needs_review"
    return "safe"

if __name__ == "__main__":
    test_event = {
        "title": "Crypto Seminar",
        "description": "Guaranteed returns! Learn how to double your money fast.",
        "organizer_behavior": {
            "events_last_24h": 7,
            "account_age_days": 1
        }
    }

    score = rule_based_risk(
        test_event["title"],
        test_event["description"],
        test_event["organizer_behavior"]
    )

    print("Safety Score:", score)
    print("Label:", label(score))
