import hashlib
import ssdeep
import sys
import tlsh

def md5(file, block_size=2**20):
    f = open(file, 'rb')
    md5 = hashlib.md5()
    while True:
        data = f.read(block_size)
        if not data:
            break
        md5.update(data)
    return md5.hexdigest()

def sha1(file):
    f = open(file, 'rb')
    return hashlib.sha1(f.read()).hexdigest()

def sha224(file):
    f = open(file, 'rb')
    return hashlib.sha224(f.read()).hexdigest()

def sha256(file):
    f = open(file, 'rb')
    return hashlib.sha256(f.read()).hexdigest()

def sha384(file):
    f = open(file, 'rb')
    return hashlib.sha384(f.read()).hexdigest()

def sha512(file):
    f = open(file, 'rb')
    return hashlib.sha512(f.read()).hexdigest()

def hash_ssdeep(file):
    f = open(file, 'rb')
    return ssdeep.hash(f.read())

def hash_tlsh(file):
    f = open(file, 'rb')
    h = tlsh.hash(f.read())
    return h

file = sys.argv[1]

print "MD5:\t" + md5(file)
print "SHA1:\t" + sha1(file)
print "SHA224:\t" + sha224(file)
print "SHA256:\t" + sha256(file)
print "SHA384:\t" + sha384(file)
print "SHA512:\t" + sha512(file)
print "SSDEEP:\t" + hash_ssdeep(file)
print "TLSH:\t" + hash_tlsh(file)
