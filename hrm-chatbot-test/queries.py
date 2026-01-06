QUERIES = {

# =====================================================
# ATTENDANCE SUMMARY (MONTH LEVEL – AttendanceSummary)
# =====================================================

# ---- Employee-specific (current month) ----
"attendance.summary.employee.currentmonth": """
SELECT PresentDays, AbsentDays, LeaveDays, LateCount, OvertimeHours
FROM dbo.AttendanceSummary
WHERE EmployeeId = ?
  AND Year = YEAR(GETDATE())
  AND Month = MONTH(GETDATE())
""",

"attendance.summary.employee.leave.currentmonth": """
SELECT LeaveDays
FROM dbo.AttendanceSummary
WHERE EmployeeId = ?
  AND Year = YEAR(GETDATE())
  AND Month = MONTH(GETDATE())
""",

"attendance.summary.employee.overtime.currentmonth": """
SELECT OvertimeHours
FROM dbo.AttendanceSummary
WHERE EmployeeId = ?
  AND Year = YEAR(GETDATE())
  AND Month = MONTH(GETDATE())
""",

# ---- Employee-specific (by month) ----
"attendance.summary.employee.bymonth": """
SELECT PresentDays, AbsentDays, LeaveDays, LateCount, OvertimeHours
FROM dbo.AttendanceSummary
WHERE EmployeeId = ?
  AND Year = ?
  AND Month = ?
""",

# ---- Aggregates / rankings (current month) ----
"attendance.summary.max.present.currentmonth": """
SELECT TOP 1 EmployeeId, PresentDays
FROM dbo.AttendanceSummary
WHERE Year = YEAR(GETDATE())
  AND Month = MONTH(GETDATE())
ORDER BY PresentDays DESC
""",

"attendance.summary.max.absent.currentmonth": """
SELECT TOP 1 EmployeeId, AbsentDays
FROM dbo.AttendanceSummary
WHERE Year = YEAR(GETDATE())
  AND Month = MONTH(GETDATE())
ORDER BY AbsentDays DESC
""",

"attendance.summary.max.late.currentmonth": """
SELECT TOP 1 EmployeeId, LateCount
FROM dbo.AttendanceSummary
WHERE Year = YEAR(GETDATE())
  AND Month = MONTH(GETDATE())
ORDER BY LateCount DESC
""",

"attendance.summary.max.overtime.currentmonth": """
SELECT TOP 1 EmployeeId, OvertimeHours
FROM dbo.AttendanceSummary
WHERE Year = YEAR(GETDATE())
  AND Month = MONTH(GETDATE())
ORDER BY OvertimeHours DESC
""",

# ---- Counts / totals (current month) ----
"attendance.summary.leave.count.currentmonth": """
SELECT COUNT(*) AS EmployeesOnLeave
FROM dbo.AttendanceSummary
WHERE Year = YEAR(GETDATE())
  AND Month = MONTH(GETDATE())
  AND LeaveDays > 0
""",

"attendance.summary.overtime.total.currentmonth": """
SELECT SUM(OvertimeHours) AS TotalOvertime
FROM dbo.AttendanceSummary
WHERE Year = YEAR(GETDATE())
  AND Month = MONTH(GETDATE())
""",

"attendance.summary.zero.present.currentmonth": """
SELECT EmployeeId
FROM dbo.AttendanceSummary
WHERE Year = YEAR(GETDATE())
  AND Month = MONTH(GETDATE())
  AND PresentDays = 0
""",

# ---- Overview (by month) ----
"attendance.summary.overview.bymonth": """
SELECT
  SUM(PresentDays) AS TotalPresentDays,
  SUM(AbsentDays) AS TotalAbsentDays,
  SUM(LeaveDays) AS TotalLeaveDays,
  SUM(LateCount) AS TotalLateCount,
  SUM(OvertimeHours) AS TotalOvertimeHours
FROM dbo.AttendanceSummary
WHERE Year = ?
  AND Month = ?
""",


# =====================================================
# ATTENDANCE DAILY (DAY LEVEL – AttendanceDaily)
# =====================================================

# ---- Employee-specific (today) ----
"attendance.employee.status.today": """
SELECT Status
FROM dbo.AttendanceDaily
WHERE AttendanceDate = (SELECT MAX(AttendanceDate) FROM dbo.AttendanceDaily)
  AND EmployeeId = ?
""",

"attendance.employee.intime.today": """
SELECT InTime
FROM dbo.AttendanceDaily
WHERE AttendanceDate = (SELECT MAX(AttendanceDate) FROM dbo.AttendanceDaily)
  AND EmployeeId = ?
""",

"attendance.employee.outtime.today": """
SELECT OutTime
FROM dbo.AttendanceDaily
WHERE AttendanceDate = (SELECT MAX(AttendanceDate) FROM dbo.AttendanceDaily)
  AND EmployeeId = ?
""",

"attendance.employee.workingminutes.today": """
SELECT WorkingMinutes
FROM dbo.AttendanceDaily
WHERE AttendanceDate = (SELECT MAX(AttendanceDate) FROM dbo.AttendanceDaily)
  AND EmployeeId = ?
""",

# ---- Counts (today) ----
"attendance.present.count.today": """
SELECT COUNT(*) AS PresentCount
FROM dbo.AttendanceDaily
WHERE AttendanceDate = (SELECT MAX(AttendanceDate) FROM dbo.AttendanceDaily)
  AND Status = 'Present'
""",

"attendance.absent.count.today": """
SELECT COUNT(*) AS AbsentCount
FROM dbo.AttendanceDaily
WHERE AttendanceDate = (SELECT MAX(AttendanceDate) FROM dbo.AttendanceDaily)
  AND Status = 'Absent'
""",

# ---- Lists (today) ----
"attendance.present.today": """
SELECT EmployeeId
FROM dbo.AttendanceDaily
WHERE AttendanceDate = (SELECT MAX(AttendanceDate) FROM dbo.AttendanceDaily)
  AND Status = 'Present'
""",

"attendance.absent.today": """
SELECT EmployeeId
FROM dbo.AttendanceDaily
WHERE AttendanceDate = (SELECT MAX(AttendanceDate) FROM dbo.AttendanceDaily)
  AND Status = 'Absent'
""",

"attendance.late.today": """
SELECT EmployeeId
FROM dbo.AttendanceDaily
WHERE AttendanceDate = (SELECT MAX(AttendanceDate) FROM dbo.AttendanceDaily)
  AND Status = 'Late'
""",

"attendance.overtime.today": """
SELECT EmployeeId, OvertimeMinutes
FROM dbo.AttendanceDaily
WHERE AttendanceDate = (SELECT MAX(AttendanceDate) FROM dbo.AttendanceDaily)
  AND OvertimeMinutes > 0
""",

# ---- Extremes (today) ----
"attendance.max.workingminutes.today": """
SELECT TOP 1 EmployeeId, WorkingMinutes
FROM dbo.AttendanceDaily
WHERE AttendanceDate = (SELECT MAX(AttendanceDate) FROM dbo.AttendanceDaily)
ORDER BY WorkingMinutes DESC
""",

"attendance.min.workingminutes.today": """
SELECT TOP 1 EmployeeId, WorkingMinutes
FROM dbo.AttendanceDaily
WHERE AttendanceDate = (SELECT MAX(AttendanceDate) FROM dbo.AttendanceDaily)
ORDER BY WorkingMinutes ASC
"""
}
