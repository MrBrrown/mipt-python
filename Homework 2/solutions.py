
def solution1():
    with open("data/source.txt", 'r') as source, open("destination.txt", "w+") as dist:
        dist.writelines(source.readlines())
    print("Done!")

def solution2():
    with open("data/prices.txt", 'r') as prices:
        sum = 0
        for line in prices:
            tmp = line.split('\t')
            sum += int(tmp[2]) * int(tmp[1])
    print("Sum is: ", sum)


def solution3():
    words_count = 0
    with open("data/text_file.txt", 'r') as text_file:
        for line in text_file:
            line = line.replace('—', '')
            words_count += len(line.split())
    print("Words count: ", words_count)


def solution4():
    with open("data/input.txt", 'r') as file, open("unique_output.txt", "w+") as dist:
        unique_lines = set()
        for line in file:
            line = line.replace('. ', '.')
            unique_lines.update(set(line.split(".")))

        for line in unique_lines:
            line += '\n'
            dist.writelines(line)

    print("Done!")