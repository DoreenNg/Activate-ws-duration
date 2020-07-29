import subprocess
from timeit import default_timer as timer

def main():

	url = input("Enter URL to dig: ")

	print("\nCOMMENCE DIGGING!")

	maintain_loop = True
	start = timer()


	while maintain_loop:
		#subprocess.call(["dig", "custws3.toffsintern.ml", ">>", "dig_output.txt"])
		dig_output_to_txt(["dig", url])
		if check_forward_cname() == True:
			maintain_loop = False
		end = timer()
		if ((end-start)/60) > 60 and maintain_loop == True:
			print("\nIt has been an hour and WebSocket is still not active. Digging shall stop here.\n")
			ws = False
			break

	if maintain_loop == False:
		print("\nWebSocket is now active!")
		print("Time taken for WebSocket to become active: {0:.2f}mins".format((end - start)/60))


def dig_output_to_txt(command):
	print (command)

	# Subproccess will input command into 'terminal' and save it in stdout using communicate()
	out = subprocess.Popen(command, stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
	stdout, stderr = out.communicate()

	# Convert bytes to string for stdout
	encoding = 'utf-8'
	stdout_string = stdout.decode(encoding)

	# Save the stdout string to a text file
	output_textfile = open("dig_output.txt", "w")
	n = output_textfile.write(stdout_string)
	output_textfile.close()

	# print stdout for confirmation
	#print (stdout)

def check_forward_cname():
	ws_cname = False

	# Open the textfile and check if that cname can be found in the dig results
	with open('dig_output.txt') as f:
		if 'websocket.cdndd.net.' in f.read():
			ws_cname = True
		return ws_cname


if __name__ == "__main__":
	main()