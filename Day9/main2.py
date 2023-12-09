def predict(sequence):
    if sequence.count(0) == len(sequence):
        return 0
    return sequence[0] - predict([sequence[i]-sequence[i-1] for i in range(1,len(sequence))])

sequences = [[int(num) for num in line.split()] for line in open('input.txt').readlines()]

ans = sum([predict(sequence) for sequence in sequences])
print(ans)