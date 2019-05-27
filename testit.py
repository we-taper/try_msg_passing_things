import namedtupled

if __name__ == '__main__':
    data = {'binks': {'says': 'meow'}}
    cat = namedtupled.map(data)
    print(cat.binks)