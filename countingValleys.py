def countingValleys(steps, path):
    run = 0
    valley = 0
    for step in path:
        if step == 'D':
            last_run, run = run, run -1
        elif step == 'U':
            last_run, run = run, run + 1
        if run == 0 and last_run < 0:
            valley = valley + 1
    return valley

print(countingValleys(8, 'UDDDUDUU'))