DTMF Echo Service
==================================

This is a [twilio](http://www.twilio.com) app that I put together to help troubleshoot a DTMF issue
from a phone system.

It's purpose is to echo back the number keys that you entered when prompted.  This can assist you in determining
if your land line/cellphone/VOIP phone is sending the signals that you think it is/should.

Requirements
------------
    $ pip install flask
    $ pip install lxml

Overview
--------
  1.  Setup a twilio account
  2.  Deploy this app to http://dtmf.example.com/
  3.  Buy a number on twilio
  4.  Add an app tied to the number you just bought
  5.  Point the app "Request URL" to http://dtmf.example.com/answer
  6.  Call your number, follow the prompts.
