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

def get_next_args(list_arg: [str], arg: str):
    next_args = []
    is_next_arg = False

    for actual_arg in list_arg:
        if is_next_arg and actual_arg[0] == '-':
            return next_args
        elif is_next_arg:
            next_args.append(actual_arg)
        if actual_arg == arg:
            is_next_arg = True
    return next_args