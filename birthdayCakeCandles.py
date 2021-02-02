def birthdayCakeCandles(candles):
    max_val = max(candles)
    return candles.count(max_val)

print(birthdayCakeCandles([1,2,4,4]))