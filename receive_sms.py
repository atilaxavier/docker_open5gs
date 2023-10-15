#!/usr/bin/env python
"""
smpplib.consts.__dir__()
['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__file__', '__cached__', '__builtins__', 'EMPTY_STRING', 'NULL_STRING', 'SEVENBIT_LENGTH', 'EIGHTBIT_LENGTH', 'UCS2_LENGTH', 'MULTIPART_HEADER_SIZE', 'SEVENBIT_PART_SIZE', 'EIGHTBIT_PART_SIZE', 'UCS2_PART_SIZE',...
If you wish to specific a special value for the TON, the available options are:
0: Unknown
1: International
2: National
3: Network Specific
4: Subscriber Number
5: Alphanumeric
6: Abbreviated
'SMPP_TON_UNK', 'SMPP_TON_INTL', 'SMPP_TON_NATNL', 'SMPP_TON_NWSPEC', 'SMPP_TON_SBSCR', 'SMPP_TON_ALNUM', 'SMPP_TON_ABBREV', 

If you wish to specific a special value for the NPI, the available options are:
Unknown = 0
ISDN/telephone numbering plan (E163/E164) = 1
Data numbering plan (X.121) = 3
Telex numbering plan (F.69) = 4
Land Mobile (E.212) =6
National numbering plan = 8
Private numbering plan = 9
ERMES numbering plan (ETSI DE/PS 3 01-3) = 10
Internet (IP) = 13
WAP Client Id (to be defined by WAP Forum) = 18
'SMPP_NPI_UNK', 'SMPP_NPI_ISDN', 'SMPP_NPI_DATA', 'SMPP_NPI_TELEX', 'SMPP_NPI_LNDMBL', 'SMPP_NPI_NATNL', 'SMPP_NPI_PRVT', 'SMPP_NPI_ERMES', 'SMPP_NPI_IP', 'SMPP_NPI_WAP'

'SMPP_ENCODING_DEFAULT', 'SMPP_ENCODING_IA5', 'SMPP_ENCODING_BINARY', 'SMPP_ENCODING_ISO88591', 'SMPP_ENCODING_BINARY2', 'SMPP_ENCODING_JIS', 'SMPP_ENCODING_ISO88595', 'SMPP_ENCODING_ISO88598', 'SMPP_ENCODING_ISO10646', 'SMPP_ENCODING_PICTOGRAM', 'SMPP_ENCODING_ISO2022JP', 'SMPP_ENCODING_EXTJIS', 'SMPP_ENCODING_KSC5601', 

'SMPP_LANG_DEFAULT', 'SMPP_LANG_EN', 'SMPP_LANG_FR', 'SMPP_LANG_ES', 'SMPP_LANG_DE', 

'SMPP_MSGMODE_DEFAULT', 'SMPP_MSGMODE_DATAGRAM', 'SMPP_MSGMODE_FORWARD', 'SMPP_MSGMODE_STOREFORWARD', 'SMPP_MSGTYPE_DEFAULT', 'SMPP_MSGTYPE_DELIVERYACK', 'SMPP_MSGTYPE_USERACK',

 'SMPP_GSMFEAT_NONE', 'SMPP_GSMFEAT_UDHI', 'SMPP_GSMFEAT_REPLYPATH', 'SMPP_GSMFEAT_UDHIREPLYPATH', 'SMPP_PID_DEFAULT', 'SMPP_PID_RIP', 'SMPP_UDHIEIE_CONCATENATED', 'SMPP_UDHIEIE_SPECIAL', 'SMPP_UDHIEIE_RESERVED', 'SMPP_UDHIEIE_PORT8', 'SMPP_UDHIEIE_PORT16', 'SMPP_UDHIEIE_CONCATENATED16', 'SMPP_MS_AVAILABILITY_STATUS_AVAILABLE', 'SMPP_MS_AVAILABILITY_STATUS_DENIED', 'SMPP_MS_AVAILABILITY_STATUS_UNAVAILABLE', 'SMPP_SMSC_DELIVERY_RECEIPT_NONE', 'SMPP_SMSC_DELIVERY_RECEIPT_BOTH', 'SMPP_SMSC_DELIVERY_RECEIPT_FAILURE', 'SMPP_SMSC_DELIVERY_RECEIPT_BITMASK', 'SMPP_SME_ACK_BITMASK', 'SMPP_SME_ACK_NONE', 'SMPP_SME_ACK_DELIVERY', 'SMPP_SME_ACK_MANUAL', 'SMPP_SME_ACK_BOTH', 'SMPP_INT_NOTIFICATION_BITMASK', 'SMPP_INT_NOTIFICATION_NONE', 'SMPP_INT_NOTIFICATION_REQUESTED', 'SMPP_VERSION_33', 'SMPP_VERSION_34', 'SMPP_NETWORK_TYPE_UNKNOWN', 'SMPP_NETWORK_TYPE_GSM', 'SMPP_NETWORK_TYPE_TDMA', 'SMPP_NETWORK_TYPE_CDMA', 'SMPP_NETWORK_TYPE_PDC', 'SMPP_NETWORK_TYPE_PHS', 'SMPP_NETWORK_TYPE_IDEN', 'SMPP_NETWORK_TYPE_AMPS', 'SMPP_NETWORK_TYPE_PAGING', 'SMPP_MESSAGE_STATE_ENROUTE', 'SMPP_MESSAGE_STATE_DELIVERED', 'SMPP_MESSAGE_STATE_EXPIRED', 'SMPP_MESSAGE_STATE_DELETED', 'SMPP_MESSAGE_STATE_UNDELIVERABLE', 'SMPP_MESSAGE_STATE_ACCEPTED', 'SMPP_MESSAGE_STATE_UNKNOWN', 'SMPP_MESSAGE_STATE_REJECTED', 'COMMAND_STATES', 'STATE_SETTERS', 'OPTIONAL_PARAMS', 'INT_PACK_FORMATS']

>>> smpplib.__dir__()
['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__path__', '__file__', '__cached__', '__builtins__', 'consts', 'exceptions', 'command_codes', 'pdu', 'ptypes', 'command', 'smpp', 'client']

>>> smpplib.smpp.__dir__()
['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__file__', '__cached__', '__builtins__', 'command', 'pdu', 'make_pdu', 'parse_pdu']

>>> pdu.__dir__()
['_client', 'allow_unknown_opt_params', 'command', '_sequence', 'status', 'client', 'source_addr_ton', 'source_addr_npi', 'source_addr', 'dest_addr_ton', 'dest_addr_npi', 'destination_addr', 'short_message', 'service_type', 'esm_class', 'protocol_id', 'priority_flag', 'schedule_delivery_time', 'validity_period', 'registered_delivery', 'replace_if_present_flag', 'data_coding', 'sm_default_msg_id', 'user_message_reference', 'source_port', 'source_addr_subunit', 'destination_port', 'dest_addr_subunit', 'sar_msg_ref_num', 'sar_total_segments', 'sar_segment_seqnum', 'more_messages_to_send', 'payload_type', 'message_payload', 'privacy_indicator', 'callback_num', 'callback_num_pres_ind', 'source_subaddress', 'dest_subaddress', 'user_response_code', 'display_time', 'sms_signal', 'ms_validity', 'ms_msg_wait_facilities', 'number_of_messages', 'alert_on_message_delivery', 'language_indicator', 'its_reply_type', 'its_session_info', 'ussd_service_op', 'sm_length', '_length', '__module__', '__doc__', 'params', 'params_order', '__init__', 'prep', '_set_vars', 'generate_params', '_generate_opt_header', '_generate_int', '_generate_string', '_generate_ostring', '_generate_int_tlv', '_generate_string_tlv', '_generate_ostring_tlv', '_int_pack_format', '_parse_int', '_parse_string', '_parse_ostring', 'is_fixed', 'parse_params', 'parse_optional_params', 'field_exists', 'field_is_optional', 'length', '_get_sequence', '_set_sequence', 'sequence', '_next_seq', 'is_vendor', 'is_request', 'is_response', 'is_error', 'get_status_desc', 'parse', 'generate', '__dict__', '__weakref__', '__repr__', '__hash__', '__str__', '__getattribute__', '__setattr__', '__delattr__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__new__', '__reduce_ex__', '__reduce__', '__subclasshook__', '__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__']

"""
#
# SMPP Library usage example
#
import smpplib
from smpplib import consts
import argparse
from time import sleep
from threading import Thread


