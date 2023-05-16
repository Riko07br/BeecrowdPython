secondsInput = int(input(""))

hours = secondsInput // 3600
secondsInput -= (hours * 3600)

minutes = secondsInput // 60
secondsInput -= (minutes * 60)

print("{}:{}:{}".format(hours, minutes, secondsInput))