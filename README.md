
# HRM Chatbot Integration

## Overview

This repository contains the backend logic and query registry for the **HRM Chatbot Integration**.
The chatbot allows users to query HRM attendance data using **text or voice input** in a safe,
controlled, and enterprise-ready manner.

The design ensures **zero hallucination risk**, **strict data access control**, and
**predictable behavior** suitable for HR and compliance-sensitive environments.

---

## Scope (Phase 1)

The initial implementation supports attendance-related queries using the following tables:

- `AttendanceDaily` – Daily attendance and real-time status
- `AttendanceSummary` – Monthly and period-based summaries

Future phases may extend support to additional HR modules.

---

## High-Level Flow

1. User opens the HRM application.
2. User interacts with the chatbot via:
   - Quick suggestion buttons
   - Text input
   - Voice input
3. The application sends the request to the backend chatbot API.
4. Input is converted to text (if voice).
5. An intent is detected using rule-based and AI-assisted matching.
6. The intent is mapped to a **predefined SQL query**.
7. The query is executed using **read-only database access**.
8. Results are formatted into a human-readable response.
9. The response is returned to the application as text (and optionally voice).

---

## Safety & Data Protection

This chatbot is designed to protect HR data at all times.

- No dynamic SQL generation
- No free-form AI-generated answers
- Strict intent-to-query mapping
- Read-only database credentials
- Deterministic outputs for the same inputs
- No modification of HR data

AI is used **only** for:
- Intent detection
- Typo tolerance
- Natural language normalization

AI is **not** used to generate data or make assumptions.

---

## Architecture

- **Frontend:** Flutter (HRM Application)
- **Backend:** .NET API (Chatbot Service)
- **Database:** SQL Server
- **Access Level:** Read-only
- **Intent Engine:** Rule-based + AI-assisted matching
- **Query Execution:** Parameterized SQL only

---

## Repository Structure

Chatbot-Integration-for-SmartPruner/
│
├── README.md                     # HRM Chatbot integration overview & design
├── attendance_daily.md           # Intent + SQL mapping for AttendanceDaily
├── attendance_summary.md         # Intent + SQL mapping for AttendanceSummary
│
├── hrm-chatbot-test/             # Chatbot PoC / test harness
   ├── app.py                    # Local chatbot test runner (CLI-based)
   ├── intent.py                 # Intent detection logic
   ├── queries.py                # Intent-to-SQL mapping registry
   ├── db.py                     # Read-only database connection & executor
   └── __pycache__/              # Python cache (ignored in production)
         

---

## Supported Features

- Daily attendance queries
- Monthly attendance summaries
- Employee-specific queries
- Count-based analytics
- Overtime tracking
- Late and absence tracking

---

## Voice Support

Voice queries follow the same execution flow as text queries:

- Voice → Speech-to-text
- Text → Intent detection
- Intent → SQL query
- SQL result → Text response
- Optional text-to-speech response

---

## Deployment Notes

- Chatbot logic is deployed as part of the backend API.
- Flutter consumes the API responses.
- No database schema changes are required.
- No additional tables are created.

---

## Design Principles

- Safety first
- No hallucination
- Predictable outputs
- Audit-friendly
- Enterprise-ready
- Easy to extend

---

## Author

**Designed & Implemented by:** Arif

---

## License

Will be added in the Future :)



