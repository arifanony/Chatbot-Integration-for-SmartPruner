from intent import detect_intent
from queries import QUERIES
from db import run_query

print("HRM Chatbot Test Runner")
print("-----------------------")


# =========================
# PARAMETER EXTRACTORS
# =========================

def extract_employee_id(text):
    for word in text.split():
        if word.isdigit():
            return int(word)
    return None


def extract_year(text):
    for word in text.split():
        if word.isdigit() and len(word) == 4:
            return int(word)
    return None


def extract_month(text):
    months = {
        "january": 1, "february": 2, "march": 3, "april": 4,
        "may": 5, "june": 6, "july": 7, "august": 8,
        "september": 9, "october": 10, "november": 11, "december": 12
    }
    for word in text.lower().split():
        if word in months:
            return months[word]
    return None


# =========================
# MAIN LOOP
# =========================

while True:
    text = input("\nAsk a question (or type exit): ")

    if text.lower() == "exit":
        break

    intent = detect_intent(text)

    if not intent:
        print("❌ Intent not recognized")
        continue

    print("✅ Intent:", intent)

    sql = QUERIES.get(intent)

    if not sql:
        print("❌ No SQL mapped for this intent")
        continue

    params = []

    # ---- EmployeeId ----
    if "EmployeeId" in sql:
        employee_id = extract_employee_id(text)
        if employee_id is None:
            print("❌ Employee ID not found in question")
            continue
        params.append(employee_id)

    # ---- Year ----
    if "Year = ?" in sql:
        year = extract_year(text)
        if year is None:
            print("❌ Year not found in question")
            continue
        params.append(year)

    # ---- Month ----
    if "Month = ?" in sql:
        month = extract_month(text)
        if month is None:
            print("❌ Month not found in question")
            continue
        params.append(month)

    # ---- Validate placeholder count ----
    placeholder_count = sql.count("?")
    if placeholder_count != len(params):
        print("❌ Missing required information in question")
        continue

    # ---- Execute Query ----
    if params:
        rows = run_query(sql, tuple(params))
    else:
        rows = run_query(sql)

    if not rows:
        print("ℹ️ No data returned")
    else:
        print("📊 Result:")
        for row in rows:
            print(row)
