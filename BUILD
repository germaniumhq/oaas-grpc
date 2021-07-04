package(default_visibility = ["PUBLIC"])


python_library(
  name="grpc",
  srcs=glob(["oaas_grpc/**/*.py"]),
  deps=[
    "//thirdparty/python:grpcio",
    "//thirdparty/python:netifaces",
    "//thirdparty/python:protobuf",

    "//oaas/oaas",
    "//oaas/registry-api",
  ]
)
