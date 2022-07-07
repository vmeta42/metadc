from dataclasses import dataclass
import typing
from diem import serde_types as st
from diem import diem_types
from diem.stdlib import (
    ScriptCall,
    ScriptFunctionCall,
    decode_u8vector_argument,
    decode_u64_argument,
    decode_address_argument,
    bcs_deserialize

)
from diem.diem_types import (
    Script,
    Module,
    ScriptFunction,
    TransactionPayload,
    TransactionPayload__ScriptFunction,
    Identifier,
    ModuleId,
    TypeTag,
    AccountAddress,
    TransactionArgument,
    TransactionArgument__Bool,
    TransactionArgument__U8,
    TransactionArgument__U64,
    TransactionArgument__U128,
    TransactionArgument__Address,
    TransactionArgument__U8Vector,
)

src_addr=bytes.fromhex("00000000000000000000000000000002")

@dataclass(frozen=True)
class ScriptCall__Meta42Accept(ScriptFunctionCall):
    pass

@dataclass(frozen=True)
class ScriptCall__Meta42Initialize(ScriptFunctionCall):
    pass

@dataclass(frozen=True)
class ScriptCall__Meta42MintToken(ScriptFunctionCall):
    path: bytes

@dataclass(frozen=True)
class ScriptCall__Meta42ShareTokenById(ScriptFunctionCall):
    recevier: diem_types.AccountAddress
    token_id: bytes
    metadata: bytes

@dataclass(frozen=True)
class ScriptCall__Meta42ShareTokenByIndex(ScriptFunctionCall):
    recevier: diem_types.AccountAddress
    index: st.uint64
    metadata: bytes


@dataclass(frozen=True)
class ScriptFunctionCall__Meta42Accept(ScriptFunctionCall):
    pass

@dataclass(frozen=True)
class ScriptFunctionCall__Meta42Initialize(ScriptFunctionCall):
    pass

@dataclass(frozen=True)
class ScriptFunctionCall__Meta42MintToken(ScriptFunctionCall):
    path: bytes

@dataclass(frozen=True)
class ScriptFunctionCall__Meta42ShareTokenById(ScriptFunctionCall):
    recevier: diem_types.AccountAddress
    token_id: bytes
    metadata: bytes

@dataclass(frozen=True)
class ScriptFunctionCall__Meta42ShareTokenByIndex(ScriptFunctionCall):
    recevier: diem_types.AccountAddress
    index: st.uint64
    metadata: bytes

def encode_meta42_module():
    # code=META42.replace(src_addr, sender.account_address.to_bytes())
    return Module(
        code=META42
    )

def encode_compare_module():
    return Module(
        code=COMPARE
    )

def encode_meta42_accept_script():
    return Script(
        code=META42_ACCEPT,
        ty_args=[],
        args=[],
    )

def encode_meta42_accept_script_function():
    return TransactionPayload__ScriptFunction(
        value=ScriptFunction(
            module=ModuleId(
                address=AccountAddress.from_hex("00000000000000000000000000000002"),
                name=Identifier("Meta42"),
            ),
            function=Identifier("accept"),
            ty_args=[],
            args=[],
        )
    )

def encode_allow_publishing_module_script(open):
    return Script(
        code=ALLOW_PUBLISHING_MODULE,
        ty_args=[],
        args=[TransactionArgument__Bool(value=open)],
    )

def encode_allow_custom_script():
    return Script(
        code=ALLOW_CUSTOM_SCRIPT,
        ty_args=[],
        args=[],
    )

def encode_meta42_initialize_script():
    return Script(
        code=META42_INITIALIZE,
        ty_args=[],
        args=[],
    )

def encode_meta42_initialize_script_function():
    return TransactionPayload__ScriptFunction(
        value=ScriptFunction(
            module=ModuleId(
                address=AccountAddress.from_hex("00000000000000000000000000000002"),
                name=Identifier("Meta42"),
            ),
            function=Identifier("initialize"),
            ty_args=[],
            args=[],
        )
    )

def encode_meta42_mint_token_script(path: bytes):
    return Script(
        code=META42_MINT_TOKEN,
        ty_args=[],
        args=[TransactionArgument__U8Vector(value=path)],
    )

def encode_meta42_mint_token_script_function(path: bytes):
    return TransactionPayload__ScriptFunction(
        value=ScriptFunction(
            module=ModuleId(
                address=AccountAddress.from_hex("00000000000000000000000000000002"),
                name=Identifier("Meta42"),
            ),
            function=Identifier("mint_token"),
            ty_args=[],
            args=[path],
        )
    )

