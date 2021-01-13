# Copyright 2019 Robert Bosch GmbH
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest

from tracetools_test.case import TraceTestCase


class TestTimer(TraceTestCase):

    def __init__(self, *args) -> None:
        super().__init__(
            *args,
            session_name_prefix='session-test-timer-all',
            events_ros=[
                'ros2:rcl_node_init',
                'ros2:rcl_timer_init',
                'ros2:rclcpp_timer_callback_added',
                'ros2:rclcpp_timer_link_node',
                'ros2:callback_start',
                'ros2:callback_end',
            ],
            nodes=['test_timer'],
        )

    def test_all(self):
        # Check events as set
        self.assertEventsSet(self._events_ros)

        # Check fields
        init_events = self.get_events_with_name('ros2:rcl_timer_init')
        for event in init_events:
            self.assertValidHandle(event, 'timer_handle')
            period_value = self.get_field(event, 'period')
            self.assertIsInstance(period_value, int)
            self.assertGreaterEqual(period_value, 0, f'invalid period value: {period_value}')

        callback_added_events = self.get_events_with_name('ros2:rclcpp_timer_callback_added')
        for event in callback_added_events:
            self.assertValidHandle(event, ['timer_handle', 'callback'])

        link_node_events = self.get_events_with_name('ros2:rclcpp_timer_link_node')
        for event in link_node_events:
            self.assertValidHandle(event, ['timer_handle', 'node_handle'])

        start_events = self.get_events_with_name('ros2:callback_start')
        for event in start_events:
            self.assertValidHandle(event, 'callback')
            # Should not be 1 for timer
            self.assertFieldEquals(
                event,
                'is_intra_process',
                0,
                'invalid value for is_intra_process',
            )

        end_events = self.get_events_with_name('ros2:callback_end')
        for event in end_events:
            self.assertValidHandle(event, 'callback')

        # Find and check given timer period
        test_timer_init_event = self.get_events_with_procname('test_timer', init_events)
        self.assertNumEventsEqual(test_timer_init_event, 1, 'none or more test timer init events')
        test_init_event = test_timer_init_event[0]
        self.assertFieldEquals(test_init_event, 'period', 1000000, 'invalid period')

        # Check that the timer_init:callback_added pair exists and has a common timer handle
        self.assertMatchingField(
            test_init_event,
            'timer_handle',
            None,
            callback_added_events,
        )
        callback_added_event = callback_added_events[0]

        # Check that there is a link_node event for the timer
        self.assertMatchingField(
            test_init_event,
            'timer_handle',
            None,
            link_node_events,
        )
        # And that the node from that node handle exists
        node_init_events = self.get_events_with_name('ros2:rcl_node_init')
        self.assertNumEventsEqual(node_init_events, 1)
        node_init_event = node_init_events[0]
        self.assertMatchingField(
            node_init_event,
            'node_handle',
            None,
            link_node_events,
        )

        # Check that the callback events correspond to the registered timer callback
        self.assertMatchingField(
            callback_added_event,
            'callback',
            None,
            start_events,
        )
        self.assertMatchingField(
            callback_added_event,
            'callback',
            None,
            end_events,
        )

        # Check that a callback start:end pair has a common callback handle
        for start_event in start_events:
            self.assertMatchingField(
                start_event,
                'callback',
                None,
                end_events,
            )


if __name__ == '__main__':
    unittest.main()
