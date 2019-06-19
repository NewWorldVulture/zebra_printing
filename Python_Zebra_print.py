import win32print
from subprocess import Popen, PIPE

def get_online_printer():
    # Uses Powershell to grab all online printers from 
    process = Popen(['Powershell', '. "./online_printers";', '&getOnlinePrinters($_)'],
        stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    stdout = stdout.strip()
    print(stdout)
    return stdout #stdout returns as bytecode. Decode it to utf8

def send_document(filename):
    try:
        printer_choice = get_online_printer().decode("utf-8")
        p = win32print.OpenPrinter(printer_choice)
        print()
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
