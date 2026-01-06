
# Supported Chatbot Questions (AttendanceSummary)

---

## Attendance summary for the current month for a specific employee

**Intent Key:** `attendance.summary.employee.currentmonth`

```sql
SELECT PresentDays, AbsentDays, LeaveDays, LateCount, OvertimeHours
FROM dbo.AttendanceSummary
WHERE EmployeeId = ?
  AND Year = YEAR(GETDATE())
  AND Month = MONTH(GETDATE());
````

**Response Rules:**

* Present {PresentDays} days, Absent {AbsentDays} days, Leave {LeaveDays} days, Late {LateCount} times, Overtime {OvertimeHours} hours.
* If no record exists: No monthly attendance data found for the employee.

---

## Attendance summary for a specific employee for a given month

**Intent Key:** `attendance.summary.employee.bymonth`

```sql
SELECT PresentDays, AbsentDays, LeaveDays, LateCount, OvertimeHours
FROM dbo.AttendanceSummary
WHERE EmployeeId = ?
  AND Year = ?
  AND Month = ?;
```

**Response Rules:**

* Present {PresentDays} days, Absent {AbsentDays} days, Leave {LeaveDays} days, Late {LateCount} times, Overtime {OvertimeHours} hours.
* If no record exists: No monthly attendance data found for the selected period.

---

## Who has the highest late count this month?

**Intent Key:** `attendance.summary.max.late.currentmonth`

```sql
SELECT TOP 1 EmployeeId, LateCount
FROM dbo.AttendanceSummary
WHERE Year = YEAR(GETDATE())
  AND Month = MONTH(GETDATE())
ORDER BY LateCount DESC;
```

**Response Rules:**

* Employee {EmployeeId} has the highest late count this month with {LateCount} late marks.
* If no record exists: No late records found for this month.

---

## Who has the most absent days this month?

**Intent Key:** `attendance.summary.max.absent.currentmonth`

```sql
SELECT TOP 1 EmployeeId, AbsentDays
FROM dbo.AttendanceSummary
WHERE Year = YEAR(GETDATE())
  AND Month = MONTH(GETDATE())
ORDER BY AbsentDays DESC;
```

**Response Rules:**

* Employee {EmployeeId} has the most absences this month with {AbsentDays} days.
* If no record exists: No absence records found for this month.

---

## Who worked the most days this month?

**Intent Key:** `attendance.summary.max.present.currentmonth`

```sql
SELECT TOP 1 EmployeeId, PresentDays
FROM dbo.AttendanceSummary
WHERE Year = YEAR(GETDATE())
  AND Month = MONTH(GETDATE())
ORDER BY PresentDays DESC;
```

**Response Rules:**

* Employee {EmployeeId} worked the most days this month with {PresentDays} days.
* If no record exists: No attendance records found for this month.

---

## Who did the most overtime this month?

**Intent Key:** `attendance.summary.max.overtime.currentmonth`

```sql
SELECT TOP 1 EmployeeId, OvertimeHours
FROM dbo.AttendanceSummary
WHERE Year = YEAR(GETDATE())
  AND Month = MONTH(GETDATE())
ORDER BY OvertimeHours DESC;
```

**Response Rules:**

* Employee {EmployeeId} logged the highest overtime this month with {OvertimeHours} hours.
* If no record exists: No overtime records found for this month.

---

## How many leave days did an employee take this month?

**Intent Key:** `attendance.summary.employee.leave.currentmonth`

```sql
SELECT LeaveDays
FROM dbo.AttendanceSummary
WHERE EmployeeId = ?
  AND Year = YEAR(GETDATE())
  AND Month = MONTH(GETDATE());
```

**Response Rules:**

* Employee took {LeaveDays} leave days this month.
* If no record exists: No leave data found for the employee this month.

---

## Total overtime hours for an employee this month

**Intent Key:** `attendance.summary.employee.overtime.currentmonth`

```sql
SELECT OvertimeHours
FROM dbo.AttendanceSummary
WHERE EmployeeId = ?
  AND Year = YEAR(GETDATE())
  AND Month = MONTH(GETDATE());
```

**Response Rules:**

* Employee logged {OvertimeHours} overtime hours this month.
* If no record exists: No overtime data found for the employee this month.

---

## Total overtime hours for all employees this month

**Intent Key:** `attendance.summary.overtime.total.currentmonth`

```sql
SELECT SUM(OvertimeHours) AS TotalOvertime
FROM dbo.AttendanceSummary
WHERE Year = YEAR(GETDATE())
  AND Month = MONTH(GETDATE());
```

**Response Rules:**

* Total overtime recorded this month is {TotalOvertime} hours.
* If no record exists: No overtime data found for this month.

---

## How many employees took leave this month?

**Intent Key:** `attendance.summary.leave.count.currentmonth`

```sql
SELECT COUNT(*) AS EmployeesOnLeave
FROM dbo.AttendanceSummary
WHERE Year = YEAR(GETDATE())
  AND Month = MONTH(GETDATE())
  AND LeaveDays > 0;
```

**Response Rules:**

* {EmployeesOnLeave} employees took leave this month.
* If no record exists: No leave records found for this month.

---

## Employees with zero present days this month

**Intent Key:** `attendance.summary.zero.present.currentmonth`

```sql
SELECT EmployeeId
FROM dbo.AttendanceSummary
WHERE Year = YEAR(GETDATE())
  AND Month = MONTH(GETDATE())
  AND PresentDays = 0;
```

**Response Rules:**

* Employees {EmployeeIds} have zero present days this month.
* If no record exists: All employees have at least one present day this month.

---

## Attendance overview for a given month

**Intent Key:** `attendance.summary.overview.bymonth`

```sql
SELECT 
  SUM(PresentDays) AS TotalPresentDays,
  SUM(AbsentDays) AS TotalAbsentDays,
  SUM(LeaveDays) AS TotalLeaveDays,
  SUM(LateCount) AS TotalLateCount,
  SUM(OvertimeHours) AS TotalOvertimeHours
FROM dbo.AttendanceSummary
WHERE Year = ?
  AND Month = ?;
```

**Response Rules:**

* Overview for {Month}/{Year}: Present {TotalPresentDays}, Absent {TotalAbsentDays}, Leave {TotalLeaveDays}, Late {TotalLateCount}, Overtime {TotalOvertimeHours}.
* If no record exists: No attendance data found for the selected month.

```


