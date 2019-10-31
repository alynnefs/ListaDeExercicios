# flake8: noqa
from unittest import TestCase

from load_balancer import LoadBalancer
from server import Server


class TestLoadBalancer(TestCase):
    def setUp(self) -> None:
        self.load_balancer = LoadBalancer(4, 2)

    def test_create_a_server_should_return_a_server_instance(self):
        server = self.load_balancer.create_a_server()
        self.assertIsInstance(server, Server)

    def test_calculate_user_should_return_one_when_exist_only_one_server_with_one_running_task(self):
        self.load_balancer.assign_task_to_server(1)
        expected = 1
        result = self.load_balancer.calculate_user()
        self.assertEqual(expected, result)

    def test_run_tasks_should_reduce_ttask_user_attribute_by_one(self):
        self.load_balancer.assign_task_to_server(1)
        self.load_balancer.run_tasks()
        expected = 3
        result = self.load_balancer.servers[0].users[0].ttask
        self.assertEqual(expected, result)

    def test_output_should_return_two_comma_two_when_exist_four_active_users(self):
        self.load_balancer.assign_task_to_server(4)
        expected = "2, 2"
        result = self.load_balancer.output()
        self.assertEqual(expected, result)

    def test_assign_task_to_server_should_create_a_server_for_a_task_when_there_is_no_server_running(self):
        self.load_balancer.assign_task_to_server(1)
        expected = 1
        result = len(self.load_balancer.servers)
        self.assertEqual(expected, result)

    def test_assign_task_to_server_should_not_create_a_server_for_a_task_when_there_is_an_available_server_running(self):
        self.load_balancer.assign_task_to_server(1)
        self.load_balancer.assign_task_to_server(1)
        expected = 1
        result = len(self.load_balancer.servers)
        self.assertEqual(expected, result)

    def test_assign_task_to_server_should_create_a_new_instance_when_there_is_a_server_running_but_not_available(self):
        self.load_balancer.assign_task_to_server(2)
        self.load_balancer.assign_task_to_server(1)
        expected = 2
        result = len(self.load_balancer.servers)
        self.assertEqual(expected, result)