def encode_meta42_share_token_by_id_script(recevier: diem_types.AccountAddress, token_id: bytes, metadata: bytes):
    return Script(
        code=META42_SHARE_TOKEN_BY_ID,
        ty_args=[],
        args=[
            TransactionArgument__Address(value=recevier),
            TransactionArgument__U8Vector(value=token_id),
            TransactionArgument__U8Vector(value=metadata)
        ]
    )

def encode_meta42_share_token_by_id_script_function(recevier: diem_types.AccountAddress, token_id: bytes, metadata: bytes):
    return TransactionPayload__ScriptFunction(
        value=ScriptFunction(
            module=ModuleId(
                address=AccountAddress.from_hex("00000000000000000000000000000002"),
                name=Identifier("Meta42"),
            ),
            function=Identifier("share_token_by_id"),
            ty_args=[],
            args=[recevier, token_id, metadata]
        )
    )


def encode_meta42_share_token_by_index_script(recevier: diem_types.AccountAddress, index: st.uint64, metadata: bytes):
    return Script(
        code=META42_SHARE_TOKEN_BY_INDEX,
        ty_args=[],
        args=[
            TransactionArgument__Address(value=recevier),
            TransactionArgument__U64(value=index),
            TransactionArgument__U8Vector(value=metadata)
        ]
    )

def encode_meta42_share_token_by_index_script_function(recevier: diem_types.AccountAddress, token_id: bytes, metadata: bytes):
    return TransactionPayload__ScriptFunction(
        value=ScriptFunction(
            module=ModuleId(
                address=AccountAddress.from_hex("00000000000000000000000000000002"),
                name=Identifier("Meta42"),
            ),
            function=Identifier("share_token_by_index"),
            ty_args=[],
            args=[recevier, token_id, metadata]
        )
    )

def decode_meta42_accept_script(script: Script) -> ScriptCall:
    return ScriptCall__Meta42Accept()


def decode_meta42_accept_script_function(script: TransactionPayload) -> ScriptFunctionCall:
    if not isinstance(script, ScriptFunction):
        raise ValueError("Unexpected transaction payload")
    return ScriptFunctionCall__Meta42Accept(
    )

def decode_meta42_initialize_script(script: Script) -> ScriptCall:
    return ScriptCall__Meta42Initialize()

def decode_meta42_initialize_script_function(script: TransactionPayload) -> ScriptFunctionCall:
    if not isinstance(script, ScriptFunction):
        raise ValueError("Unexpected transaction payload")
    return ScriptFunctionCall__Meta42Initialize()

def decode_meta42_mint_token_script(script: Script) -> ScriptCall:
    return ScriptCall__Meta42MintToken(
        path=decode_u8vector_argument(script.ty_args[0])
    )

def decode_meta42_mint_token_script_function(script: TransactionPayload) -> ScriptFunctionCall:
    if not isinstance(script, ScriptFunction):
        raise ValueError("Unexpected transaction payload")
    return ScriptFunctionCall__Meta42MintToken(
        path=bcs_deserialize(script.ty_args[0], bytes)[0]
    )

def decode_meta42_share_token_by_id_script(script: Script) -> ScriptCall:
    return ScriptCall__Meta42ShareTokenById(
        recevier=decode_address_argument(script.args[0]),
        token_id=decode_u8vector_argument(script.ty_args[1]),
        metadata=decode_u8vector_argument(script.ty_args[2]),

    )

def decode_meta42_share_token_by_id_script_function(script: TransactionPayload) -> ScriptFunctionCall:
    if not isinstance(script, ScriptFunction):
        raise ValueError("Unexpected transaction payload")
    return ScriptFunctionCall__Meta42Accept(
        recevier=bcs_deserialize(script.ty_args[0], AccountAddress)[0],
        token_id=bcs_deserialize(script.ty_args[1],bytes)[0],
        metadata=bcs_deserialize(script.ty_args[2],bytes)[0],
    )

def decode_meta42_share_token_by_index_script(script: Script) -> ScriptCall:
    return ScriptCall__Meta42ShareTokenById(
        recevier=decode_address_argument(script.args[0]),
        index=decode_u64_argument(script.ty_args[1]),
        metadata=decode_u8vector_argument(script.ty_args[2]),

    )

def decode_meta42_share_token_by_index_script_function(script: TransactionPayload) -> ScriptFunctionCall:
    if not isinstance(script, ScriptFunction):
        raise ValueError("Unexpected transaction payload")
    return ScriptFunctionCall__Meta42Accept(
        recevier=bcs_deserialize(script.ty_args[0], AccountAddress)[0],
        index=bcs_deserialize(script.ty_args[1],st.uint64)[0],
        metadata=bcs_deserialize(script.ty_args[2],bytes)[0],
    )

