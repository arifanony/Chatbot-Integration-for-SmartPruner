def detect_intent(text: str):
    text = text.lower()

    # =====================================================
    # ATTENDANCE SUMMARY (MONTH LEVEL)
    # =====================================================

    # ---- Employee-specific (highest priority) ----
    if "attendance summary" in text and "employee" in text and "this month" in text:
        return "attendance.summary.employee.currentmonth"

    if "attendance summary" in text and "employee" in text and "month" in text:
        return "attendance.summary.employee.bymonth"

    if "leave" in text and "employee" in text and "this month" in text:
        return "attendance.summary.employee.leave.currentmonth"

    if "overtime" in text and "employee" in text and "this month" in text:
        return "attendance.summary.employee.overtime.currentmonth"

    # ---- Rankings / max (this month) ----
    if ("most" in text or "highest" in text) and "overtime" in text and "this month" in text:
        return "attendance.summary.max.overtime.currentmonth"

    if ("most" in text or "highest" in text) and "late" in text and "this month" in text:
        return "attendance.summary.max.late.currentmonth"

    if ("most" in text or "highest" in text) and "absent" in text and "this month" in text:
        return "attendance.summary.max.absent.currentmonth"

    if (
        ("most" in text or "highest" in text)
        and "this month" in text
        and ("present" in text or "worked" in text or "days" in text)
    ):
        return "attendance.summary.max.present.currentmonth"

    # ---- Counts / totals (this month) ----
    if "how many" in text and "leave" in text and "this month" in text:
        return "attendance.summary.leave.count.currentmonth"

    if "total" in text and "overtime" in text and "this month" in text:
        return "attendance.summary.overtime.total.currentmonth"

    if "zero" in text and "present" in text and "this month" in text:
        return "attendance.summary.zero.present.currentmonth"

    # ---- Overview ----
    if "attendance" in text and "overview" in text:
        return "attendance.summary.overview.bymonth"


    # =====================================================
    # ATTENDANCE DAILY (DAY LEVEL)
    # =====================================================

    # ---- Employee-specific (today) ----
    if "status" in text and "employee" in text and "today" in text:
        return "attendance.employee.status.today"

    if "check in" in text or "checked in" in text:
        return "attendance.employee.intime.today"

    if "check out" in text or "checked out" in text:
        return "attendance.employee.outtime.today"

    if "worked" in text and "minutes" in text and "today" in text:
        return "attendance.employee.workingminutes.today"

    # ---- Counts (today) — MUST COME BEFORE LISTS ----
    if "how many" in text and "present" in text and "today" in text:
        return "attendance.present.count.today"

    if "how many" in text and "absent" in text and "today" in text:
        return "attendance.absent.count.today"

    # ---- Lists (today) ----
    if "present" in text and "today" in text:
        return "attendance.present.today"

    if "absent" in text and "today" in text:
        return "attendance.absent.today"

    if "late" in text and "today" in text:
        return "attendance.late.today"

    if "overtime" in text and "today" in text:
        return "attendance.overtime.today"

    # ---- Extremes (today) ----
    if ("most" in text or "longest" in text) and "worked" in text and "today" in text:
        return "attendance.max.workingminutes.today"

    if ("least" in text or "minimum" in text) and "worked" in text and "today" in text:
        return "attendance.min.workingminutes.today"

    return None
