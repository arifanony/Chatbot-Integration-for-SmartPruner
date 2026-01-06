# AttendanceDaily – HRM Chatbot Query Registry

**Table Name:** `dbo.AttendanceDaily`  
**Granularity:** One row per Employee per Day  
**Use Case:** Real-time / date-specific attendance queries  
**Data Nature:** Final, business-approved (NOT raw logs)

---

## Table Purpose

`AttendanceDaily` stores finalized daily attendance records for each employee.
This table is the **single source of truth** for all day-level attendance queries
such as presence, absence, lateness, working hours, and overtime.

This table MUST be used for:
- Today’s attendance
- Specific date attendance
- Real-time chatbot responses

---

## Key Columns

- `AttendanceDate` – Date of attendance
- `EmployeeId` – Unique employee identifier
- `ShiftId` – Shift assigned
- `InTime` – First check-in time
- `OutTime` – Last check-out time
- `WorkingMinutes` – Total minutes worked
- `OvertimeMinutes` – Overtime in minutes
- `Status` – Present / Absent / Late
- `ClockOutStatus` – Additional status (nullable)

---

# Supported Chatbot Questions & Queries

---

## 1. Who is absent today?

**Intent Key:** `attendance.absent.today`

```sql
SELECT EmployeeId
FROM dbo.AttendanceDaily
WHERE AttendanceDate = CAST(GETDATE() AS DATE)
  AND Status = 'Absent';
```

**Response Template:**

* If rows exist:
  `Employees {EmployeeIds} are absent today.`
* If no rows:
  `No employees are absent today.`

---

## 2. Who is present today?

**Intent Key:** `attendance.present.today`

```sql
SELECT EmployeeId
FROM dbo.AttendanceDaily
WHERE AttendanceDate = CAST(GETDATE() AS DATE)
  AND Status = 'Present';
```

**Response Template:**

* `Employees {EmployeeIds} are present today.`

---

## 3. Who came late today?

**Intent Key:** `attendance.late.today`

```sql
SELECT EmployeeId
FROM dbo.AttendanceDaily
WHERE AttendanceDate = CAST(GETDATE() AS DATE)
  AND Status = 'Late';
```

**Response Template:**

* `Employees {EmployeeIds} came late today.`
* If no rows:
  `No employees came late today.`

---

## 4. Is employee X present today?

**Intent Key:** `attendance.employee.status.today`

```sql
SELECT Status
FROM dbo.AttendanceDaily
WHERE AttendanceDate = CAST(GETDATE() AS DATE)
  AND EmployeeId = @EmployeeId;
```

**Response Template:**

* `Employee {EmployeeId} is {Status} today.`
* If no row:
  `No attendance record found for employee {EmployeeId} today.`

---

## 5. How many employees are present today?

**Intent Key:** `attendance.present.count.today`

```sql
SELECT COUNT(*) AS PresentCount
FROM dbo.AttendanceDaily
WHERE AttendanceDate = CAST(GETDATE() AS DATE)
  AND Status = 'Present';
```

**Response Template:**

* `{PresentCount} employees are present today.`

---

## 6. How many employees are absent today?

**Intent Key:** `attendance.absent.count.today`

```sql
SELECT COUNT(*) AS AbsentCount
FROM dbo.AttendanceDaily
WHERE AttendanceDate = CAST(GETDATE() AS DATE)
  AND Status = 'Absent';
```

**Response Template:**

* `{AbsentCount} employees are absent today.`

---

## 7. What time did employee X check in today?

**Intent Key:** `attendance.employee.intime.today`

```sql
SELECT InTime
FROM dbo.AttendanceDaily
WHERE AttendanceDate = CAST(GETDATE() AS DATE)
  AND EmployeeId = @EmployeeId;
```

**Response Template:**

* `Employee {EmployeeId} checked in at {InTime}.`
* If NULL:
  `Employee {EmployeeId} has not checked in today.`

---

## 8. What time did employee X check out today?

**Intent Key:** `attendance.employee.outtime.today`

```sql
SELECT OutTime
FROM dbo.AttendanceDaily
WHERE AttendanceDate = CAST(GETDATE() AS DATE)
  AND EmployeeId = @EmployeeId;
```

**Response Template:**

* `Employee {EmployeeId} checked out at {OutTime}.`
* If NULL:
  `Employee {EmployeeId} has not checked out yet.`

---

## 9. How many minutes did employee X work today?

**Intent Key:** `attendance.employee.workingminutes.today`

```sql
SELECT WorkingMinutes
FROM dbo.AttendanceDaily
WHERE AttendanceDate = CAST(GETDATE() AS DATE)
  AND EmployeeId = @EmployeeId;
```

**Response Template:**

* `Employee {EmployeeId} worked for {WorkingMinutes} minutes today.`

---

## 10. Who worked the longest today?

**Intent Key:** `attendance.max.workingminutes.today`

```sql
SELECT TOP 1 EmployeeId, WorkingMinutes
FROM dbo.AttendanceDaily
WHERE AttendanceDate = CAST(GETDATE() AS DATE)
ORDER BY WorkingMinutes DESC;
```

**Response Template:**

* `Employee {EmployeeId} worked the longest today with {WorkingMinutes} minutes.`

---

## 11. Who worked the least today?

**Intent Key:** `attendance.min.workingminutes.today`

```sql
SELECT TOP 1 EmployeeId, WorkingMinutes
FROM dbo.AttendanceDaily
WHERE AttendanceDate = CAST(GETDATE() AS DATE)
ORDER BY WorkingMinutes ASC;
```

**Response Template:**

* `Employee {EmployeeId} worked the least today with {WorkingMinutes} minutes.`

---

## 12. Who did overtime today?

**Intent Key:** `attendance.overtime.today`

```sql
SELECT EmployeeId, OvertimeMinutes
FROM dbo.AttendanceDaily
WHERE AttendanceDate = CAST(GETDATE() AS DATE)
  AND OvertimeMinutes > 0;
```

**Response Template:**

* `Employees {EmployeeIds} did overtime today.`
* If no rows:
  `No overtime was recorded today.`

---

## 13. Attendance summary for a specific date

**Intent Key:** `attendance.summary.bydate`

```sql
SELECT Status, COUNT(*) AS Count
FROM dbo.AttendanceDaily
WHERE AttendanceDate = @Date
GROUP BY Status;
```

**Response Template:**

* `On {Date}, attendance status breakdown is: {StatusCounts}.`

---

## Design Rules (Important)

1. This table is used ONLY for daily or date-specific queries
2. Do NOT use this table for monthly or period summaries
3. No dynamic SQL is allowed
4. AI must NOT invent employee IDs or statuses
5. If no data exists, respond gracefully with “No data available”

---

## Notes for Integration

* All queries are READ-ONLY
* Safe for chatbot integration
* AI responsibility is limited to:

  * Intent detection
  * Parameter extraction
  * Response narration

---

```

---


