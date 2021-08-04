package(default_visibility = ["PUBLIC"])

subinclude("//build/please:python.plz")

python_library(
  name="grpc-lib",
  deps=[
    "//build/thirdparty/python:netifaces",
    "//build/thirdparty/python:protobuf",
    "//build/thirdparty/python:grpcio",

    "//oaas/oaas:oaas-lib",
    "//oaas/registry-api:registry-api-lib",
  ],
  srcs=glob(["oaas_grpc/**/*.py"]),
)

ge_python_library(
  name="grpc",
  deps=[
    "//build/thirdparty/gepython:netifaces",
    "//build/thirdparty/gepython:protobuf",
    "//build/thirdparty/gepython:grpcio",

    "//oaas/oaas",
    "//oaas/registry-api",
  ],
  srcs=glob(["oaas_grpc/**/*.py"]),
)