COMPARE=b"\xa1\x1c\xeb\x0b\x03\x00\x00\x00\x08\x01\x00\x04\x03\x04\x1b\x04\x1f\x04\x05\x23\x27\x07\x4a\x3a\x08\x84\x01\x10\x06\x94\x01\x09\x0c\x9d\x01\xec\x01\x00\x00\x00\x01\x00\x02\x00\x01\x00\x00\x03\x02\x01\x00\x00\x04\x03\x01\x00\x01\x05\x05\x06\x01\x00\x01\x06\x08\x09\x01\x00\x03\x01\x04\x01\x02\x06\x0a\x02\x06\x0a\x02\x01\x02\x02\x03\x03\x02\x02\x02\x05\x02\x03\x03\x02\x01\x01\x06\x0a\x09\x00\x01\x03\x00\x02\x06\x0a\x09\x00\x03\x01\x06\x09\x00\x07\x43\x6f\x6d\x70\x61\x72\x65\x06\x56\x65\x63\x74\x6f\x72\x0d\x63\x6d\x70\x5f\x62\x63\x73\x5f\x62\x79\x74\x65\x73\x07\x63\x6d\x70\x5f\x75\x36\x34\x06\x63\x6d\x70\x5f\x75\x38\x06\x6c\x65\x6e\x67\x74\x68\x06\x62\x6f\x72\x72\x6f\x77\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x02\x01\x00\x02\x01\x02\x02\x01\x01\x00\x01\x00\x00\x04\x3d\x0a\x00\x38\x00\x0c\x03\x0a\x01\x38\x00\x0c\x04\x0a\x03\x0a\x04\x11\x01\x0c\x05\x0a\x03\x06\x00\x00\x00\x00\x00\x00\x00\x00\x24\x03\x0f\x05\x14\x0a\x04\x06\x00\x00\x00\x00\x00\x00\x00\x00\x24\x0c\x06\x05\x16\x09\x0c\x06\x0b\x06\x03\x19\x05\x37\x0a\x03\x06\x01\x00\x00\x00\x00\x00\x00\x00\x17\x0c\x03\x0a\x04\x06\x01\x00\x00\x00\x00\x00\x00\x00\x17\x0c\x04\x0a\x00\x0a\x03\x38\x01\x14\x0a\x01\x0a\x04\x38\x01\x14\x11\x02\x0c\x02\x0a\x02\x31\x00\x22\x03\x30\x05\x36\x0b\x01\x01\x0b\x00\x01\x0a\x02\x02\x05\x0a\x0b\x01\x01\x0b\x00\x01\x0a\x05\x02\x01\x00\x00\x00\x03\x16\x0a\x00\x0a\x01\x21\x03\x05\x05\x08\x07\x00\x0c\x03\x05\x14\x0a\x00\x0a\x01\x23\x03\x0d\x05\x10\x07\x02\x0c\x02\x05\x12\x07\x01\x0c\x02\x0b\x02\x0c\x03\x0b\x03\x02\x02\x00\x00\x00\x03\x16\x0a\x00\x0a\x01\x21\x03\x05\x05\x08\x07\x00\x0c\x03\x05\x14\x0a\x00\x0a\x01\x23\x03\x0d\x05\x10\x07\x02\x0c\x02\x05\x12\x07\x01\x0c\x02\x0b\x02\x0c\x03\x0b\x03\x02\x00"
META42=b"\xa1\x1c\xeb\x0b\x03\x00\x00\x00\x0b\x01\x00\x12\x02\x12\x2c\x03\x3e\x93\x01\x04\xd1\x01\x24\x05\xf5\x01\xda\x01\x07\xcf\x03\x88\x05\x08\xd7\x08\x20\x06\xf7\x08\x3a\x0a\xb1\x09\x61\x0c\x92\x0a\xa7\x05\x0d\xb9\x0f\x0c\x00\x00\x01\x01\x01\x02\x01\x03\x01\x04\x01\x05\x01\x06\x01\x07\x01\x08\x00\x09\x08\x00\x00\x0a\x06\x00\x00\x0b\x08\x00\x00\x0c\x06\x00\x00\x0d\x06\x00\x00\x0e\x06\x00\x00\x0f\x06\x00\x00\x10\x05\x00\x06\x06\x07\x01\x00\x00\x04\x1e\x04\x01\x06\x01\x00\x11\x00\x01\x00\x00\x12\x02\x01\x00\x00\x13\x03\x04\x00\x00\x14\x05\x01\x00\x00\x15\x06\x01\x00\x00\x16\x01\x02\x00\x00\x17\x07\x08\x00\x00\x18\x00\x01\x00\x00\x19\x09\x01\x00\x00\x1a\x0a\x01\x00\x00\x1b\x0b\x01\x00\x07\x29\x00\x02\x00\x08\x2a\x01\x0d\x01\x00\x04\x2b\x00\x0f\x01\x06\x01\x2c\x02\x02\x00\x02\x2d\x13\x04\x01\x00\x05\x2e\x04\x04\x00\x04\x2f\x15\x01\x01\x06\x08\x30\x18\x19\x01\x00\x08\x31\x1a\x13\x01\x00\x03\x32\x1b\x1c\x00\x06\x33\x1d\x1e\x01\x00\x06\x34\x01\x1e\x01\x00\x08\x35\x21\x22\x01\x00\x08\x36\x23\x01\x01\x00\x06\x37\x25\x22\x01\x00\x06\x38\x26\x1d\x01\x00\x0c\x0c\x0d\x0e\x0d\x10\x0d\x11\x0f\x0c\x11\x0e\x11\x16\x12\x0c\x13\x0c\x15\x19\x16\x19\x0d\x16\x17\x0c\x18\x0c\x19\x19\x1a\x19\x11\x10\x11\x11\x01\x06\x0c\x00\x01\x05\x01\x06\x08\x07\x01\x0a\x02\x03\x05\x0a\x02\x0a\x02\x04\x05\x05\x0a\x02\x0a\x02\x02\x05\x0a\x02\x01\x0b\x08\x01\x03\x02\x06\x0c\x0a\x02\x04\x06\x0c\x05\x0a\x02\x0a\x02\x04\x06\x0c\x05\x03\x0a\x02\x01\x08\x07\x01\x0a\x09\x00\x01\x08\x03\x01\x0b\x09\x01\x09\x00\x01\x08\x05\x01\x08\x04\x03\x01\x03\x01\x01\x06\x09\x00\x03\x07\x08\x02\x01\x03\x02\x07\x0b\x09\x01\x09\x00\x09\x00\x01\x08\x06\x05\x07\x08\x00\x0a\x02\x03\x03\x06\x08\x07\x01\x06\x0a\x09\x00\x01\x03\x02\x06\x0a\x09\x00\x03\x02\x06\x0a\x02\x06\x0a\x02\x01\x02\x01\x09\x00\x01\x0b\x08\x01\x09\x00\x03\x05\x01\x03\x06\x07\x08\x00\x05\x01\x03\x08\x07\x0a\x02\x02\x06\x0a\x09\x00\x06\x09\x00\x01\x01\x02\x07\x0a\x09\x00\x09\x00\x05\x03\x0b\x08\x01\x03\x05\x01\x03\x01\x06\x0b\x08\x01\x09\x00\x01\x07\x0b\x08\x01\x09\x00\x0b\x07\x08\x00\x05\x07\x08\x00\x01\x03\x01\x03\x01\x03\x08\x07\x0a\x02\x06\x4d\x65\x74\x61\x34\x32\x04\x56\x41\x53\x50\x03\x42\x43\x53\x07\x43\x6f\x6d\x70\x61\x72\x65\x05\x45\x76\x65\x6e\x74\x04\x48\x61\x73\x68\x06\x4f\x70\x74\x69\x6f\x6e\x06\x53\x69\x67\x6e\x65\x72\x06\x56\x65\x63\x74\x6f\x72\x0b\x41\x63\x63\x6f\x75\x6e\x74\x49\x6e\x66\x6f\x10\x42\x75\x72\x6e\x65\x64\x54\x6f\x6b\x65\x6e\x45\x76\x65\x6e\x74\x0a\x47\x6c\x6f\x62\x61\x6c\x49\x6e\x66\x6f\x10\x4d\x69\x6e\x74\x65\x64\x54\x6f\x6b\x65\x6e\x45\x76\x65\x6e\x74\x12\x52\x65\x63\x65\x69\x76\x65\x64\x54\x6f\x6b\x65\x6e\x45\x76\x65\x6e\x74\x0e\x53\x65\x6e\x74\x54\x6f\x6b\x65\x6e\x45\x76\x65\x6e\x74\x10\x53\x68\x61\x72\x65\x64\x54\x6f\x6b\x65\x6e\x45\x76\x65\x6e\x74\x05\x54\x6f\x6b\x65\x6e\x06\x61\x63\x63\x65\x70\x74\x15\x61\x73\x73\x65\x72\x74\x5f\x6d\x61\x74\x65\x34\x32\x5f\x61\x63\x63\x6f\x75\x6e\x74\x10\x63\x6f\x6d\x70\x75\x74\x65\x5f\x74\x6f\x6b\x65\x6e\x5f\x69\x64\x11\x65\x6d\x69\x74\x5f\x6d\x69\x6e\x74\x65\x64\x5f\x65\x76\x65\x6e\x74\x17\x65\x6d\x69\x74\x5f\x73\x68\x61\x72\x65\x64\x5f\x74\x6f\x6b\x65\x6e\x5f\x65\x76\x65\x6e\x74\x11\x67\x65\x74\x5f\x61\x64\x6d\x69\x6e\x5f\x61\x64\x64\x72\x65\x73\x73\x15\x67\x65\x74\x5f\x74\x6f\x6b\x65\x6e\x5f\x69\x6e\x64\x65\x78\x5f\x62\x79\x5f\x69\x64\x0a\x69\x6e\x69\x74\x69\x61\x6c\x69\x7a\x65\x0a\x6d\x69\x6e\x74\x5f\x74\x6f\x6b\x65\x6e\x11\x73\x68\x61\x72\x65\x5f\x74\x6f\x6b\x65\x6e\x5f\x62\x79\x5f\x69\x64\x14\x73\x68\x61\x72\x65\x5f\x74\x6f\x6b\x65\x6e\x5f\x62\x79\x5f\x69\x6e\x64\x65\x78\x06\x74\x6f\x6b\x65\x6e\x73\x0d\x6d\x69\x6e\x74\x65\x64\x5f\x65\x76\x65\x6e\x74\x73\x0b\x45\x76\x65\x6e\x74\x48\x61\x6e\x64\x6c\x65\x0b\x73\x65\x6e\x74\x5f\x65\x76\x65\x6e\x74\x73\x0f\x72\x65\x63\x65\x69\x76\x65\x64\x5f\x65\x76\x65\x6e\x74\x73\x0b\x64\x75\x6d\x6d\x79\x5f\x66\x69\x65\x6c\x64\x0d\x73\x68\x61\x72\x65\x64\x5f\x65\x76\x65\x6e\x74\x73\x08\x74\x6f\x6b\x65\x6e\x5f\x69\x64\x09\x68\x64\x66\x73\x5f\x70\x61\x74\x68\x06\x6d\x69\x6e\x74\x65\x72\x06\x73\x65\x6e\x64\x65\x72\x08\x6d\x65\x74\x61\x64\x61\x74\x61\x08\x72\x65\x63\x65\x69\x76\x65\x72\x0a\x61\x64\x64\x72\x65\x73\x73\x5f\x6f\x66\x05\x65\x6d\x70\x74\x79\x10\x6e\x65\x77\x5f\x65\x76\x65\x6e\x74\x5f\x68\x61\x6e\x64\x6c\x65\x0e\x70\x61\x72\x65\x6e\x74\x5f\x61\x64\x64\x72\x65\x73\x73\x08\x74\x6f\x5f\x62\x79\x74\x65\x73\x08\x73\x68\x61\x33\x5f\x32\x35\x36\x0a\x65\x6d\x69\x74\x5f\x65\x76\x65\x6e\x74\x06\x6c\x65\x6e\x67\x74\x68\x06\x62\x6f\x72\x72\x6f\x77\x0d\x63\x6d\x70\x5f\x62\x63\x73\x5f\x62\x79\x74\x65\x73\x04\x73\x6f\x6d\x65\x04\x6e\x6f\x6e\x65\x08\x63\x6f\x6e\x74\x61\x69\x6e\x73\x09\x70\x75\x73\x68\x5f\x62\x61\x63\x6b\x07\x69\x73\x5f\x73\x6f\x6d\x65\x07\x65\x78\x74\x72\x61\x63\x74\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x03\x08\x11\x27\x00\x00\x00\x00\x00\x00\x03\x08\x12\x27\x00\x00\x00\x00\x00\x00\x03\x08\x13\x27\x00\x00\x00\x00\x00\x00\x03\x08\x10\x27\x00\x00\x00\x00\x00\x00\x05\x10\x45\x8d\x62\x33\x00\xe7\x97\x45\x1b\x3e\x79\x4a\x45\xb4\x10\x65\x00\x02\x04\x1c\x0a\x08\x07\x1d\x0b\x09\x01\x08\x03\x1f\x0b\x09\x01\x08\x05\x20\x0b\x09\x01\x08\x04\x01\x02\x01\x21\x01\x02\x02\x02\x1d\x0b\x09\x01\x08\x03\x22\x0b\x09\x01\x08\x06\x03\x02\x03\x23\x0a\x02\x24\x0a\x02\x25\x05\x04\x02\x03\x26\x05\x23\x0a\x02\x27\x0a\x02\x05\x02\x03\x28\x05\x23\x0a\x02\x27\x0a\x02\x06\x02\x04\x26\x05\x28\x05\x23\x0a\x02\x27\x0a\x02\x07\x02\x01\x24\x0a\x02\x00\x01\x00\x00\x02\x18\x0a\x00\x11\x0b\x0c\x01\x0a\x01\x11\x01\x0a\x01\x29\x00\x20\x03\x0a\x05\x15\x0a\x00\x38\x00\x0a\x00\x38\x01\x0a\x00\x38\x02\x0b\x00\x38\x03\x12\x00\x2d\x00\x05\x17\x0b\x00\x01\x02\x01\x00\x00\x00\x12\x14\x0a\x00\x11\x05\x21\x03\x05\x05\x08\x08\x0c\x03\x05\x0d\x0a\x00\x11\x0e\x11\x05\x21\x0c\x03\x0b\x03\x0c\x01\x0b\x01\x03\x13\x07\x03\x27\x02\x02\x00\x00\x00\x04\x06\x0b\x00\x38\x04\x0c\x01\x0b\x01\x11\x10\x02\x03\x00\x00\x01\x02\x14\x12\x11\x05\x29\x02\x0c\x04\x0b\x04\x03\x07\x06\x15\x27\x00\x00\x00\x00\x00\x00\x27\x11\x05\x2a\x02\x0c\x03\x0b\x03\x0f\x00\x0b\x01\x0b\x02\x0a\x00\x12\x03\x38\x05\x02\x04\x00\x00\x01\x02\x14\x13\x11\x05\x29\x02\x0c\x05\x0b\x05\x03\x07\x06\x15\x27\x00\x00\x00\x00\x00\x00\x27\x11\x05\x2a\x02\x0c\x04\x0b\x04\x0f\x01\x0a\x00\x0a\x01\x0b\x02\x0b\x03\x12\x06\x38\x06\x02\x05\x00\x00\x00\x01\x02\x07\x04\x02\x06\x00\x00\x01\x00\x17\x2b\x0a\x00\x2a\x00\x0c\x02\x0a\x02\x10\x02\x38\x07\x0c\x05\x06\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x04\x0a\x04\x0a\x05\x23\x03\x0e\x05\x27\x0a\x02\x10\x02\x0a\x04\x38\x08\x0c\x06\x0b\x06\x11\x02\x0c\x03\x0e\x03\x0e\x01\x11\x14\x31\x00\x21\x03\x1d\x05\x22\x0b\x02\x01\x0a\x04\x38\x09\x02\x0a\x04\x06\x01\x00\x00\x00\x00\x00\x00\x00\x16\x0c\x04\x05\x09\x0b\x02\x01\x38\x0a\x02\x07\x01\x00\x00\x1f\x1c\x0a\x00\x11\x0b\x0c\x01\x0a\x01\x11\x05\x21\x0c\x02\x0b\x02\x03\x0d\x0b\x00\x01\x07\x01\x27\x0a\x01\x29\x02\x20\x03\x12\x05\x19\x0a\x00\x0a\x00\x38\x01\x0a\x00\x38\x0b\x12\x02\x2d\x02\x0b\x00\x11\x00\x02\x08\x01\x00\x02\x00\x02\x20\x2c\x0a\x00\x11\x0b\x0c\x03\x0a\x03\x11\x01\x0b\x00\x11\x00\x0a\x03\x2a\x00\x0c\x02\x0a\x01\x12\x07\x0c\x06\x0e\x06\x11\x02\x0c\x07\x0a\x02\x10\x02\x0e\x06\x38\x0c\x20\x0c\x04\x0b\x04\x03\x1c\x0b\x02\x01\x06\x19\x27\x00\x00\x00\x00\x00\x00\x27\x0a\x02\x0f\x02\x0b\x06\x38\x0d\x0a\x03\x0a\x07\x0a\x01\x11\x03\x0b\x02\x0f\x03\x0b\x07\x0b\x01\x0a\x03\x12\x03\x38\x05\x02\x09\x01\x00\x02\x00\x02\x24\x19\x0a\x00\x11\x0b\x0c\x06\x0a\x06\x0b\x02\x11\x06\x0c\x05\x0e\x05\x38\x0e\x0c\x07\x0b\x07\x03\x10\x0b\x00\x01\x06\x10\x27\x00\x00\x00\x00\x00\x00\x27\x0d\x05\x38\x0f\x0c\x04\x0b\x00\x0a\x01\x0a\x04\x0b\x03\x11\x0a\x02\x0a\x01\x00\x02\x00\x02\x27\x48\x0b\x00\x11\x0b\x0c\x05\x0a\x05\x11\x01\x0a\x05\x29\x00\x0c\x07\x0b\x07\x03\x0c\x07\x00\x27\x0a\x01\x29\x00\x0c\x09\x0b\x09\x03\x13\x07\x00\x27\x0a\x05\x2a\x00\x0c\x06\x0b\x06\x10\x02\x0a\x02\x38\x08\x14\x0c\x0d\x0e\x0d\x11\x02\x0c\x0e\x0a\x01\x2a\x00\x0c\x04\x0a\x04\x10\x02\x0e\x0d\x38\x0c\x20\x0c\x0b\x0b\x0b\x03\x2e\x0b\x04\x01\x07\x02\x27\x0b\x04\x0f\x02\x0b\x0d\x38\x0d\x0a\x05\x0a\x01\x0a\x0e\x0a\x03\x11\x04\x0a\x05\x2a\x00\x0f\x04\x0a\x01\x0a\x0e\x0a\x03\x12\x05\x38\x10\x0a\x01\x2a\x00\x0f\x05\x0a\x05\x0b\x0e\x0b\x03\x12\x04\x38\x11\x02\x02\x00\x02\x01\x00\x00\x00\x01\x00\x02\x00\x03\x00"
ALLOW_PUBLISHING_MODULE=b"\xa1\x1c\xeb\x0b\x03\x00\x00\x00\x05\x01\x00\x02\x03\x02\x05\x05\x07\x08\x07\x0f\x30\x08\x3f\x10\x00\x00\x00\x01\x02\x01\x00\x02\x0c\x01\x00\x02\x06\x0c\x01\x1f\x44\x69\x65\x6d\x54\x72\x61\x6e\x73\x61\x63\x74\x69\x6f\x6e\x50\x75\x62\x6c\x69\x73\x68\x69\x6e\x67\x4f\x70\x74\x69\x6f\x6e\x0f\x73\x65\x74\x5f\x6f\x70\x65\x6e\x5f\x6d\x6f\x64\x75\x6c\x65\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x01\x04\x0e\x00\x0a\x01\x11\x00\x02"
ALLOW_CUSTOM_SCRIPT=b"\xa1\x1c\xeb\x0b\x03\x00\x00\x00\x05\x01\x00\x02\x03\x02\x05\x05\x07\x06\x07\x0d\x30\x08\x3d\x10\x00\x00\x00\x01\x02\x01\x00\x01\x0c\x00\x01\x06\x0c\x1f\x44\x69\x65\x6d\x54\x72\x61\x6e\x73\x61\x63\x74\x69\x6f\x6e\x50\x75\x62\x6c\x69\x73\x68\x69\x6e\x67\x4f\x70\x74\x69\x6f\x6e\x0f\x73\x65\x74\x5f\x6f\x70\x65\x6e\x5f\x73\x63\x72\x69\x70\x74\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x01\x03\x0e\x00\x11\x00\x02"


