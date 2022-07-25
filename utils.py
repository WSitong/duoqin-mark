import time


def format_time(time_token: float) -> str:
    t = time.localtime(time_token)
    return time.strftime('%Y-%m-%d', t)


def format_size(size: int) -> str:
    units = ('B', 'KB', 'MB', 'GB', 'TB')
    i = 0
    while size > 999:
        size /= 1024
        i += 1
        if i == (len(units) - 1):
            break
    return f'{round(size, 2)}{units[i]}'
