import re
from textwrap import dedent
from textwrap import wrap

import pyperclip  # https://pypi.org/project/pyperclip/


def wrap_(text: str | None = None, width: int = 88) -> str | None:
    """Wraps text while preserving indentation.

    If text is None, the text in the device's clipboard is wrapped. If text is not None,
    the clipboard is not modified and the wrapped text is returned.
    """
    if text is None:
        text_ = pyperclip.paste()
    else:
        text_ = text
    if not text_:
        raise ValueError("Nothing to wrap.")
    first_line = text_.split("\n")[0]
    indent_n = len(first_line) - len(first_line.lstrip())
    indent = " " * indent_n
    if "\r\n" in text_:
        texts = text_.split("\r\n\r\n")
    else:
        texts = text_.split("\n\n")
    spaces_pattern = re.compile(r"(?<=\S)\s\s(?=\S)")
    for i, t in enumerate(texts):
        lines = wrap(
            dedent(t),
            width=width,
            tabsize=4,
            initial_indent=indent,
            subsequent_indent=indent,
        )
        texts[i] = "\n".join(lines)
        texts[i] = spaces_pattern.sub(" ", texts[i])
    if text is None:
        pyperclip.copy("\n\n".join(texts))
    else:
        return "\n\n".join(texts)


if __name__ == "__main__":
    wrap_()
