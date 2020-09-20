import unittest
import oaas
import test.test_pb2_grpc as test_pb2_grpc
import test.test_pb2 as test_pb2


oaas.client("test-service")(test_pb2_grpc.TestServiceStub)


@oaas.service("test-service")
class TestService(test_pb2_grpc.TestServiceServicer):
    def ping(self, request: test_pb2.Ping, context) -> test_pb2.Pong:
        result = test_pb2.Pong()

        result.text = request.text + "-pong"
        result.len = len(request.text)

        return result


class TestGrpcSerialization(unittest.TestCase):
    def test_serialization(self) -> None:
        client = oaas.get_client(test_pb2_grpc.TestServiceStub)
        result = client.ping(test_pb2.Ping(text="ping"))

        self.assertEqual("ping-pong", result.text)
        self.assertEqual("4", result.len)
