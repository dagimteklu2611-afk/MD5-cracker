import hashlib

def crack_hash(target_hash, wordlist_file="wordlist.txt"):
    target_hash = target_hash.strip().lower()
    try:
        with open(wordlist_file, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                word = line.strip()
                if word:
                    computed_hash = hashlib.md5(word.encode("utf-8")).hexdigest()
                    if computed_hash == target_hash:
                        return f"[+] Match found! Plaintext: {word}"
        return "[-] No matching hash found in wordlist."
    except FileNotFoundError:
        return f"[-] Error: '{wordlist_file}' file not found."

if __name__ == "__main__":
    user_input = input("Enter MD5 hash: ")
    print(crack_hash(user_input))
