import json
import os
from datetime import datetime
from pathlib import Path

# Store data in user's home directory
DATA_DIR = Path.home() / ".standup-bot"
DATA_FILE = DATA_DIR / "entries.json"
CONFIG_FILE = DATA_DIR / "config.json"


def ensure_data_dir():
    """Make sure the data folder exists."""
    DATA_DIR.mkdir(exist_ok=True)


def load_entries() -> list:
    """Load all standup entries from the file."""
    ensure_data_dir()
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_entries(entries: list):
    """Save all standup entries to the file."""
    ensure_data_dir()
    with open(DATA_FILE, "w") as f:
        json.dump(entries, f, indent=2)


def get_today_entry() -> dict | None:
    """Get today's entry if it exists."""
    today = datetime.now().strftime("%Y-%m-%d")
    entries = load_entries()
    for entry in entries:
        if entry["date"] == today:
            return entry
    return None


def save_entry(yesterday: str, today: str, blockers: str) -> dict:
    """Save a new standup entry."""
    entries = load_entries()
    now = datetime.now()
    entry = {
        "date": now.strftime("%Y-%m-%d"),
        "day": now.strftime("%A"),
        "time": now.strftime("%H:%M"),
        "yesterday": yesterday,
        "today": today,
        "blockers": blockers,
    }

    # Remove existing entry for today if editing
    entries = [e for e in entries if e["date"] != entry["date"]]
    entries.append(entry)

    # Sort by date
    entries.sort(key=lambda x: x["date"])
    save_entries(entries)
    return entry


def load_config() -> dict:
    """Load user config."""
    ensure_data_dir()
    if not CONFIG_FILE.exists():
        return {}
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)


def save_config(config: dict):
    """Save user config."""
    ensure_data_dir()
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=2)
