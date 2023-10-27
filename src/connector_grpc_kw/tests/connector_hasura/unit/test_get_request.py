import json
from unittest.mock import MagicMock
from unittest.mock import patch
from typing import Any
from connector_grpc_kw.commands.rpc_request import RpcRequest

class TestRpcRequest:
    def test_success_get_request(self) -> None:
         with patch("requests.post") as mock_post:
             a = RpcRequest(
               url = "172.23.15.189:31101",
               service_name = "Loans",
               rpc_name = "GetLenderSchedule",
               data = {
                    "LenderScheduleID": 1109734
                }
             )
             func = getattr(a,'execute')
             result = func(config= Any, task_data= Any)
             print(result['response'])

             a = RpcRequest(
               url = "172.23.15.189:31101",
               service_name = "Loans",
               rpc_name = "DetailLoan",
               data = {
                    "LoanID": 6
                }
             )
             func = getattr(a,'execute')
             result = func(config= Any, task_data= Any)
             print(result['response'])

             a = RpcRequest(
               url = "172.23.15.189:31101",
               service_name = "Loans",
               rpc_name = "GetLoanContract",
               data = {
                    "LoanID": 6
                }
             )
             func = getattr(a,'execute')
             result = func(config= Any, task_data= Any)
             print(result['response'])

             a = RpcRequest(
               url = "172.23.2.97:31103",
               service_name = "Users",
               rpc_name = "GetUserByEmail",
               data = {
                    "email": "johan.radot+pliv-2549.355025@koinworks.com"
                }
             )
             func = getattr(a,'execute')
             result = func(config= Any, task_data= Any)
             print(result['response'])
