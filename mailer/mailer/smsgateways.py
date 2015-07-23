from collections import namedtuple

SMSGateway = namedtuple('SMSGateway', ['carrier', 'sms', 'mms'])

us_gateways = {gw.carrier: gw for gw in [
    SMSGateway('Alltell', 'message.alltell.com', None),
    SMSGateway('AT&T', 'txt.att.net', 'mms.att.net'),
    SMSGateway('Boost Mobile', 'myboostmobile.com', None),
    SMSGateway('Nextel', 'messaging.nextel.com', None),
    SMSGateway('Sprint', 'messaging.sprintpcs.com', 'pm.sprint.com'),
    SMSGateway('T-Mobile', 'tmomail.net', None),
    SMSGateway('US Cellular', 'email.uscc.net', 'mms.uscc.net'),
    SMSGateway('Verizon', 'vtext.com', 'vzwpix.com'),
    SMSGateway('Virgin', 'vmobl.com', None)
]}

ALLTELL = us_gateways['Alltell']
ATT = us_gateways['AT&T']
BOOST_MOBILE = us_gateways['Boost Mobile']
NEXTEL = us_gateways['Nextel']
SPRINT = us_gateways['Sprint']
T_MOBILE = us_gateways['T-Mobile']
US_CELLULAR = us_gateways['US Cellular']
VERIZON = us_gateways['Verizon']
VIRGIN = us_gateways['Virgin']
