def count_peaks_valleys(price_action):
    if len(price_action) < 3:
        return (0, 0)
    else:
        upps = 0
        downs = 0
        for i in range(1, len(price_action) - 1):
            if (price_action[i] < price_action[i - 1]) and (price_action[i] < price_action[i + 1]):
                downs += 1
            elif (price_action[i] > price_action[i - 1]) and (price_action[i] > price_action[i + 1]):
                upps += 1
        return (upps, downs)
    
print(count_peaks_valleys([1, 2, 3, 2, 1]))
print(count_peaks_valleys([1, 2, 3, 2, 1, 2]))
print(count_peaks_valleys([7, 6, 5, 10, 11, 12, 10, 9, 10]))
print(count_peaks_valleys([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
