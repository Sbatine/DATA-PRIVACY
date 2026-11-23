def main():
    questions = [
        "Is user privacy respected?",
        "Is user consent obtained?",
        "Is personal data protected?",
        "Is data collected only when necessary?",
        "Is data used fairly?",
        "Is user information kept confidential?",
    ]

    score = 0
    print("DATA PRIVACY ETHICS CHECKER")
    print("---------------------------")

    for question in questions:
        answer = input(question + " (yes/no): ").strip().lower()
        if answer == "yes":
            score += 1

    total = len(questions)
    print("\nETHICAL ASSESSMENT REPORT")
    print("-------------------------")
    print("Total questions:", total)
    print("Ethical practices followed:", score)
    print("Issues found:", total - score)

    if score == total:
        print("Result: Good ethical practices")
    elif score >= 4:
        print("Result: Improvement needed")
    else:
        print("Result: Poor ethical practices")

    print("\nProtecting privacy is everyone's responsibility.")


if __name__ == "__main__":
    main()
