from concurrent import futures

import grpc
import oaas
import oaas._registrations as registrations
import oaas_grpc.rpc.registry_pb2_grpc as registry_pb2_grpc
import oaas_grpc.rpc.registry_pb2 as registry_pb2


oaas.client("oaas-registry")(registry_pb2_grpc.OaasRegistryStub)


class GrpcServerMiddleware(oaas.ServerMiddleware):
    def serve(self) -> None:
        server_address: str = f"[::]:{self.port}"
        server = grpc.server(futures.ThreadPoolExecutor())

        # we add the types to the server
        for ctype, cdef in registrations.clients.items():
            ctype.add_to_server(ctype(), server)

        server.start()

        registry: registry_pb2_grpc.OaasRegistryStub = None

        for ctype, cdef in registrations.clients.items():
            registration = registry_pb2.ServiceRegistration(
                serviceDefinition=registry_pb2.ServiceDefinition(),
                serviceAddress=[registry_pb2.ServiceAddress()]
            )
            registry.registerService(registration)

        port = server.add_insecure_port(server_address)

    def join(self) -> None:
        pass
