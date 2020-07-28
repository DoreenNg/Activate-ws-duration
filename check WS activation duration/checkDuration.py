import subprocess
from timeit import default_timer as timer

def main():
	print("COMMENCE DIGGING!")

	maintainLoop = True
	start = timer()

	while maintainLoop:
		#subprocess.call(["dig", "custws3.toffsintern.ml", ">>", "dig_output.txt"])
		cmdOuputToTxtfile(["dig", "checkws1.toffsintern.ml"])
		if checkForwardCname() == True:
			maintainLoop = False

	end = timer()
	print("WebSocket is now active!")
	print("Time taken for WebSocket to become active:" (end - start)/60)


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