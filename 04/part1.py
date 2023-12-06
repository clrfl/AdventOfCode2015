import hashlib

inpt = "ckczppom"
val = 0
while True:
    result = hashlib.md5((inpt + str(val)).encode())
    if str(result.hexdigest())[:5] == "00000":
        print(val)
        break
    val += 1
