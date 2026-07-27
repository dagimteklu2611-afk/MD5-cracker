import hashlib

def generate_side_by_side(wordlist_path="wordlist.txt", output_path="hashes.txt"):
    try:
        with open(wordlist_path, "r", encoding="utf-8", errors="ignore") as infile, \
             open(output_path, "w", encoding="utf-8") as outfile:
            count = 0
            for line in infile:
                word = line.strip()
                if word:
                    # Calculate MD5 hash
                    md5_hash = hashlib.md5(word.encode("utf-8")).hexdigest()
                    # Write side-by-side format (hash:word)
                    outfile.write(f"{md5_hash}:{word}\n")
                    count += 1
        print(f"[+] Successfully generated {count} side-by-side pairs in '{output_path}'!")
    except FileNotFoundError:
        print(f"[-] Error: Could not find '{wordlist_path}'.")

if __name__ == "__main__":
    generate_side_by_side()
