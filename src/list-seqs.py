import argparse
import sys

parser = argparse.ArgumentParser(prog = "list-seqs")
parser.add_argument("-path", nargs = 1, type = str, help = "Path to input fastq file")

args = parser.parse_args()

fastq_file_object = open(r"{path}".format(path=args.path[0]), "r")

for i in fastq_file_object:
	if i[0] != "@":
		sys.stdout.write(i)