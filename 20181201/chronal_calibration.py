def main():
    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()
        result = chronal_calibration(lines)
        print()

def chronal_calibration(lines):
        sum = 0
        for line in lines:
                if '+' in line:
                        numeric = int(line.split('+')[1])
                        sum += numeric
                elif '-' in line:
                        numeric = int(line.split('-')[1])
                        sum -= numeric
        print('Calibrated total is {}'.format(sum))
        return sum

if __name__ == '__main__':
    main()