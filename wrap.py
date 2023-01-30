import platform
import re
import time
from textwrap import dedent
from textwrap import wrap

import keyboard
import pyperclip


def wrap_on_ctrl_c() -> None:
    """Wraps text when it enters the device's clipboard."""
    if platform.system() == "Darwin":  # macOS
        kb_shortcut = "cmd+c"
    else:
        kb_shortcut = "ctrl+c"
    print(f"Copy (with {kb_shortcut}) and paste to wrap text.")
    try:
        while True:
            keyboard.wait(kb_shortcut)
            time.sleep(0.05)  # Wait for the clipboard to be updated.
            pyperclip.copy(wrap_(pyperclip.paste()))
    except KeyboardInterrupt:
        print("Exiting.")


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
    text_ = text_.replace("\r\n", "\n")
    first_line = text_.split("\n")[0]
    indent_n = len(first_line) - len(first_line.lstrip())
    indent = " " * indent_n
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
    wrap_on_ctrl_c()