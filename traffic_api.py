import grpc
import command_pb2, command_pb2_grpc

_HOST = 'localhost'
_PORT = '10085'


def get_traffic(email):
    res = {}
    conn = grpc.insecure_channel(_HOST + ':' + _PORT)
    client = command_pb2_grpc.StatsServiceStub(conn)
    response = client.GetStats(
        command_pb2.GetStatsRequest(name="user>>>%s>>>traffic>>>downlink" % email, reset=False))
    if response.stat:
        res["downlink"] = response.stat.value
    response = client.GetStats(
        command_pb2.GetStatsRequest(name="user>>>%s>>>traffic>>>uplink" % email, reset=False))
    if response.stat:
        res["uplink"] = response.stat.value
    return res


if __name__ == '__main__':
    print(get_traffic('123@gmail.com'))
