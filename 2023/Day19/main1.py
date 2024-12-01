def decide(part, workflow='in'):
    for rule in workflows[workflow]:
        if (part[rule[0]]-rule[2])*rule[1] > 0:
            if rule[3] in 'AR':
                return rule[3]
            return decide(part, rule[3])

workflows, parts = [line.split() for line in open('input.txt').read().split('\n\n')]

for workflow_ind, workflow in enumerate(workflows):
    open_bracket = workflow.find('{')
    rules = workflow[open_bracket+1:-1].split(',')
    for rule_ind, rule in enumerate(rules[:-1]):
        colon = rule.find(':')
        rules[rule_ind] = ['xmas'.find(rule[0]), [1,-1][rule[1]=='<'], int(rule[2:colon]), rule[colon+1:]]
    rules[-1] = [0, 1, -1, rules[-1]]
    workflows[workflow_ind] = [workflow[:open_bracket], rules]

workflows = dict(workflows)
parts = [[int(category[2:]) for category in part[1:-1].split(',')] for part in parts]

ans = 0
for part in parts:
    if decide(part) == 'A':
        ans += sum(part)

print(ans)