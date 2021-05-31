import requests
import hashlib
import datetime


def logger(path):
    def inner(func):
        def wrapped(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(path, 'a', encoding='utf-8') as f:
                time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                line = [time, func.__name__, args, kwargs, result]
                f.write(str(line) + '\n')
            return result
        return wrapped
    return inner


@logger('logs.txt')
def plus(a, b):
    return a + b


@logger('logs.txt')
def get_page(link):
    response = requests.get(link)
    return response.status_code


@logger('logs.txt')
def hash_this(string):
    return hashlib.md5(string.encode('utf-8')).hexdigest()


def main():
    print(plus(4, 5))
    print(get_page('https://google.com'))
    print(hash_this('pls hash this string'))


if __name__ == '__main__':
    main()
