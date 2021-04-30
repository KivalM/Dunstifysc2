import time
import os
# hotkeys

pause = "p"
unpause = "p"

# variables

timestamps = []
time_s = []
supply = []
item = []
notes = []


start_time = 0
curr_time = 0
check_interval = 0.05

# TODO pausing and start on keypress

time_offset = 0

notif_string = '''dunstify -h string:x-dunst-stack-tag:sc2 "{} --> {}" "{} \n {}"'''


def readfile():
    with open("bo.txt", "r") as file:
        x = file.readlines()
        for I in x:
            line_list = I.split("\t")
            print(line_list)
            supply.append(int(line_list[0]))
            time_list = line_list[1].lstrip().split(":")
            time_seconds = int(time_list[0])*60 + int(time_list[1])
            time_s.append(time_seconds)
            timestamps.append(line_list[1].lstrip())
            item.append(line_list[2].lstrip())
            notes.append(line_list[3].lstrip().replace("\n", ""))


def notify_send(index):
    print(notif_string.format(
        timestamps[index], supply[index], item[index], notes[index]))
    os.system(notif_string.format(
        timestamps[index], supply[index], item[index], notes[index])
    )


def mainloop():
    start_time = time.perf_counter()
    index = 0
    while True:
        curr_time = time.perf_counter()
        print(time_s[index])
        print(curr_time + time_offset - start_time)
        if (curr_time + time_offset - start_time) >= time_s[index]:
            notify_send(index)
            index += 1
        else:
            time.sleep(check_interval)


if __name__ == "__main__":

    readfile()
    print(notes)
    mainloop()
