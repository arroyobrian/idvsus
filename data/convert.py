import os
from PyPDF2 import PdfFileWriter, PdfFileReader
from subprocess import call

path = os.getcwd()
fileList = os.listdir(path)
fileExt = ".pdf"
pdfs = filter(lambda File: File[-4:] == fileExt, fileList)

for pdf in pdfs:
    outputFile = PdfFileWriter()
    handle = open(pdf, 'rb')
    try:
        inputFile = PdfFileReader(handle)
    except Exception:
        handle.close()
        continue

    pageNum = inputFile.getNumPages()

    for i in xrange(0, pageNum-10):
        outputFile.addPage(inputFile.getPage(i))

    outStream = file("cut_" + pdf, 'wb')
    outputFile.write(outStream)

    outStream.close()
    handle.close()

# credit to http://stackoverflow.com/questions/35817/how-to-escape-os-system-calls-in-python
def shellquote(s):
    return "'" + s.replace("'", "'\\''") + "'"


# THIS PART REQUIRES THE LINUX CMDLINE TOOL pdftotext!!!
# DNR otherwise!
baseCommand = "pdftotext"
pdfs = filter(lambda pdf : pdf[:4] == 'cut_', pdfs)
for pdf in pdfs:
    finPdf = shellquote('' + pdf)[1:-1]
    fileDest = "%s%s" % (finPdf[:-4], ".txt")
    encodeCmd = "-enc"
    codec = "Latin1"
    call([baseCommand, encodeCmd, codec, finPdf, fileDest])

