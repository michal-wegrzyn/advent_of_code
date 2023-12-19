def count_accepts(ranges, workflow='in'):
    ranges = [r.copy() for r in ranges]
    ans = 0
    for rule in workflows[workflow]:
        if any(r[0] > r[1] for r in ranges):
            break
        
        curr_ranges = [r.copy() for r in ranges]
        if rule[1] == '>':
            curr_ranges[rule[0]][0] = max(curr_ranges[rule[0]][0], rule[2]+1)
            ranges[rule[0]][1] = min(ranges[rule[0]][1], rule[2])
        else:
            curr_ranges[rule[0]][1] = min(curr_ranges[rule[0]][1], rule[2]-1)
            ranges[rule[0]][0] = max(ranges[rule[0]][0], rule[2])

        if any(r[0] > r[1] for r in curr_ranges):
            continue
        
        if rule[3] == 'A':
            mult = 1
            for minimum, maximum in curr_ranges:
                mult *= maximum - minimum + 1
            ans += mult
            continue
        
        if rule[3] == 'R':
            continue
        
        ans += count_accepts(curr_ranges, rule[3])
    return ans

workflows = open('input.txt').read().split('\n\n')[0].split()

for workflow_ind, workflow in enumerate(workflows):
    open_bracket = workflow.find('{')
    rules = workflow[open_bracket+1:-1].split(',')
    for rule_ind, rule in enumerate(rules[:-1]):
        colon = rule.find(':')
        rules[rule_ind] = ['xmas'.find(rule[0]), rule[1], int(rule[2:colon]), rule[colon+1:]]
    rules[-1] = [0, '>', -1, rules[-1]]
    workflows[workflow_ind] = [workflow[:open_bracket], rules]

workflows = dict(workflows)

ans = count_accepts([[1,4000]]*4)
print(ans)