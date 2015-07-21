from collections import namedtuple

SMSGateway = namedtuple('SMSGateway', ['carrier', 'sms', 'mms'])

ALLTELL = SMSGateway('Alltell', 'message.alltell.com', None)
ATT = SMSGateway('AT&T', 'txt.att.net', 'mms.att.net')
BOOST = SMSGateway('Boost Mobile', 'myboostmobile.com', None)
NEXTEL = SMSGateway('Nextel', 'messaging.nextel.com', None)
SPRINT = SMSGateway('Sprint', 'messaging.sprintpcs.com', 'pm.sprint.com')
TMOBILE = SMSGateway('T-Mobile', 'tmomail.net', None)
US_CELLULAR = SMSGateway('US Cellular', 'email.uscc.net', 'mms.uscc.net')
VERIZON = SMSGateway('Verizon', 'vtext.com', 'vzwpix.com')
VIRGIN = SMSGateway('Virgin', 'vmobl.com', None)
