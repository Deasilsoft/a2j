def is_record(path: str) -> bool:
    return path.find("..") == -1


def record(path: str) -> str:
    return "records/" + path
