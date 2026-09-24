# Eligibility checks

age = 21
education = "B.Sc"
percentage = 67

if age >= 18 and education in {"B.Sc", "BCA", "B.Tech"} and percentage >= 60:
    print("Meets the basic eligibility criteria")
else:
    print("Does not meet the basic criteria")

# Loan document screening
income = 45000
credit_score = 735
documents_complete = True

if income >= 25000 and credit_score >= 700 and documents_complete:
    print("Application can move to the next stage")
else:
    print("Additional review required")
