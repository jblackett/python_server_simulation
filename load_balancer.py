'''
the load balancer
'''
# import servers modules
import computer1
import computer2
import computer3

# list of servers
SERVERS = [computer1, computer2, computer3]


# Load balancing algorithm
# alternates which computer is used in order
def get_server():
    '''
    switch between servers in order
    '''
    try:
        return next(get_server.s)
    except StopIteration:
        get_server.s = iter(SERVERS)
        return next(get_server.s)

setattr(get_server, 's', iter(SERVERS))

