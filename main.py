import json
import os
import time
from datetime import datetime
from instagrapi import Client
from instagrapi.exceptions import ChallengeRequired
import gender_guesser.detector as gender

# === Load credentials ===
with open("cred.json") as f:
    creds = json.load(f)

USERNAME = creds["username"]
PASSWORD = creds["password"]
SESSION_FILE = "session.json"

cl = Client()

# === Load saved session or login ===
if os.path.exists(SESSION_FILE):
    print("[*] Loading session...")
    cl.load_settings(SESSION_FILE)
    try:
        cl.login(USERNAME, PASSWORD)
        print("[+] Logged in using saved session!")
    except Exception as e:
        print("[!] Session failed, trying fresh login...", e)
        cl = Client()
else:
    print("[*] No saved session, logging in fresh...")

if not cl.user_id:
    try:
        cl.login(USERNAME, PASSWORD)
        print("[+] Logged in successfully!")
        cl.dump_settings(SESSION_FILE)
        print("[*] Session saved for next time.")
    except ChallengeRequired:
        print("[!] Instagram is asking for a verification code (challenge).")
        exit()

# === Start timer ===
start_time = datetime.now()

# === Get following list ===
print("[*] Fetching your following list...")
following_dict = cl.user_following(cl.user_id)

# === Gender detection ===
d = gender.Detector()
female_users = []

print("[*] Detecting female users...")
for user_id, profile in following_dict.items():
    name = profile.full_name.strip().split(" ")[0] if profile.full_name else ""
    guess = d.get_gender(name)
    if guess in ['female', 'mostly_female']:
        print(f"[+] Likely Female: {name} ({profile.username})")
        female_users.append((user_id, profile.username))

# === Export detected users to JSON ===
if female_users:
    export_data = [{"username": username, "user_id": user_id} for user_id, username in female_users]
    with open("female_users.json", "w") as f:
        json.dump(export_data, f, indent=4)
    print(f"[📁] Exported {len(female_users)} users to female_users.json")

# === Confirm before unfollowing ===
print(f"\n[!] Found {len(female_users)} likely female accounts.")
confirm = input("Unfollow them? (yes/no): ").strip().lower()

unfollowed_count = 0

if confirm == "yes":
    for user_id, username in female_users:
        try:
            cl.user_unfollow(user_id)
            unfollowed_count += 1
            print(f"[-] Unfollowed: {username}")
            time.sleep(2)
        except Exception as e:
            print(f"[!] Could not unfollow {username}: {e}")
else:
    print("[-] Cancelled. No users were unfollowed.")

# === Time summary ===
end_time = datetime.now()
elapsed = end_time - start_time
print("\n=== ✅ DONE ===")
print(f"⏱️ Time Elapsed: {elapsed}")
print(f"👋 Total Unfollowed: {unfollowed_count}")
