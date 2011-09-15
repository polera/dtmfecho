__author__ = 'James Polera'
__email__  = 'james@uncryptic.com'
__since__  = '2011-09-14'


from lxml import etree

class Receiver(object):

    def prepare(self):
        greeting = ["Hello, welcome to the DTMF echo service.",
                    "Brought to you by Uncryptic Communications.",
                    "Get in touch at http://www.uncryptic.com."]
        for sentence in greeting:
            say = etree.SubElement(self.root, "Say")
            say.text = sentence

    def __init__(self):
        self.root = etree.Element("Response")
        self.prepare()

    def pickup(self, handler, method):
        gatherer = etree.SubElement(self.root,"Gather",action=handler,method=method)
        say      = etree.SubElement(gatherer,"Say")
        say.text = "Enter some digits that you would like to be echoed, then press pound."
        return etree.tostring(self.root, xml_declaration=True, encoding='UTF-8')