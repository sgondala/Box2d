#! /usr/bin/env python3.3
try:
    filename = "../doc/cs296_report_06.tex"
    inFile = open(filename)
except OSError:
    print("Report not found")
else:
    def WriteHeading(heading, no, outFile):
        outFile.write("<h" + str(no) + " style=\"font-family: sans-serif, monospace; font-weight:Bold;\">")
        outFile.write(Heading)
        outFile.write("</h" + str(no) + ">\n")
    def addImage(no, outFile):
        if '1' in no or '2' in no or '3' in no or '4' in no or '5' in no:
            no = no.replace('k','m')
        outFile.write("<img src=\""+ str(no) + "\" alt=\"plot" + str(no) + "\" height=\"50%\" width=\"52%\">\n")
    subsection = "\subsection{"
    section = "\section{"
    incG = "\includegraphics"
    Heading = ""
    outFile = open("../doc/g06_report.html", "w")
    Start = "<!DOCTYPE html PUBLIC \"-//W3C//DTD HTML 4.01 Transitional//EN\"\n\"http://www.w3.org/TR/html4/loose.dtd\">\n<html>\n<head>\n<title>"
    outFile.write(Start)
    while True:
        l = inFile.readline()
        lLow = l.lower()
        if '\\title' == l[0:6]:
            title = l[l.find("{") + 1:l.find("}")].replace('\\\\','<br>')
            outFile.write(title)
            break
    while True:
        l = inFile.readline()
        lLow = l.lower()
        if "pagebreak" in lLow:
            break
    outFile.write("</title>\n<style type=\"text/css\">\nbody {margin-left: 10%; margin-right: 10%; color: black; background: white; font-family: monospace;} \n </style>\n</head>\n<body>\n")
    WriteHeading(Heading, 1, outFile)
    outFile.write("<br><br>\n")
    flag = False
    while True:
        l = inFile.readline()
        lLow = l.lower()
        if "bibliographystyle" in lLow:
            break
        if subsection in lLow:
            if flag:
                outFile.write("</p>\n")
            sInd = lLow.find(subsection) + 12
            eInd = lLow.find("}")
            Heading = l[sInd:eInd]
            WriteHeading(Heading, 2, outFile)
            outFile.write("<p>")
            flag = True
        elif section in lLow:
            if flag:
                outFile.write("</p>\n")
            sInd = lLow.find(section) + 9
            eInd = lLow.find("}")
            Heading = l[sInd:eInd]
            WriteHeading(Heading, 2, outFile)
            outFile.write("<p>")
            flag = True
        elif incG in l:
            sInd = lLow.find("{") + 1
            eInd = lLow.find("}")
            imgF = l[sInd:eInd]
            addImage(imgF, outFile)
        else:
            if "\\\\" in lLow:
                l = l.replace("\\\\","<br>").replace("\\cite{","").replace("}","")
                lLow = l.lower()
            outFile.write(l)
    outFile.write("</body>\n")
