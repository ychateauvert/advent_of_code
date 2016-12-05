#!/usr/bin/env python

import hashlib

def find_password(door_id, part_2=False):
    index = 0
    door_id.encode('utf-8')
    password = []
    if part_2:
        password = dict()
    while True:
        to_be_hashed = "".join([door_id, str(index)]).encode('utf-8')
        password_hash = hashlib.md5(to_be_hashed).hexdigest()
        if password_hash[:5] == '00000':
            print('Found hash: %s' % password_hash)
            if part_2:
                pos, char = password_hash[5:7]
                if pos in map(str, range(0, 8)) and pos not in password:
                    password[pos] = char
                    print("[%s] Position %s, Char: %s" % (password_hash, pos, char))

                    if len(password) == 8:
                        print(password)
                        return "".join([password[str(x)] for x in range(0, 8)])

            else:
                password.append(password_hash[5])

                if len(password) == 8:
                    return "".join(password)
        index = index + 1



def main():
    seed = 'cxdnnyjw'
    print("Password for door %s is %s" % (seed, find_password(seed, True)))


if __name__ == '__main__':
    main()
