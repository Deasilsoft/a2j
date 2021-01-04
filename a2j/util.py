def is_record(path):
    return str.find(path, "..") == -1


def get_record(path):
    return "recs/" + path
