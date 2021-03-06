from hunabku.Hunabku import Hunabku
import socket
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--db', type=str, default='colav',
                    help='database name (default colav)')
parser.add_argument(
    '--ip',
    type=str,
    default=None,
    help='local server ip (optional for public ip)')
parser.add_argument('--port', type=int, default=8080,
                    help='server port (default 8080)')
parser.add_argument('--apikey', type=str, default='colavudea', help='apikey')


args = parser.parse_args()
if args.ip is None:
    ip = socket.gethostbyname(socket.gethostname())
else:
    ip = args.ip

if __name__ == '__main__':
    server = Hunabku(apikey=args.apikey, ip=ip, port=args.port)
    server.start()
