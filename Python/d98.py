# Multiprocessing 

import requests
import multiprocessing
import concurrent.futures 

def downloadFile(url,name):
    print(f"Started Downloading {name}")
    r = requests.get(url, allow_redirects=True)
    open(f'files/file{name}.jpg', 'wb').write(r.content)
    print(f"Finished Downloading {name}")

url="https://picsum.photos/2000/3000"

# Using multiprocessing

pros=[]
for i in range(50):
    # downloadFile(url,i)
    p=multiprocessing.Process(target=downloadFile,args=[url,i])
    p.start()
    pros.append(p)

for p in pros:
    p.join()

# Using concurrent.futures

with concurrent.futures.ProcessPoolExecutor() as executor:
    l1=[url for i in range(60)]
    l2=[i for i in range(60)]
    results=executor.map(downloadFile,l1,l2)
    for r in results:
        print(r)




