import hashlib

def hash(text):
  has = hashlib.sha256(text.encode()).hexdigest()
  return has

hash("Sid")
