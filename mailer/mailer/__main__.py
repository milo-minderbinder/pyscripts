#!/usr/bin/env python

import argparse
from .client import Mailer


parser = argparse.ArgumentParser()
parser.add_argument('-S', '--server',
                    default='smtp.gmail.com',
                    help='SMTP server hostname')
parser.add_argument('-P', '--port',
                    type=int,
                    default=587,
                    help='SMTP port')
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

client = Mailer(args.email, args.server, args.port, args.password)
client.send_text(args.recipients.split(','), args.message)
