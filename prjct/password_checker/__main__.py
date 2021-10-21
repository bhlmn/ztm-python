import requests
import hashlib
import sys


def request_api_data(query_char):
    url = f'https://api.pwnedpasswords.com/range/{query_char}'
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the API and try again.')
    return res


def read_response(res):
    print(res.text)


def get_password_leak_counts(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return '0'


def pwned_api_check(pswd):
    sha1_pswd = hashlib.sha1(pswd.encode('utf-8')).hexdigest().upper()
    head, tail = sha1_pswd[:5], sha1_pswd[5:]
    res = request_api_data(head)
    count = get_password_leak_counts(res.text, tail)
    if count == '0':
        return(f'Congrats! Password "{pswd}" has not been hacked.')
    else:
        return(f'Uh oh! Password "{pswd}" has been hacked {count} times.')


def main(args):
    for password in args:
        print(pwned_api_check(password))


if __name__ == '__main__':
    main(sys.argv[1:])