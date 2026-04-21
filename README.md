# LSN-0104 — Introduction to Programming with Python
**Hult International Business School**

Instructor: 
C. Todd Lombardo — todd.lombardo@faculty.hult.edu

<img width="875" height="432" alt="imagen" src="https://github.com/user-attachments/assets/783de040-3cd0-4053-8662-7c1b038406bf" />

---

## Open in Codespaces

The fastest way to start coding — no installation required. Click the button below and you'll have a fully configured Python environment running in your browser in about 60 seconds.

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/Hult-LSN0104/SUM1-2026?template=true)

> **First time?** See [How to Use This Repo](#how-to-use-this-repo) below.

---

## What's in This Repo

```
📁 sessions/          Slides and starter code, organised by session
📁 datasets/          CSV files used in class activities
📁 problem-sets/      Weekly assignments with instructions and starter files
📁 capstone/          Final project brief and dataset
📄 resources.md       Useful links: docs, practice sites, free books
```

---

## How to Use This Repo

### Option A — GitHub Codespaces (recommended)
Works entirely in your browser. Nothing to install.

1. Click the **Open in GitHub Codespaces** button above
2. Wait about 60 seconds for the environment to load
3. You'll see a VS Code editor in your browser — you're ready to code
4. Navigate to the session folder (e.g. `sessions/week1-session1/`)
5. Open `starter.py` and follow the instructions inside

> Your Codespace saves automatically. You can close the tab and come back later — your work will still be there.

### Option B — Run locally — {{ ONLY IF OPTION A WILL NOT WORK }}
If you prefer to work on your own machine:

1. Install [Python 3.x](https://python.org/downloads) and [VS Code](https://code.visualstudio.com)
2. Install the Python extension in VS Code
3. Clone this repo or download it as a ZIP
4. Open the folder in VS Code and start coding

---

## Set Up Your Anthropic API Key

Some activities in this course use AI via the Anthropic API. You'll need your own key.

1. Go to [console.anthropic.com](https://console.anthropic.com) and create an account
2. Navigate to **Settings → Billing** and add $5 in credits (plenty for the whole course)
3. Navigate to **Settings → API Keys → Create Key**, copy the key (starts with `sk-ant-...`)
4. On GitHub: click your profile picture → **Settings → Codespaces → Codespaces secrets → New secret**
5. Name: `ANTHROPIC_API_KEY`, Value: paste your key
6. Under "Repository access," select your copy of this course repo
7. **Restart your Codespace** for the secret to load

Verify it worked — in your Codespace terminal:

```bash
echo $ANTHROPIC_API_KEY | wc -c
```

Should show ~108 (not 1). 
If you get 1, the secret didn't load. Stop and start your Codespace from github.com/codespaces.

---

## Course Structure at a Glance

| Week | Topic | Sessions |
|------|-------|----------|
| 1 | Getting Started with Python | Setup, syntax, variables, data types |
| 2 | Working with Data and Text | Strings, numbers, business calculations |
| 3 | Control Structures | Conditionals, loops, midpoint quiz |
| 4 | Functions | Modular programming, error handling |
| 5 | Data Collections | Lists, tuples, dictionaries |
| 6 | File Handling & Capstone | CSV files, final project, presentations |

Full syllabus and assignment details are on Canvas.

---

## Datasets

These files are used in class activities and problem sets. They live in the `datasets/` folder.

| File | Used In |
|------|---------|
| `customers.csv` | Session 3 — string cleaning exercise |
| `sales.csv` | Sessions 11 & 12 — file I/O and capstone |
| `inventory.csv` | Session 9 — lists activity |
| `transactions.csv` | Session 12 — capstone project |

---

## Problem Sets

Problem sets are released each week after the second session. You'll find them in the `problem-sets/` folder. Each one has:
- `instructions.md` — what to do and how it's graded
- `starter.py` — a file with structure already in place; fill in your code where indicated

Submit your completed `.py` file on Canvas by the deadline.

---

## Resources

See [`resources.md`](resources.md) for a curated list of links — documentation, practice exercises, and free books.

---

## Questions?

- **During class:** just ask
- **Outside class:** post in the Canvas discussion board so everyone benefits from the answer
- **Email:** todd.lombardo@faculty.hult.edu — I aim to reply within 24 to 36 hours on weekdays

---

*This repository is for LSN-0104 students at Hult International Business School.* 

*Please do not share starter code or solutions publicly.*
