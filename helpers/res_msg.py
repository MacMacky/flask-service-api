responses = {
    200: "SUCCESS",
    400: "No Data Found!",
    401: "Unauthorized!",
    404: "Not Found!",
    408: "Request Timeout!",
    409: "The request could not be completed due to a conflict with the current state of the resource.",
    463: "The HTTP POST data has lacking required parameters. This would be a good time to double check spelling.",
    500: "Internal Server Error.",
    503: "Service Unavailable.",
    0: "Unable to process request. The system encountered some technical problem. Sorry for the inconvenience.",
    1: "Unable to process request. Please review your data and try again.",
    2: "Unable to process request. Connection timeout occured. Please try again later.",
    3: "Unable to process request. Failed in connecting to server. Please try again later.",
    4: "Incorrect Username Or Password. Please Try Again.",
    5: "RequiredParameterMissing.",
    6: "Email and Password Field Empty!",
    7: "Email Field Required!",
    8: "Password Field Required",
    9: "Wrong Email/Password!",
    10: "Success in Sending Email Message.",
    11: "Failed in Sending Email Message. Something went wrong. Please try again later.",
    12: "Seller Successfully Enabled.",
    13: "The minimum password length must be greater than 5 characters and maximum password length is 20 characters",
    14: "Password must have at least one lowercase letter, one uppercase letter, one digit and one special character.",
    15: "Password Successfully Changed.",
    16: "No Token Provided.",
    17: "Invalid Token.",
}


def res_msg(code: int = 0) -> str:
    try:
        return responses[code]
    except KeyError as e:
        return responses[0]

