def text_to_csv(path_to_text_file, separator):
    with open(path_to_text_file, 'r') as txt_file, open('my.csv', 'w') as csv_file:
        for line in txt_file:
            csv_file.write(line.replace(separator, '; '))


if __name__ == '__main__':
    text_to_csv('/Users/evgeniy/Desktop/English__Children of the corn.txt', '\t')
