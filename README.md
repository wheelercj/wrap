# wrap

Quickly wrap text in **any** text editor.

![wrap demo](https://media.giphy.com/media/JBremwdj3OuFLhTsOr/giphy.gif)

## usage

1. Download wrap.py.
2. `pip install keyboard pyperclip`.
3. Run the code with `py wrap.py` or `python3 wrap.py`. This will not wrap text yet; it just adds a temporary keyboard shortcut.
4. Select text and press ctrl+' or cmd+' to wrap it!
5. Press ctrl+c or cmd+c on the script when you're done wrapping.

If you will use this often, you might want to [create a custom terminal command](https://wheelercj.github.io/notes/pages/20220320181252.html).

The default wrap width is 88 characters. You can change the wrap width by changing the `WRAP_WIDTH` variable near the top of wrap.py.

You can also change the keyboard shortcut for wrapping by changing the `WRAP_SHORTCUT` variable near the top of wrap.py.
