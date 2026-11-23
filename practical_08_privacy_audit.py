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


OUTPUT
DATA PRIVACY AUDIT
------------------

Is personal data encrypted? yes
Encryption : PASS

Is user consent collected? yes
User Consent : PASS

Are strong passwords used? no
Password Security : RISK FOUND

Is data access restricted? yes
Access Control : PASS

Are regular backups maintained? no
Backup Security : RISK FOUND

Is personal data deleted when no longer needed? yes
Data Retention : PASS

AUDIT REPORT
Total Checks: 6
Passed Checks: 4
Risk Found: 2
Privacy Score: 66.66666666666666 %
