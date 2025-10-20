from sys import argv
import os

def file_stats(filename, index):
    line_count = 0
    total_words = 0
    with open(filename, 'rt') as input_file:
            for line in input_file.readlines():
                line_count += 1
                total_words += len(line.split())

            word_average = total_words / line_count if line_count != 0 else 0.0

    print("\tfile name:", filename)
    print("\tQnt of lines:", line_count)
    print("\tTotal words: ", total_words)
    print("\tAverage words per line: ", word_average)

    if index == 1:
         with open("summary.txt", "w"):
              pass
         
    with open("summary.txt", "at") as output_file:
         output_file.write(f"""file number: {index}
\tfile name: {filename}
\tQnt of lines: {line_count}
\tTotal words: {total_words}
\tAverage words per line: {word_average}
========================================\n""")


argc = len(argv)
if argc < 2:
    print(f'usage: {argv[0]} <files>...')
    exit(-1)

for index, filename in enumerate(argv[1:]):
     file_stats(filename, index + 1)




