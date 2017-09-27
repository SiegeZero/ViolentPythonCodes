import re
import optparse
from scapy.all import *
def findCreditCard(raw):
    RE = re.findall("3[47][0-9]{13}", raw)
    if RE:
        print "Found Credit Card Number:" + RE[0]
def findSchoolNumber(raw):
    RE = re.findall("3201[345]0[0-9]{6}", raw)
    if RE:
        print "Found School Number:" + RE[0]
def main():
    tests = []
    tests.append('I would like to buy 1337 copies of that dvd')
    tests.append('Bill my card: 378282246310005 for \$2600')
    for test in tests:
        findCreditCard(test)

def main2():
    raw = pkt.sprintf("%Raw.load%")
    findSchoolNumber( raw)
if __name__ == '__main__':
    main()
