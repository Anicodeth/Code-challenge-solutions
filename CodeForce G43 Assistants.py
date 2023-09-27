t = int(input())

for _ in range(t):
    n = int(input())
    intervals = []
    for _ in range(n):
        interval = list(map(int, input().split(" ")))
        intervals.append(interval)
    intervals.sort( key = lambda x : x[0])
    assistants = 0
    end_times = []
    for times in intervals:
        start, end = times
        if not end_times:
            assistants += 1
            end_times.append(end)

        else:
            found = False
            for i, ending in enumerate(end_times):
                if start >= ending:
                    end_times[i] = end
                    found = True
                    break
            if not found:
                    assistants += 1
                    end_times.append(end)





        


    print(assistants)
