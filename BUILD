load("@pip//:requirements.bzl", "requirement")


py_library(
  name="grpc",
  srcs=glob(["oaas_grpc/**/*.py"]),
  imports=[""],
  deps=[
    "//oaas/oaas",
    "//oaas/registry-api",
    requirement('netifaces'),
    requirement('protobuf'),
    requirement('grpcio'),
  ]
)

package(default_visibility = ["//visibility:public"])
