import datetime
from pathlib import Path

# 📁 Paths
desktop = Path.home() / "Desktop"
today_file = desktop / "today.md"
archive_root = Path.home() / "todo" / "past"

# 📅 Dates
today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
yesterday_str = yesterday.isoformat()
year = str(yesterday.year)
month = f"{yesterday.month:02d}"
archive_dir = archive_root / year / month
archive_dir.mkdir(parents=True, exist_ok=True)

# 📄 Archive yesterday's today.md
yesterday_file = archive_dir / f"{yesterday_str}.md"
unfinished_tasks = []
repeating_tasks = []

if today_file.exists():
    with open(today_file, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("- [ ]"):
            unfinished_tasks.append(line)
        elif "#daily" in stripped.lower():
            # Convert completed to unchecked
            reset_line = line.replace("- [x]", "- [ ]").replace("- [X]", "- [ ]")
            repeating_tasks.append(reset_line)

    today_file.rename(yesterday_file)

# 📝 Create new today.md
with open(today_file, "w", encoding="utf-8") as f:
    f.write(f"# 📅 {today.isoformat()}\n\n")
    f.write("## 🔥 Top 3 Tasks\n\n")
    f.write("## 🧠 Brain Dump\n\n")

    if repeating_tasks:
        f.write("## 🔁 Recurring Tasks\n")
        f.writelines(repeating_tasks)
        f.write("\n")

    if unfinished_tasks:
        f.write(f"## 📌 Carried Over from {yesterday_str}\n")
        f.writelines(unfinished_tasks)
