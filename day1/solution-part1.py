import sys

xinput = sys.stdin.readline()
xinput = xinput.rstrip('\n')

sum = 0
for idx, x in enumerate(xinput):
    idx2 = idx + 1
    if idx2 >= (len(xinput)):
        idx2 = 0
    if x == xinput[idx2]:
        sum = sum + int(x)
print(sum)
