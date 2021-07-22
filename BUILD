package(default_visibility = ["PUBLIC"])

subinclude("//build/please:python.plz")

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
