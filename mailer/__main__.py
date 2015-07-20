import argparse
from .client import Mailer


parser = argparse.ArgumentParser()
parser.add_argument('-S', '--server',
                    help='SMTP server hostname',
                    default='smtp.gmail.com')
parser.add_argument('-P', '--port',
                    type=int,
                    help='SMTP port',
                    default=587)
parser.add_argument('-e', '--email',
                    required=True,
                    help='Sender email', )
parser.add_argument('-p', '--password',
                    required=True,
                    help='Sender email password')
parser.add_argument('-r', '--recipients',
                    required=True,
                    help='Comma separated list of recipients')
parser.add_argument('message', help='Email message body')
args = parser.parse_args()

client = Mailer(args.username, args.smtp_host, args.smtp_port, args.password)
client.send_text(args.recipients.split(','), args.message)