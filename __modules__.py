def data_is_not_empty(data):
    if data.get('query', {}) != {}:
        return True
    else:
        return False