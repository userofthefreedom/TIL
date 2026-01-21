T = int(input())
answer_sheet = []
for i in range(1,T+1):
    row_count = int(input())
    a = []
    for j in range(row_count):
        a.append(input().split())

    num_90 = []
    for k in range(row_count):
        line = ''
        for l in range(row_count):
            line += a[row_count-1-l][k]
        num_90.append(line)
    
    num_180 = []
    for k in range(row_count):
        line = ''
        for l in range(row_count):
            line += a[row_count-1-k][row_count-1-l]
        num_180.append(line)
    
    num_270 = []
    for k in range(row_count):
        line = ''
        for l in range(row_count):
            line += a[l][row_count-1-k]
        num_270.append(line)
    
    answer_sheet.append(f'#{i}')
    for m in range(row_count):
        answer_sheet.append(f'{num_90[m]} {num_180[m]} {num_270[m]}')
    
print('\n'.join(answer_sheet))