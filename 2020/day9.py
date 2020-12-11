if __name__ == "__main__":
    with open('inputs/day9.txt') as f:
        inputs = []
        data = []
        invalid = []
        for count, line in enumerate(f):
            v = False
            num = int(line.strip())
            inputs.append(num)
            if count < 25:
                data.append(num)
                v = True
            else:
                for i in range(0, len(data)):
                    break_outer = False
                    for j in range(0, len(data)):
                        if i == j or data[i] == data[j]:
                            continue
                        if (data[i] + data[j]) == num:
                            v = True
                            break_outer = True
                    if break_outer:
                        break
                data.append(num)
                data.pop(0)
            if not v:
                invalid.append(num)
        print(invalid)
        result = None
        for i in range(len(inputs)):
            break_outer = False
            sum = inputs[i]
            for j in range(i+1, len(inputs)):
                sum += inputs[j]
                if sum == 29221323:
                    result = inputs[i:j]
                    break_outer = True
                    break
            if break_outer:
                break
        result.sort()
        print(result[0] + result[-1])


