from datetime import datetime

def isPrime(n):
    if n <= 1 :
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

now = datetime.now()

current_time = now.strftime("%H:%M:%S")
strtime=current_time.split(':')
strtime=strtime[0]+strtime[1]+strtime[2] # grafoyme thn trexousa wra (WRA:LEPTA:DEYTEROLEPTA) enwmenh xwris dhladh ta ':'
intime = int(strtime)                    # kai th metatrepoyme se akeraio
print("Current time as an integer is :",intime)
if(intime%2==0):                         #enas artios de mporei na einai asfalhs
    print(intime,"is not a safe prime - False")
else:                                    #an einai perittos elegxoume
    if(isPrime(int(intime/2))):
        print(intime,"is a safe prime - True")
    else:
        print(intime,"is not a safe prime - False")