META42_ACCEPT=b"\xa1\x1c\xeb\x0b\x03\x00\x00\x00\x05\x01\x00\x02\x03\x02\x05\x05\x07\x06\x07\x0d\x0e\x08\x1b\x10\x00\x00\x00\x01\x02\x01\x00\x01\x0c\x00\x01\x06\x0c\x06\x4d\x65\x74\x61\x34\x32\x06\x61\x63\x63\x65\x70\x74\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x01\x03\x0e\x00\x11\x00\x02"
META42_INITIALIZE=b"\xa1\x1c\xeb\x0b\x03\x00\x00\x00\x05\x01\x00\x02\x03\x02\x05\x05\x07\x06\x07\x0d\x12\x08\x1f\x10\x00\x00\x00\x01\x02\x01\x00\x01\x0c\x00\x01\x06\x0c\x06\x4d\x65\x74\x61\x34\x32\x0a\x69\x6e\x69\x74\x69\x61\x6c\x69\x7a\x65\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x01\x03\x0e\x00\x11\x00\x02"
META42_MINT_TOKEN=b"\xa1\x1c\xeb\x0b\x03\x00\x00\x00\x05\x01\x00\x02\x03\x02\x05\x05\x07\x0a\x07\x11\x12\x08\x23\x10\x00\x00\x00\x01\x02\x01\x00\x02\x0c\x0a\x02\x00\x02\x06\x0c\x0a\x02\x06\x4d\x65\x74\x61\x34\x32\x0a\x6d\x69\x6e\x74\x5f\x74\x6f\x6b\x65\x6e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x01\x04\x0e\x00\x0b\x01\x11\x00\x02"
META42_SHARE_TOKEN_BY_ID=b"\xa1\x1c\xeb\x0b\x03\x00\x00\x00\x05\x01\x00\x02\x03\x02\x05\x05\x07\x10\x07\x17\x19\x08\x30\x10\x00\x00\x00\x01\x02\x01\x00\x04\x0c\x05\x0a\x02\x0a\x02\x00\x04\x06\x0c\x05\x0a\x02\x0a\x02\x06\x4d\x65\x74\x61\x34\x32\x11\x73\x68\x61\x72\x65\x5f\x74\x6f\x6b\x65\x6e\x5f\x62\x79\x5f\x69\x64\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x01\x06\x0e\x00\x0a\x01\x0b\x02\x0b\x03\x11\x00\x02"
META42_SHARE_TOKEN_BY_INDEX=b"\xa1\x1c\xeb\x0b\x03\x00\x00\x00\x05\x01\x00\x02\x03\x02\x05\x05\x07\x0e\x07\x15\x1c\x08\x31\x10\x00\x00\x00\x01\x02\x01\x00\x04\x0c\x05\x03\x0a\x02\x00\x04\x06\x0c\x05\x03\x0a\x02\x06\x4d\x65\x74\x61\x34\x32\x14\x73\x68\x61\x72\x65\x5f\x74\x6f\x6b\x65\x6e\x5f\x62\x79\x5f\x69\x6e\x64\x65\x78\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x01\x06\x0e\x00\x0a\x01\x0a\x02\x0b\x03\x11\x00\x02"


