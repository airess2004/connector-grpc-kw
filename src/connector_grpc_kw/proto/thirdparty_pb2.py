# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: thirdparty.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from . import common_pb2 as common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10thirdparty.proto\x12\x07packets\x1a\x19google/protobuf/any.proto\x1a\x0c\x63ommon.proto\"\x84\x01\n\x16InputGetUCLPefindoData\x12\x11\n\tBirthDate\x18\x01 \x01(\t\x12\x10\n\x08\x46ullname\x18\x02 \x01(\t\x12\x0b\n\x03NIK\x18\x03 \x01(\t\x12\x0e\n\x06UserID\x18\x04 \x01(\x03\x12\x15\n\rAverageIncome\x18\x05 \x01(\x01\x12\x11\n\tIsPartner\x18\x06 \x01(\x08\"^\n\x17OutputGetUCLPefindoData\x12\x0e\n\x06Status\x18\x01 \x01(\x05\x12\x0f\n\x07Message\x18\x02 \x01(\t\x12\"\n\x04\x44\x61ta\x18\x03 \x01(\x0b\x32\x14.google.protobuf.Any\"\xd1\x01\n\x12InputGetFraudscore\x12\x0e\n\x06KtpUri\x18\x01 \x01(\t\x12\x11\n\tSelfieUri\x18\x02 \x01(\t\x12\x11\n\tUniqueKey\x18\x03 \x01(\t\x12\x13\n\x0bReferenceID\x18\x04 \x01(\x03\x12\x10\n\x08\x46ullName\x18\x05 \x01(\t\x12\x12\n\nNationalID\x18\x06 \x01(\t\x12\x13\n\x0b\x44\x61teOfBirth\x18\x07 \x01(\t\x12\x14\n\x0cPlaceOfBirth\x18\x08 \x01(\t\x12\x0f\n\x07\x41\x64\x64ress\x18\t \x01(\t\x12\x0e\n\x06Gender\x18\n \x01(\t\"Z\n\x13OutputGetFraudscore\x12\x0e\n\x06Status\x18\x01 \x01(\x05\x12\x0f\n\x07Message\x18\x02 \x01(\t\x12\"\n\x04\x44\x61ta\x18\x03 \x01(\x0b\x32\x14.google.protobuf.Any\"\x96\x01\n\x16InputGetPefindoSummary\x12\x11\n\tPefindoID\x18\x01 \x01(\t\x12\x10\n\x08\x46ullName\x18\x02 \x01(\t\x12\x13\n\x0b\x42irthOfDate\x18\x03 \x01(\t\x12\x0b\n\x03NIK\x18\x04 \x01(\t\x12\x12\n\nSearchType\x18\x05 \x01(\t\x12\x0c\n\x04NPWP\x18\x06 \x01(\t\x12\x13\n\x0bPefindoType\x18\x07 \x01(\t\"W\n\x10OutputThirdParty\x12\x0e\n\x06Status\x18\x01 \x01(\x05\x12\x0f\n\x07Message\x18\x02 \x01(\t\x12\"\n\x04\x44\x61ta\x18\x03 \x01(\x0b\x32\x14.google.protobuf.Any\"F\n\x10OutputExecAsliRI\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\"\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any\"W\n\x0fInputExecAsliRI\x12\x0e\n\x06UserID\x18\x01 \x01(\x03\x12$\n\x06Params\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x0e\n\x06\x41\x63tion\x18\x03 \x01(\t\"/\n\x1dInputDigiSignBorrowerRegister\x12\x0e\n\x06LoanID\x18\x01 \x01(\x03\"T\n\x1eOutputDigiSignBorrowerRegister\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\"\n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any\"\x99\x01\n\x15InputGetPefindoResult\x12\x0c\n\x04Type\x18\x01 \x01(\t\x12\x12\n\nDocumentNo\x18\x02 \x01(\t\x12\x10\n\x08\x46ullName\x18\x03 \x01(\t\x12\x0f\n\x07\x41\x64\x64ress\x18\x04 \x01(\t\x12\x11\n\tBirthDate\x18\x05 \x01(\t\x12\x0e\n\x06LoanID\x18\x06 \x01(\x03\x12\x18\n\x10MotherMaidenName\x18\x07 \x01(\t\"T\n\x16OutputGetPefindoResult\x12\x0e\n\x06Status\x18\x01 \x01(\x05\x12*\n\x04\x44\x61ta\x18\x02 \x03(\x0b\x32\x1c.packets.PefindoResultReport\":\n\x13PefindoResultReport\x12\x11\n\tPefindoID\x18\x01 \x01(\x03\x12\x10\n\x08Response\x18\x02 \x01(\t\"5\n\x0fInputGetCountry\x12\x13\n\x0bKeywordName\x18\x01 \x01(\t\x12\r\n\x05Limit\x18\x02 \x01(\x05\"6\n\x10InputGetProvince\x12\x13\n\x0bKeywordName\x18\x01 \x01(\t\x12\r\n\x05Limit\x18\x02 \x01(\x05\"b\n\x0cInputGetCity\x12\n\n\x02ID\x18\x05 \x01(\x03\x12\x0c\n\x04\x43ode\x18\x04 \x01(\t\x12\x13\n\x0bKeywordName\x18\x02 \x01(\t\x12\x14\n\x0cProvinceCode\x18\x01 \x01(\t\x12\r\n\x05Limit\x18\x03 \x01(\x05\"H\n\x10InputGetDistrict\x12\x10\n\x08\x43ityCode\x18\x01 \x01(\t\x12\x13\n\x0bKeywordName\x18\x02 \x01(\t\x12\r\n\x05Limit\x18\x03 \x01(\x05\"O\n\x13InputGetSubDistrict\x12\x14\n\x0c\x44istrictCode\x18\x01 \x01(\t\x12\x13\n\x0bKeywordName\x18\x02 \x01(\t\x12\r\n\x05Limit\x18\x03 \x01(\x05\";\n\x12InputGetPostalCode\x12\x10\n\x08\x44istrict\x18\x01 \x01(\t\x12\x13\n\x0bSubDistrict\x18\x02 \x01(\t\"T\n&InputGetParentLocationFromProvinceName\x12\x14\n\x0cRemovePrefix\x18\x01 \x01(\x08\x12\x14\n\x0cProvinceName\x18\x02 \x01(\t\"L\n\"InputGetParentLocationFromCityName\x12\x14\n\x0cRemovePrefix\x18\x01 \x01(\x08\x12\x10\n\x08\x43ityName\x18\x02 \x01(\t\"T\n&InputGetParentLocationFromDistrictName\x12\x14\n\x0cRemovePrefix\x18\x01 \x01(\x08\x12\x14\n\x0c\x44istrictName\x18\x02 \x01(\t\"p\n)InputGetParentLocationFromSubDistrictName\x12\x14\n\x0cRemovePrefix\x18\x01 \x01(\x08\x12\x14\n\x0c\x44istrictName\x18\x02 \x01(\t\x12\x17\n\x0fSubDistrictName\x18\x03 \x01(\t\"E\n\x17InputCheckProvinceExist\x12\x14\n\x0cRemovePrefix\x18\x01 \x01(\x08\x12\x14\n\x0cProvinceName\x18\x02 \x01(\t\"=\n\x13InputCheckCityExist\x12\x14\n\x0cRemovePrefix\x18\x01 \x01(\x08\x12\x10\n\x08\x43ityName\x18\x02 \x01(\t\"E\n\x17InputCheckDistrictExist\x12\x14\n\x0cRemovePrefix\x18\x01 \x01(\x08\x12\x14\n\x0c\x44istrictName\x18\x02 \x01(\t\"a\n\x1aInputCheckSubDistrictExist\x12\x14\n\x0cRemovePrefix\x18\x01 \x01(\x08\x12\x14\n\x0c\x44istrictName\x18\x02 \x01(\t\x12\x17\n\x0fSubDistrictName\x18\x03 \x01(\t\",\n\x1aInputGetPefindoCalculation\x12\x0e\n\x06LoanID\x18\x01 \x01(\x03\"X\n\x1bOutputGetPefindoCalculation\x12\x0e\n\x06Status\x18\x01 \x01(\x05\x12)\n\x04\x44\x61ta\x18\x02 \x03(\x0b\x32\x1b.packets.PefindoCalculation\"V\n\x12PefindoCalculation\x12\x11\n\tPefindoID\x18\x01 \x01(\x03\x12\x17\n\x0fTotalObligation\x18\x02 \x01(\x01\x12\x14\n\x0cPefindoGrade\x18\x03 \x01(\t\"\xf0\x01\n\x1bParamCreatePolicyPasarPolis\x12\x0f\n\x07Product\x18\x01 \x01(\t\x12\x11\n\tPackageID\x18\x02 \x01(\t\x12\x16\n\x0e\x43ontractNumber\x18\x03 \x01(\t\x12\x0c\n\x04Name\x18\x04 \x01(\t\x12\x13\n\x0b\x44\x61teOfBirth\x18\x05 \x01(\t\x12\x0e\n\x06Gender\x18\x06 \x01(\t\x12\x0f\n\x07\x41\x64\x64ress\x18\x07 \x01(\t\x12\x0b\n\x03KTP\x18\x08 \x01(\t\x12\x17\n\x0f\x43reditStartDate\x18\t \x01(\t\x12\x15\n\rCreditDueDate\x18\n \x01(\t\x12\x14\n\x0c\x43reditAmount\x18\x0b \x01(\x03\"J\n\x10OutputPasarPolis\x12\x0e\n\x06Status\x18\x01 \x01(\x05\x12&\n\x08Response\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any\"M\n\x1fParamCancellationFlowPasarPolis\x12\x15\n\rExecutionDate\x18\x01 \x01(\t\x12\x13\n\x0bReferenceID\x18\x02 \x01(\t\"1\n\"ParamGettingPolicyStatusPasarPolis\x12\x0b\n\x03IDs\x18\x01 \x03(\t\"\xaf\x02\n\x17InputRevinitivScreening\x12\x14\n\x0c\x44ocumentType\x18\x01 \x01(\t\x12\x1c\n\x14IdentificationNumber\x18\x02 \x01(\t\x12\x0c\n\x04Name\x18\x03 \x01(\t\x12\x11\n\tGivenName\x18\x04 \x01(\t\x12\x10\n\x08LastName\x18\x05 \x01(\t\x12\x1b\n\x13\x43ountryPlaceOfBirth\x18\x06 \x01(\t\x12\x13\n\x0b\x44\x61teOfBirth\x18\x07 \x01(\t\x12\x0e\n\x06Gender\x18\x08 \x01(\t\x12\x0f\n\x07\x43ountry\x18\t \x01(\t\x12\x13\n\x0bNationality\x18\n \x01(\t\x12\x14\n\x0cIssuingState\x18\x0b \x01(\t\x12\x1b\n\x13PassportNationality\x18\x0c \x01(\t\x12\x12\n\nExpiryDate\x18\r \x01(\t\"O\n\x1c\x42\x61tchInputSendClevertapEvent\x12/\n\x05Items\x18\x01 \x03(\x0b\x32 .packets.InputSendClevertapEvent\"g\n\x17InputSendClevertapEvent\x12\x10\n\x08Identity\x18\x01 \x01(\t\x12\x11\n\tEventName\x18\x02 \x01(\t\x12\'\n\tEventData\x18\x03 \x01(\x0b\x32\x14.google.protobuf.Any\";\n\x18OutputSendClevertapEvent\x12\x0e\n\x06Status\x18\x01 \x01(\x05\x12\x0f\n\x07Message\x18\x02 \x01(\t\"[\n\"BatchInputSendClevertapProfileData\x12\x35\n\x05Items\x18\x01 \x03(\x0b\x32&.packets.InputSendClevertapProfileData\"\\\n\x1dInputSendClevertapProfileData\x12\x10\n\x08Identity\x18\x01 \x01(\t\x12)\n\x0bProfileData\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any\"A\n\x1eOutputSendClevertapProfileData\x12\x0e\n\x06Status\x18\x01 \x01(\x05\x12\x0f\n\x07Message\x18\x02 \x01(\t\"_\n\x15InputOyGetBankInquiry\x12\x15\n\rRecipientBank\x18\x01 \x01(\t\x12\x18\n\x10RecipientAccount\x18\x02 \x01(\t\x12\x15\n\rRecipientName\x18\x03 \x01(\t\"a\n\x16OutputOyGetBankInquiry\x12\x0e\n\x06Status\x18\x01 \x01(\x05\x12\x0f\n\x07Message\x18\x02 \x01(\t\x12&\n\x08Response\x18\x03 \x01(\x0b\x32\x14.google.protobuf.Any\"\xe1\x01\n\x17InputSendAppsFlyerEvent\x12\x0e\n\x06UserID\x18\x01 \x01(\x03\x12\x14\n\x0cPlatformType\x18\x02 \x01(\t\x12\x11\n\tEventName\x18\x03 \x01(\t\x12\x44\n\nEventValue\x18\x04 \x03(\x0b\x32\x30.packets.InputSendAppsFlyerEvent.EventValueEntry\x1aG\n\x0f\x45ventValueEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any:\x02\x38\x01\"7\n%InputGetMonthlyInstallmentOtherVendor\x12\x0e\n\x06UserID\x18\x01 \x01(\x03\"b\n&OutputGetMonthlyInstallmentOtherVendor\x12\x0e\n\x06Status\x18\x01 \x01(\x05\x12\x0f\n\x07Message\x18\x02 \x01(\t\x12\x17\n\x0fTotalObligation\x18\x03 \x01(\x01\"\xca\x01\n\x12NetsuiteItemObject\x12\x13\n\x0bReferenceID\x18\x01 \x01(\t\x12\x17\n\x0fReferenceUserID\x18\x02 \x01(\x03\x12\x12\n\nSyncMethod\x18\x03 \x01(\t\x12\x33\n\x04\x44\x61ta\x18\x04 \x03(\x0b\x32%.packets.NetsuiteItemObject.DataEntry\x1a=\n\tDataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1f\n\x05value\x18\x02 \x01(\x0b\x32\x10.packets.PObject:\x02\x38\x01\"\xfd\x01\n\x17SyncToNetsuiteArguments\x12\x0c\n\x04Type\x18\x01 \x01(\t\x12\x12\n\nSyncMethod\x18\x02 \x01(\t\x12*\n\x05Items\x18\x03 \x03(\x0b\x32\x1b.packets.NetsuiteItemObject\x12>\n\x07Options\x18\x04 \x03(\x0b\x32-.packets.SyncToNetsuiteArguments.OptionsEntry\x12\x12\n\nOperatedBy\x18\x05 \x01(\t\x1a@\n\x0cOptionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1f\n\x05value\x18\x02 \x01(\x0b\x32\x10.packets.PObject:\x02\x38\x01\"&\n\x12InputGetVendorByID\x12\x10\n\x08VendorID\x18\x01 \x01(\x03\"G\n\x13UpsertVendorRequest\x12\x0c\n\x04UUID\x18\x01 \x01(\t\x12\"\n\x04\x44\x61ta\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any\"(\n\x18GetVendorByUUIDArguments\x12\x0c\n\x04UUID\x18\x01 \x01(\t\"(\n\x18GetVendorByCodeArguments\x12\x0c\n\x04\x43ode\x18\x01 \x01(\t\"%\n\x14GetScopesByCodesArgs\x12\r\n\x05\x43odes\x18\x01 \x03(\t\"_\n\x18GetScopesByCodesReponses\x12\x0e\n\x06Status\x18\x01 \x01(\x05\x12\x0f\n\x07Message\x18\x02 \x01(\t\x12\"\n\x04\x44\x61ta\x18\x03 \x01(\x0b\x32\x14.google.protobuf.Any\";\n\x15\x41pplyVendorScopesArgs\x12\"\n\x04\x44\x61ta\x18\x01 \x01(\x0b\x32\x14.google.protobuf.Any\"=\n\x1a\x41pplyVendorScopesResponses\x12\x0e\n\x06Status\x18\x01 \x01(\x05\x12\x0f\n\x07Message\x18\x02 \x01(\t\"?\n\x19InputRevinitivScreeningV2\x12\"\n\x04\x44\x61ta\x18\x01 \x01(\x0b\x32\x14.google.protobuf.Any\"T\n\x1aInputGetMasterLocationList\x12\x13\n\x0bSubDistrict\x18\x01 \x01(\t\x12\x12\n\nPostalCode\x18\x02 \x01(\t\x12\r\n\x05Limit\x18\x03 \x01(\x05\"\xce\x03\n\x0cInputClikNAE\x12\x0e\n\x06UserID\x18\x01 \x01(\x03\x12\x10\n\x08\x46ullName\x18\x02 \x01(\t\x12\x11\n\tBirthDate\x18\x03 \x01(\t\x12\x12\n\nBirthPlace\x18\x04 \x01(\t\x12\x0e\n\x06Gender\x18\x05 \x01(\t\x12\x14\n\x0cIdentityType\x18\x06 \x01(\t\x12\x16\n\x0eIdentityNumber\x18\x07 \x01(\t\x12\x0f\n\x07\x41\x64\x64ress\x18\x08 \x01(\t\x12\x10\n\x08\x44istrict\x18\t \x01(\t\x12\x13\n\x0bSubDistrict\x18\n \x01(\t\x12\x10\n\x08\x43ityCode\x18\x0b \x01(\t\x12\x12\n\nPostalCode\x18\x0c \x01(\t\x12\x13\n\x0b\x43ountryCode\x18\r \x01(\t\x12\x13\n\x0bPhoneNumber\x18\x0e \x01(\t\x12\x16\n\x0eSubjectRefDate\x18\x0f \x01(\t\x12!\n\x19ProviderApplicationNumber\x18\x10 \x01(\x03\x12\x14\n\x0c\x43ontractCode\x18\x11 \x01(\t\x12\x1b\n\x13\x43ontractRequestDate\x18\x12 \x01(\t\x12\x19\n\x11\x41pplicationAmount\x18\x13 \x01(\t\x12\x15\n\rAgreementDate\x18\x14 \x01(\t\x12\x0f\n\x07\x44ueDate\x18\x15 \x01(\t\"f\n\rOutputClikNAE\x12\r\n\x05\x45rror\x18\x01 \x01(\x08\x12\"\n\x04\x44\x61ta\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any\x12\"\n\x04Meta\x18\x03 \x01(\x0b\x32\x14.google.protobuf.Any\"\xb8\x02\n\x0e\x46reshSalesDeal\x12\x13\n\x0bReferenceID\x18\x01 \x01(\x03\x12\x15\n\rReferenceType\x18\x02 \x01(\t\x12\x0e\n\x06\x41mount\x18\x03 \x01(\x01\x12\x0e\n\x06Vendor\x18\x04 \x01(\t\x12\x11\n\tApplyDate\x18\x05 \x01(\t\x12\x0c\n\x04\x43ode\x18\x06 \x01(\t\x12\x0f\n\x07Product\x18\x07 \x01(\t\x12\x12\n\nLastAction\x18\x08 \x01(\t\x12\x18\n\x10\x44isbursementTime\x18\t \x01(\t\x12\x14\n\x0c\x44ocumentNeed\x18\n \x01(\t\x12\x31\n\x08\x42orrower\x18\x0b \x01(\x0b\x32\x1f.packets.FreshSalesDealBorrower\x12\x31\n\nDealDetail\x18\x0c \x01(\x0b\x32\x1d.packets.FreshSalesDealDetail\"D\n\x16\x46reshSalesDealBorrower\x12\x0c\n\x04Name\x18\x01 \x01(\t\x12\r\n\x05Phone\x18\x02 \x01(\t\x12\r\n\x05\x45mail\x18\x03 \x01(\t\"[\n\x14\x46reshSalesDealDetail\x12\x10\n\x08Pipeline\x18\x01 \x01(\t\x12\r\n\x05Stage\x18\x02 \x01(\t\x12\x0e\n\x06Reason\x18\x03 \x01(\t\x12\x12\n\nClosedTime\x18\x04 \x01(\t\"\xe7\x01\n\x1aInsertMixpanelEventRequest\x12\x12\n\nevent_name\x18\x01 \x01(\t\x12\x13\n\x0b\x64istinct_id\x18\x02 \x01(\t\x12R\n\x10\x65vent_properties\x18\x03 \x03(\x0b\x32\x38.packets.InsertMixpanelEventRequest.EventPropertiesEntry\x1aL\n\x14\x45ventPropertiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any:\x02\x38\x01\"9\n\x1bInsertMixpanelEventResponse\x12\x1a\n\x12mixpanel_events_id\x18\x01 \x01(\x03\x32\xa8\x1d\n\nThirdparty\x12\x46\n\rExecuteAsliRI\x12\x18.packets.InputExecAsliRI\x1a\x19.packets.OutputExecAsliRI\"\x00\x12m\n\x18\x42orrowerRegisterDigiSign\x12&.packets.InputDigiSignBorrowerRegister\x1a\'.packets.OutputDigiSignBorrowerRegister\"\x00\x12U\n\x10GetPefindoResult\x12\x1e.packets.InputGetPefindoResult\x1a\x1f.packets.OutputGetPefindoResult\"\x00\x12Y\n\x15GetMasterLocationList\x12#.packets.InputGetMasterLocationList\x1a\x19.packets.OutputThirdParty\"\x00\x12\x43\n\nGetCountry\x12\x18.packets.InputGetCountry\x1a\x19.packets.OutputThirdParty\"\x00\x12\x45\n\x0bGetProvince\x12\x19.packets.InputGetProvince\x1a\x19.packets.OutputThirdParty\"\x00\x12=\n\x07GetCity\x12\x15.packets.InputGetCity\x1a\x19.packets.OutputThirdParty\"\x00\x12\x45\n\x0bGetDistrict\x12\x19.packets.InputGetDistrict\x1a\x19.packets.OutputThirdParty\"\x00\x12K\n\x0eGetSubDistrict\x12\x1c.packets.InputGetSubDistrict\x1a\x19.packets.OutputThirdParty\"\x00\x12I\n\rGetPostalCode\x12\x1b.packets.InputGetPostalCode\x1a\x19.packets.OutputThirdParty\"\x00\x12q\n!GetParentLocationFromProvinceName\x12/.packets.InputGetParentLocationFromProvinceName\x1a\x19.packets.OutputThirdParty\"\x00\x12i\n\x1dGetParentLocationFromCityName\x12+.packets.InputGetParentLocationFromCityName\x1a\x19.packets.OutputThirdParty\"\x00\x12q\n!GetParentLocationFromDistrictName\x12/.packets.InputGetParentLocationFromDistrictName\x1a\x19.packets.OutputThirdParty\"\x00\x12w\n$GetParentLocationFromSubDistrictName\x12\x32.packets.InputGetParentLocationFromSubDistrictName\x1a\x19.packets.OutputThirdParty\"\x00\x12S\n\x12\x43heckProvinceExist\x12 .packets.InputCheckProvinceExist\x1a\x19.packets.OutputThirdParty\"\x00\x12K\n\x0e\x43heckCityExist\x12\x1c.packets.InputCheckCityExist\x1a\x19.packets.OutputThirdParty\"\x00\x12S\n\x12\x43heckDistrictExist\x12 .packets.InputCheckDistrictExist\x1a\x19.packets.OutputThirdParty\"\x00\x12Y\n\x15\x43heckSubDistrictExist\x12#.packets.InputCheckSubDistrictExist\x1a\x19.packets.OutputThirdParty\"\x00\x12\x64\n\x15GetPefindoCalculation\x12#.packets.InputGetPefindoCalculation\x1a$.packets.OutputGetPefindoCalculation\"\x00\x12[\n\x16\x43reatePolicyPasarPolis\x12$.packets.ParamCreatePolicyPasarPolis\x1a\x19.packets.OutputPasarPolis\"\x00\x12\x63\n\x1a\x43\x61ncellationFlowPasarPolis\x12(.packets.ParamCancellationFlowPasarPolis\x1a\x19.packets.OutputPasarPolis\"\x00\x12i\n\x1dGettingPolicyStatusPasarPolis\x12+.packets.ParamGettingPolicyStatusPasarPolis\x1a\x19.packets.OutputPasarPolis\"\x00\x12S\n\x12RevinitivScreening\x12 .packets.InputRevinitivScreening\x1a\x19.packets.OutputThirdParty\"\x00\x12W\n\x14RevinitivScreeningV2\x12\".packets.InputRevinitivScreeningV2\x1a\x19.packets.OutputThirdParty\"\x00\x12`\n\x12SendClevertapEvent\x12%.packets.BatchInputSendClevertapEvent\x1a!.packets.OutputSendClevertapEvent\"\x00\x12r\n\x18SendClevertapProfileData\x12+.packets.BatchInputSendClevertapProfileData\x1a\'.packets.OutputSendClevertapProfileData\"\x00\x12U\n\x10OyGetBankInquiry\x12\x1e.packets.InputOyGetBankInquiry\x1a\x1f.packets.OutputOyGetBankInquiry\"\x00\x12S\n\x12SendAppsFlyerEvent\x12 .packets.InputSendAppsFlyerEvent\x1a\x19.packets.OutputThirdParty\"\x00\x12\x85\x01\n GetMonthlyInstallmentOtherVendor\x12..packets.InputGetMonthlyInstallmentOtherVendor\x1a/.packets.OutputGetMonthlyInstallmentOtherVendor\"\x00\x12M\n\x0eSyncToNetsuite\x12 .packets.SyncToNetsuiteArguments\x1a\x17.packets.PViewResponses\"\x00\x12X\n\x11GetUCLPefindoData\x12\x1f.packets.InputGetUCLPefindoData\x1a .packets.OutputGetUCLPefindoData\"\x00\x12L\n\rGetFraudScore\x12\x1b.packets.InputGetFraudscore\x1a\x1c.packets.OutputGetFraudscore\"\x00\x12Q\n\x11GetPefindoSummary\x12\x1f.packets.InputGetPefindoSummary\x1a\x19.packets.OutputThirdParty\"\x00\x12:\n\x07\x43likNAE\x12\x15.packets.InputClikNAE\x1a\x16.packets.OutputClikNAE\"\x00\x12I\n\rGetVendorByID\x12\x1b.packets.InputGetVendorByID\x1a\x19.packets.OutputThirdParty\"\x00\x12O\n\x0fGetVendorByUUID\x12!.packets.GetVendorByUUIDArguments\x1a\x17.packets.PViewResponses\"\x00\x12I\n\x0cUpsertVendor\x12\x1c.packets.UpsertVendorRequest\x1a\x19.packets.OutputThirdParty\"\x00\x12O\n\x0fGetVendorByCode\x12!.packets.GetVendorByCodeArguments\x1a\x17.packets.PViewResponses\"\x00\x12V\n\x10GetScopesByCodes\x12\x1d.packets.GetScopesByCodesArgs\x1a!.packets.GetScopesByCodesReponses\"\x00\x12Z\n\x11\x41pplyVendorScopes\x12\x1e.packets.ApplyVendorScopesArgs\x1a#.packets.ApplyVendorScopesResponses\"\x00\x12J\n\x14UpsertFreshSalesDeal\x12\x17.packets.FreshSalesDeal\x1a\x17.packets.FreshSalesDeal\"\x00\x12\x62\n\x13InsertMixpanelEvent\x12#.packets.InsertMixpanelEventRequest\x1a$.packets.InsertMixpanelEventResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'thirdparty_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _INPUTSENDAPPSFLYEREVENT_EVENTVALUEENTRY._options = None
  _INPUTSENDAPPSFLYEREVENT_EVENTVALUEENTRY._serialized_options = b'8\001'
  _NETSUITEITEMOBJECT_DATAENTRY._options = None
  _NETSUITEITEMOBJECT_DATAENTRY._serialized_options = b'8\001'
  _SYNCTONETSUITEARGUMENTS_OPTIONSENTRY._options = None
  _SYNCTONETSUITEARGUMENTS_OPTIONSENTRY._serialized_options = b'8\001'
  _INSERTMIXPANELEVENTREQUEST_EVENTPROPERTIESENTRY._options = None
  _INSERTMIXPANELEVENTREQUEST_EVENTPROPERTIESENTRY._serialized_options = b'8\001'
  _globals['_INPUTGETUCLPEFINDODATA']._serialized_start=71
  _globals['_INPUTGETUCLPEFINDODATA']._serialized_end=203
  _globals['_OUTPUTGETUCLPEFINDODATA']._serialized_start=205
  _globals['_OUTPUTGETUCLPEFINDODATA']._serialized_end=299
  _globals['_INPUTGETFRAUDSCORE']._serialized_start=302
  _globals['_INPUTGETFRAUDSCORE']._serialized_end=511
  _globals['_OUTPUTGETFRAUDSCORE']._serialized_start=513
  _globals['_OUTPUTGETFRAUDSCORE']._serialized_end=603
  _globals['_INPUTGETPEFINDOSUMMARY']._serialized_start=606
  _globals['_INPUTGETPEFINDOSUMMARY']._serialized_end=756
  _globals['_OUTPUTTHIRDPARTY']._serialized_start=758
  _globals['_OUTPUTTHIRDPARTY']._serialized_end=845
  _globals['_OUTPUTEXECASLIRI']._serialized_start=847
  _globals['_OUTPUTEXECASLIRI']._serialized_end=917
  _globals['_INPUTEXECASLIRI']._serialized_start=919
  _globals['_INPUTEXECASLIRI']._serialized_end=1006
  _globals['_INPUTDIGISIGNBORROWERREGISTER']._serialized_start=1008
  _globals['_INPUTDIGISIGNBORROWERREGISTER']._serialized_end=1055
  _globals['_OUTPUTDIGISIGNBORROWERREGISTER']._serialized_start=1057
  _globals['_OUTPUTDIGISIGNBORROWERREGISTER']._serialized_end=1141
  _globals['_INPUTGETPEFINDORESULT']._serialized_start=1144
  _globals['_INPUTGETPEFINDORESULT']._serialized_end=1297
  _globals['_OUTPUTGETPEFINDORESULT']._serialized_start=1299
  _globals['_OUTPUTGETPEFINDORESULT']._serialized_end=1383
  _globals['_PEFINDORESULTREPORT']._serialized_start=1385
  _globals['_PEFINDORESULTREPORT']._serialized_end=1443
  _globals['_INPUTGETCOUNTRY']._serialized_start=1445
  _globals['_INPUTGETCOUNTRY']._serialized_end=1498
  _globals['_INPUTGETPROVINCE']._serialized_start=1500
  _globals['_INPUTGETPROVINCE']._serialized_end=1554
  _globals['_INPUTGETCITY']._serialized_start=1556
  _globals['_INPUTGETCITY']._serialized_end=1654
  _globals['_INPUTGETDISTRICT']._serialized_start=1656
  _globals['_INPUTGETDISTRICT']._serialized_end=1728
  _globals['_INPUTGETSUBDISTRICT']._serialized_start=1730
  _globals['_INPUTGETSUBDISTRICT']._serialized_end=1809
  _globals['_INPUTGETPOSTALCODE']._serialized_start=1811
  _globals['_INPUTGETPOSTALCODE']._serialized_end=1870
  _globals['_INPUTGETPARENTLOCATIONFROMPROVINCENAME']._serialized_start=1872
  _globals['_INPUTGETPARENTLOCATIONFROMPROVINCENAME']._serialized_end=1956
  _globals['_INPUTGETPARENTLOCATIONFROMCITYNAME']._serialized_start=1958
  _globals['_INPUTGETPARENTLOCATIONFROMCITYNAME']._serialized_end=2034
  _globals['_INPUTGETPARENTLOCATIONFROMDISTRICTNAME']._serialized_start=2036
  _globals['_INPUTGETPARENTLOCATIONFROMDISTRICTNAME']._serialized_end=2120
  _globals['_INPUTGETPARENTLOCATIONFROMSUBDISTRICTNAME']._serialized_start=2122
  _globals['_INPUTGETPARENTLOCATIONFROMSUBDISTRICTNAME']._serialized_end=2234
  _globals['_INPUTCHECKPROVINCEEXIST']._serialized_start=2236
  _globals['_INPUTCHECKPROVINCEEXIST']._serialized_end=2305
  _globals['_INPUTCHECKCITYEXIST']._serialized_start=2307
  _globals['_INPUTCHECKCITYEXIST']._serialized_end=2368
  _globals['_INPUTCHECKDISTRICTEXIST']._serialized_start=2370
  _globals['_INPUTCHECKDISTRICTEXIST']._serialized_end=2439
  _globals['_INPUTCHECKSUBDISTRICTEXIST']._serialized_start=2441
  _globals['_INPUTCHECKSUBDISTRICTEXIST']._serialized_end=2538
  _globals['_INPUTGETPEFINDOCALCULATION']._serialized_start=2540
  _globals['_INPUTGETPEFINDOCALCULATION']._serialized_end=2584
  _globals['_OUTPUTGETPEFINDOCALCULATION']._serialized_start=2586
  _globals['_OUTPUTGETPEFINDOCALCULATION']._serialized_end=2674
  _globals['_PEFINDOCALCULATION']._serialized_start=2676
  _globals['_PEFINDOCALCULATION']._serialized_end=2762
  _globals['_PARAMCREATEPOLICYPASARPOLIS']._serialized_start=2765
  _globals['_PARAMCREATEPOLICYPASARPOLIS']._serialized_end=3005
  _globals['_OUTPUTPASARPOLIS']._serialized_start=3007
  _globals['_OUTPUTPASARPOLIS']._serialized_end=3081
  _globals['_PARAMCANCELLATIONFLOWPASARPOLIS']._serialized_start=3083
  _globals['_PARAMCANCELLATIONFLOWPASARPOLIS']._serialized_end=3160
  _globals['_PARAMGETTINGPOLICYSTATUSPASARPOLIS']._serialized_start=3162
  _globals['_PARAMGETTINGPOLICYSTATUSPASARPOLIS']._serialized_end=3211
  _globals['_INPUTREVINITIVSCREENING']._serialized_start=3214
  _globals['_INPUTREVINITIVSCREENING']._serialized_end=3517
  _globals['_BATCHINPUTSENDCLEVERTAPEVENT']._serialized_start=3519
  _globals['_BATCHINPUTSENDCLEVERTAPEVENT']._serialized_end=3598
  _globals['_INPUTSENDCLEVERTAPEVENT']._serialized_start=3600
  _globals['_INPUTSENDCLEVERTAPEVENT']._serialized_end=3703
  _globals['_OUTPUTSENDCLEVERTAPEVENT']._serialized_start=3705
  _globals['_OUTPUTSENDCLEVERTAPEVENT']._serialized_end=3764
  _globals['_BATCHINPUTSENDCLEVERTAPPROFILEDATA']._serialized_start=3766
  _globals['_BATCHINPUTSENDCLEVERTAPPROFILEDATA']._serialized_end=3857
  _globals['_INPUTSENDCLEVERTAPPROFILEDATA']._serialized_start=3859
  _globals['_INPUTSENDCLEVERTAPPROFILEDATA']._serialized_end=3951
  _globals['_OUTPUTSENDCLEVERTAPPROFILEDATA']._serialized_start=3953
  _globals['_OUTPUTSENDCLEVERTAPPROFILEDATA']._serialized_end=4018
  _globals['_INPUTOYGETBANKINQUIRY']._serialized_start=4020
  _globals['_INPUTOYGETBANKINQUIRY']._serialized_end=4115
  _globals['_OUTPUTOYGETBANKINQUIRY']._serialized_start=4117
  _globals['_OUTPUTOYGETBANKINQUIRY']._serialized_end=4214
  _globals['_INPUTSENDAPPSFLYEREVENT']._serialized_start=4217
  _globals['_INPUTSENDAPPSFLYEREVENT']._serialized_end=4442
  _globals['_INPUTSENDAPPSFLYEREVENT_EVENTVALUEENTRY']._serialized_start=4371
  _globals['_INPUTSENDAPPSFLYEREVENT_EVENTVALUEENTRY']._serialized_end=4442
  _globals['_INPUTGETMONTHLYINSTALLMENTOTHERVENDOR']._serialized_start=4444
  _globals['_INPUTGETMONTHLYINSTALLMENTOTHERVENDOR']._serialized_end=4499
  _globals['_OUTPUTGETMONTHLYINSTALLMENTOTHERVENDOR']._serialized_start=4501
  _globals['_OUTPUTGETMONTHLYINSTALLMENTOTHERVENDOR']._serialized_end=4599
  _globals['_NETSUITEITEMOBJECT']._serialized_start=4602
  _globals['_NETSUITEITEMOBJECT']._serialized_end=4804
  _globals['_NETSUITEITEMOBJECT_DATAENTRY']._serialized_start=4743
  _globals['_NETSUITEITEMOBJECT_DATAENTRY']._serialized_end=4804
  _globals['_SYNCTONETSUITEARGUMENTS']._serialized_start=4807
  _globals['_SYNCTONETSUITEARGUMENTS']._serialized_end=5060
  _globals['_SYNCTONETSUITEARGUMENTS_OPTIONSENTRY']._serialized_start=4996
  _globals['_SYNCTONETSUITEARGUMENTS_OPTIONSENTRY']._serialized_end=5060
  _globals['_INPUTGETVENDORBYID']._serialized_start=5062
  _globals['_INPUTGETVENDORBYID']._serialized_end=5100
  _globals['_UPSERTVENDORREQUEST']._serialized_start=5102
  _globals['_UPSERTVENDORREQUEST']._serialized_end=5173
  _globals['_GETVENDORBYUUIDARGUMENTS']._serialized_start=5175
  _globals['_GETVENDORBYUUIDARGUMENTS']._serialized_end=5215
  _globals['_GETVENDORBYCODEARGUMENTS']._serialized_start=5217
  _globals['_GETVENDORBYCODEARGUMENTS']._serialized_end=5257
  _globals['_GETSCOPESBYCODESARGS']._serialized_start=5259
  _globals['_GETSCOPESBYCODESARGS']._serialized_end=5296
  _globals['_GETSCOPESBYCODESREPONSES']._serialized_start=5298
  _globals['_GETSCOPESBYCODESREPONSES']._serialized_end=5393
  _globals['_APPLYVENDORSCOPESARGS']._serialized_start=5395
  _globals['_APPLYVENDORSCOPESARGS']._serialized_end=5454
  _globals['_APPLYVENDORSCOPESRESPONSES']._serialized_start=5456
  _globals['_APPLYVENDORSCOPESRESPONSES']._serialized_end=5517
  _globals['_INPUTREVINITIVSCREENINGV2']._serialized_start=5519
  _globals['_INPUTREVINITIVSCREENINGV2']._serialized_end=5582
  _globals['_INPUTGETMASTERLOCATIONLIST']._serialized_start=5584
  _globals['_INPUTGETMASTERLOCATIONLIST']._serialized_end=5668
  _globals['_INPUTCLIKNAE']._serialized_start=5671
  _globals['_INPUTCLIKNAE']._serialized_end=6133
  _globals['_OUTPUTCLIKNAE']._serialized_start=6135
  _globals['_OUTPUTCLIKNAE']._serialized_end=6237
  _globals['_FRESHSALESDEAL']._serialized_start=6240
  _globals['_FRESHSALESDEAL']._serialized_end=6552
  _globals['_FRESHSALESDEALBORROWER']._serialized_start=6554
  _globals['_FRESHSALESDEALBORROWER']._serialized_end=6622
  _globals['_FRESHSALESDEALDETAIL']._serialized_start=6624
  _globals['_FRESHSALESDEALDETAIL']._serialized_end=6715
  _globals['_INSERTMIXPANELEVENTREQUEST']._serialized_start=6718
  _globals['_INSERTMIXPANELEVENTREQUEST']._serialized_end=6949
  _globals['_INSERTMIXPANELEVENTREQUEST_EVENTPROPERTIESENTRY']._serialized_start=6873
  _globals['_INSERTMIXPANELEVENTREQUEST_EVENTPROPERTIESENTRY']._serialized_end=6949
  _globals['_INSERTMIXPANELEVENTRESPONSE']._serialized_start=6951
  _globals['_INSERTMIXPANELEVENTRESPONSE']._serialized_end=7008
  _globals['_THIRDPARTY']._serialized_start=7011
  _globals['_THIRDPARTY']._serialized_end=10763
# @@protoc_insertion_point(module_scope)