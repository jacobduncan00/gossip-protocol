import argparse
from colorama import Fore, Back, Style
from random import randint

def gossip_protocol(n, x):
    remaining_nodes = list(range(n))
    infected_nodes = [0]
    buffer = [0]
    g = 0
    while buffer:
        for j in range(x):
            random_node = remaining_nodes[randint(0, len(remaining_nodes) - 1)]
            if random_node not in infected_nodes:
                buffer.append(random_node)
                infected_nodes.append(random_node)
        buffer.pop()
        g += 1
    if len(infected_nodes) == n:
        print(Fore.GREEN + Style.BRIGHT + '[PASS] ' + Style.RESET_ALL)
        print(Fore.MAGENTA + Style.BRIGHT + '[MSG] ' + Style.RESET_ALL + 'The packet reached all nodes')
        # after     {} iterations'.format(g))
        return 1
    else:
        print(Fore.RED + Style.BRIGHT + '[FAIL] ' + Style.RESET_ALL)
        print(Fore.MAGENTA + Style.BRIGHT + '[MSG] ' + Style.RESET_ALL + 'The packet did NOT reach all nodes')
        # after {} iterations'.format(g))
        return 0

def protocol_iterator(n, x, iterations, protocol=gossip_protocol):
    success_count = 0
    for i in range(iterations):
        print(Fore.BLUE + Style.BRIGHT + "[ITERATION {}]".format(i) + Style.RESET_ALL)
        success_count += protocol(n, x)
        print()
    print('In' + Fore.MAGENTA, round((success_count / iterations * 100)),
    '%' + Style.RESET_ALL + ' of cases all nodes received the packet')


if __name__ == "__main__":
    # n = nodes, x = steps
    protocol_iterator(n=20, x=4, iterations=100, protocol=gossip_protocol)
