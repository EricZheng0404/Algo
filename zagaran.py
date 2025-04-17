"""
A retry mechanism for handling API calls with rate limiting and error handling.

This function attempts to make an API call up to 5 times, handling rate limiting
(status 429) by retrying, while failing fast for other error codes.

Args: (just so I can get the output of the function)
    api_call (function): A function that makes an API call and returns a dictionary
        with 'status' and 'text' keys. The status should be an integer HTTP status code.

Returns:
    str: The 'text' from the API response if successful (status 200)

Raises:
    Exception: If the API returns an error status code other than 429
    Exception: If the API returns status 429 for 5 consecutive attempts
"""
def retry(api_call):
    max_attempts = 0
    while max_attempts < 5:
        result = api_call()
        if result["status"] == 200:
            return result["text"]
        elif result["status"] == 429:
            max_attempts += 1
            if max_attempts == 5:
                raise Exception("Reached max attempts")
        else:
            raise Exception(f"Error code {result['status']}")
        
# api_call1(): Return status 200 the first time, should return "Hello World"
def api_call1():
    return {"status": 200, "text": "Hello World"}

# api_call2(): Return status 500 (Error code) the first time, should throw error
def api_call2():
    return {"status": 500, "text": "Hello World"}
   
# api_call3(): Return status 429 for four time and return 200 for the 5th time
counter3 = 0
def api_call3():
    global counter3
    while counter3 < 4:
        counter3 += 1
        return {"status": 429, "text": "Hello World"}
    if counter3 == 4:
        return {"status": 200, "text": "Hello World"}
    
# api_call4(): Return status 429 for five times
counter4 = 0
def api_call4():
    global counter3
    while counter3 < 5:
        counter3 += 1
        return {"status": 429, "text": "Hello World"}

        
if __name__ == "__main__":
    # assert retry(api_call1) == "Hello World"
    # retry(api_call2) 
    # retry(api_call3)
    retry(api_call4)
