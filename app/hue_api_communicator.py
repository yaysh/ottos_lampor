import os
import requests


'''
    A controller that sets up an environment that let's you control the philips hue bridge
    from home:
        Link official to API: 
            https://developers.meethue.com/develop/get-started-2/?fbclid=IwAR3dWTw1018ackcRonGMkk93qp35_fILWtBNltzM-wABqSABm8hBDyYguek
'''


'''
    PARAMS:
        ip_address: str

    Purpose:
        Generate the full URL that will be used to access the philips hue API.
        An URL needs to be generated as it uses the local IP address.
    TODO:
        Automatically find the IP address
'''
def createGenerateKeyURL(ip_address):
    url = 'https://' + ip_address + '/debug/clip.html'
    r = requests.get(url)
    if r.status_code != 200:
        print("Error generating an URL that can communicate with the device.\
            Ensure that the IP address is correct.")
    return url


def generateAuthenticatedAPIURL(ip_address, key):
    url ='https://{}/api/{}/'.format(ip_address, key)
    return url


'''
    Returns:
        ip_address: Str
    Purpose:
        Read the IP address stored in the folder /static/ip_address.txt
        and return it as a string
'''
def loadIPAddress():
    f = open(os.path.abspath('../') + "/app/static/ipaddress.txt", "r")
    line = f.read()
    return str(line.strip())


def generateKey(base_url):
    url = base_url + '/api'
    body = {
        "devicetype":"my_hue_app#iphone peter"
    }
    r = requests.post(url=url, data=body)
    # TODO: Read to make sure success is made,
    # furthermore, read the username that is supplied
    # Should be something like this:
    #     success: {
    #         "username": "someusername"
    #     }



def start():
    # Ip address to the philips device bridge
    ip_address = loadIPAddress()
    
    # Generates an URL that enables the creation of an authenticated user
    key_generation_url = createGenerateKeyURL(ip_address)
    
    # Generates the key that represents an authenticated user, key is used
    # in the URL to allow the user to access the API.
    key = generateKey(key_generation_url)

    # The API that is now authenticated and allows for access of the philips
    # lighting system
    authenticated_api_url = generateAuthenticatedAPIURL(ip_address, key)


    

if __name__ == "__main__":
    start()