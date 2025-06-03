# Daily Todo Generator 🗓️

A minimalistic daily todo generator for macOS that:

- Archives your previous `today.md` from Desktop into a dated folder structure
- Carries over unfinished tasks from the previous day
- Automatically restores recurring tasks (tagged with `#daily`) even if completed
- Creates a fresh `today.md` on your Desktop every day

## 🛠 Setup

1. Save the script as `daily_todo.py` in `~/scripts/`
2. Make sure you have Python 3 installed (macOS has it by default)
3. Create a `LaunchAgent` to run it daily (see below)

## 🚀 LaunchAgent Setup (macOS)

1. Create `~/Library/LaunchAgents/com.user.daily.todo.plist` (UPDATE eugeneperminov AND PATH /Users/eugeneperminov/Projects/daily-md/daily_todo.p WITH YOUR USERNAME AND PATH TO DOWNLOADDED PY SCRIPT):

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
 "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key>
  <string>com.eugeneperminov.daily.todo</string>

  <key>ProgramArguments</key>
  <array>
    <string>/usr/bin/python3</string>
    <string>/Users/eugeneperminov/Projects/daily-md/daily_todo.py</string>
  </array>

  <key>StartCalendarInterval</key>
  <dict>
    <key>Hour</key>
    <integer>0</integer>
    <key>Minute</key>
    <integer>0</integer>
  </dict>

  <key>RunAtLoad</key>
  <true/>

  <key>StandardOutPath</key>
  <string>/tmp/daily_todo.log</string>
  <key>StandardErrorPath</key>
  <string>/tmp/daily_todo.err</string>
</dict>
</plist>
```

2. Load the agent (UPDATE eugeneperminov WITH YOUR USERNAME):

```bash
launchctl load ~/Library/LaunchAgents/com.eugeneperminov.daily.todo.plist
```

## 🔁 Recurring Tasks

Any task ending with `#daily` will reappear each day, even if completed:

```markdown
- [x] Morning stretch #daily
```

Becomes:

```markdown
- [ ] Morning stretch #daily
```

## 📂 File Structure

- Desktop/today.md — your current todo
- ~/todo/past/YYYY/MM/YYYY-MM-DD.md — archived todos

## ✅ Enjoy productive mornings!
