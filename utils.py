import time


def format_time(time_token: float) -> str:
    t = time.localtime(time_token)
    return time.strftime('%Y-%m-%d', t)
