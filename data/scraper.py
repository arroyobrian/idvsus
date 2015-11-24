import requests
from pyquery import PyQuery as pq
from time import sleep
from subprocess import call

baseUrl = 'http://www.supremecourt.gov/oral_arguments/argument_transcript/'

# getting all of the case
caseUrlDict = {}

for year in xrange(2000, 2016):
    urlRequest = baseUrl + str(year)
    page = requests.get(urlRequest)
    txt = pq(page.text)
    dataRows = pq(txt('.datatables tr a')[1:])
    for case in dataRows:
        caseUrl = pq(case).attr('href')
        caseID = pq(case).text()
        caseUrlDict[caseID] = caseUrl
    sleep(1)

baseCommand = "wget -nv "

for case, url in caseUrlDict.viewitems():
    print "Moving on..."
    command = baseCommand + baseUrl + url
    call(command.split(' '))
    sleep(1)


