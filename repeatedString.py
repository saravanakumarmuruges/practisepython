def repeatedString1(s, n):
    return s.count("a") * (n // len(s)) + (s[:n%len(s)].count("a"))

def repaetedString2(s, n):
    ans_1 = ((s.count("a"))*n) // len(s)
    ans_2 = s[:n % len(s)].count("a")
    return ans_1, ans_2, ans_1+ans_2

print(repeatedString1('epsxyyflvrrrxzvnoenvpegvuonodjoxfwdmcvwctmekpsnamchznsoxaklzjgrqruyzavshfbmuhdwwmpbkwcuomqhiyvuztwvq', 549382313570))
print(repaetedString2('epsxyyflvrrrxzvnoenvpegvuonodjoxfwdmcvwctmekpsnamchznsoxaklzjgrqruyzavshfbmuhdwwmpbkwcuomqhiyvuztwvq', 549382313570))