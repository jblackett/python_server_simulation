'''
this module simulates users making requests to a server
it will check with load balancer to see which computer to use
'''

# import the load balancer
import load_balancer


# generate random numbers,
# ask load balancer which computer to use,
# make the request and print the results
if __name__ == '__main__':
    from random import randint

    # simulate requests
    for i in range(20):
        # create random numbers
        num_a = randint(5, 8)
        num_b = randint(5, 10)

        server = load_balancer.get_server()

        print('-'*8)
        print('using', server.get_name())
        print(server.multiply_handler(num_a, num_b))
        print('-'*8)
