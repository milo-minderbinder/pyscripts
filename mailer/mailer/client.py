import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)


class Mailer(object):
    def __init__(self, sender, host, port=25, password=None,
                 use_tls=True, local_hostname=None):
        """ A Mailer instance wraps smtplib functions and allows clients to
        define common SMTP connection parameters, including sender email
        address, SMTP host and port, authentication details, and channel
        security.


        :param sender: sender's email address (e.g. foo@bar.com)
        :param host: FQDN of SMTP host
        :param port: SMTP port (default is standard SMTP port 25)
        :param password: if specified, SMTP client will login to SMTP host at
        connect
        :param use_tls: use secure TLS channel for communication (default is
        True)
        :param local_hostname: FQDN of host to identify client as to SMTP host
        (default is FQDN of local host)
        """
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
        """ Send message to recipients as plaintext.


        :param recipients: list of recipient email addresses
        :param body: message body text
        :param subject: subject line of email (default is no subject line)
        """
        msg = MIMEText(body)
        if subject:
            msg['Subject'] = subject
        msg['From'] = self._sender
        msg['To'] = ', '.join(recipients)
        log.debug('Sending text message to recipients: %s' % str(recipients))
        self._send(msg, recipients)

    def send_mail(self, recipients, body, subject=None):
        """ Send message to recipients as multipart/alternative media, with both
        HTML and plaintext attachments of the message.


        :param recipients: list of recipient email addresses
        :param body: message body text
        :param subject: subject line of email (default is no subject line)
        """
        msg = MIMEMultipart('alternative')
        if subject:
            msg['Subject'] = subject
        msg['From'] = self._sender
        msg['To'] = ', '.join(recipients)
        msg.attach(MIMEText(body, 'html'))
        msg.attach(MIMEText(body, 'plain'))
        log.debug('Sending email message to recipients: %s' % str(recipients))
        self._send(msg, recipients)
