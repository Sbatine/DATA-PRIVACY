def main():
    questions = {
        "Is personal data encrypted?": "Encryption",
        "Is user consent collected?": "User Consent",
        "Are strong passwords used?": "Password Security",
        "Is data access restricted?": "Access Control",
        "Are regular backups maintained?": "Backup Security",
        "Is personal data deleted when no longer needed?": "Data Retention",
    }

    score = 0
    print("DATA PRIVACY AUDIT")
    print("------------------")

    for question, category in questions.items():
        answer = input(question + " (yes/no): ").strip().lower()
        if answer == "yes":
            score += 1
            print(category, ": PASS")
        else:
            print(category, ": RISK FOUND")

    total = len(questions)
    print("\nAUDIT REPORT")
    print("Total checks:", total)
    print("Passed checks:", score)
    print("Risks found:", total - score)
    print("Privacy score:", round(score / total * 100, 2), "%")


if __name__ == "__main__":
    main()
