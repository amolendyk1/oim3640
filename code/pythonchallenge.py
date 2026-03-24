# puzzle 0
print(2**38)

# puzzle 1
encrypted = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."


def histogram(s):
     """Return a dictionary mapping each character in s to the number of times it apears in s."""
     d = {}
     for c in s:
        d[c] = d.get(c, 0) + 1
    return d