Function getOnlinePrinters($_)
{
    # Create empty array to add printer names
    $printer_names = @()
    # Use WQL to filter out printers that are online now
    $printers_online_raw = Get-WmiObject -query "SELECT Name FROM Win32_Printer WHERE (PortName LIKE 'USB%') AND (WorkOffline = False)" 
    foreach ($printer in $printers_online_raw) {
        $printer_names += $printer.Name
    }
    return $printer_names
}
