# Time taken for WebSocket to become activated (Linux terminal)
## Check how long WebSocket takes to activate after publishing on the T2 portal
dig_output.txt is just a sample of how the output file would look like.

### How to run:
1. Download Python file.
2. Edit the URL on line 12 to be the URL we are checking. Save the file.
3. After publishing, open the terminal and run the Python file using ```python3 checkDuration.py```
4. When WebSocket is activated, "WebSocket is now active!" will be printed out.
5. The script will stop running and the duration it took will be printed out in minutes.
