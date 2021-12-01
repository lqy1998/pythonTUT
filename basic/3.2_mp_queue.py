import multiprocessing as mp

def job(q):
    result = 0
    for i in range(1000):
        result += i + i**2
    q.put(result)

if __name__ == '__main__':
    q = mp.Queue()
    p1 = mp.Process(target=job,args=(q,))     
    p2 = mp.Process(target=job,args=(q,))

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    res1 = q.get()
    res2 = q.get()

    print(res1 + res2)