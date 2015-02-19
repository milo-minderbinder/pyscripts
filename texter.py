import smtplib


class Texter(object):

    def __init__(self, host, port, username, password):
        self._host = host
        self._port = port
        self._username = username
        self._password = password

    def send_text(self, recipients, msg_body):
        msg_content = ('from: %s\r\n'
                       'to: %s\r\n'
                       'mime-version: 1.0\r\n'
                       'content-type: text/html\r\n'
                       '\r\n%s'
                       % (self._username, ', '.join(recipients), msg_body))
        server = smtplib.SMTP(self._host, self._port)
        server.ehlo()
        server.starttls()
        server.login(self._username, self._password)
        server.sendmail(self._username, recipients, msg_content)
        server.close()
