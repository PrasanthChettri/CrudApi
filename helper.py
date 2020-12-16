def ResponseModel(data, message):
    #helper Response Func
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }
