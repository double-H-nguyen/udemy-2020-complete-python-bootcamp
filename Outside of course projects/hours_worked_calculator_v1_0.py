""" 
Calculate hours worked
Only takes in military time (hh:mm)
"""


def main():
    times = GetTimes()
    startTimeInSecs = ConvertTimeToSeconds(times['startTime'])
    endTimeInSecs = ConvertTimeToSeconds(times['endTime'])
    CalcHoursWorked(startTimeInSecs, endTimeInSecs)


def GetTimes():
    startTime = input('Enter your start time (hh:mm): ')
    endTime = input('Enter your end time (hh:mm): ')

    return {"startTime": startTime, "endTime": endTime}


def ConvertTimeToSeconds(time):
    timeLst = time.split(':')
    hour = int(timeLst[0])
    minute = int(timeLst[1])

    totalSeconds = (hour * 3600) + (minute * 60)
    return totalSeconds


def CalcHoursWorked(start, end):
    secondsWorked = end - start
    hoursWorked = round(secondsWorked / 3600, 2)
    print(f"Total hours worked: {hoursWorked}")


if __name__ == "__main__":
    main()
