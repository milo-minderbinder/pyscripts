import os
import os.path
import argparse


class Finding(object):

    def __init__(self, raw_data):
        raw_data = raw_data.split('\t')
        self.trace = raw_data[0]
        self.severity = raw_data[1]
        self.classification = raw_data[2]
        self.vuln_type = raw_data[3]
        self.api = raw_data[4]
        self.source = raw_data[5]
        self.sink = raw_data[6]
        self.directory = raw_data[7]
        self.filename = raw_data[8]
        self.calling_method = raw_data[9]
        self.line = raw_data[10]
        self.bundle = raw_data[11]
        self.cwe = raw_data[12].strip()

    def get_full_path(self):
        return '%s\\%s(%s)' % (self.directory, self.filename, self.line)


def parse_and_write(infile, outfile):
    findings = []
    with open(infile, 'r') as f:
        findings = [Finding(line) for line in f]
    with open(outfile, 'w') as f:
        for finding in findings:
            f.write(finding.get_full_path() + '\n')


def main():
    desc = 'A simple utility to parse pasted text from AppScan Source findings'
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('-o', '--outfile',
                        default=os.path.join(os.getcwd(),
                                             'findings_formatted.out'),
                        help='Path to the output file')
    parser.add_argument('input_file',
                        help='Path to file containing pasted AppScan text')
    args = parser.parse_args()
    outfile = os.path.realpath(args.outfile)
    infile = os.path.realpath(args.input_file)
    if not os.path.isfile(infile):
        print 'Could not find input file: %s' % infile
        return
    parse_and_write(infile, outfile)


if __name__ == '__main__':
    main()
