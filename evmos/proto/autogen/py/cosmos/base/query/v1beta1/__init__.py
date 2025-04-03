# Generated by the protocol buffer compiler.  DO NOT EDIT!
# sources: cosmos/base/query/v1beta1/pagination.proto
# plugin: python-betterproto
# This file has been @generated

from dataclasses import dataclass

import betterproto


@dataclass(eq=False, repr=False)
class PageRequest(betterproto.Message):
    """
    PageRequest is to be embedded in gRPC request messages for efficient
    pagination. Ex:
     message SomeRequest {
             Foo some_parameter = 1;
             PageRequest pagination = 2;
     }
    """

    key: bytes = betterproto.bytes_field(1)
    """
    key is a value returned in PageResponse.next_key to begin
    querying the next page most efficiently. Only one of offset or key
    should be set.
    """

    offset: int = betterproto.uint64_field(2)
    """
    offset is a numeric offset that can be used when key is unavailable.
    It is less efficient than using key. Only one of offset or key should
    be set.
    """

    limit: int = betterproto.uint64_field(3)
    """
    limit is the total number of results to be returned in the result page.
    If left empty it will default to a value to be set by each app.
    """

    count_total: bool = betterproto.bool_field(4)
    """
    count_total is set to true  to indicate that the result set should include
    a count of the total number of items available for pagination in UIs.
    count_total is only respected when offset is used. It is ignored when key
    is set.
    """

    reverse: bool = betterproto.bool_field(5)
    """
    reverse is set to true if results are to be returned in the descending order.
    Since: cosmos-sdk 0.43
    """


@dataclass(eq=False, repr=False)
class PageResponse(betterproto.Message):
    """
    PageResponse is to be embedded in gRPC response messages where the
    corresponding request message has used PageRequest.
     message SomeResponse {
             repeated Bar results = 1;
             PageResponse page = 2;
     }
    """

    next_key: bytes = betterproto.bytes_field(1)
    """
    next_key is the key to be passed to PageRequest.key to
    query the next page most efficiently
    """

    total: int = betterproto.uint64_field(2)
    """
    total is total number of results available if PageRequest.count_total
    was set, its value is undefined otherwise
    """
