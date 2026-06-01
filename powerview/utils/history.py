from sys import platform

if platform == "linux" or platform == "linux2":
    import gnureadline as readline
else:
    try:
        import pyreadline3 as readline
    except ImportError:
        import readline  # fallback for macOS which has it built-in


def get_shell_history(last, unique):
    '''return the last x number of {,unique} shell history'''
    hist_len = readline.get_current_history_length() - 1
    if last > hist_len:
        last = hist_len
    returnable_hist_items = []
    cursor = hist_len
    while (not len(returnable_hist_items) == last) and (not cursor == 1):
        analyze_this = readline.get_history_item(cursor)
        if unique:
            if analyze_this not in returnable_hist_items:
                returnable_hist_items.append(analyze_this)
        else:
            returnable_hist_items.append(analyze_this)
        cursor -= 1
    return returnable_hist_items
