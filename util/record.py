def is_record(path):
    return str.find(path, "..") == -1


def record(path):
    return "recs/" + path
