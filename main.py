from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
	return {"Hello": "This is Bounty Assesment Test"}

@app.get("/binary-to-decimal/{input_number}")
def read_number(input_number: int, q: Union[str, None] = None):
	#total length of binary number
	s = str(input_number)
	n = len(str(input_number))

	#check if input number is proper binary number
	for x in s:
		if int(x) != 0 and int(x) != 1:
			return {"error": "this is not proper binary number." }

	decimal_output = 0
	start_index = 0
	for i in range(n-1,-1,-1):
		decimal_output = decimal_output + int(s[start_index]) * pow(2,i)
		start_index = start_index + 1

	return {"binary_input": input_number, "decimal_output:": decimal_output }

@app.get("/decimal-to-binary/{input_number}")
def read_number(input_number: int, q: Union[str, None] = None):

	n = input_number
	x = ""
	while n:
	    x = str(n % 2) + x
	    n //= 2
	    
	return {"decimal_input": input_number, "binary_output:": x }

#@app.get("/items/{item_id}")
#def read_item(item_id: int, q: Union[str, None] = None):
#	return {"item_id": item_id, "q": q}
