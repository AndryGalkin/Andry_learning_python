inp_dur = input("Ваше число: ")
inp_dur = int(inp_dur)
SEC_IN_HR = 3600
SEC_IN_DAY = 86400

if inp_dur <= 60:
    dt = [0, 0, 0, inp_dur]

elif 60 <= inp_dur < SEC_IN_HR:
    dt = [0, 0, inp_dur // 60, inp_dur % 60]

elif SEC_IN_HR <= inp_dur < SEC_IN_DAY:
    dt = [0, inp_dur // SEC_IN_HR, (inp_dur % SEC_IN_HR) // 60, inp_dur % 60]

elif inp_dur >= SEC_IN_DAY:
    dt = [inp_dur // SEC_IN_DAY, (inp_dur % SEC_IN_DAY) // SEC_IN_HR, (inp_dur % SEC_IN_HR) // 60, inp_dur % 60]

print(f"{dt[0]} д. {dt[1]} ч. {dt[2]} мин. {dt[3]} сек.")
