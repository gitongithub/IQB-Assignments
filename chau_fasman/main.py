def calc1(i):
    count = 0
    for k in range(6):
        if dict1[s[i + k]] >= 1:
            count += 1
    return count


def right_extend(j):
    while j - 3 >= 0:
        temp_count = 0
        for k in range(0, 4):
            temp_count += dict1[s[j - k]]
        if temp_count >= 4:
            for k in range(0, 4):
                alpha[j - k] = 'H'
            j -= 1
        else:
            break


def left_extend(j):
    while j + 4 <= len(s):
        temp_count = 0
        for k in range(0, 4):
            temp_count += dict1[s[j + k]]
        if temp_count >= 4:
            for k in range(0, 4):
                alpha[j + k] = 'H'
            j += 1
        else:
            break


def calc2(i):
    count = 0
    for k in range(5):
        if dict2[s[i + k]] > 1:
            count += 1
    return count


def right_extend_b(j):
    while j - 3 >= 0:
        temp_count = 0
        for k in range(0, 4):
            temp_count += dict2[s[j - k]]
        if temp_count >= 4:
            for k in range(0, 4):
                beta[j - k] = 'S'
            j -= 1
        else:
            break


def left_extend_b(j):
    while j + 4 <= len(s):
        temp_count = 0
        for k in range(0, 4):
            temp_count += dict2[s[j + k]]
        if temp_count >= 4:
            for k in range(0, 4):
                beta[j + k] = 'S'
            j += 1
        else:
            break


s = 'SGFRKMAFPSGKVEGCMVQVTCGTTTLNGLWLDDTVYCPRHVICTAEDMLNPNYEDLLIRKSNHSFLVQAGNVQLRVIGHSMQNCLLRLKVDTSNPKTPKYKFVRIQPGQTFSVLACYNGSPSGVYQCAMRPNHTIKGSFLNGSCGSVGF'
alpha = []
beta = []
ans = []
for i in range(len(s)):
    alpha = alpha + ["_"]
    beta = beta + ["_"]
    ans = ans + ["_"]
dict1 = {'E': 1.53, 'A': 1.45, 'L': 1.34, 'H': 1.24, 'M': 1.20, 'Q': 1.17, 'W': 1.14, 'V': 1.14, 'F': 1.12, 'K': 1.07,
         'I': 1.00, 'D': 0.98, 'T': 0.82, 'S': 0.79, 'R': 0.79, 'C': 0.77, 'N': 0.73, 'Y': 0.61, 'P': 0.59, 'G': 0.53}
dict2 = {'M': 1.67, 'V': 1.65, 'I': 1.60, 'C': 1.30, 'Y': 1.29, 'F': 1.28, 'Q': 1.23, 'L': 1.22, 'T': 1.20, 'W': 1.19,
         'A': 0.97, 'R': 0.90, 'G': 0.81, 'D': 0.80, 'K': 0.74, 'S': 0.72, 'H': 0.71, 'N': 0.65, 'P': 0.62, 'E': 0.26}
i = 0
while i < len(s) - 5:
    count = calc1(i)
    if count >= 4:
        for k in range(6):
            alpha[i + k] = 'H'
        right_extend(i + 3)
        left_extend(i + 2)
    i += 1
i = 0
while i < len(s) - 4:
    count = calc2(i)
    if count >= 3:
        for k in range(5):
            beta[i + k] = 'S'
        right_extend_b(i + 2)
        left_extend_b(i + 2)
    i += 1
# print("".join(alpha))
# print("".join(beta))
i = 0
while i < len(s):
    if alpha[i] == '_' and beta[i] == '_':
        ans[i] = 'T'
        i += 1
    elif alpha[i] == 'H' and beta[i] == '_':
        ans[i] = 'H'
        i += 1
    elif alpha[i] == '_' and beta[i] == 'S':
        ans[i] = 'S'
        i += 1
    else:
        t_count = 0
        k = 0
        while i + k < len(s) and alpha[i + k] == 'H' and beta[i + k] == 'S':
            k += 1
        a_count = 0
        b_count = 0
        for j in range(0, k):
            a_count += dict1[s[i + j]]
            b_count += dict2[s[i + j]]
        if a_count >= b_count:
            for j in range(0, k):
                ans[i + j] = 'H'
        else:
            for j in range(0, k):
                ans[i + j] = 'S'
        i += k
print("".join(ans))
