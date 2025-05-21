import requests

# url = "api.github.com/repos/kubernetes/kubernetes/pulls"
# requests.get(url)
# The above code will not work because the URL is not complete and does not include the protocol (http or https).
# The correct URL should be:
url = "https://api.github.com/repos/kubernetes/kubernetes/pulls"
response = requests.get(url)

entire_response = response.json()

for i in range(len(entire_response)):
    print(entire_response[i]["user"]["login"])