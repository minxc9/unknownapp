# unknownapp
This is an unknown application written in Java

---- For Submission (you must fill in the information below) ----
### Use Case Diagram
![unknownapp-3](https://github.com/user-attachments/assets/7bd0b347-b7aa-44f0-861d-78095b127675)


### Flowchart of the main workflow
```mermaid
flowchart TD
    A([Start]) --> B[Load or seed data]
    B --> C[Login menu]
    C --> D{Who?}
    D -- Exit --> E([Save and exit])
    D -- Student --> F{ID exists?}
    F -- No --> C
    F -- new --> H[Create profile]
    F -- Yes --> SM
    H --> SM
    D -- Admin --> K{Password correct?}
    K -- No --> C
    K -- Yes --> AM

    subgraph Student
        SM[Student menu]
        SM --> S1[View catalog]
        SM --> S2[Register for course]
        SM --> S3[Drop a course]
        SM --> S4[View schedule]
        SM --> S5[View billing]
        SM --> S6[Edit profile]
        S2 --> S2A{Enrollment check}
        S2A -- Failed --> SM
        S2A -- Passed --> SM
        S3 --> S3A{Enrolled?}
        S3A -- No --> SM
        S3A -- Yes --> SM
    end

    subgraph Admin
        AM[Admin menu]
        AM --> A1[View catalog]
        AM --> A2[View class roster]
        AM --> A3[View all students]
        AM --> A4[Add or edit student]
        AM --> A5[Add or edit course]
        AM --> A6[View student schedule]
        AM --> A7[View billing]
    end

    SM --> S7([Logout and save])
    AM --> A8([Logout and save])
    S7 --> C
    A8 --> C
```

### Prompts
"Write a Python version of View My Schedule for students to See all currently enrolled courses + total credits"
