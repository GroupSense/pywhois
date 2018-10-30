

class PywhoisError(Exception):
    '''
    base exception
    '''


class WhoisServerNotFoundError(PywhoisError):
    '''
    Apparently some TLDs don't offer whois servers
    '''


class DomainNotFoundError(PywhoisError):
    '''
    Domain doesn't exist
    '''
