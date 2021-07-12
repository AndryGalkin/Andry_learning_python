for percent in range(20):
    if percent % 10 == 1 and percent % 100 != 11:
        print(percent, "процент ")
    elif 1 < percent % 10 < 5 and not 11 < percent % 100 < 15:
        print(percent, "процента ")
    else:
        print(percent, "процентов ")
        
