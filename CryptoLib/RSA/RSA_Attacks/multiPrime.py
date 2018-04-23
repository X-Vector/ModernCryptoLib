from utilities import egcd,modinv

def multiPrime(primes_array,n,e,c):
    primes = primes_array
    ts = []
    xs = []
    ds = []
    for i in range(len(primes)):
    	ds.append(modinv(e, primes[i]-1))
    m = primes[0]
    for i in range(1, len(primes)):
    	ts.append(modinv(m, primes[i]))
    	m = m * primes[i]
    for i in range(len(primes)):
    	xs.append(pow((c%primes[i]), ds[i], primes[i]))
    x = xs[0]
    m = primes[0]
    for i in range(1, len(primes)):
    	x = x + m * ((xs[i] - x % primes[i]) * (ts[i-1] % primes[i]))
    	m = m * primes[i]
    return hex(x%n)[2:-1].decode("hex")
