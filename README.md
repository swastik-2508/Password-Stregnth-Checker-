# Password Security Tool
### VIT Bhopal University — Python Mini Project

A lightweight, educational **Password Strength Checker** built with Python. Helps users evaluate and improve their passwords through real-time scoring, detailed feedback, and security best practice guidance.

---

## Overview

Weak passwords are one of the most common causes of account compromise. This tool educates users on what makes a password strong, evaluates passwords against key security criteria, and provides actionable, structured feedback.

> **Phase 1** — Password Strength Checker   
> **Phase 2** — Password Generator *(Coming Soon)*

---

## Features

| Feature | Description |
|---|---|
| **Strength Scoring** | 12-point scoring system across 4 security dimensions |
| **Length Analysis** | Scores from 0–4 based on password length (16+ is excellent) |
| **Character Variety** | Checks for uppercase, lowercase, digits, and special characters |
| **Common Password Check** | Flags passwords found in a known weak-password list |
| **Pattern Detection** | Detects sequential (`abc`, `123`) and repetitive (`aaa`, `111`) patterns |
| **Visual Strength Bar** | ASCII progress bar with percentage score |
| **Detailed Feedback** | Itemised checklist of pass/fail criteria with recommendations |
| **Security Tips** | Built-in reference guide for password best practices |

---

## Getting Started

### Prerequisites

- Python 3.x (no external libraries required — uses standard library only)

### Installation

```bash
# Clone the repository
git clone https://github.com/[YourUsername]/VIT-BHOPAL-PASSWORD-STRENGTH-CHECKER.git

# Navigate into the project directory
cd VIT-BHOPAL-PASSWORD-STRENGTH-CHECKER

# Run the tool
python Password_Checker_Final.py
```

---

## Usage

When launched, the tool presents a simple interactive menu:

```
============================================================
               PASSWORD SECURITY TOOL
============================================================
       Protect Your Digital Life with Strong Passwords!
============================================================

MAIN MENU:
------------------------------------------------------------
1. Check Password Strength
2. Generate Strong Password   ← Phase 2 (Coming Soon)
3. View Security Tips
4. Exit
------------------------------------------------------------
```

### Option 1 — Check Password Strength
Enter any password and receive an instant analysis:
- Numerical score out of 12
- ASCII strength bar with percentage
- Overall rating: `VERY WEAK` → `WEAK` → `MODERATE` → `STRONG` → `VERY STRONG`
- Itemised feedback for each criterion

### Option 3 — View Security Tips
Displays 10 essential best practices for password and account security.

---

## Scoring System

| Criterion | Max Points | Details |
|---|---|---|
| **Length** | +4 | 8+ chars = 2pts, 12+ = 3pts, 16+ = 4pts |
| **Uppercase** | +1 | Contains at least one A–Z character |
| **Lowercase** | +1 | Contains at least one a–z character |
| **Digits** | +1 | Contains at least one 0–9 character |
| **Special Chars** | +1 | Contains `!@#$%^&*` etc. |
| **Common Password** | −3 | Found in known weak-password list |
| **Patterns** | −1 | Sequential or repetitive characters detected |

| Score | Rating |
|---|---|
| 9–12 | VERY STRONG |
| 7–8 | STRONG |
| 5–6 | MODERATE |
| 3–4 | WEAK |
| 0–2 | VERY WEAK |

---

## Project Structure

```
VIT-BHOPAL-PASSWORD-STRENGTH-CHECKER/
├── Password_Checker_Final.py   # Main application script
├── README.md                   # Project documentation
└── STATEMENT.md                # Project problem statement & scope
```

---

## Roadmap

- [x] Phase 1: Password Strength Checker (CLI)
- [ ] Phase 2: Customisable Password Generator
- [ ] Phase 3: GUI version with Tkinter
- [ ] Entropy-based scoring
- [ ] External wordlist / HaveIBeenPwned API integration

---

## Contributing

Contributions are welcome! To get started:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/YourFeature`
3. Commit your changes: `git commit -m 'Add YourFeature'`
4. Push to the branch: `git push origin feature/YourFeature`
5. Open a Pull Request

Please keep code clean, commented, and consistent with the existing style.

---

## Privacy

This tool processes all passwords **locally** on your machine. No passwords are stored, logged, or transmitted anywhere.

---

## Academic Info

| Field | Details |
|---|---|
| **University** | VIT Bhopal University |
| **Student** | Swastik Kumar Barik |
| **Registration No.** | 25BOE10064 |
| **Guide** | Dr. A Balaji |

---

## License

This project is open source and available under the [MIT License](LICENSE).
