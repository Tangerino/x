
from pymodbus.client.sync import ModbusTcpClient


def main():
    client = ModbusTcpClient('10.0.0.230')
    client.set_debug(True)
    result = client.read_holding_registers(3180, 6, unit=14)
    print(result)
    client.close()
