from concurrent import futures
from typing import Optional, Type

import grpc
import oaas
import oaas._registrations as registrations
from oaas_grpc import OaasGrpcClient
from oaas_grpc.server.find_ips import find_ips
from oaas_registry_api.rpc.registry_pb2 import OaasServiceDefinition
from oaas_registry_api.rpc.registry_pb2_grpc import OaasRegistryStub


def find_add_to_server_base(t: Type) -> Optional[Type]:
    items_to_process = {t}

    while items_to_process:
        item = items_to_process.pop()

        if hasattr(item, "add_to_server"):
            return item

        items_to_process.update(item.__bases__)

    return None


class OaasGrpcServer(oaas.ServerMiddleware):
    def __init__(self, *, port=8999):
        self.port = port
        self._is_serving = False

    def serve(self) -> None:
        if self._is_serving:
            return

        self._is_serving = True

        ensure_grpc_client()

        server_address: str = f"[::]:{self.port}"
        self.server = grpc.server(futures.ThreadPoolExecutor())

        # we add the types to the server and only after we start it we
        # notify the oaas registry about the new services
        for service_definition in registrations.services:
            if not self.can_serve(service_definition):
                continue

            print(
                f"Added GRPC service: {service_definition.gav} as {service_definition.code}"
            )

            find_add_to_server_base(service_definition.code).add_to_server(  # type: ignore
                service_definition.code(), self.server
            )

        port = self.server.add_insecure_port(server_address)

        locations = find_ips(port=self.port)

        print(f"listening on {port}")
        self.server.start()

        # we register the services
        registry = oaas.get_client(OaasRegistryStub)

        for service_definition in registrations.services:
            registry.register_service(
                OaasServiceDefinition(
                    namespace=service_definition.namespace,
                    name=service_definition.name,
                    version=service_definition.version,
                    locations=locations,
                )
            )

    def join(self) -> None:
        self.server.wait_for_termination()

    def can_serve(self, service_definition: oaas.ServiceDefinition) -> bool:
        return find_add_to_server_base(service_definition.code) is not None


def ensure_grpc_client():
    """
    If we're exposing gRPC services, we also need to register them
    into the oaas-registry. For this to happen, we need to have the
    OaasGrpcClient registered. If the user forgot to add it, we'll
    add it ourselves.
    """
    for client in registrations.clients_middleware:
        if isinstance(client, OaasGrpcClient):
            return

    oaas.register_client_provider(OaasGrpcClient())
