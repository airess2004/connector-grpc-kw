
import requests
import os
import grpc
import sys
from connector_grpc_kw.proto import *
from google.protobuf.struct_pb2 import Struct
from google.protobuf.descriptor import FileDescriptor
from typing import Any
from google.protobuf.any_pb2 import Any
import json
from modulefinder import ModuleFinder


class RpcRequest():
    def __init__(self,
        url: str,
        service_name: str | None,
        rpc_name: str | None,
        data: dict[str, Any] | None,
    ):
        self.url = url
        self.service_name = service_name
        self.rpc_name = rpc_name
        self.data = data

    def execute(self, config, task_data):
        pb_2_mods = [m for m in sys.modules.values() if m and "connector_grpc_kw.proto." in m.__name__ and m.__name__.endswith("_pb2")]
        service_stub = f"{self.service_name}Stub"
        service_pb_2 = ""
        for mod in pb_2_mods:
            if self.service_name in mod.DESCRIPTOR.services_by_name.keys():
                service_pb_2 = mod

        pb_2_grpc_mods = [m for m in sys.modules.values() if m and "connector_grpc_kw.proto." in m.__name__ and m.__name__.endswith("_pb2_grpc")]
        service_pb_2_grpc = ""
        for mod in pb_2_grpc_mods:
            if service_stub in dir(mod):'Loans'
                service_pb_2_grpc = mod

        file_descriptor = service_pb_2.DESCRIPTOR
        service_types = file_descriptor.services_by_name
        your_service_descriptor = service_types[self.service_name]
        grpc_server_host = self.url
        request_name = your_service_descriptor.methods_by_name[self.rpc_name].input_type.name
        request = getattr(service_pb_2,request_name)()
        for field in your_service_descriptor.methods_by_name[self.rpc_name].input_type.fields:
            setattr(request , field.name, self.data[field.name])

        try:
            with grpc.insecure_channel(grpc_server_host) as channel:
                current_stub = getattr(service_pb_2_grpc,service_stub)
                stub = current_stub(channel)
                func = getattr(stub,self.rpc_name)
                grpc_response = func(request)
                output_dict = {}
                for field, value in grpc_response.ListFields():
                    if isinstance(value, Any):
                        if len(value.value) > 0:
                            try:
                               output_dict[field.name] = json.loads(value.value)
                            except Exception as e:
                               output_dict[field.name] = str(value)
                    else:
                        output_dict[field.name] = value
                json_string = json.dumps(output_dict, indent=4)
            return {
                "response": json_string,
                "status": "200",
                "mimetype": "application/json",
            }
        except Exception as e:
            return {
                "response": f'{"error": {e}}',
                "status": 500,
                "mimetype": "application/json",
            }
