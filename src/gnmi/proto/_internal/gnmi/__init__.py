# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: github.com/openconfig/gnmi/proto/gnmi/gnmi.proto, github.com/openconfig/gnmi/proto/collector/collector.proto
# plugin: python-betterproto
from dataclasses import dataclass
from typing import AsyncIterable, AsyncIterator, Dict, Iterable, List, Optional, Union

import betterproto
import grpclib


class Encoding(betterproto.Enum):
    """
    Encoding defines the value encoding formats that are supported by the gNMI
    protocol. These encodings are used by both the client (when sending Set
    messages to modify the state of the target) and the target when serializing
    data to be returned to the client (in both Subscribe and Get RPCs).
    Reference: gNMI Specification Section 2.3
    """

    JSON = 0
    BYTES = 1
    PROTO = 2
    ASCII = 3
    JSON_IETF = 4


class SubscriptionMode(betterproto.Enum):
    """
    SubscriptionMode is the mode of the subscription, specifying how the target
    must return values in a subscription. Reference: gNMI Specification Section
    3.5.1.3
    """

    TARGET_DEFINED = 0
    ON_CHANGE = 1
    SAMPLE = 2


class SubscriptionListMode(betterproto.Enum):
    STREAM = 0
    ONCE = 1
    POLL = 2


class UpdateResultOperation(betterproto.Enum):
    INVALID = 0
    DELETE = 1
    REPLACE = 2
    UPDATE = 3


class GetRequestDataType(betterproto.Enum):
    ALL = 0
    CONFIG = 1
    STATE = 2
    OPERATIONAL = 3


@dataclass
class Notification(betterproto.Message):
    """
    Notification is a re-usable message that is used to encode data from the
    target to the client. A Notification carries two types of changes to the
    data tree:  - Deleted values (delete) - a set of paths that have been
    removed from the    data tree.  - Updated values (update) - a set of path-
    value pairs indicating the path    whose value has changed in the data
    tree. Reference: gNMI Specification Section 2.1
    """

    timestamp: int = betterproto.int64_field(1)
    prefix: "Path" = betterproto.message_field(2)
    # An alias for the path specified in the prefix field. Reference: gNMI
    # Specification Section 2.4.2
    alias: str = betterproto.string_field(3)
    update: List["Update"] = betterproto.message_field(4)
    delete: List["Path"] = betterproto.message_field(5)
    # This notification contains a set of paths that are always updated together
    # referenced by a globally unique prefix.
    atomic: bool = betterproto.bool_field(6)


@dataclass
class Update(betterproto.Message):
    """
    Update is a re-usable message that is used to store a particular Path,
    Value pair. Reference: gNMI Specification Section 2.1
    """

    path: "Path" = betterproto.message_field(1)
    value: "Value" = betterproto.message_field(2)
    val: "TypedValue" = betterproto.message_field(3)
    duplicates: int = betterproto.uint32_field(4)


@dataclass
class TypedValue(betterproto.Message):
    """
    TypedValue is used to encode a value being sent between the client and
    target (originated by either entity).
    """

    string_val: str = betterproto.string_field(1, group="value")
    int_val: int = betterproto.int64_field(2, group="value")
    uint_val: int = betterproto.uint64_field(3, group="value")
    bool_val: bool = betterproto.bool_field(4, group="value")
    bytes_val: bytes = betterproto.bytes_field(5, group="value")
    float_val: float = betterproto.float_field(6, group="value")
    decimal_val: "Decimal64" = betterproto.message_field(7, group="value")
    leaflist_val: "ScalarArray" = betterproto.message_field(8, group="value")
    any_val: "betterproto_lib_google_protobuf.Any" = betterproto.message_field(
        9, group="value"
    )
    json_val: bytes = betterproto.bytes_field(10, group="value")
    json_ietf_val: bytes = betterproto.bytes_field(11, group="value")
    ascii_val: str = betterproto.string_field(12, group="value")
    # Protobuf binary encoded bytes. The message type is not included. See the
    # specification at
    # github.com/openconfig/reference/blob/master/rpc/gnmi/protobuf-vals.md for a
    # complete specification.
    proto_bytes: bytes = betterproto.bytes_field(13, group="value")


