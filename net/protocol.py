SMSG_LOGIN_DATA = 0x0069
SMSG_CHAR_LOGIN = 0x006b
SMSG_CHAR_MAP_INFO = 0x0071
SMSG_MAP_LOGIN_SUCCESS = 0x0073
SMSG_MAP_LOGIN_SUCCESS = 0x0073
CMSG_CHAR_SERVER_CONNECT = 0x0065
CMSG_CHAR_SELECT = 0x0066
CMSG_MAP_SERVER_CONNECT = 0x0072
CMSG_CHAT_WHISPER = 0x0096
CMSG_CHAT_MESSAGE = 0x008c
CMSG_MAP_LOADED = 0x007d

SMSG_WHISPER = 0x0097
SMSG_BEING_CHAT = 0x008d

SMSG_PLAYER_CHAT = 0x008e
CMSG_PLAYER_CHANGE_ACT = 0x0089

SMSG_PLAYER_INVENTORY = 0x01ee
SMSG_PLAYER_INVENTORY_ADD = 0x00a0
SMSG_PLAYER_INVENTORY_REMOVE = 0x00af
SMSG_PLAYER_EQUIPMENT = 0x00a4
SMSG_PLAYER_STAT_UPDATE_1 = 0x00b0
SMSG_PLAYER_STAT_UPDATE_2 = 0x00b1

SMSG_PLAYER_STORAGE_EQUIP = 0x00a6
SMSG_PLAYER_STORAGE_ITEMS = 0x01f0
SMSG_PLAYER_STORAGE_STATUS = 0x00f2
SMSG_PLAYER_STORAGE_ADD = 0x00f4
SMSG_PLAYER_STORAGE_REMOVE = 0x00f6
SMSG_PLAYER_STORAGE_CLOSE = 0x00f8

SMSG_BEING_VISIBLE = 0x0078
SMSG_BEING_MOVE = 0x007b
SMSG_BEING_REMOVE = 0x0080
SMSG_PLAYER_MOVE = 0x01da
SMSG_PLAYER_WARP = 0x0091
SMSG_PLAYER_UPDATE_1 = 0x01d8
SMSG_PLAYER_UPDATE_2 = 0x01d9
SMSG_BEING_NAME_RESPONSE = 0x0095 # Has to be requested
SMSG_BEING_ACTION = 0x008a

CMSG_ITEM_PICKUP = 0x009f
CMSG_PLAYER_ATTACK = 0x0089
CMSG_PLAYER_STOP_ATTACK = 0x0118
CMSG_PLAYER_CHANGE_DIR = 0x009b
CMSG_PLAYER_CHANGE_DEST = 0x0085
CMSG_PLAYER_EMOTE = 0x00bf
SMSG_WALK_RESPONSE = 0x0087

CMSG_MOVE_TO_STORAGE = 0x00f3
CMSG_MOVE_FROM_STORAGE = 0x00f5
CMSG_CLOSE_STORAGE = 0x00f7

CMSG_TRADE_REQUEST = 0x00e4
CMSG_TRADE_RESPONSE = 0x00e6
CMSG_TRADE_ITEM_ADD_REQUEST = 0x00e8
CMSG_TRADE_CANCEL_REQUEST = 0x00ed
CMSG_TRADE_ADD_COMPLETE = 0x00eb
CMSG_TRADE_OK = 0x00ef

SMSG_TRADE_REQUEST = 0x00e5 #/**< Receiving a request to trade */
SMSG_TRADE_RESPONSE = 0x00e7
SMSG_TRADE_ITEM_ADD = 0x00e9
SMSG_TRADE_ITEM_ADD_RESPONSE = 0x01b1 #/**< Not standard eAthena! */
SMSG_TRADE_OK = 0x00ec
SMSG_TRADE_CANCEL = 0x00ee
SMSG_TRADE_COMPLETE = 0x00f0

SMSG_ITEM_VISIBLE = 0x009d
SMSG_ITEM_DROPPED = 0x009e
SMSG_ITEM_REMOVE = 0x00a1

inventory_offset = 2
storage_offset = 1
MAX_STORAGE = 300
MAX_INVENTORY = 99
MAX_AMOUNT = 30000
