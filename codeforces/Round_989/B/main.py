amount_tasks = int(input())

for _ in range(amount_tasks):
    amount_digits = int(input())
    digits = sorted(list(map(int, input().split())))

    running = 1
    changed = None

    def rewind_change():
        global changed
        global running
        running = (running / (changed + 1)) * (changed)

    for digit in digits:
        if changed is None:
            changed = digit
            digit += 1
            running *= digit
        else:
            if digit < changed:
                rewind_change()
                changed = digit
                digit += 1
                running *= digit
            else:
                running *= digit

    print(running)



















