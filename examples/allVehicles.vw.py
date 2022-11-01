import argparse
import logging

from weconnect import weconnect


def main():
    """ Simple example showing how to retrieve all vehciles from the account """
    parser = argparse.ArgumentParser(
        prog='allVehciles',
        description='Example retrieving all vehciles in the account')
    parser.add_argument('-u', '--username', help='Username of Volkswagen id', required=True)
    parser.add_argument('-p', '--password', help='Password of Volkswagen id', required=True)
    parser.add_argument('-d', '--debug', help='Turn on debug logging', default=False, action='store_true')

    args = parser.parse_args()
    if args.debug:
        logging.basicConfig(level=logging.DEBUG)

    print('#  Initialize WeConnect')
    weConnect = weconnect.WeConnect(username=args.username, password=args.password, updateAfterLogin=False, loginOnInit=False)
    print('#  Login')
    weConnect.login()
    print('#  update')
    weConnect.update()
    print('#  print results')
    for vin, vehicle in weConnect.vehicles.items():
        del vin
        print(vehicle)
    print('#  done')


if __name__ == '__main__':
    main()
