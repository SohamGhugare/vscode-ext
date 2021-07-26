# IPC Commands are in the following format
# {2digitcode}: {arg1}|||{arg2}|||{argn}

import json


def show_quick_pick(data, options):
    data = json.dumps(data)
    options = json.dumps(options)
    print(f"QP: {data}|||{options}")
    res = input()
    return json.loads(res)


def _base(func, text, *args):
    print(
        f"SM: {func}|||{text}" + "|||" * bool(args) + "|||".join(args),
        flush=True,
        end="",
    )
    res = input()
    return res


def show_info_message(text, *args):
    return _base("showInformationMessage", text, *args)


def show_warn_message(text, *args):
    return _base("showWarningMessage", text, *args)


def show_error_message(text, *args):
    return _base("showErrorMessage", text, *args)
