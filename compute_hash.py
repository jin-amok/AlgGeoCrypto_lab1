import hashlib
import struct

def compute_sha256_u32(preimage_u32):
    preimage_bytes = b''.join(struct.pack('>I', x) for x in preimage_u32)
    digest = hashlib.sha256(preimage_bytes).digest()
    return list(struct.unpack('>8I', digest))

preimage = [0, 0, 0, 0, 0, 0, 0, 1]
hash_result = compute_sha256_u32(preimage)

print("Preimage:", preimage)
print("Hash:    ", hash_result)
print("\nКоманда для ZoKrates:")
print("zokrates compute-witness -a", " ".join(str(x) for x in preimage), " ".join(str(x) for x in hash_result))
