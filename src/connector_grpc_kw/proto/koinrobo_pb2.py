# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: koinrobo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0ekoinrobo.proto\x12\x07packets\x1a\x19google/protobuf/any.proto\"\'\n\x14InputRoboOrderDetail\x12\x0f\n\x07OrderID\x18\x01 \x01(\x03\"\\\n\x15OutputRoboOrderDetail\x12\x0e\n\x06Status\x18\x01 \x01(\x05\x12\x0f\n\x07Message\x18\x02 \x01(\t\x12\"\n\x04\x44\x61ta\x18\x03 \x01(\x0b\x32\x14.google.protobuf.Any\"V\n\x08RoboUser\x12\x0c\n\x04UUID\x18\x01 \x01(\t\x12\x0c\n\x04Name\x18\x02 \x01(\t\x12\r\n\x05Group\x18\x03 \x01(\t\x12\r\n\x05Value\x18\x04 \x01(\t\x12\x10\n\x08IsActive\x18\x05 \x01(\x08\",\n\rInputRoboUser\x12\x0c\n\x04Name\x18\x01 \x01(\t\x12\r\n\x05Group\x18\x02 \x01(\t\"S\n\x0eOutputRoboUser\x12\x0f\n\x07Success\x18\x01 \x01(\x08\x12\x0f\n\x07Message\x18\x02 \x01(\t\x12\x1f\n\x04\x44\x61ta\x18\x03 \x01(\x0b\x32\x11.packets.RoboUser\"\x80\x01\n\x18\x43heckoutRoboInstantInput\x12\x11\n\tProductID\x18\x01 \x01(\x03\x12\x0e\n\x06\x41mount\x18\x02 \x01(\x01\x12\x0c\n\x04Rate\x18\x03 \x01(\x01\x12\r\n\x05Month\x18\x04 \x01(\x03\x12\x14\n\x0cRolloverType\x18\x05 \x01(\t\x12\x0e\n\x06UserID\x18\x06 \x01(\x03\"R\n\x19\x43heckoutRoboInstantOutput\x12\x0f\n\x07Success\x18\x01 \x01(\x08\x12\x14\n\x0c\x45rrorMessage\x18\x02 \x01(\t\x12\x0e\n\x06\x43\x61rtID\x18\x03 \x01(\x03\"<\n\x19InputGetOrderRoboByUserID\x12\x0e\n\x06UserID\x18\x01 \x01(\x03\x12\x0f\n\x07OrderID\x18\x02 \x01(\x03\"T\n\x1aOutputGetOrderRoboByUserID\x12\x0f\n\x07Success\x18\x01 \x01(\x08\x12\x14\n\x0c\x45rrorMessage\x18\x02 \x01(\t\x12\x0f\n\x07OrderID\x18\x03 \x01(\x03\"\x15\n\x13InputListRoboUserID\"&\n\x14OutputListRoboUserID\x12\x0e\n\x06UserID\x18\x01 \x03(\x03\"?\n\"InputGetRoboBatchPerfomanceDetails\x12\x19\n\x11RoboBatchDetailID\x18\x01 \x01(\x03\"\xe7\x01\n#OutputGetRoboBatchPerfomanceDetails\x12\x19\n\x11RoboBatchDetailID\x18\x01 \x01(\x03\x12\x0e\n\x06UserID\x18\x02 \x01(\x03\x12\x11\n\tFundingID\x18\x03 \x01(\x03\x12\x0e\n\x06LoanID\x18\x04 \x01(\x03\x12\x0f\n\x07IsClear\x18\x05 \x01(\x08\x12\x11\n\tPrincipal\x18\x06 \x01(\x01\x12\x10\n\x08Interest\x18\x07 \x01(\x01\x12\x15\n\rOrderDetailID\x18\x08 \x01(\x03\x12\x11\n\tPphAmount\x18\t \x01(\x01\x12\x12\n\nTenureType\x18\n \x01(\t\"/\n\x16InputRoboDailyInterest\x12\x15\n\rOrderDetailID\x18\x01 \x01(\x03\"\x87\x01\n\x17OutputRoboDailyInterest\x12\x15\n\rFundingAmount\x18\x01 \x01(\x01\x12\x1f\n\x17\x43urrentExpectedInterest\x18\x02 \x01(\x01\x12\x1c\n\x14TotalCurrentInterest\x18\x03 \x01(\x01\x12\x16\n\x0eTotalPPHAmount\x18\x04 \x01(\x01\"A\n\x14InputRoboLoanDetails\x12\x19\n\x11RoboBatchDetailID\x18\x01 \x01(\x03\x12\x0e\n\x06UserID\x18\x02 \x01(\x03\"\x9f\x03\n\x15OutputRoboLoanDetails\x12\x13\n\x0bRoboBatchID\x18\x01 \x01(\x03\x12\x19\n\x11RoboBatchDetailID\x18\x02 \x01(\x03\x12\x0c\n\x04Name\x18\x03 \x01(\t\x12\x1b\n\x13TotalInvestedAmount\x18\x04 \x01(\x01\x12\x15\n\rAllocatedFund\x18\x05 \x01(\x01\x12\x0e\n\x06Tenure\x18\x06 \x01(\x03\x12\x0c\n\x04Rate\x18\x07 \x01(\x01\x12\x12\n\nIsRollover\x18\x08 \x01(\x08\x12\x17\n\x0fRolloverMessage\x18\t \x01(\t\x12\x1e\n\x16InterestCalculatedDays\x18\n \x01(\x03\x12\x12\n\nTenureType\x18\x0b \x01(\t\x12\x0f\n\x07\x42reakOn\x18\x0c \x01(\t\x12\x0f\n\x07\x44ueDate\x18\r \x01(\t\x12\x14\n\x0cStartingDate\x18\x0e \x01(\t\x12\x0b\n\x03Url\x18\x0f \x01(\t\x12\x13\n\x0bHasRollover\x18\x10 \x01(\x08\x12\x14\n\x0cRolloverType\x18\x11 \x01(\t\x12\x14\n\x0cLockRollover\x18\x12 \x01(\x08\x12\x0f\n\x07IsClear\x18\x13 \x01(\x08\"E\n\x1aRoboBorrowerDetailsListFor\x12\x19\n\x11RoboBatchDetailID\x18\x01 \x01(\x03\x12\x0c\n\x04page\x18\x02 \x01(\x03\"\x86\x01\n\x13RoboBorrowerDetails\x12\r\n\x05Grade\x18\x01 \x01(\t\x12\x0e\n\x06LoanID\x18\x02 \x01(\x03\x12\x13\n\x0bLoanProduct\x18\x03 \x01(\t\x12\x10\n\x08LoanCode\x18\x04 \x01(\t\x12)\n\x0f\x42orrowerPurpose\x18\x05 \x01(\x0b\x32\x10.packets.Purpose\")\n\x07Purpose\x12\x0f\n\x07Purpose\x18\x01 \x01(\t\x12\r\n\x05\x42\x61\x64ge\x18\x02 \x01(\t\"T\n\x1dOutputRoboBorrowerDetailsList\x12\x33\n\rRoboBorrowers\x18\x01 \x03(\x0b\x32\x1c.packets.RoboBorrowerDetails\"\xea\x01\n\x16InputListOfFundedRobos\x12\x0e\n\x06UserID\x18\x01 \x01(\x03\x12\r\n\x05Month\x18\x02 \x01(\x03\x12\x0c\n\x04Year\x18\x03 \x01(\x03\x12\x1c\n\x14IsSeeAllPeriodEnable\x18\x04 \x01(\x08\x12\x13\n\x0bProductType\x18\x05 \x03(\t\x12>\n\x0cTenureFilter\x18\x06 \x03(\x0b\x32(.packets.TenureFilterGetListOfFundedRobo\x12\x11\n\tIsOngoing\x18\x07 \x01(\t\x12\x0e\n\x06Offset\x18\x08 \x01(\x03\x12\r\n\x05Limit\x18\t \x01(\x03\"M\n\x1fTenureFilterGetListOfFundedRobo\x12\x14\n\x0cMinimumRange\x18\x01 \x01(\x03\x12\x14\n\x0cMaximumRange\x18\x02 \x01(\x03\"\xfa\x03\n\x15\x44\x61taListOfFundedRobos\x12\n\n\x02ID\x18\x01 \x01(\x03\x12\x15\n\rBatchDetailID\x18\x02 \x01(\x03\x12\x11\n\tFundingID\x18\x03 \x01(\x03\x12\x0c\n\x04Name\x18\x04 \x01(\t\x12\x10\n\x08LoanCode\x18\x05 \x01(\t\x12\x0f\n\x07IsClear\x18\x06 \x01(\x08\x12\x12\n\nLoanStatus\x18\x07 \x01(\t\x12\x11\n\tIconColor\x18\x08 \x01(\t\x12\x0f\n\x07IconUrl\x18\t \x01(\t\x12\x0e\n\x06Tenure\x18\n \x01(\x03\x12\x12\n\nTenureType\x18\x0b \x01(\t\x12\x0c\n\x04Rate\x18\x0c \x01(\x01\x12\x11\n\tExtraRate\x18\r \x01(\x01\x12\x0f\n\x07StartAt\x18\x0e \x01(\t\x12\x0f\n\x07\x44ueDate\x18\x0f \x01(\t\x12\x13\n\x0bHasRollover\x18\x10 \x01(\x08\x12\x19\n\x11IsRolloverProduct\x18\x11 \x01(\x08\x12\x14\n\x0cRolloverType\x18\x12 \x01(\t\x12\x17\n\x0fRolloverMessage\x18\x13 \x01(\t\x12\x14\n\x0cLockRollover\x18\x14 \x01(\x08\x12\x16\n\x0e\x41llocatedFunds\x18\x15 \x01(\x01\x12\x16\n\x0eInterestAmount\x18\x16 \x01(\x01\x12\x16\n\x0eTotalPPHAmount\x18\x17 \x01(\x01\x12\x0f\n\x07\x42reakOn\x18\x18 \x01(\t\x12\r\n\x05LAUrl\x18\x19 \x01(\t\"T\n\x17OutputListOfFundedRobos\x12\x39\n\x11ListOfFundedRobos\x18\x01 \x03(\x0b\x32\x1e.packets.DataListOfFundedRobos2\xb2\x07\n\x08KoinRobo\x12Q\n\x0eGetOrderDetail\x12\x1d.packets.InputRoboOrderDetail\x1a\x1e.packets.OutputRoboOrderDetail\"\x00\x12@\n\x0bGetRoboUser\x12\x16.packets.InputRoboUser\x1a\x17.packets.OutputRoboUser\"\x00\x12^\n\x13\x43heckoutRoboInstant\x12!.packets.CheckoutRoboInstantInput\x1a\".packets.CheckoutRoboInstantOutput\"\x00\x12\x61\n\x14GetOrderRoboByUserID\x12\".packets.InputGetOrderRoboByUserID\x1a#.packets.OutputGetOrderRoboByUserID\"\x00\x12R\n\x11GetListRoboUserID\x12\x1c.packets.InputListRoboUserID\x1a\x1d.packets.OutputListRoboUserID\"\x00\x12|\n\x1dGetRoboBatchPerfomanceDetails\x12+.packets.InputGetRoboBatchPerfomanceDetails\x1a,.packets.OutputGetRoboBatchPerfomanceDetails\"\x00\x12[\n\x14GetRoboDailyInterest\x12\x1f.packets.InputRoboDailyInterest\x1a .packets.OutputRoboDailyInterest\"\x00\x12U\n\x12GetRoboLoanDetails\x12\x1d.packets.InputRoboLoanDetails\x1a\x1e.packets.OutputRoboLoanDetails\"\x00\x12k\n\x1aGetRoboBorrowerDetailsList\x12#.packets.RoboBorrowerDetailsListFor\x1a&.packets.OutputRoboBorrowerDetailsList\"\x00\x12[\n\x14GetListOfFundedRobos\x12\x1f.packets.InputListOfFundedRobos\x1a .packets.OutputListOfFundedRobos\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'koinrobo_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_INPUTROBOORDERDETAIL']._serialized_start=54
  _globals['_INPUTROBOORDERDETAIL']._serialized_end=93
  _globals['_OUTPUTROBOORDERDETAIL']._serialized_start=95
  _globals['_OUTPUTROBOORDERDETAIL']._serialized_end=187
  _globals['_ROBOUSER']._serialized_start=189
  _globals['_ROBOUSER']._serialized_end=275
  _globals['_INPUTROBOUSER']._serialized_start=277
  _globals['_INPUTROBOUSER']._serialized_end=321
  _globals['_OUTPUTROBOUSER']._serialized_start=323
  _globals['_OUTPUTROBOUSER']._serialized_end=406
  _globals['_CHECKOUTROBOINSTANTINPUT']._serialized_start=409
  _globals['_CHECKOUTROBOINSTANTINPUT']._serialized_end=537
  _globals['_CHECKOUTROBOINSTANTOUTPUT']._serialized_start=539
  _globals['_CHECKOUTROBOINSTANTOUTPUT']._serialized_end=621
  _globals['_INPUTGETORDERROBOBYUSERID']._serialized_start=623
  _globals['_INPUTGETORDERROBOBYUSERID']._serialized_end=683
  _globals['_OUTPUTGETORDERROBOBYUSERID']._serialized_start=685
  _globals['_OUTPUTGETORDERROBOBYUSERID']._serialized_end=769
  _globals['_INPUTLISTROBOUSERID']._serialized_start=771
  _globals['_INPUTLISTROBOUSERID']._serialized_end=792
  _globals['_OUTPUTLISTROBOUSERID']._serialized_start=794
  _globals['_OUTPUTLISTROBOUSERID']._serialized_end=832
  _globals['_INPUTGETROBOBATCHPERFOMANCEDETAILS']._serialized_start=834
  _globals['_INPUTGETROBOBATCHPERFOMANCEDETAILS']._serialized_end=897
  _globals['_OUTPUTGETROBOBATCHPERFOMANCEDETAILS']._serialized_start=900
  _globals['_OUTPUTGETROBOBATCHPERFOMANCEDETAILS']._serialized_end=1131
  _globals['_INPUTROBODAILYINTEREST']._serialized_start=1133
  _globals['_INPUTROBODAILYINTEREST']._serialized_end=1180
  _globals['_OUTPUTROBODAILYINTEREST']._serialized_start=1183
  _globals['_OUTPUTROBODAILYINTEREST']._serialized_end=1318
  _globals['_INPUTROBOLOANDETAILS']._serialized_start=1320
  _globals['_INPUTROBOLOANDETAILS']._serialized_end=1385
  _globals['_OUTPUTROBOLOANDETAILS']._serialized_start=1388
  _globals['_OUTPUTROBOLOANDETAILS']._serialized_end=1803
  _globals['_ROBOBORROWERDETAILSLISTFOR']._serialized_start=1805
  _globals['_ROBOBORROWERDETAILSLISTFOR']._serialized_end=1874
  _globals['_ROBOBORROWERDETAILS']._serialized_start=1877
  _globals['_ROBOBORROWERDETAILS']._serialized_end=2011
  _globals['_PURPOSE']._serialized_start=2013
  _globals['_PURPOSE']._serialized_end=2054
  _globals['_OUTPUTROBOBORROWERDETAILSLIST']._serialized_start=2056
  _globals['_OUTPUTROBOBORROWERDETAILSLIST']._serialized_end=2140
  _globals['_INPUTLISTOFFUNDEDROBOS']._serialized_start=2143
  _globals['_INPUTLISTOFFUNDEDROBOS']._serialized_end=2377
  _globals['_TENUREFILTERGETLISTOFFUNDEDROBO']._serialized_start=2379
  _globals['_TENUREFILTERGETLISTOFFUNDEDROBO']._serialized_end=2456
  _globals['_DATALISTOFFUNDEDROBOS']._serialized_start=2459
  _globals['_DATALISTOFFUNDEDROBOS']._serialized_end=2965
  _globals['_OUTPUTLISTOFFUNDEDROBOS']._serialized_start=2967
  _globals['_OUTPUTLISTOFFUNDEDROBOS']._serialized_end=3051
  _globals['_KOINROBO']._serialized_start=3054
  _globals['_KOINROBO']._serialized_end=4000
# @@protoc_insertion_point(module_scope)
