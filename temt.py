import hashlib
h = hashlib.new("sha256")
h.update(b"123")
print(h.hexdigest())
