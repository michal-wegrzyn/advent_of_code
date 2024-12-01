from collections import deque

modules = [module.split(' -> ') for module in open('input.txt').read().strip().split('\n')]
inputs = {}

for ind, (name, destinations) in enumerate(modules):
    module_type = name[0]
    if name != 'broadcaster':
        name = name[1:]
    destinations = destinations.split(', ')
    modules[ind][0] = name
    modules[ind][1] = [module_type, destinations]
    if module_type == '%':
        modules[ind][1].append(0)
    for destination in destinations:
        if not destination in inputs:
            inputs[destination] = {}
        inputs[destination][name] = 0
modules = dict(modules)

pulse_count = [0, 0]
process_modules = deque()

for _ in range(1000):
    process_modules.append(['broadcaster', 0])
    while len(process_modules):
        name, pulse_type = process_modules.popleft()
        pulse_count[pulse_type] += 1
        if not name in modules:
            continue
        module_info = modules[name]
        if module_info[0] == 'b':
            for d in module_info[1]:
                inputs[d][name] = pulse_type
                process_modules.append([d, pulse_type])
        elif module_info[0] == '%':
            if pulse_type == 1:
                continue
            module_info[2] = 1-module_info[2]
            for d in module_info[1]:
                inputs[d][name] = module_info[2]
                process_modules.append([d, module_info[2]])
            assert module_info[2] == modules[name][2]
        else:
            new_pulse_type = 1-all(inputs[name].values())
            for d in module_info[1]:
                inputs[d][name] = new_pulse_type
                process_modules.append([d, new_pulse_type])

ans = pulse_count[0]*pulse_count[1]
print(ans)