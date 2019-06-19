# zebra_printing
Code for printing to Zebra printers using Python and Powershell

`online_printers.ps1` finds all online printers connected via USB.
`Python_Zebra_print.py` sends the contents of a document to the printer as raw_bytes.

`ZPL_art_writer.py` takes what's in your clipboard (requires `pyperclip`) and writes ZPL program to send to the printer under `zpl_art.zpl`.
