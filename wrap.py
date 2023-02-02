import platform
import re
import time
from textwrap import dedent
from textwrap import wrap

import keyboard
import pyperclip


WRAP_WIDTH = 88
if platform.system() == "Darwin":  # macOS
    WRAP_SHORTCUT = "cmd+'"
else:
    WRAP_SHORTCUT = "ctrl+'"


def wrap_on_keyboard_shortcut() -> None:
    """Wraps text when the user presses the keyboard shortcut."""
    print(f"Press {WRAP_SHORTCUT} to wrap text.")
    if platform.system() == "Darwin":  # macOS
        CTRL_KEY = "cmd"
    else:
        CTRL_KEY = "ctrl"
    try:
        while True:
            keyboard.wait(WRAP_SHORTCUT)
            keyboard.send(f"{CTRL_KEY}+c")
            time.sleep(0.05)  # Wait for the clipboard to be updated.
            text = pyperclip.paste()
            wrapped_text = wrap_(text, width=WRAP_WIDTH)
            pyperclip.copy(wrapped_text)
            keyboard.send(f"{CTRL_KEY}+v")
    except KeyboardInterrupt:
        print("Exiting.")


def wrap_(
    text: str | None = None,
    width: int = 88,
    keep_indentation: bool = True,
) -> str | None:
    """Wraps text to a chosen width.

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
    indent = " " * indent_n if keep_indentation else ""
    width -= 0 if keep_indentation else indent_n
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
    wrap_on_keyboard_shortcut()
