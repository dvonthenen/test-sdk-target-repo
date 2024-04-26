# swagger_client.DefaultApi

All URIs are relative to *http://api.example.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_get**](DefaultApi.md#users_get) | **GET** /users | Returns a list of users.

# **users_get**
> list[str] users_get()

Returns a list of users.

Optional extended description in CommonMark or HTML.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    # Returns a list of users.
    api_response = api_instance.users_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->users_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

