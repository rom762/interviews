def guess_time(tasks, period, threshold, alert_times):
    alert_times = [int(x) for x in alert_times.split()]
    alert_times.sort()
    counter = 0
    current_second = 0
    while counter < threshold:
        current_second += 1
        if current_second in alert_times:
            counter += 1
            alert_times = [t for t in alert_times if t != current_second]
            alert_times.append(current_second + period)
            alert_times.sort()

    return current_second


print(guess_time(6, 5, 10, '1 2 3 4 5 6'))
print(guess_time(5, 7, 12, '5 22 17 13 8'))
