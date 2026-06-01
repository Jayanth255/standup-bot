# 🗓️ Standup Bot

A beautiful daily standup logger for developers — right in your terminal.

No more forgetting what you worked on. Just type `standup log` every morning,
answer 3 questions, and your work diary is saved automatically.

---

## ✨ Features

- 📝 **Log** daily standups with 3 quick prompts
- 📋 **View** past entries in a clean terminal UI
- 📊 **Summary** — generate a weekly digest of your work
- ⚙️ **Config** — personalize with your name and team
- 💾 All data saved locally in `~/.standup-bot/`

---

## 🚀 Installation

**Requirements:** Python 3.8+ and `click`

```bash
# Clone the repo
git clone https://github.com/yourusername/standup-bot.git
cd standup-bot

# Install dependencies
pip install click

# Install the CLI tool
pip install -e .
```

---

## 📖 Usage

```bash
# Log today's standup
standup log

# View recent entries (last 7 by default)
standup view
standup view --limit 14

# Get a weekly summary
standup summary
standup summary --days 14

# Set up your name and team
standup config
standup config --show
```

---

## 💡 Example Session

```
$ standup log

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  🗓️  Daily Standup — Monday, June 01 2026
  Good morning, Alex! 👋
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Answer these 3 quick questions:

1️⃣  What did you work on yesterday?
  → Fixed the login bug and wrote unit tests

2️⃣  What will you work on today?
  → Start on the dashboard redesign

3️⃣  Any blockers? (Enter to skip)
  → Waiting for design mockups from the team

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ✅ Standup logged at 09:02!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

## 📁 Project Structure

```
standup-bot/
├── standup/
│   ├── main.py          # CLI entry point
│   ├── storage.py       # Data read/write
│   └── commands/
│       ├── log.py       # standup log
│       ├── view.py      # standup view
│       ├── summary.py   # standup summary
│       └── config.py    # standup config
├── pyproject.toml
└── README.md
```

---

## 🔮 Roadmap

- [ ] Slack webhook integration
- [ ] AI-generated weekly summary
- [ ] Export to Markdown / PDF
- [ ] GitHub Discussions posting

---

## 📄 License

MIT — free to use and modify.
