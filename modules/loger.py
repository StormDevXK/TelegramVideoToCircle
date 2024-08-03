import time


def log_bot(chat_id: int, username: str, func: str, message: str = None):
    current_time = time.time()
    local_time = time.localtime(current_time)
    formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(f'{formatted_time} | id{chat_id} @{username} | {func} | {message}\n')
