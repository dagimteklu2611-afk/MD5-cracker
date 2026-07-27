def crack_hash(target_hash, hash_file="hashes.txt"):
    target_hash = target_hash.strip().lower()
    try:
        with open(hash_file, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if ":" in line:
                    h, word = line.split(":", 1)
                    if h.strip().lower() == target_hash:
                        return f"[+] Match found! Plaintext: {word.strip()}"
        return "[-] No matching hash found in hash list."
    except FileNotFoundError:
        return f"[-] Error: '{hash_file}' not found. Run generate_hashes.py first."

if __name__ == "__main__":
    user_input = input("Enter MD5 hash: ")
    print(crack_hash(user_input))
