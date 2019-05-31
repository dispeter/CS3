import hashlib

hashed = []

with open('hashed.txt') as f:
    hashed_list = [line.strip() for line in f.readlines()]


with open('pwlist.txt') as f:
    pwds = [pwd.strip() for pwd in f.readlines()]
    for p in pwds:
        hashed_password = hashlib.md5(p.encode('utf-8')).hexdigest()
        if hashed_password in hashed_list:
            print('Found: ', p, 'as', hashed_password)