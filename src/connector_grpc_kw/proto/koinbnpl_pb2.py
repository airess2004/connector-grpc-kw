# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: koinbnpl.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import common_pb2 as common__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0ekoinbnpl.proto\x12\x07packets\x1a\x0c\x63ommon.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x19google/protobuf/any.proto\"\xbf\x01\n\x1bUpsertVendorDetailArguments\x12\x0c\n\x04UUID\x18\x01 \x01(\t\x12>\n\x05\x44\x61tas\x18\x02 \x03(\x0b\x32/.packets.UpsertVendorDetailArguments.DatasEntry\x12\x12\n\nOperatedBy\x18\x03 \x01(\t\x1a>\n\nDatasEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1f\n\x05value\x18\x02 \x01(\x0b\x32\x10.packets.PObject:\x02\x38\x01\"7\n\x15GetBNPLLimitArguments\x12\x0e\n\x06UserID\x18\x01 \x01(\x03\x12\x0e\n\x06Status\x18\x02 \x03(\t\"\x88\x02\n\x12\x42NPLLimitResponses\x12 \n\x06Status\x18\x01 \x01(\x0b\x32\x10.packets.PStatus\x12\n\n\x02ID\x18\x02 \x01(\x03\x12\x0e\n\x06\x41mount\x18\x03 \x01(\x01\x12\x12\n\nFreeAmount\x18\x04 \x01(\x01\x12\x17\n\x0fRemainingAmount\x18\x05 \x01(\x01\x12\x15\n\rReserveAmount\x18\x06 \x01(\x01\x12-\n\tExpiredAt\x18\x07 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x12\n\nvendorUUID\x18\x08 \x01(\t\x12-\n\tCreatedAt\x18\t \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"O\n\x19ReserveBNPLLimitArguments\x12\x0e\n\x06UserID\x18\x01 \x01(\x03\x12\x0e\n\x06\x41mount\x18\x02 \x01(\x01\x12\x12\n\nOperatedBy\x18\x03 \x01(\t\"P\n\x1aRollbackBNPLLimitArguments\x12\x0e\n\x06UserID\x18\x01 \x01(\x03\x12\x0e\n\x06\x41mount\x18\x02 \x01(\x01\x12\x12\n\nOperatedBy\x18\x03 \x01(\t\"_\n\x15UseBNPLLimitArguments\x12\x0e\n\x06UserID\x18\x01 \x01(\x03\x12\x0e\n\x06\x41mount\x18\x02 \x01(\x01\x12\x12\n\nForceClaim\x18\x03 \x01(\t\x12\x12\n\nOperatedBy\x18\x04 \x01(\t\"O\n\x19ReleaseBNPLLimitArguments\x12\x0e\n\x06UserID\x18\x01 \x01(\x03\x12\x0e\n\x06\x41mount\x18\x02 \x01(\x01\x12\x12\n\nOperatedBy\x18\x03 \x01(\t\"2\n\"GetBNPLVendorDetailByUUIDArguments\x12\x0c\n\x04UUID\x18\x01 \x01(\t\"\xcf\x04\n\x19RequestBNPLLimitArguments\x12\r\n\x05Limit\x18\x01 \x01(\x01\x12\x39\n\x08Personal\x18\x02 \x01(\x0b\x32\'.packets.RequestBNPLLimitPersonalObject\x12\x39\n\x08\x42usiness\x18\x03 \x01(\x0b\x32\'.packets.RequestBNPLLimitBusinessObject\x12\x1d\n\x15\x46irstAccountCreatedAt\x18\x04 \x01(\t\x12P\n\x0fMonthlyRevenues\x18\x05 \x03(\x0b\x32\x37.packets.RequestBNPLLimitArguments.MonthlyRevenuesEntry\x12\x35\n\x06Vendor\x18\x06 \x01(\x0b\x32%.packets.RequestBNPLLimitVendorObject\x12\x12\n\nOperatedBy\x18\x07 \x01(\t\x12\x10\n\x08\x43lientID\x18\x08 \x01(\t\x12\x11\n\tUserAgent\x18\t \x01(\t\x12X\n\x13MonthlyTransactions\x18\n \x03(\x0b\x32;.packets.RequestBNPLLimitArguments.MonthlyTransactionsEntry\x1a\x36\n\x14MonthlyRevenuesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01:\x02\x38\x01\x1a:\n\x18MonthlyTransactionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x01:\x02\x38\x01\"\x96\x01\n\x1cRequestBNPLLimitVendorObject\x12\n\n\x02ID\x18\x01 \x01(\x03\x12\x0c\n\x04UUID\x18\x02 \x01(\t\x12\x0c\n\x04\x43ode\x18\x03 \x01(\t\x12\x0c\n\x04Name\x18\x04 \x01(\t\x12\x30\n\x0cRegisteredAt\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06Status\x18\x06 \x01(\t\"\xeb\x03\n\x1eRequestBNPLLimitPersonalObject\x12\x10\n\x08\x46ullname\x18\x01 \x01(\t\x12\x0b\n\x03NIK\x18\x02 \x01(\t\x12\x10\n\x08KtpImage\x18\x03 \x01(\t\x12\x16\n\x0eKtpSelfieImage\x18\x04 \x01(\t\x12\x17\n\x0f\x46\x61milyCardImage\x18\x05 \x01(\t\x12\x0e\n\x06Gender\x18\x06 \x01(\t\x12\x14\n\x0cPlaceOfBirth\x18\x07 \x01(\t\x12\x13\n\x0b\x44\x61teOfBirth\x18\x08 \x01(\t\x12\x15\n\rMaritalStatus\x18\t \x01(\t\x12\x10\n\x08Religion\x18\n \x01(\t\x12\x11\n\tEducation\x18\x0b \x01(\t\x12\x12\n\nOccupation\x18\x0c \x01(\t\x12\x18\n\x10TotalOtherIncome\x18\r \x01(\t\x12\x1b\n\x13OtherSourceOfIncome\x18\x0e \x01(\t\x12\x11\n\tNetSalary\x18\x0f \x01(\x01\x12\x12\n\nMyPosition\x18\x10 \x01(\t\x12?\n\x07\x41\x64\x64ress\x18\x11 \x01(\x0b\x32..packets.RequestBNPLLimitPersonalAddressObject\x12=\n\x06Spouse\x18\x12 \x01(\x0b\x32-.packets.RequestBNPLLimitPersonalSpouseObject\"\xee\x01\n%RequestBNPLLimitPersonalAddressObject\x12\x0f\n\x07\x41\x64\x64ress\x18\x01 \x01(\t\x12\x12\n\nPostalCode\x18\x02 \x01(\t\x12\x13\n\x0bSubDistrict\x18\x03 \x01(\t\x12\x10\n\x08\x44istrict\x18\x04 \x01(\t\x12\x0c\n\x04\x43ity\x18\x05 \x01(\t\x12\x10\n\x08Province\x18\x06 \x01(\t\x12\x0f\n\x07\x43ountry\x18\x07 \x01(\t\x12\x13\n\x0bHasLiveHere\x18\x08 \x01(\x08\x12\x1b\n\x13HomeOwnershipStatus\x18\t \x01(\t\x12\x16\n\x0e\x44urationOfStay\x18\n \x01(\t\"\xb3\x01\n$RequestBNPLLimitPersonalSpouseObject\x12 \n\x18RelationshipWithBorrower\x18\x01 \x01(\t\x12\x0e\n\x06KtpNIK\x18\x02 \x01(\t\x12\x10\n\x08KtpImage\x18\x03 \x01(\t\x12\x10\n\x08\x46ullname\x18\x04 \x01(\t\x12\x11\n\tPhoneArea\x18\x05 \x01(\t\x12\x13\n\x0bPhoneNumber\x18\x06 \x01(\t\x12\r\n\x05\x45mail\x18\x07 \x01(\t\"\xbf\x03\n\x1eRequestBNPLLimitBusinessObject\x12\x0c\n\x04Type\x18\x01 \x01(\t\x12\x0c\n\x04Name\x18\x02 \x01(\t\x12\x13\n\x0b\x44\x65scription\x18\x03 \x01(\t\x12\x0f\n\x07Website\x18\x04 \x01(\t\x12\r\n\x05\x45mail\x18\x05 \x01(\t\x12\x11\n\tPhoneArea\x18\x06 \x01(\t\x12\x13\n\x0bPhoneNumber\x18\x07 \x01(\t\x12\x15\n\rOwnerFullname\x18\x08 \x01(\t\x12\x11\n\tNpwpImage\x18\t \x01(\t\x12\x14\n\x0cLicenseImage\x18\n \x01(\t\x12\x14\n\x0c\x41verageSales\x18\x0b \x01(\x01\x12\x14\n\x0c\x45stablisedIn\x18\x0c \x01(\t\x12\x18\n\x10NumberOfEmployee\x18\r \x01(\t\x12\x1a\n\x12\x42\x61nkStatementImage\x18\x0e \x01(\t\x12\x1b\n\x13OwnershipPercentage\x18\x0f \x01(\x01\x12\x10\n\x08\x43\x61tegory\x18\x10 \x01(\t\x12?\n\x07\x41\x64\x64ress\x18\x11 \x01(\x0b\x32..packets.RequestBNPLLimitBusinessAddressObject\x12\x12\n\nSiupNumber\x18\x12 \x01(\t\"s\n%RequestBNPLLimitBusinessAddressObject\x12\x0f\n\x07\x41\x64\x64ress\x18\x01 \x01(\t\x12\x12\n\nPostalCode\x18\x02 \x01(\t\x12\x13\n\x0bSubDistrict\x18\x03 \x01(\t\x12\x10\n\x08\x44istrict\x18\x04 \x01(\t\"(\n\x16GetLoanDetailsArgument\x12\x0e\n\x06LoanID\x18\x01 \x01(\x03\"7\n\x15GetDistributorRequest\x12\n\n\x02ID\x18\x01 \x01(\x03\x12\x12\n\nVendorUUID\x18\x02 \x01(\t\"\xb7\x01\n\x0b\x44istributor\x12\n\n\x02ID\x18\x01 \x01(\x03\x12\x0c\n\x04Name\x18\x02 \x01(\t\x12\x13\n\x0bPhoneNumber\x18\x03 \x01(\t\x12\r\n\x05\x45mail\x18\x04 \x01(\t\x12\x10\n\x08\x42\x61nkName\x18\x05 \x01(\t\x12\x10\n\x08\x42\x61nkCode\x18\x06 \x01(\t\x12\x12\n\nBankBranch\x18\x07 \x01(\t\x12\x17\n\x0f\x42\x61nkAccountName\x18\x08 \x01(\t\x12\x19\n\x11\x42\x61nkAccountNumber\x18\t \x01(\t2\xbd\x06\n\x08Koinbnpl\x12U\n\x12UpsertVendorDetail\x12$.packets.UpsertVendorDetailArguments\x1a\x17.packets.PViewResponses\"\x00\x12I\n\x08GetLimit\x12\x1e.packets.GetBNPLLimitArguments\x1a\x1b.packets.BNPLLimitResponses\"\x00\x12_\n\x15GetVendorDetailByUUID\x12+.packets.GetBNPLVendorDetailByUUIDArguments\x1a\x17.packets.PViewResponses\"\x00\x12Q\n\x0cReserveLimit\x12\".packets.ReserveBNPLLimitArguments\x1a\x1b.packets.BNPLLimitResponses\"\x00\x12S\n\rRollbackLimit\x12#.packets.RollbackBNPLLimitArguments\x1a\x1b.packets.BNPLLimitResponses\"\x00\x12I\n\x08UseLimit\x12\x1e.packets.UseBNPLLimitArguments\x1a\x1b.packets.BNPLLimitResponses\"\x00\x12Q\n\x0cReleaseLimit\x12\".packets.ReleaseBNPLLimitArguments\x1a\x1b.packets.BNPLLimitResponses\"\x00\x12Q\n\x0cRequestLimit\x12\".packets.RequestBNPLLimitArguments\x1a\x1b.packets.BNPLLimitResponses\"\x00\x12K\n\rGetLoanDetail\x12\x1f.packets.GetLoanDetailsArgument\x1a\x17.packets.PViewResponses\"\x00\x12H\n\x0eGetDistributor\x12\x1e.packets.GetDistributorRequest\x1a\x14.packets.Distributor\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'koinbnpl_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _UPSERTVENDORDETAILARGUMENTS_DATASENTRY._options = None
  _UPSERTVENDORDETAILARGUMENTS_DATASENTRY._serialized_options = b'8\001'
  _REQUESTBNPLLIMITARGUMENTS_MONTHLYREVENUESENTRY._options = None
  _REQUESTBNPLLIMITARGUMENTS_MONTHLYREVENUESENTRY._serialized_options = b'8\001'
  _REQUESTBNPLLIMITARGUMENTS_MONTHLYTRANSACTIONSENTRY._options = None
  _REQUESTBNPLLIMITARGUMENTS_MONTHLYTRANSACTIONSENTRY._serialized_options = b'8\001'
  _globals['_UPSERTVENDORDETAILARGUMENTS']._serialized_start=102
  _globals['_UPSERTVENDORDETAILARGUMENTS']._serialized_end=293
  _globals['_UPSERTVENDORDETAILARGUMENTS_DATASENTRY']._serialized_start=231
  _globals['_UPSERTVENDORDETAILARGUMENTS_DATASENTRY']._serialized_end=293
  _globals['_GETBNPLLIMITARGUMENTS']._serialized_start=295
  _globals['_GETBNPLLIMITARGUMENTS']._serialized_end=350
  _globals['_BNPLLIMITRESPONSES']._serialized_start=353
  _globals['_BNPLLIMITRESPONSES']._serialized_end=617
  _globals['_RESERVEBNPLLIMITARGUMENTS']._serialized_start=619
  _globals['_RESERVEBNPLLIMITARGUMENTS']._serialized_end=698
  _globals['_ROLLBACKBNPLLIMITARGUMENTS']._serialized_start=700
  _globals['_ROLLBACKBNPLLIMITARGUMENTS']._serialized_end=780
  _globals['_USEBNPLLIMITARGUMENTS']._serialized_start=782
  _globals['_USEBNPLLIMITARGUMENTS']._serialized_end=877
  _globals['_RELEASEBNPLLIMITARGUMENTS']._serialized_start=879
  _globals['_RELEASEBNPLLIMITARGUMENTS']._serialized_end=958
  _globals['_GETBNPLVENDORDETAILBYUUIDARGUMENTS']._serialized_start=960
  _globals['_GETBNPLVENDORDETAILBYUUIDARGUMENTS']._serialized_end=1010
  _globals['_REQUESTBNPLLIMITARGUMENTS']._serialized_start=1013
  _globals['_REQUESTBNPLLIMITARGUMENTS']._serialized_end=1604
  _globals['_REQUESTBNPLLIMITARGUMENTS_MONTHLYREVENUESENTRY']._serialized_start=1490
  _globals['_REQUESTBNPLLIMITARGUMENTS_MONTHLYREVENUESENTRY']._serialized_end=1544
  _globals['_REQUESTBNPLLIMITARGUMENTS_MONTHLYTRANSACTIONSENTRY']._serialized_start=1546
  _globals['_REQUESTBNPLLIMITARGUMENTS_MONTHLYTRANSACTIONSENTRY']._serialized_end=1604
  _globals['_REQUESTBNPLLIMITVENDOROBJECT']._serialized_start=1607
  _globals['_REQUESTBNPLLIMITVENDOROBJECT']._serialized_end=1757
  _globals['_REQUESTBNPLLIMITPERSONALOBJECT']._serialized_start=1760
  _globals['_REQUESTBNPLLIMITPERSONALOBJECT']._serialized_end=2251
  _globals['_REQUESTBNPLLIMITPERSONALADDRESSOBJECT']._serialized_start=2254
  _globals['_REQUESTBNPLLIMITPERSONALADDRESSOBJECT']._serialized_end=2492
  _globals['_REQUESTBNPLLIMITPERSONALSPOUSEOBJECT']._serialized_start=2495
  _globals['_REQUESTBNPLLIMITPERSONALSPOUSEOBJECT']._serialized_end=2674
  _globals['_REQUESTBNPLLIMITBUSINESSOBJECT']._serialized_start=2677
  _globals['_REQUESTBNPLLIMITBUSINESSOBJECT']._serialized_end=3124
  _globals['_REQUESTBNPLLIMITBUSINESSADDRESSOBJECT']._serialized_start=3126
  _globals['_REQUESTBNPLLIMITBUSINESSADDRESSOBJECT']._serialized_end=3241
  _globals['_GETLOANDETAILSARGUMENT']._serialized_start=3243
  _globals['_GETLOANDETAILSARGUMENT']._serialized_end=3283
  _globals['_GETDISTRIBUTORREQUEST']._serialized_start=3285
  _globals['_GETDISTRIBUTORREQUEST']._serialized_end=3340
  _globals['_DISTRIBUTOR']._serialized_start=3343
  _globals['_DISTRIBUTOR']._serialized_end=3526
  _globals['_KOINBNPL']._serialized_start=3529
  _globals['_KOINBNPL']._serialized_end=4358
# @@protoc_insertion_point(module_scope)
