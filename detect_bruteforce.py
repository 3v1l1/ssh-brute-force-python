import re
from datetime import datetime

log_file = "ssh_logs.txt"

# Regex patterns
failed_pattern = re.compile(r"Failed password for (invalid user )?(\w+) from ([\d\.]+)")
success_pattern = re.compile(r"Accepted password for (\w+) from ([\d\.]+)")

# Store failed attempts
failed_attempts = {}

# Track already alerted IPs
alerted_ips = set()

# Function to extract timestamp
def extract_time(line):
    parts = line.split()
    if len(parts) > 0:
        return parts[0].split("T")[0] + " " + parts[0].split("T")[1][:8]
    return "Unknown"

with open(log_file, "r") as file:
    for line in file:

        # -------------------------
        # 1. Detect FAILED attempts
        # -------------------------
        failed_match = failed_pattern.search(line)
        if failed_match:
            user = failed_match.group(2)
            ip = failed_match.group(3)
            time = extract_time(line)

            if ip not in failed_attempts:
                failed_attempts[ip] = []

            failed_attempts[ip].append({
                "user": user,
                "time": time
            })

        # -------------------------
        # 2. Detect SUCCESS login
        # -------------------------
        success_match = success_pattern.search(line)
        if success_match:
            user = success_match.group(1)
            ip = success_match.group(2)
            time = extract_time(line)

            # -------------------------
            # 3. Correlation logic
            # -------------------------
            if ip in failed_attempts and len(failed_attempts[ip]) >= 3 and ip not in alerted_ips:

                print("\n🚨 BRUTE FORCE ALERT 🚨")
                print(f"IP Address      : {ip}")
                print(f"Successful User : {user}")
                print(f"Total Failures  : {len(failed_attempts[ip])}")
                print(f"Success Time    : {time}")
                print("Failure Timeline:")

                for attempt in failed_attempts[ip]:
                    print(f"  - {attempt['time']} (user: {attempt['user']})")

                print("-" * 60)

                alerted_ips.add(ip)