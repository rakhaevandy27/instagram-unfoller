# Instagram Auto-Unfollow (Female Detection)

This Python script automatically unfollows Instagram accounts that are likely female based on their first names, using a gender detection library.

## 🔧 Features

- ✅ Login to Instagram using saved session or credentials
- ✅ Detect likely female accounts using `gender-guesser`
- ✅ Export list of female users to `female_users.json`
- ✅ Optional unfollow confirmation
- ✅ Logs time elapsed and total unfollowed
- ✅ Auto-installs required packages

---

## 📦 Requirements

The script auto-installs everything, but for manual setup:

```bash
pip install instagrapi gender-guesser
```

---

## 📁 Folder Structure

```
.
├── main.py                 # The main script
├── cred.json              # Your Instagram credentials
├── session.json           # Saved session file (auto-created)
├── female_users.json      # Exported list of female accounts (auto-created)
└── README.md              # This file
```

---

## 🔐 `cred.json` Format

```json
{
  "username": "your_instagram_username",
  "password": "your_instagram_password"
}
```

---

## 🚀 How to Run

```bash
python main.py
```

- The script will auto-install missing packages.
- It fetches your followings, detects likely female accounts, and gives you the option to unfollow them.
- Results are exported to `female_users.json`.

---

## ⚠️ Disclaimer

This tool is for **educational and personal use only**. Use responsibly and avoid violating Instagram's terms of service.

---

## 🛡️ Tips

- Add `cred.json` and `session.json` to `.gitignore` before pushing to GitHub.
- Use a throwaway/test account when experimenting.

---

## ❤️ Credits

Built using:
- [instagrapi](https://github.com/adw0rd/instagrapi)
- [gender-guesser](https://pypi.org/project/gender-guesser/)
