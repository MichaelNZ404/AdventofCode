import sys

xinput = sys.stdin.readline()
xinput = xinput.rstrip('\n')

sum = 0
for idx, x in enumerate(xinput):
    idx2 = idx + int(len(xinput)/2)
    if idx2 >= (len(xinput)):
        idx2 = idx2 - len(xinput)
    if x == xinput[idx2]:
        sum = sum + int(x)
print(sum)