@dataclass
class Path(betterproto.Message):
    """
    Path encodes a data tree path as a series of repeated strings, with each
    element of the path representing a data tree node name and the associated
    attributes. Reference: gNMI Specification Section 2.2.2.
    """

    # Elements of the path are no longer encoded as a string, but rather within
    # the elem field as a PathElem message.
    element: List[str] = betterproto.string_field(1)
    origin: str = betterproto.string_field(2)
    elem: List["PathElem"] = betterproto.message_field(3)
    target: str = betterproto.string_field(4)


@dataclass
class PathElem(betterproto.Message):
    """
    PathElem encodes an element of a gNMI path, along with any attributes
    (keys) that may be associated with it. Reference: gNMI Specification
    Section 2.2.2.
    """

    name: str = betterproto.string_field(1)
    key: Dict[str, str] = betterproto.map_field(
        2, betterproto.TYPE_STRING, betterproto.TYPE_STRING
    )


@dataclass
class Value(betterproto.Message):
    """
    Value encodes a data tree node's value - along with the way in which the
    value is encoded. This message is deprecated by gNMI 0.3.0. Reference: gNMI
    Specification Section 2.2.3.
    """

    value: bytes = betterproto.bytes_field(1)
    type: "Encoding" = betterproto.enum_field(2)


@dataclass
class Error(betterproto.Message):
    """
    Error message previously utilised to return errors to the client.
    Deprecated in favour of using the
    google.golang.org/genproto/googleapis/rpc/status message in the RPC
    response. Reference: gNMI Specification Section 2.5
    """

    code: int = betterproto.uint32_field(1)
    message: str = betterproto.string_field(2)
    data: "betterproto_lib_google_protobuf.Any" = betterproto.message_field(3)


@dataclass
class Decimal64(betterproto.Message):
    """
    Decimal64 is used to encode a fixed precision decimal number. The value is
    expressed as a set of digits with the precision specifying the number of
    digits following the decimal point in the digit set.
    """

    digits: int = betterproto.int64_field(1)
    precision: int = betterproto.uint32_field(2)


@dataclass
class ScalarArray(betterproto.Message):
    """ScalarArray is used to encode a mixed-type array of values."""

    # The set of elements within the array. Each TypedValue message should
    # specify only elements that have a field identifier of 1-7 (i.e., the values
    # are scalar values).
    element: List["TypedValue"] = betterproto.message_field(1)


@dataclass
class SubscribeRequest(betterproto.Message):
    """
    SubscribeRequest is the message sent by the client to the target when
    initiating a subscription to a set of paths within the data tree. The
    request field must be populated and the initial message must specify a
    SubscriptionList to initiate a subscription. The message is subsequently
    used to define aliases or trigger polled data to be sent by the target.
    Reference: gNMI Specification Section 3.5.1.1
    """

    subscribe: "SubscriptionList" = betterproto.message_field(1, group="request")
    poll: "Poll" = betterproto.message_field(3, group="request")
    aliases: "AliasList" = betterproto.message_field(4, group="request")
    # Extension messages associated with the SubscribeRequest. See the gNMI
    # extension specification for further definition.
    extension: List["_gnmi_ext__.Extension"] = betterproto.message_field(5)


@dataclass
class Poll(betterproto.Message):
    """
    Poll is sent within a SubscribeRequest to trigger the device to send
    telemetry updates for the paths that are associated with the subscription.
    Reference: gNMI Specification Section Section 3.5.1.4
    """

    pass


@dataclass
class SubscribeResponse(betterproto.Message):
    """
    SubscribeResponse is the message used by the target within a Subscribe RPC.
    The target includes a Notification message which is used to transmit values
    of the path(s) that are associated with the subscription. The same message
    is to indicate that the target has sent all data values once (is
    synchronized). Reference: gNMI Specification Section 3.5.1.4
    """

    update: "Notification" = betterproto.message_field(1, group="response")
    # Indicate target has sent all values associated with the subscription at
    # least once.
    sync_response: bool = betterproto.bool_field(3, group="response")
    # Deprecated in favour of google.golang.org/genproto/googleapis/rpc/status
    error: "Error" = betterproto.message_field(4, group="response")
    # Extension messages associated with the SubscribeResponse. See the gNMI
    # extension specification for further definition.
    extension: List["_gnmi_ext__.Extension"] = betterproto.message_field(5)


