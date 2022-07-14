def pingcheck(ip):
    import os
    resp = os.system('ping {} -n 8'.format(ip))
    return resp
