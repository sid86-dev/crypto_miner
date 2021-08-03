import hashlib


has = hashlib.sha256("Sid".encode()).hexdigest()

# print(has)

NONCE_LIMIT = 1000000

zeroes = 4

def mine(block_number, transactions, previous_hash):
    for nonce in range(NONCE_LIMIT):
        base_text = str(block_number) + transactions + previous_hash + str(nonce)
        hash_try = hashlib.sha256(base_text.encode()).hexdigest()
        if hash_try.startswith('0' * zeroes):
            print(f"Found Hash with Nonce: {nonce}")
            return hash_try
        # else:
        #     print("Hash not found")
    return -1

block_number = 24
transactions = "7509ff08880"
previous_hash = "462c090282bf97e6371c5803ebfb872002f7f19440e00b8dfc8b14959e132ee8"

combined_text = str(block_number) + transactions + previous_hash + str(138304)
# print(hashlib.sha256(combined_text.encode()).hexdigest())

mine(block_number, transactions, previous_hash)