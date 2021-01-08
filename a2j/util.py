def is_record(record):
    return str(record).find("..") == -1


def record(record):
    return "records/" + str(record)
