""" 
* Calculate hours worked
* Takes in military time (hh:mm)

Update:
* Allow user to input multiple times before final calculation
* Takes into account if hours worked were taken place over two days
"""


def main():
    totalHoursWorked = 0

    times = GetTimes()
    for time in times:
        startTimeInSecs = ConvertTimeToSeconds(time['startTime'])
        endTimeInSecs = ConvertTimeToSeconds(time['endTime'])
        totalHoursWorked += CalcHoursWorked(startTimeInSecs, endTimeInSecs)

    print(f"Total hours worked: {totalHoursWorked}")


def GetTimes():
    timesLst = []
    done = False

    while not done:
        startTime = input('Enter start time (hh:mm): ')
        endTime = input('Enter end time (hh:mm): ')
        timesLst.append({"startTime": startTime, "endTime": endTime})

        isUserDone = input('Add more? (Y/N): ')
        # If user does not explcitely say yes,
        # then exit loop
        if (isUserDone.lower() != 'y'):
            done = True

    return timesLst


def ConvertTimeToSeconds(time):
    timeLst = time.split(':')
    hour = int(timeLst[0])
    minute = int(timeLst[1])

    totalSeconds = (hour * 3600) + (minute * 60)
    return totalSeconds


def CalcHoursWorked(start, end):
    secondsWorked = 0

    # if working past midnight
    if start > end:
        t1 = abs(start - 86400)  # 86400 = num of secs in a day
        t2 = abs(0 - end)
        secondsWorked = t1 + t2
    else:
        secondsWorked = end - start

    hoursWorked = round(float(secondsWorked) / 3600, 2)
    return hoursWorked


if __name__ == "__main__":
    main()
