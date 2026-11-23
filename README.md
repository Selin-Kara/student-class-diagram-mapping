# Mapping Design to Code (Student Class Diagram)

This repository contains a simple Python implementation mapped from a **Student - Course UML Class Diagram**.

## UML Class Diagram

```text
+---------------------------+          +---------------------------+
|          Student          |          |          Course           |
+---------------------------+          +---------------------------+
| - student_id: String      |          | - course_code: String     |
| - name: String            |          | - course_name: String     |
| - department: String      |  1    *  | - credit: int             |
| - courses: List           |----------|                           |
+---------------------------+          +---------------------------+
| + add_course(course)      |          | + display_course()        |
| + show_info()             |          |                           |
+---------------------------+          +---------------------------+
```

## Files
- `student_system.py`: Python implementation of the `Student` and `Course` classes with a test scenario.