@dataclass
class SubscriptionList(betterproto.Message):
    """
    SubscriptionList is used within a Subscribe message to specify the list of
    paths that the client wishes to subscribe to. The message consists of a
    list of (possibly prefixed) paths, and options that relate to the
    subscription. Reference: gNMI Specification Section 3.5.1.2
    """

    prefix: "Path" = betterproto.message_field(1)
    subscription: List["Subscription"] = betterproto.message_field(2)
    # Whether target defined aliases are allowed within the subscription.
    use_aliases: bool = betterproto.bool_field(3)
    qos: "QosMarking" = betterproto.message_field(4)
    mode: "SubscriptionListMode" = betterproto.enum_field(5)
    # Whether elements of the schema that are marked as eligible for aggregation
    # should be aggregated or not.
    allow_aggregation: bool = betterproto.bool_field(6)
    # The set of schemas that define the elements of the data tree that should be
    # sent by the target.
    use_models: List["ModelData"] = betterproto.message_field(7)
    # The encoding that the target should use within the Notifications generated
    # corresponding to the SubscriptionList.
    encoding: "Encoding" = betterproto.enum_field(8)
    # An optional field to specify that only updates to current state should be
    # sent to a client. If set, the initial state is not sent to the client but
    # rather only the sync message followed by any subsequent updates to the
    # current state. For ONCE and POLL modes, this causes the server to send only
    # the sync message (Sec. 3.5.2.3).
    updates_only: bool = betterproto.bool_field(9)


@dataclass
class Subscription(betterproto.Message):
    """
    Subscription is a single request within a SubscriptionList. The path
    specified is interpreted (along with the prefix) as the elements of the
    data tree that the client is subscribing to. The mode determines how the
    target should trigger updates to be sent. Reference: gNMI Specification
    Section 3.5.1.3
    """

    path: "Path" = betterproto.message_field(1)
    mode: "SubscriptionMode" = betterproto.enum_field(2)
    sample_interval: int = betterproto.uint64_field(3)
    # Indicates whether values that have not changed should be sent in a SAMPLE
    # subscription.
    suppress_redundant: bool = betterproto.bool_field(4)
    # Specifies the maximum allowable silent period in nanoseconds when
    # suppress_redundant is in use. The target should send a value at least once
    # in the period specified.
    heartbeat_interval: int = betterproto.uint64_field(5)


@dataclass
class QosMarking(betterproto.Message):
    """
    QOSMarking specifies the DSCP value to be set on transmitted telemetry
    updates from the target. Reference: gNMI Specification Section 3.5.1.2
    """

    marking: int = betterproto.uint32_field(1)


@dataclass
class Alias(betterproto.Message):
    """
    Alias specifies a data tree path, and an associated string which defines an
    alias which is to be used for this path in the context of the RPC. The
    alias is specified as a string which is prefixed with "#" to disambiguate
    it from data tree element paths. Reference: gNMI Specification Section
    2.4.2
    """

    path: "Path" = betterproto.message_field(1)
    alias: str = betterproto.string_field(2)


@dataclass
class AliasList(betterproto.Message):
    """
    AliasList specifies a list of aliases. It is used in a SubscribeRequest for
    a client to create a set of aliases that the target is to utilize.
    Reference: gNMI Specification Section 3.5.1.6
    """

    alias: List["Alias"] = betterproto.message_field(1)


@dataclass
class SetRequest(betterproto.Message):
    """
    SetRequest is sent from a client to the target to update values in the data
    tree. Paths are either deleted by the client, or modified by means of being
    updated, or replaced. Where a replace is used, unspecified values are
    considered to be replaced, whereas when update is used the changes are
    considered to be incremental. The set of changes that are specified within
    a single SetRequest are considered to be a transaction. Reference: gNMI
    Specification Section 3.4.1
    """

    prefix: "Path" = betterproto.message_field(1)
    delete: List["Path"] = betterproto.message_field(2)
    replace: List["Update"] = betterproto.message_field(3)
    update: List["Update"] = betterproto.message_field(4)
    # Extension messages associated with the SetRequest. See the gNMI extension
    # specification for further definition.
    extension: List["_gnmi_ext__.Extension"] = betterproto.message_field(5)


