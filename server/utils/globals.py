import secrets
from flask_restplus import Resource, abort, reqparse, fields


def unpack(j, *args, **kargs):
    if kargs.get("required", True):
        not_found = [arg for arg in args if arg not in j]
        if not_found:
            expected = ", ".join(map(str, not_found))
            abort(kargs.get("error", 400), "Expected request object to contain: " + expected)
    return [j.get(arg, None) for arg in args]
