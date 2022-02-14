

def code_block_init(*args) -> None:

    for content in args:
        print(content)


def ink(the_text: str):
    from random import choice

    box: tuple = (
        '\033[1:30m', '\033[1:31m', '\033[1:32m', '\033[1:33m', '\033[1:34m', '\033[1:35m', '\033[1:36m',
        '\033[1:37m', '\033[1:38m',
    )

    return f"{choice(box)}{the_text}{box[-1]}"
