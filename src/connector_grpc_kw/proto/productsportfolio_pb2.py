# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: productsportfolio.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17productsportfolio.proto\x12\x07packets\"\xd4\x01\n\x1fLenderRepaymentSchedulesSummary\x12\x0e\n\x06UserID\x18\x01 \x01(\x03\x12\x0e\n\x06LoanID\x18\x02 \x01(\x03\x12\x11\n\tFundingID\x18\x03 \x01(\x03\x12\x1c\n\x14TotalPrincipalReturn\x18\x04 \x01(\x01\x12\x1b\n\x13TotalInterestReturn\x18\x05 \x01(\x01\x12\x17\n\x0fTotalLateReturn\x18\x06 \x01(\x01\x12\x17\n\x0fTotalCommission\x18\x07 \x01(\x01\x12\x11\n\tIsPrefund\x18\x08 \x01(\x08\"\xef\x01\n\x1dRoboPurchaseSuccessfulDetails\x12\x0e\n\x06UserID\x18\x01 \x01(\x03\x12\x0e\n\x06LoanID\x18\x02 \x01(\x03\x12\x11\n\tFundingID\x18\x03 \x01(\x03\x12\x13\n\x0bProductCode\x18\x04 \x01(\t\x12\x13\n\x0bProductType\x18\x05 \x01(\t\x12\x18\n\x10\x43\x61shFundedAmount\x18\x06 \x01(\x02\x12\x18\n\x10KoinFundedAmount\x18\x07 \x01(\x02\x12\x1e\n\x16TotalExpectedPrincipal\x18\x08 \x01(\x02\x12\x1d\n\x15TotalExpectedInterest\x18\t \x01(\x02\"8\n#UpdatePortfolioPostDisbursementResp\x12\x11\n\tIsSuccess\x18\x01 \x01(\x08\"^\n\x19PurchaseSuccessfulSummary\x12\x0e\n\x06UserID\x18\x01 \x01(\x03\x12\x31\n\x0fPurchaseDetails\x18\x02 \x03(\x0b\x32\x18.packets.PurchaseDetails\"\xa5\x01\n\x0fPurchaseDetails\x12\x0e\n\x06LoanID\x18\x01 \x01(\x03\x12\x13\n\x0bProductCode\x18\x02 \x01(\t\x12\x13\n\x0bProductType\x18\x03 \x01(\t\x12\x18\n\x10\x43\x61shFundedAmount\x18\x04 \x01(\x01\x12\x18\n\x10KoinFundedAmount\x18\x05 \x01(\x01\x12\x11\n\tFundingID\x18\x06 \x01(\x03\x12\x11\n\tIsPrefund\x18\x07 \x01(\x08\"6\n!CreateOrUpdatePortfolioPostStatus\x12\x11\n\tIsSuccess\x18\x01 \x01(\x08\"j\n\x1bLenderOrderCancelledDetails\x12\x0e\n\x06UserID\x18\x01 \x01(\x03\x12\x13\n\x0bProductCode\x18\x02 \x01(\t\x12\x12\n\nCashAmount\x18\x03 \x01(\x01\x12\x12\n\nKoinAmount\x18\x04 \x01(\x01\"(\n\x13PortfolioUpdateResp\x12\x11\n\tIsSuccess\x18\x01 \x01(\x08\"B\n\x1eLoanCancelledByBorrowerDetails\x12\x0e\n\x06LoanID\x18\x01 \x01(\x03\x12\x10\n\x08LoanCode\x18\x02 \x01(\t\"5\n\x0eNLPLoanDetails\x12\x0e\n\x06LoanID\x18\x01 \x01(\x03\x12\x13\n\x0bProductCode\x18\x02 \x01(\t\"U\n\x1dProvisionFundSpreadingDetails\x12\x0e\n\x06LoanID\x18\x01 \x01(\x03\x12\x13\n\x0bProductCode\x18\x02 \x01(\t\x12\x0f\n\x07UserIds\x18\x03 \x03(\x03\";\n\x14PortfolioLoanDetails\x12\x0e\n\x06UserID\x18\x01 \x01(\x03\x12\x13\n\x0bProductCode\x18\x02 \x01(\t\"\xfd\x04\n\x10PortfolioDetails\x12\x13\n\x0bPortfolioID\x18\x01 \x01(\x03\x12\x0e\n\x06UserID\x18\x02 \x01(\x03\x12\x0e\n\x06LoanID\x18\x03 \x01(\x03\x12\x13\n\x0bProductCode\x18\x04 \x01(\t\x12\x11\n\tFundingID\x18\x05 \x01(\x03\x12\x13\n\x0bProductType\x18\x06 \x01(\t\x12\x18\n\x10\x43\x61shFundedAmount\x18\x07 \x01(\x01\x12\x18\n\x10KoinFundedAmount\x18\x08 \x01(\x01\x12\x1e\n\x16TotalExpectedPrincipal\x18\t \x01(\x01\x12\x1d\n\x15TotalExpectedInterest\x18\n \x01(\x01\x12\x19\n\x11TotalExpectedLate\x18\x0b \x01(\x01\x12\x1f\n\x17TotalExpectedCommission\x18\x0c \x01(\x01\x12\"\n\x1aTotalPrincipalCashReceived\x18\r \x01(\x01\x12\"\n\x1aTotalPrincipalKoinReceived\x18\x0e \x01(\x01\x12\x1d\n\x15TotalInterestReceived\x18\x0f \x01(\x01\x12\x19\n\x11TotalLateReceived\x18\x10 \x01(\x01\x12\x1f\n\x17TotalDeductedCommission\x18\x11 \x01(\x01\x12\x1c\n\x14TotalLatePreDeducted\x18\x12 \x01(\x01\x12\x17\n\x0fPortfolioStatus\x18\x13 \x01(\t\x12\x19\n\x11RestructureStatus\x18\x14 \x01(\t\x12\x11\n\tIsPrefund\x18\x15 \x01(\x08\x12\x1a\n\x12LenderAgreementURL\x18\x16 \x01(\t\x12\x11\n\tPPNAmount\x18\x17 \x01(\x01\x12\x11\n\tPPHAmount\x18\x18 \x01(\x01\"I\n\x14PortfolioDetailsResp\x12\x31\n\x0eProductDetails\x18\x01 \x03(\x0b\x32\x19.packets.PortfolioDetails\"B\n\x1d\x45xistencePortfolioUsersParams\x12\x0f\n\x07UserIDs\x18\x01 \x03(\x03\x12\x10\n\x08LoanCode\x18\x02 \x01(\t\".\n\x1b\x45xistencePortfolioUsersResp\x12\x0f\n\x07UserIDs\x18\x01 \x03(\x03\"1\n\x1fPortfolioAccountValueInputParam\x12\x0e\n\x06UserID\x18\x01 \x01(\x03\"\x82\x01\n\x1cPortfolioAccountValueDetails\x12\x1e\n\x16TotalExpectedPrincipal\x18\x01 \x01(\x01\x12\x1e\n\x16TotalReceivedPrincipal\x18\x02 \x01(\x01\x12\"\n\x1aTotalPortfolioAccountValue\x18\x03 \x01(\x01\x32\xa4\t\n\x11ProductsPortfolio\x12{\n\x1fUpdatePortfolioPostDisbursement\x12(.packets.LenderRepaymentSchedulesSummary\x1a,.packets.UpdatePortfolioPostDisbursementResp\"\x00\x12\x81\x01\n-CreateOrUpdatePortfolioPostSuccessfulPurchase\x12\".packets.PurchaseSuccessfulSummary\x1a*.packets.CreateOrUpdatePortfolioPostStatus\"\x00\x12o\n\'UpdatePortfolioWhenLenderOrderCancelled\x12$.packets.LenderOrderCancelledDetails\x1a\x1c.packets.PortfolioUpdateResp\"\x00\x12u\n*UpdatePortfolioWhenLoanCancelledByBorrower\x12\'.packets.LoanCancelledByBorrowerDetails\x1a\x1c.packets.PortfolioUpdateResp\"\x00\x12\\\n!UpdatePortfolioWhenLoanBecomesNPL\x12\x17.packets.NLPLoanDetails\x1a\x1c.packets.PortfolioUpdateResp\"\x00\x12\x84\x01\n:UpdatePortfolioWhenProvisionFundSpreadToLenderSuccessfully\x12&.packets.ProvisionFundSpreadingDetails\x1a\x1c.packets.PortfolioUpdateResp\"\x00\x12{\n1CreateOrUpdatePortfolioPostRoboPurchaseSuccessful\x12&.packets.RoboPurchaseSuccessfulDetails\x1a\x1c.packets.PortfolioUpdateResp\"\x00\x12`\n\x1eGetPortfolioForUserAndLoanCode\x12\x1d.packets.PortfolioLoanDetails\x1a\x1d.packets.PortfolioDetailsResp\"\x00\x12l\n\x1aGetExistencePortfolioUsers\x12&.packets.ExistencePortfolioUsersParams\x1a$.packets.ExistencePortfolioUsersResp\"\x00\x12t\n\x1fGetPortfolioAccountValueForUser\x12(.packets.PortfolioAccountValueInputParam\x1a%.packets.PortfolioAccountValueDetails\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'productsportfolio_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_LENDERREPAYMENTSCHEDULESSUMMARY']._serialized_start=37
  _globals['_LENDERREPAYMENTSCHEDULESSUMMARY']._serialized_end=249
  _globals['_ROBOPURCHASESUCCESSFULDETAILS']._serialized_start=252
  _globals['_ROBOPURCHASESUCCESSFULDETAILS']._serialized_end=491
  _globals['_UPDATEPORTFOLIOPOSTDISBURSEMENTRESP']._serialized_start=493
  _globals['_UPDATEPORTFOLIOPOSTDISBURSEMENTRESP']._serialized_end=549
  _globals['_PURCHASESUCCESSFULSUMMARY']._serialized_start=551
  _globals['_PURCHASESUCCESSFULSUMMARY']._serialized_end=645
  _globals['_PURCHASEDETAILS']._serialized_start=648
  _globals['_PURCHASEDETAILS']._serialized_end=813
  _globals['_CREATEORUPDATEPORTFOLIOPOSTSTATUS']._serialized_start=815
  _globals['_CREATEORUPDATEPORTFOLIOPOSTSTATUS']._serialized_end=869
  _globals['_LENDERORDERCANCELLEDDETAILS']._serialized_start=871
  _globals['_LENDERORDERCANCELLEDDETAILS']._serialized_end=977
  _globals['_PORTFOLIOUPDATERESP']._serialized_start=979
  _globals['_PORTFOLIOUPDATERESP']._serialized_end=1019
  _globals['_LOANCANCELLEDBYBORROWERDETAILS']._serialized_start=1021
  _globals['_LOANCANCELLEDBYBORROWERDETAILS']._serialized_end=1087
  _globals['_NLPLOANDETAILS']._serialized_start=1089
  _globals['_NLPLOANDETAILS']._serialized_end=1142
  _globals['_PROVISIONFUNDSPREADINGDETAILS']._serialized_start=1144
  _globals['_PROVISIONFUNDSPREADINGDETAILS']._serialized_end=1229
  _globals['_PORTFOLIOLOANDETAILS']._serialized_start=1231
  _globals['_PORTFOLIOLOANDETAILS']._serialized_end=1290
  _globals['_PORTFOLIODETAILS']._serialized_start=1293
  _globals['_PORTFOLIODETAILS']._serialized_end=1930
  _globals['_PORTFOLIODETAILSRESP']._serialized_start=1932
  _globals['_PORTFOLIODETAILSRESP']._serialized_end=2005
  _globals['_EXISTENCEPORTFOLIOUSERSPARAMS']._serialized_start=2007
  _globals['_EXISTENCEPORTFOLIOUSERSPARAMS']._serialized_end=2073
  _globals['_EXISTENCEPORTFOLIOUSERSRESP']._serialized_start=2075
  _globals['_EXISTENCEPORTFOLIOUSERSRESP']._serialized_end=2121
  _globals['_PORTFOLIOACCOUNTVALUEINPUTPARAM']._serialized_start=2123
  _globals['_PORTFOLIOACCOUNTVALUEINPUTPARAM']._serialized_end=2172
  _globals['_PORTFOLIOACCOUNTVALUEDETAILS']._serialized_start=2175
  _globals['_PORTFOLIOACCOUNTVALUEDETAILS']._serialized_end=2305
  _globals['_PRODUCTSPORTFOLIO']._serialized_start=2308
  _globals['_PRODUCTSPORTFOLIO']._serialized_end=3496
# @@protoc_insertion_point(module_scope)