def received_handler(pdu):
	#print(pdu.__dir__())
	"""
	['_client', 'allow_unknown_opt_params', 'command', '_sequence', 'status', 'client', 'source_addr_ton', 'source_addr_npi', 'source_addr', 'esme_addr_ton', 'esme_addr_npi', 'esme_addr', 'ms_availability_status', 'length', '__module__', '__doc__', 'params', 'params_order', '__init__', '_set_vars', 'generate_params', '_generate_opt_header', '_generate_int', '_generate_string', '_generate_ostring', '_generate_int_tlv', '_generate_string_tlv', '_generate_ostring_tlv', '_int_pack_format', '_parse_int', '_parse_string', '_parse_ostring', 'is_fixed', 'parse_params', 'parse_optional_params', 'field_exists', 'field_is_optional', '_get_sequence', '_set_sequence', 'sequence', '_next_seq', 'is_vendor', 'is_request', 'is_response', 'is_error', 'get_status_desc', 'parse', 'generate', '__dict__', '__weakref__', '__repr__', '__hash__', '__str__', '__getattribute__', '__setattr__', '__delattr__', '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__new__', '__reduce_ex__', '__reduce__', '__subclasshook__', '__init_subclass__', '__format__', '__sizeof__', '__dir__', '__class__']
	"""

	#print(pdu.params)
	"""
	{'source_addr_ton': <Param of <class 'int'>>, 'source_addr_npi': <Param of <class 'int'>>, 'source_addr': <Param of <class 'str'>>, 'esme_addr_ton': <Param of <class 'int'>>, 'esme_addr_npi': <Param of <class 'int'>>, 'esme_addr': <Param of <class 'str'>>, 'ms_availability_status': <Param of <class 'int'>>}
	"""

	#print(pdu.get_status_desc)
	#<bound method PDU.get_status_desc of <smpplib.command.AlertNotification object at 0x7f1e8c0107f0>>
	
	#print(pdu.__str__)
	#<method-wrapper '__str__' of AlertNotification object at 0x7f1e8c0107f0>

	print("pdu status: %s"%pdu.status)
	print("received_handler - Recebido - sequence: %s"%pdu.sequence)
	print("received_handler - Recebido - de: %s ; para: %s"%((pdu.source_addr).decode(), (pdu.esme_addr)))
	#qsm = pdu.client.query_message(message_id = pdu.sequence, source_addr_ton = str(pdu.source_addr_ton), source_addr_npi = str(pdu.source_addr_npi), source_addr = pdu.source_addr.decode() )
	#if (pdu.ms_availability_status == consts.SMPP_MS_AVAILABILITY_STATUS_AVAILABLE):
	if pdu.command == consts.SMPP_ESME_ROK:
		# Process received message
		message_text = pdu.short_message
		print("received_handler - Recebido - Mensagem: %s\n"%(message_text))