@dataclass
class SetResponse(betterproto.Message):
    """
    SetResponse is the response to a SetRequest, sent from the target to the
    client. It reports the result of the modifications to the data tree that
    were specified by the client. Errors for this RPC should be reported using
    the https://github.com/googleapis/googleapis/blob/master/google/rpc/status.
    proto message in the RPC return. The gnmi.Error message can be used to add
    additional details where required. Reference: gNMI Specification Section
    3.4.2
    """

    prefix: "Path" = betterproto.message_field(1)
    # A set of responses specifying the result of the operations specified in the
    # SetRequest.
    response: List["UpdateResult"] = betterproto.message_field(2)
    message: "Error" = betterproto.message_field(3)
    timestamp: int = betterproto.int64_field(4)
    # Extension messages associated with the SetResponse. See the gNMI extension
    # specification for further definition.
    extension: List["_gnmi_ext__.Extension"] = betterproto.message_field(5)


@dataclass
class UpdateResult(betterproto.Message):
    """
    UpdateResult is used within the SetResponse message to communicate the
    result of an operation specified within a SetRequest message. Reference:
    gNMI Specification Section 3.4.2
    """

    # Deprecated timestamp for the UpdateResult, this field has been replaced by
    # the timestamp within the SetResponse message, since all mutations effected
    # by a set should be applied as a single transaction.
    timestamp: int = betterproto.int64_field(1)
    path: "Path" = betterproto.message_field(2)
    message: "Error" = betterproto.message_field(3)
    op: "UpdateResultOperation" = betterproto.enum_field(4)


@dataclass
class GetRequest(betterproto.Message):
    """
    GetRequest is sent when a client initiates a Get RPC. It is used to specify
    the set of data elements for which the target should return a snapshot of
    data. The use_models field specifies the set of schema modules that are to
    be used by the target - where use_models is not specified then the target
    must use all schema models that it has. Reference: gNMI Specification
    Section 3.3.1
    """

    prefix: "Path" = betterproto.message_field(1)
    path: List["Path"] = betterproto.message_field(2)
    type: "GetRequestDataType" = betterproto.enum_field(3)
    encoding: "Encoding" = betterproto.enum_field(5)
    use_models: List["ModelData"] = betterproto.message_field(6)
    # Extension messages associated with the GetRequest. See the gNMI extension
    # specification for further definition.
    extension: List["_gnmi_ext__.Extension"] = betterproto.message_field(7)


@dataclass
class GetResponse(betterproto.Message):
    """
    GetResponse is used by the target to respond to a GetRequest from a client.
    The set of Notifications corresponds to the data values that are requested
    by the client in the GetRequest. Reference: gNMI Specification Section
    3.3.2
    """

    notification: List["Notification"] = betterproto.message_field(1)
    error: "Error" = betterproto.message_field(2)
    # Extension messages associated with the GetResponse. See the gNMI extension
    # specification for further definition.
    extension: List["_gnmi_ext__.Extension"] = betterproto.message_field(3)


@dataclass
class CapabilityRequest(betterproto.Message):
    """
    CapabilityRequest is sent by the client in the Capabilities RPC to request
    that the target reports its capabilities. Reference: gNMI Specification
    Section 3.2.1
    """

    # Extension messages associated with the CapabilityRequest. See the gNMI
    # extension specification for further definition.
    extension: List["_gnmi_ext__.Extension"] = betterproto.message_field(1)


@dataclass
class CapabilityResponse(betterproto.Message):
    """
    CapabilityResponse is used by the target to report its capabilities to the
    client within the Capabilities RPC. Reference: gNMI Specification Section
    3.2.2
    """

    supported_models: List["ModelData"] = betterproto.message_field(1)
    supported_encodings: List["Encoding"] = betterproto.enum_field(2)
    g_nmi_version: str = betterproto.string_field(3)
    # Extension messages associated with the CapabilityResponse. See the gNMI
    # extension specification for further definition.
    extension: List["_gnmi_ext__.Extension"] = betterproto.message_field(4)


