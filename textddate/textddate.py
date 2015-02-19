#!/usr/bin/python
import os
import os.path
import subprocess
import ConfigParser
import texter


CONFIG_FILE = os.path.join(os.path.dirname(__file__), 'textddate.conf')
config = ConfigParser.RawConfigParser()
config.read(CONFIG_FILE)


def main():
    # Call ddate to generate message text
    ddate_format_str = config.get('Message', 'ddate_format_string')
    msg_text = subprocess.check_output(['ddate', ddate_format_str])

    # Use Jasypt to decrypt email account password
    jasypt_path = os.path.realpath(config.get('Jasypt', 'install_path'))
    jasypt_pass = os.environ[config.get('Jasypt', 'passwd_env_var')]
    enc_password = config.get('Email', 'encrypted_password')
    password = (subprocess.check_output([
        os.path.join(jasypt_path, 'bin', 'decrypt.sh'),
        'input=%s' % enc_password,
        'password=%s' % jasypt_pass,
        'verbose=false'])).strip()
    username = config.get('Email', 'username')
    recipients = config.get('Message', 'recipients').split(';')

    # Authenticate to the SMTP server and send the message!
    host = config.get('Email', 'smtp_host')
    port = config.get('Email', 'smtp_port')
    t = texter.Texter(host, port, username, password)
    print 'Sending text to %s from %s:\n%s' % (recipients, username, msg_text)
    t.send_text(recipients, msg_text)


if __name__ == '__main__':
    main()