META42_SCRIPT_ENCODER_MAP: typing.Dict[typing.Type[ScriptCall], typing.Callable[[ScriptCall], Script]] = {
    ScriptCall__Meta42Accept: encode_meta42_accept_script,
    ScriptCall__Meta42Initialize: encode_meta42_initialize_script,
    ScriptCall__Meta42MintToken: encode_meta42_mint_token_script,
    ScriptCall__Meta42ShareTokenById: encode_meta42_share_token_by_id_script,
    ScriptCall__Meta42ShareTokenByIndex: encode_meta42_share_token_by_index_script
}

# pyre-ignore
META42_SCRIPT_FUNCTION_ENCODER_MAP: typing.Dict[
    typing.Type[ScriptFunctionCall], typing.Callable[[ScriptFunctionCall], TransactionPayload]
] = {
    ScriptFunctionCall__Meta42Accept: encode_meta42_accept_script_function,
    ScriptFunctionCall__Meta42Initialize: encode_meta42_initialize_script_function,
    ScriptFunctionCall__Meta42MintToken: encode_meta42_mint_token_script_function,
    ScriptFunctionCall__Meta42ShareTokenById: encode_meta42_share_token_by_id_script_function,
    ScriptFunctionCall__Meta42ShareTokenByIndex: encode_meta42_share_token_by_index_script_function,
}


META42_SCRIPT_DECODER_MAP: typing.Dict[bytes, typing.Callable[[Script], ScriptCall]] = {
    META42_ACCEPT: decode_meta42_accept_script,
    META42_INITIALIZE: decode_meta42_initialize_script,
    META42_MINT_TOKEN: decode_meta42_mint_token_script,
    META42_SHARE_TOKEN_BY_ID: decode_meta42_share_token_by_id_script,
    META42_SHARE_TOKEN_BY_INDEX: decode_meta42_share_token_by_index_script,
}

META42_SCRIPT_FUNCTION_DECODER_MAP: typing.Dict[str, typing.Callable[[TransactionPayload], ScriptFunctionCall]] = {
    "META42accept": decode_meta42_accept_script_function,
    "META42initialize": decode_meta42_initialize_script_function,
    "META42mint_token": decode_meta42_mint_token_script_function,
    "META42share_token_by_id": decode_meta42_share_token_by_id_script_function,
    "META42share_token_by_index": decode_meta42_share_token_by_index_script_function,
}