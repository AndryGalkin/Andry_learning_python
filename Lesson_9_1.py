from time import sleep


class TrafficLight:


    def running(self):
        times = [7, 2, 7, 2]
        colors = ['\033[31m', '\033[33m', '\033[32m', '\033[33m']
        end_color = '\033[0m'
        n = 0
        while True:
                print(f'\r{colors[n]}███{end_color}', end='')
                sleep(times[n])
                n += 1
                if n >= 4: n = 0


tr_lt = TrafficLight()
tr_lt1 = TrafficLight()
tr_lt.running()
