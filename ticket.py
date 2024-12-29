def lucky_ticket():
    n = 0
    for i1 in range(0,10):
        for i2 in range(0,10):
            for i3 in range(0,10):
                for i4 in range(0,10):
                    for i5 in range(0,10):
                        for i6 in range(0,10):
                            if i1 + i2 + i3 == i4 + i5 + i6:
                                n += 1
    return n - 1
print(lucky_ticket())