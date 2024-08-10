n = input()
count = 0
for i in range (0,len(n)):
        if n[i] == 'a' or 'e' or 'i' or 'o' or 'u' or 'A' or 'E' or 'I' or 'O' or 'U':
            count+=1
print(count)        