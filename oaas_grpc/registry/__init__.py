import oaas

import oaas_grpc.rpc.registry_pb2_grpc as registry_pb2_grpc


@oaas.service("oaas-registry")
class OaasRegistry(registry_pb2_grpc.OaasRegistryStub):
    def registerService(self, service_registration):
        pass

