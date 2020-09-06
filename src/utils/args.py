# module utils

def is_arg(list_arg: [str], arg: str):
    for actual_arg in list_arg:
        if actual_arg == arg:
            return True
    return False

def get_next_arg(list_arg: [str], arg: str):
    is_next_arg = False
    for actual_arg in list_arg:
        if is_next_arg:
            return actual_arg
        if actual_arg == arg:
            is_next_arg = True
    return ""