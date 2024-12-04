import pytest
from battery import Battery
from unittest.mock import Mock

todo = pytest.mark.skip(reason='todo: pending spec')

@pytest.fixture
def charged_battery():
    return Battery(100)

@pytest.fixture
def partially_charged_battery():
    b = Battery(100)
    b.mCharge = 70
    return b


'''
Design and implement unit test cases in a program called test_battery.py that thoroughly verify the functionality of the methods. For all but the parts of recharge and drain that interact with the 'external monitor' do not use test doubles - just write asserts to ensure that the functions correctly change the state of the battery. 
'''


def describe_Battery():

    def describe_recharge():
        # your test cases here
        def it_should_recharge_the_battery_by_the_amount_specified(partially_charged_battery):
            assert partially_charged_battery.recharge(20) == True
            assert partially_charged_battery.mCharge == 90

        def it_should_not_recharge_the_battery_by_a_negative_amount(charged_battery):
            assert charged_battery.recharge(-20) == False
            assert charged_battery.mCharge == 100

        def it_should_not_recharge_the_battery_past_its_capacity(charged_battery):
            assert charged_battery.recharge(20) == False
            assert charged_battery.mCharge == 100

    def describe_drain():
        # your test cases here
        def it_should_drain_the_battery_by_the_amount_specified(partially_charged_battery):
            assert partially_charged_battery.drain(20) == True
            assert partially_charged_battery.mCharge == 50

        def it_should_not_drain_the_battery_by_a_negative_amount(partially_charged_battery):
            assert partially_charged_battery.drain(-20) == False
            assert partially_charged_battery.mCharge == 70

        def it_should_not_drain_the_battery_past_its_capacity(partially_charged_battery):
            assert partially_charged_battery.drain(80) == True
            assert partially_charged_battery.mCharge == 0     


'''
For the external monitor portion of recharge and drain, implement test doubles for the notify_recharge and notify_drain methods as you deem appropriate.  Use stubs to force the desired test outcomes, and use mocks to verify correct implementation details. (That the function was called correctly as a part of recharge and drain.)
'''   

def describe_Battery_with_external_monitor():

    def describe_recharge():
        # your test cases here
        def it_should_notify_external_monitor_of_recharge(partially_charged_battery):
            monitor = Mock()
            partially_charged_battery.external_monitor = monitor
            partially_charged_battery.recharge(20)
            monitor.notify_recharge.assert_called_once_with(90)

        def it_should_not_notify_external_monitor_of_recharge_when_not_recharging_with_negative_amount(partially_charged_battery):
            monitor = Mock()
            partially_charged_battery.external_monitor = monitor
            partially_charged_battery.recharge(-20)
            monitor.notify_recharge.assert_not_called()

        def it_should_not_notify_external_monitor_of_recharge_when_not_recharging_past_capacity(charged_battery):
            monitor = Mock()
            charged_battery.external_monitor = monitor
            charged_battery.recharge(20)
            monitor.notify_recharge.assert_not_called()

    def describe_drain():
        # your test cases here
        def it_should_notify_external_monitor_of_drain_when_draining(partially_charged_battery):
            monitor = Mock()
            partially_charged_battery.external_monitor = monitor
            partially_charged_battery.drain(20)
            monitor.notify_drain.assert_called_once_with(50)

        def it_should_not_notify_external_monitor_of_drain_when_draining_with_negative_amount(partially_charged_battery):
            monitor = Mock()
            partially_charged_battery.external_monitor = monitor
            partially_charged_battery.drain(-20)
            monitor.notify_drain.assert_not_called()