import pyperclip
# Take contents of clipboard, add whitespace to avoid cutter issues
# Replace the ZPL control characters with benign characters
art = "\n\n"+pyperclip.paste().replace('^','*').replace('~','-')+"\n\n"

size = 1

art = art.split('\n')
# Initialize program lines with settings setup
program_lines = ['^XA^MMC^LL'+ str(len(art)*size*20) +',y']

# Create standard lines of code for the script
for i,line in enumerate(art):
    # Program one line of the ascii art
	program_lines.append("^FO20," + str(i*size*20) + "^ADN,"+str(size*18)+","+str(size*10)+"^FD "+line+"^FS\n\n")

program = ''.join(program_lines)+"^XZ"

print(program, file=open("zpl_art.zpl", "w+"))
