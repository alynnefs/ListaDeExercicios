import sys

from load_balancer import LoadBalancer


with open("input.txt", "r") as file:
    filereader = file.readlines()

ttask_invalid_mesage = (
    "ttask input is an invalid option. it should be a number between 1 or 10"
)

umax_invalid_mesage = (
    "umax input is an invalid option. it should be a number between 1 or 10"
)

tasks = [int(i.rstrip("\n")) for i in filereader]
TTASK = int(tasks[0])
if TTASK < 1 or TTASK > 10:
    print(ttask_invalid_mesage)
    sys.exit()

UMAX = int(tasks[1])
if UMAX < 1 or UMAX > 10:
    print(umax_invalid_mesage)
    sys.exit()

load_balancer = LoadBalancer(TTASK, UMAX)
tasks = tasks[2:]

with open("output.txt", "w") as output_file:
    for i in tasks:
        load_balancer.run_tasks()
        load_balancer.assign_task_to_server(i)
        load_balancer.calculate_user()
        output_file.write(load_balancer.output())
        output_file.write("\n")

    while len(load_balancer.servers):
        load_balancer.run_tasks()
        load_balancer.calculate_user()
        output_file.write(load_balancer.output())
        output_file.write("\n")

    output_file.write(str(load_balancer.total))
