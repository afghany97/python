from time import gmtime, strftime

import time , os , datetime

filename = str(datetime.date.today()) + ".txt"

opened = False

now = datetime.datetime.now()

counter = 1

while True:
    os.chdir('C:\\timelog')

    file = open(filename, 'a')

    if counter == 1:

		file.write("our start....")

    		file.write('\n')

    if not opened:

	    responce = os.system("e:")

	    if responce == 0:

	    	opened = True

	    	file.write(strftime("access it at , %H:%M:%S", gmtime()))

    file.write('\n')

    file.write(strftime("%H:%M:%S", gmtime()))

    file.write('\n')

    file.close()

    print(counter)

    counter = counter + 1

    time.sleep(5 * 60)
