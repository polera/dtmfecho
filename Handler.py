from lxml import etree

class Handler(object):

    def prepare(self):
        greeting = ["You entered"]
        for sentence in greeting:
            say = etree.SubElement(self.root, "Say")
            say.text = sentence

    def __init__(self, dtmf_string):
        self.root = etree.Element("Response")
        self.dtmf_string = dtmf_string
        self.prepare()

    def say_goodbye(self):
        say = etree.SubElement(self.root, "Say")
        say.text = "Goodbye"

    def read_back(self):
        print "DTMF %s" % self.dtmf_string
        for digit in self.dtmf_string:
            say = etree.SubElement(self.root, "Say")
            say.text = "%s " % str(digit)
        self.say_goodbye()
        return etree.tostring(self.root)
    