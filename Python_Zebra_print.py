# Created by Ada

import win32print
from subprocess import Popen, PIPE

def get_online_printer():
    # Calls Powershell script to grab all online printers from Win32_Printer
    process = Popen(['Powershell', '. "./online_printers";', '&getOnlinePrinters($_)'],
        stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    # stdout returns as byte-object. Strip trailing newline and decode it to utf8
    return stdout.strip().decode("utf-8")

def send_document(filename):
    # Try to get printer. If it fails, print out exact error.
    try:
        p = win32print.OpenPrinter(get_online_printer())
        try:
            #open printer, print, close out printer 
            win32print.StartDocPrinter(p, 1,("Printer Test", None, "RAW"))
            win32print.StartPagePrinter(p)
            win32print.WritePrinter(p, filename)
            win32print.EndPagePrinter(p)
        except Exception as e:
            print("Print Error: ", e)
        win32print.ClosePrinter(p)
    except Exception as e:
        print("Could not find printer: ", e)
        
with open("PrinterTestFile.zpl") as filename:
    send_document(bytes(filename.read(), "utf-8"))
