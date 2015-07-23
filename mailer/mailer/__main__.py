#!/usr/bin/env python

import argparse
from .client import Mailer
from smsgateways import us_gateways


def main():
    parser = argparse.ArgumentParser(description='A simple email utility')
    parser.add_argument('-S', '--server',
                        default='smtp.gmail.com',
                        help='SMTP server hostname')
    parser.add_argument('-P', '--port',
                        type=int,
                        default=587,
                        help='SMTP port')
    parser.add_argument('-i', '--insecure',
                        action='store_false',
                        default=True,
                        help='Do not use secure TLS channel to communicate',
                        dest='use_tls')
    parser.add_argument('-l', '--local-hostname',
                        help='Local hostname to identify as',
                        dest='local_hostname')
    parser.add_argument('-e', '--email',
                        required=True,
                        help='Sender email', )
    parser.add_argument('-p', '--password',
                        help='Sender email password')
    parser.add_argument('-r', '--recipients',
                        required=True,
                        help=('Comma separated list of recipients. Recipient '
                              'addresses can be in either the standard email '
                              'addresses form (e.g. "bob@example.com") or in a '
                              'special SMS address format, if sending an email '
                              'to a cell phone as an SMS (text) message. To '
                              'send an SMS message, recipient addresses should '
                              'be in the form <10_digit_cell_number>@<carrier> '
                              '(e.g. "2021234567@US Cellular"). '
                              'Accepted US Cell Carriers are: %s' %
                              str(us_gateways.keys())))
    parser.add_argument('-s', '--subject',
                        help='Subject line of email')
    parser.add_argument('message', help='Email message body')
    args = parser.parse_args()

    recipients = []
    for recipient in [r.strip() for r in args.recipients.split(',')]:
        parts = recipient.split('@')
        if parts[1] in us_gateways:
            parts[1] = us_gateways[parts[1]].sms
        recipients.append('@'.join(parts))
    client = Mailer(args.email, args.server,
                    port=args.port,
                    password=args.password,
                    use_tls=args.use_tls,
                    local_hostname=args.local_hostname)
    client.send_text(recipients, args.message, subject=args.subject)


if __name__ == '__main__':
    main()
