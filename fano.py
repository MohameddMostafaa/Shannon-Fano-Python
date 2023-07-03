prob = [0.4, 0.2, 0.12, 0.08, 0.08, 0.08, 0.04]
prob.sort(reverse=True)
code = []

for p in prob:
    code.append("")



def get_smallest_difference_index(arr):
    smallest = arr[0]
    smallest_index = 0

    for i in range(len(arr)):
        if smallest > arr[i]:
            smallest = arr[i]
            smallest_index = i

    return smallest_index




def get_sums(arr):
    sums = []
    for i in range(len(arr) - 1):
        temp1 = 0
        temp2 = 0
        j = i
        k = i + 1
        while(j >= 0):
            temp1 += arr[j]
            j -= 1
        while(k < len(arr)):
            temp2 += arr[k]
            k += 1
    
        sums.append(abs(temp1 - temp2))


    return sums


def fill_code(lower, upper, smallest):
    i = lower
    while (i <= upper):
        if i <= smallest + lower:
            code[i] += '0'

        else:
            code[i] += '1'

        i += 1

def get_index_2d(arr, i):
    if i == 0:
        return 0
    else:
        index = 0
        for x in range(len(arr)):
            if x < i:
                if type(arr[x]) == list:
                    index += len(arr[x])
                else:
                    index += 1
        return index



sums = get_sums(prob)
smallest_diff_index = get_smallest_difference_index(sums)

prob_parts = []

prob_parts.append(prob[ :smallest_diff_index + 1])
prob_parts.append(prob[smallest_diff_index + 1: ])

fill_code(0, len(prob) - 1, smallest_diff_index)


i = 0
while i < len(prob_parts):
    new_arr = []
    if type(prob_parts[i]) == list:
        if len(prob_parts[i]) >= 2:
            sums2 = get_sums(prob_parts[i])
            smallest_diff_index2 = get_smallest_difference_index(sums2)
            fill_code(get_index_2d(prob_parts, i), get_index_2d(prob_parts, i) + (len(prob_parts[i]) - 1), smallest_diff_index2)
            if i > 0:
                new_arr[len(new_arr):len(new_arr)] =  prob_parts[ :i]
            # new_arr[len(new_arr):len(new_arr)] = prob_parts[i][ :smallest_diff_index2 + 1]
            # new_arr[len(new_arr):len(new_arr)] = prob_parts[i][smallest_diff_index2 + 1: ]
            new_arr.insert(len(new_arr), prob_parts[i][ :smallest_diff_index2 + 1])
            new_arr.insert(len(new_arr), prob_parts[i][smallest_diff_index2 + 1: ])
            if i < len(prob_parts) - 1:
                new_arr[len(new_arr):len(new_arr)] = prob_parts[i+1: ]
            prob_parts = new_arr
            i = 0
        else:
            i += 1
    else:
        i += 1    

print(code)

msg = "011000110001111"

str = ""
decoding = ""

for num in msg:
     str += num
     if str in code:
         decoding += f"X{code.index(str) + 1} "
         str = ""

print(decoding)