def sent_handler(pdu):
	print("sent_handler - Enviado: sent_seq=%s ; msgid=%s"%(pdu.sequence, pdu.message_id))


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='receive_sms.py. Rotina para recebimento de SMS sobre SMPP com OsmoSMSC.')
	parser.add_argument('-a', '--addr', dest='smpp_svr_addr', default='172.22.0.31', action="store_true",
					help='Endereco do servidor SMPP. Default \'172.22.0.31\'')
	parser.add_argument('-p', '--port', dest='smpp_svr_port', default=2775, action="store_true",
					help='Porta do servidor SMPP. Default 2775')						
	parser.add_argument('-s', '--sid', dest='smpp_sid', default="timlab", action="store_true",
					help='SMPP System ID. Default \'timlab\'')
	parser.add_argument('-pw', '--pwd', dest='pwd', default='timlab', action="store_true",
					help='Senha do servidor SMPP. Default \'timlab\'')	
	inarg = parser.parse_args()

	smpp_svr_addr = inarg.smpp_svr_addr
	smpp_svr_port = inarg.smpp_svr_port
	smpp_sid = inarg.smpp_sid
	pwd = inarg.pwd      

	print("Aguardando mensagens...\n")
	client = smpplib.client.Client(smpp_svr_addr, smpp_svr_port)

	client.set_message_received_handler(received_handler)

	client.connect()
	client.bind_transceiver(system_id=smpp_sid, password=pwd)


	t = Thread(target=client.listen)
	t.start()
	#t.join()
	#client.listen()
	
	res = "a"
	while res != "Q":
		res = input("Digite Q para sair.\n\n")

	print("Desconectando")

	client.unbind()
	client.disconnect()
