import subprocess
from timeit import default_timer as timer

def main():

	url = input("Enter URL to dig: ")

	print("COMMENCE DIGGING!")

	maintainLoop = True
	start = timer()

	while maintainLoop:
		#subprocess.call(["dig", "custws3.toffsintern.ml", ">>", "dig_output.txt"])
		cmdOuputToTxtfile(["dig", url])
		if checkForwardCname() == True:
			maintainLoop = False
		end = timer()
		if ((end-start)/60) > 60:
			print("It has been an hour and WebSocket is still not active. Digging shall stop here.")
			ws = False
			break

	if ws != False:
		print("WebSocket is now active!")
		print("Time taken for WebSocket to become active: " (end - start)/60)


def cmdOuputToTxtfile(command):
	print (command)

	# Subproccess will input command into 'terminal' and save it in stdout using communicate()
	out = subprocess.Popen(command, stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
	stdout, stderr = out.communicate()

	# Convert bytes to string for stdout
	encoding = 'utf-8'
	stdoutString = stdout.decode(encoding)

	# Save the stdout string to a text file
	outputText = open("dig_output.txt", "w")
	n = outputText.write(stdoutString)
	outputText.close()

	# print stdout for confirmation
	#print (stdout)

def checkForwardCname():
	wsCname = False
	with open('dig_output.txt') as f:
		if 'websocket.cdndd.net.' in f.read():
			wsCname = True
		return wsCname


if __name__ == "__main__":
	main()