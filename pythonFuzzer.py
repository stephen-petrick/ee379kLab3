import sys, socket #, ipaddress
from fuzzbang.alphanumericfuzzer import AlphaNumericFuzzer
#Credit to https://jmcph4.github.io/2018/01/19/writing-a-simple-fuzzer-in-python/
#for fuzzing module

def generate_input(n):
    """
    Returns an alphanumeric string with a length no greater than n.
    """
    fuzzer = AlphaNumericFuzzer(0, n)
    
    return fuzzer.generate()

if __name__ == "__main__":
    # usage
	"""
    if len(sys.argv) != 3:
        print("usage: python3 fuzztut.py num_cases max_length")
        exit(1)
	"""        
   
 # command-line arguments    
	num_cases = int(sys.argv[1]) # number of test cases to run
	max_length = int(sys.argv[2]) # maximum length of each string
	instruction = sys.argv[3] #particular instruciton of server we're fuzzing
	print(num_cases)
	results = [] # list for storing the result of each test
	#target = ipaddress.ip_address('10.0.2.4')
    
    # main loop
	for i in range(num_cases):

	
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		#s.settimeout(2) #runs code every 2 seconds, i think
		s.connect(('10.0.2.4',9999)) #hard code server IP address
		s.recv(9999)

		input = generate_input(max_length) # generate input string of max length specified at cmdline
		print (input)
		#s.send(input)
#s.encode() for python3 but would need a decode command serverside as well
		s.send((instruction+" "+input).encode())
		return_value = s.recv(9999) # run name with our input
		print(return_value.decode())
"""	#something wrong with formatting the output for .format(test["output"])	  
		# save test results to our global results list
		test_result = {}
		test_result["num"] = i
		test_result["input"] = input
		test_result["output"] = return_value.decode()
		print(return_value)
		
		results.append(test_result)

	# print summary
	for test in results:
		print("Case #{:d}:".format(test["num"]))
		print("    IN: " + test["input"])
		print("    OUT: {:4d}".format(test["output"]))
		print("\n")
"""