@dataclass
class ModelData(betterproto.Message):
    """
    ModelData is used to describe a set of schema modules. It can be used in a
    CapabilityResponse where a target reports the set of modules that it
    supports, and within the SubscribeRequest and GetRequest messages to
    specify the set of models from which data tree elements should be reported.
    Reference: gNMI Specification Section 3.2.3
    """

    name: str = betterproto.string_field(1)
    organization: str = betterproto.string_field(2)
    version: str = betterproto.string_field(3)


@dataclass
class ReconnectRequest(betterproto.Message):
    target: List[str] = betterproto.string_field(1)


@dataclass
class Nil(betterproto.Message):
    pass


class GNmiStub(betterproto.ServiceStub):
    async def capabilities(
        self, *, extension: List["_gnmi_ext__.Extension"] = []
    ) -> "CapabilityResponse":
        """
        Capabilities allows the client to retrieve the set of capabilities that
        is supported by the target. This allows the target to validate the
        service version that is implemented and retrieve the set of models that
        the target supports. The models can then be specified in subsequent
        RPCs to restrict the set of data that is utilized. Reference: gNMI
        Specification Section 3.2
        """

        request = CapabilityRequest()
        if extension is not None:
            request.extension = extension

        return await self._unary_unary(
            "/gnmi.gNMI/Capabilities", request, CapabilityResponse
        )

    async def get(
        self,
        *,
        prefix: Optional["Path"] = None,
        path: List["Path"] = [],
        type: "GetRequestDataType" = 0,
        encoding: "Encoding" = 0,
        use_models: List["ModelData"] = [],
        extension: List["_gnmi_ext__.Extension"] = [],
    ) -> "GetResponse":
        """
        Retrieve a snapshot of data from the target. A Get RPC requests that
        the target snapshots a subset of the data tree as specified by the
        paths included in the message and serializes this to be returned to the
        client using the specified encoding. Reference: gNMI Specification
        Section 3.3
        """

        request = GetRequest()
        if prefix is not None:
            request.prefix = prefix
        if path is not None:
            request.path = path
        request.type = type
        request.encoding = encoding
        if use_models is not None:
            request.use_models = use_models
        if extension is not None:
            request.extension = extension

        return await self._unary_unary("/gnmi.gNMI/Get", request, GetResponse)

    async def set(
        self,
        *,
        prefix: Optional["Path"] = None,
        delete: List["Path"] = [],
        replace: List["Update"] = [],
        update: List["Update"] = [],
        extension: List["_gnmi_ext__.Extension"] = [],
    ) -> "SetResponse":
        """
        Set allows the client to modify the state of data on the target. The
        paths to modified along with the new values that the client wishes to
        set the value to. Reference: gNMI Specification Section 3.4
        """

        request = SetRequest()
        if prefix is not None:
            request.prefix = prefix
        if delete is not None:
            request.delete = delete
        if replace is not None:
            request.replace = replace
        if update is not None:
            request.update = update
        if extension is not None:
            request.extension = extension

        return await self._unary_unary("/gnmi.gNMI/Set", request, SetResponse)

    async def subscribe(
        self,
        request_iterator: Union[
            AsyncIterable["SubscribeRequest"], Iterable["SubscribeRequest"]
        ],
    ) -> AsyncIterator["SubscribeResponse"]:
        """
        Subscribe allows a client to request the target to send it values of
        particular paths within the data tree. These values may be streamed at
        a particular cadence (STREAM), sent one off on a long-lived channel
        (POLL), or sent as a one-off retrieval (ONCE). Reference: gNMI
        Specification Section 3.5
        """

        async for response in self._stream_stream(
            "/gnmi.gNMI/Subscribe",
            request_iterator,
            SubscribeRequest,
            SubscribeResponse,
        ):
            yield response


class CollectorStub(betterproto.ServiceStub):
    async def reconnect(self, *, target: List[str] = []) -> "Nil":
        """
        Reconnect requests that the existing connections for one or more
        specified targets will be stopped and new connections established.
        """

        request = ReconnectRequest()
        request.target = target

        return await self._unary_unary("/gnmi.Collector/Reconnect", request, Nil)


from .. import gnmi_ext as _gnmi_ext__
import betterproto.lib.google.protobuf as betterproto_lib_google_protobuf
