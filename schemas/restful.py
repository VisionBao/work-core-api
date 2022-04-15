from pydantic import BaseModel
from pydantic.generics import GenericModel

from typing import TypeVar, Generic, Optional

T = TypeVar('T')
TT = TypeVar('TT')

class RestfulModel(GenericModel, Generic[T]):
    success: bool = True  # if request is success
    data: Optional[T] = None  # response data
    errorCode: Optional[str] = ''  # code for errorType
    errorMessage: Optional[str] = ''  # message display to user
    showType: Optional[
        str] = ''  # error display type： 0 silent; 1 message.warn; 2 message.error; 4 notification; 9 page
    traceId: Optional[str] = ''  # Convenient for back-end Troubleshooting: unique request ID
    host: Optional[str] = ''  # Convenient for backend Troubleshooting: host of current access server


class RestfulErrorModel(GenericModel, Generic[T]):
    success: bool = False  # if request is success
    data: Optional[T] = ''  # response data
    errorCode: Optional[str] = ''  # code for errorType
    errorMessage: Optional[str] = ''  # message display to user
    showType: Optional[
        str] = ''  # error display type： 0 silent; 1 message.warn; 2 message.error; 4 notification; 9 page
    traceId: Optional[str] = ''  # Convenient for back-end Troubleshooting: unique request ID
    host: Optional[str] = ''  # Convenient for backend Troubleshooting: host of current access server


class ListModel(GenericModel, Generic[TT]):
    list: Optional[TT] = ''
    current: Optional[int] = None
    pageSize: Optional[int] = None
    total: Optional[int] = None
