def calc1(i):
    temp = 0
    for k in range(6):
        temp += dict2[s[i + k]]
    return temp


def calc2(i):
    temp = 0
    for k in range(5):
        temp += dict4[s[i + k]]
    return temp


s = 'SGFRKMAFPSGKVEGCMVQVTCGTTTLNGLWLDDTVYCPRHVICTAEDMLNPNYEDLLIRKSNHSFLVQAGNVQLRVIGHSMQNCLLRLKVDTSNPKTPKYKFVRIQPGQTFSVLACYNGSPSGVYQCAMRPNHTIKGSFLNGSCGSVGF'
alpha = []
beta = []
for i in range(len(s)):
    alpha = alpha + ["_"]
    beta = beta + ["_"]
dict1 = {'E': 1.53, 'A': 1.45, 'L': 1.34, 'H': 1.24, 'M': 1.20, 'Q': 1.17, 'W': 1.14, 'V': 1.14, 'F': 1.12, 'K': 1.07,
         'I': 1.00, 'D': 0.98, 'T': 0.82, 'S': 0.79, 'R': 0.79, 'C': 0.77, 'N': 0.73, 'Y': 0.61, 'P': 0.59, 'G': 0.53}
dict2 = {'E': 1, 'A': 1, 'L': 1, 'H': 1, 'M': 1, 'Q': 1, 'W': 1, 'V': 1, 'F': 1, 'K': 0.5,
         'I': 0.5, 'D': 0, 'T': 0, 'S': 0, 'R': 0, 'C': 0, 'N': -1, 'Y': -1, 'P': -1, 'G': -1}
dict3 = {'M': 1.67, 'V': 1.65, 'I': 1.60, 'C': 1.30, 'Y': 1.29, 'F': 1.28, 'Q': 1.23, 'L': 1.22, 'T': 1.20, 'W': 1.19,
         'A': 0.97, 'R': 0.90, 'G': 0.81, 'D': 0.80, 'K': 0.74, 'S': 0.72, 'H': 0.71, 'N': 0.65, 'P': 0.62, 'E': 0.26}
dict4 = {'M': 1, 'V': 1, 'I': 1, 'C': 1, 'Y': 1, 'F': 1, 'Q': 1, 'L': 1, 'T': 1, 'W': 1,
         'A': 0.5, 'R': 0, 'G': 0, 'D': 0, 'K': -1, 'S': -1, 'H': -1, 'N': -1, 'P': -1, 'E': -1}
score = 0
i = 0
while i < len(s) - 5:
    score = calc1(i)
    if score >= 4:
        for k in range(6):
            alpha[i + k] = 'H'
        i += 6
    else:
        i += 1
score = 0
i = 0
while i < len(s) - 4:
    score = calc2(i)
    if score > 3:
        for k in range(5):
            beta[i + k] = 'S'
        i += 5
    else:
        i += 1
print(len(alpha))
print("".join(alpha))
print("".join(beta))
