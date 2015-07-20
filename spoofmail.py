import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-x', '--smtp_server')
    parser.add_argument('-p', '--smtp_port', default=25)
    parser.add_argument('-h', '--local_hostname')
    parser.add_argument('-t', '--recipient')
    parser.add_argument('-f', '--sender')
    parser.add_argument('-s', '--subject')
    parser.add_argument('message')
    args = parser.parse_args()
    msg_text = ''
    with open(args.message, 'r') as f:
        msg_text += f.read()
    msg = MIMEMultipart('alternative')
    msg['Subject'] = args.subject
    msg['From'] = args.sender
    msg['To'] = args.recipient
    msg.attach(MIMEText(msg_text, 'html'))

    client = smtplib.SMTP(args.smtp_server,
                          args.smtp_port,
                          args.local_hostname)
    print(str(client.ehlo_or_helo_if_needed()))
    print(msg)
    print(str(client.sendmail(args.sender, args.recipient, msg.as_string())))
    print(str(client.quit()))


if __name__ == '__main__':
    main()
