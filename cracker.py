import hashlib

HASHLIST_TABLE = {
    "5f4dcc3b5aa765d61d8327deb882cf99": "password",
    "21232f297a57a5a743894a0e4a801fc3": "admin",
    "098f6bcd4621d373cade4e832627b4f6": "test",
    "e10adc3949ba59abbe56e057f20f883e": "123456"
}

def check_hash(target_hash):
    target_hash = target_hash.strip().lower()
    if target_hash in HASHLIST_TABLE:
        return f"Plain text: {HASHLIST_TABLE[target_hash]}"
    else:
        return "No matching hash identified. Please try again."

if __name == "main__":
    user_input = input("Enter MD5 hash: ")
    print(check_hash(user_input))
