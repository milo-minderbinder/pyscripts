import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging
logging.basicConfig(level=logging.DEBUG)


log = logging.getLogger(__name__)


class Mailer(object):

    def __init__(self, sender, host, port=25, password=None,
                 use_tls=True, local_hostname=None):
        self._sender = sender
        self._host = host
        self._port = port
        self._password = password
        self._use_tls = use_tls
        self._local_hostname = local_hostname
        log.debug('Instantiated new Mailer')

    def _send(self, msg, recipients):
        smtp = smtplib.SMTP(self._host, self._port,
                            local_hostname=self._local_hostname)
        try:
            smtp.ehlo_or_helo_if_needed()
            if self._use_tls:
                smtp.starttls()
                smtp.ehlo()
            if self._password is not None:
                smtp.login(self._sender, self._password)
            smtp.sendmail(self._sender, recipients, msg.as_string())
        except Exception as e:
            log.error('Failed to send message: %s' % str(e))
        finally:
            smtp.quit()

    def send_text(self, recipients, body, subject=None):
        msg = MIMEText(body)
        if subject:
            msg['Subject'] = subject
        msg['From'] = self._sender
        msg['To'] = ', '.join(recipients)
        log.debug('Sending text message to recipients: %s' % str(recipients))
        self._send(msg, recipients)

    def send_mail(self, recipients, body, subject=None):
        msg = MIMEMultipart('alternative')
        if subject:
            msg['Subject'] = subject
        msg['From'] = self._sender
        msg['To'] = ', '.join(recipients)
        msg.attach(MIMEText(body, 'html'))
        msg.attach(MIMEText(body, 'plain'))
        log.debug('Sending email message to recipients: %s' % str(recipients))
        self._send(msg, recipients)
