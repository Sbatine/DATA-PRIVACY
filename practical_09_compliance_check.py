def main():
    requirements = [
        "User Consent",
        "Data Encryption",
        "Privacy Policy",
        "Access Control",
        "Data Backup",
        "Data Deletion Policy",
    ]

    completed = []
    print("DATA PROTECTION COMPLIANCE CHECK")
    print("--------------------------------")

    for item in requirements:
        answer = input(f"Is {item} implemented? (yes/no): ").strip().lower()
        if answer == "yes":
            completed.append(item)

    print("\nCOMPLIANCE REPORT")
    print("-----------------")
    for item in requirements:
        status = "Compliant" if item in completed else "Not Compliant"
        print(f"{item}: {status}")

    total = len(requirements)
    done = len(completed)
    print("\nTotal requirements:", total)
    print("Completed:", done)
    print("Pending:", total - done)
    print("Completion percentage:", round(done / total * 100, 2), "%")


if __name__ == "__main__":
    main()



OUTPUT
DATA PROTECTION COMPLIANCE CHECK
--------------------------------

Is User Consent implemented? yes
Is Data Encryption implemented? yes
Is Privacy Policy implemented? no
Is Access Control implemented? yes
Is Data Backup implemented? no
Is Data Deletion Policy implemented? yes

COMPLIANCE REPORT
-----------------
User Consent : Compliant
Data Encryption : Compliant
Privacy Policy : Not Compliant
Access Control : Compliant
Data Backup : Not Compliant
Data Deletion Policy : Compliant

Total Requirements: 6
Completed: 4
Pending: 2
Completion Percentage: 66.67 %
