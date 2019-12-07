from itertools import cycle

def main():
    with open('input_2.txt', 'r') as f:
        lines = f.read().splitlines()
        result = chronal_calibration(lines)
        print('Result is: {}'.format(result))

def chronal_calibration(lines):
        sum = 0
        old_sums = {sum}
        cycle_lines = cycle(lines)
        for line in cycle_lines:
                if '+' in line:
                        numeric = int(line.split('+')[1])
                        sum += numeric
                elif '-' in line:
                        numeric = int(line.split('-')[1])
                        sum -= numeric
                
                if sum in old_sums:
                        return sum
                else:
                        old_sums.add(sum)

if __name__ == '__main__':
    main()