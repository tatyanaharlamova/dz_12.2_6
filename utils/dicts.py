def get_val(collection, key, default='git'):
    if collection == {}:
        return default
    else:
        for k in collection.keys():
            if k == key:
                return collection[k]
            else:
                return default


