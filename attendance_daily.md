

# Supported Chatbot Questions – AttendanceDaily

---

## attendance.absent.today

```sql
SELECT EmployeeId
FROM dbo.AttendanceDaily
WHERE AttendanceDate = (SELECT MAX(AttendanceDate) FROM dbo.AttendanceDaily)
  AND Status = 'Absent';
````

**Response Rules**

* Employees {EmployeeIds} are absent today.
* If no rows: No employees are absent today.

---

## attendance.present.today

```sql
SELECT EmployeeId
FROM dbo.AttendanceDaily
WHERE AttendanceDate = (SELECT MAX(AttendanceDate) FROM dbo.AttendanceDaily)
  AND Status = 'Present';
```

**Response Rules**

* Employees {EmployeeIds} are present today.

---

## attendance.late.today

```sql
SELECT EmployeeId
FROM dbo.AttendanceDaily
WHERE AttendanceDate = (SELECT MAX(AttendanceDate) FROM dbo.AttendanceDaily)
  AND Status = 'Late';
```

**Response Rules**

* Employees {EmployeeIds} came late today.
* If no rows: No employees came late today.

---

## attendance.employee.status.today

```sql
SELECT Status
FROM dbo.AttendanceDaily
WHERE AttendanceDate = (SELECT MAX(AttendanceDate) FROM dbo.AttendanceDaily)
  AND EmployeeId = ?;
```

**Response Rules**

* Employee is {Status} today.
* If no row: No attendance record found for the employee today.

---

## attendance.present.count.today

```sql
SELECT COUNT(*) AS PresentCount
FROM dbo.AttendanceDaily
WHERE AttendanceDate = (SELECT MAX(AttendanceDate) FROM dbo.AttendanceDaily)
  AND Status = 'Present';
```

**Response Rules**

* {PresentCount} employees are present today.

---

## attendance.absent.count.today

```sql
SELECT COUNT(*) AS AbsentCount
FROM dbo.AttendanceDaily
WHERE AttendanceDate = (SELECT MAX(AttendanceDate) FROM dbo.AttendanceDaily)
  AND Status = 'Absent';
```

**Response Rules**

* {AbsentCount} employees are absent today.

---

## attendance.employee.intime.today

```sql
SELECT InTime
FROM dbo.AttendanceDaily
WHERE AttendanceDate = (SELECT MAX(AttendanceDate) FROM dbo.AttendanceDaily)
  AND EmployeeId = ?;
```

**Response Rules**

* Employee checked in at {InTime}.
* If NULL: Employee has not checked in today.

---

## attendance.employee.outtime.today

```sql
SELECT OutTime
FROM dbo.AttendanceDaily
WHERE AttendanceDate = (SELECT MAX(AttendanceDate) FROM dbo.AttendanceDaily)
  AND EmployeeId = ?;
```

**Response Rules**

* Employee checked out at {OutTime}.
* If NULL: Employee has not checked out yet.

---

## attendance.employee.workingminutes.today

```sql
SELECT WorkingMinutes
FROM dbo.AttendanceDaily
WHERE AttendanceDate = (SELECT MAX(AttendanceDate) FROM dbo.AttendanceDaily)
  AND EmployeeId = ?;
```

**Response Rules**

* Employee worked for {WorkingMinutes} minutes today.

---

## attendance.max.workingminutes.today

```sql
SELECT TOP 1 EmployeeId, WorkingMinutes
FROM dbo.AttendanceDaily
WHERE AttendanceDate = (SELECT MAX(AttendanceDate) FROM dbo.AttendanceDaily)
ORDER BY WorkingMinutes DESC;
```

**Response Rules**

* Employee worked the longest today with {WorkingMinutes} minutes.

---

## attendance.min.workingminutes.today

```sql
SELECT TOP 1 EmployeeId, WorkingMinutes
FROM dbo.AttendanceDaily
WHERE AttendanceDate = (SELECT MAX(AttendanceDate) FROM dbo.AttendanceDaily)
ORDER BY WorkingMinutes ASC;
```

**Response Rules**

* Employee worked the least today with {WorkingMinutes} minutes.

---

## attendance.overtime.today

```sql
SELECT EmployeeId, OvertimeMinutes
FROM dbo.AttendanceDaily
WHERE AttendanceDate = (SELECT MAX(AttendanceDate) FROM dbo.AttendanceDaily)
  AND OvertimeMinutes > 0;
```

**Response Rules**

* Employees {EmployeeIds} did overtime today.
* If no rows: No overtime was recorded today.


