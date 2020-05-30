import sys
sys.path.append('../')
from app.hue_api_communicator import loadIPAddress


def test_file_returns_str():
    ip_address = loadIPAddress()
    assert(isinstance(ip_address, str))