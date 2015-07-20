from collections import namedtuple
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


SMSGateway = namedtuple('SMSGateway', ['carrier', 'sms', 'mms'])


ALLTELL  = SMSGateway('Alltell', 'message.alltell.com')
ATT = SMSGateway('AT&T', 'txt.att.net', 'mms.att.net')
BOOST = SMSGateway('Boost Mobile', 'myboostmobile.com',  None)
NEXTEL = SMSGateway('Nextel', 'messaging.nextel.com', None)
SPRINT = SMS('Sprint', 'messaging.sprintpcs.com', 'pm.sprint.com')
TMOBILE = SMS('T-Mobile', 'tmomail.net', None)
US_CELLULAR = SMS('US Cellular', 'email.uscc.net', 'mms.uscc.net')
VERIZON = SMS('Verizon', 'vtext.com', 'vzwpix.com')
VIRGIN = SMS('Virgin', 'vmobl.com', None)


class Mailer(object):

    def __init__(self, sender, host, port=25, password=None,
                 use_tls=True, local_hostname=None):
        self._sender = sender
        self._host = host
        self._port = port
        self._password = password
        self._use_tls = use_tls
        self._local_hostname = local_hostname

    def _send(self, msg, recipients):
        with smtplib.SMTP(self._host, self._port,
                          local_hostname=self._local_hostname) as smtp:
            smtp.ehlo_or_helo_if_needed()
            if self._use_tls:
                smtp.starttls()
                smtp.ehlo()
            if self._password is not None:
                smtp.login(self._sender, self._password)
            smtp.send_message(msg, from_addr=self._sender, to_addrs=recipients)

    def send_text(self, recipients, body, subject=None):
        msg = MIMEText(body)
        if subject:
            msg['Subject'] = subject
        msg['From'] = self._sender
        msg['To'] = ', '.join(recipients)
        self._send(msg, recipients)

    def send_mail(self, recipients, body, subject=None):
        msg = MIMEMultipart('alternative')
        if subject:
            msg['Subject'] = subject
        msg['From'] = self._sender
        msg['To'] = ', '.join(recipients)
        msg.attach(MIMEText(body, 'html'))
        msg.attach(MIMEText(body, 'plain'))
        self._send(msg, recipients)