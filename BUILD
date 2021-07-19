package(default_visibility = ["PUBLIC"])

subinclude("//build/please:python.plz")

ge_python_library(
  name="grpc",
  deps=[
    "//build/thirdparty/python:netifaces",
    "//build/thirdparty/python:protobuf",
    "//build/thirdparty/python:grpcio",

    "//oaas/oaas",
    "//oaas/registry-api",
  ],
  srcs=glob(["oaas_grpc/**/*.py"]),
)
