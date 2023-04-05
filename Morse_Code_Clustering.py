bits = "0000000011011010011100000110000001111110100111110011111100000000000111011111111011111011111000000101100011111100000111110011101100000100000"

bits+="0001"
def decode_bits(bits):

    #bits = bits[int(bits.index('1')) : len(bits)-bits[::-1].index('1')]
    bits = bits[int(bits.index('1')) :]

    counter = 0
    prev = '1'
    message_hz = []

    for i in bits:
        if i==prev:
            counter += 1
        else:
            message_hz.append(counter)
            counter = 0
            prev = i
            counter += 1

    return message_hz[:-1]


def decode_morse(bits):
    morse_code = bits
   # print(morse_code)
    words = morse_code.split("   ")

    message = ""
    for word in words:
        message += " "
        for bokva in word.split(" "):
            if bokva != "":
                message += MORSE_CODE[bokva]

    message_clean = ""
    clean = 0
    for i in message:
        if i == " ": clean +=1
        else: break
    return message[clean:]

data = decode_bits(bits)

#print(data)

i=0
ones = []
zeros = []

print(data)

while i!=len(data):
    if i%2==0: ones.append(data[i])
    else: zeros.append(data[i])
    i+=1

def k_k(data, k):

    d = data.copy()
    
    if k==3:
        centroid = [0, sum(d)/len(d), max(d)]
        cluster = [[],[],[]]
    if k==2:
        centroid = [0, max(d)]
        cluster = [[],[]]


    flag = True

    while flag:
        cluster = [[],[],[]]
        old_c = centroid.copy()
        for i in d:
            buf =[]
            for l in range(k):
                buf.append( (i-centroid[l])**2 )
            cluster[buf.index(min(buf))].append(i)
    
        for new_c in range(k):
            summed_c = sum(cluster[new_c]) + centroid[new_c]
            counter = len(cluster[new_c])+1
            centroid[new_c] = (summed_c/counter)

        if old_c == centroid:
            flag = False
        else: print("Learning....\n")

    message = ""

    print(cluster)
    for i in d:
        buf = []
        for cl in range(k):
            buf.append((i-centroid[cl])**2)
        index = buf.index(min(buf))
        
        if k==3:
            if index == 0:
                print("i: {} = char".format(i))
                message+= "c"
            elif index == 1:
                print("i: {} = in word".format(i))
                message +="i"
            elif index ==2:
                print("i: {} = word".format(i))
                message+="b"
        elif k==2:
            if index == 0:
                print("i: {} = .".format(i))
                message+= "."
            elif index == 1:
                print("i: {} = -".format(i))
                message +="-"

    return message


message_zeros = k_k(zeros, 3)
message_ones = k_k(ones, 2)

print(message_zeros, message_ones)



final = ""


for i in range(len(message_zeros)):
    final+=message_ones[i]
    final+=message_zeros[i]

final+=message_ones[-1]

final = final.replace("c", "")
final = final.replace("i", " ")
final = final.replace("b", "   ")
print(final)
