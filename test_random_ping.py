import unittest
import requests
from unittest.mock import patch, MagicMock

import random_ping  # replace with the actual name of your script file, e.g., 'import random_ping'

class TestPingUrl(unittest.TestCase):
    @patch("random_ping.requests.get")
    @patch("random_ping.logging.info")
    def test_ping_url_success(self, mock_logging_info, mock_requests_get):
        # Mock a successful response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_requests_get.return_value = mock_response

        # Call the function
        random_ping.ping_url("https://example.com")

        # Check that logging was called with the expected status code
        mock_logging_info.assert_any_call("Pinged https://example.com - Status Code: 200")

    @patch("random_ping.requests.get", side_effect=requests.RequestException("Connection error"))
    @patch("random_ping.logging.info")
    def test_ping_url_failure(self, mock_logging_info, mock_requests_get):
        # Call the function with a mocked failure
        random_ping.ping_url("https://example.com")

        # Check that logging was called with the error message
        mock_logging_info.assert_any_call("Failed to ping https://example.com - Error: Connection error")

class TestRunRandomPing(unittest.TestCase):
    @patch("random_ping.ping_url")
    @patch("random_ping.logging.info")
    @patch("random_ping.time.sleep", side_effect=lambda x: None)  # Skip sleep to speed up tests
    @patch("random_ping.random.randint", return_value=5)  # Set random wait time for predictability
    def test_run_random_ping(self, mock_randint, mock_sleep, mock_logging_info, mock_ping_url):
        # Stop after one loop for test purposes
        with patch("random_ping.run_random_ping", side_effect=KeyboardInterrupt):
            try:
                random_ping.run_random_ping("https://example.com", 10)
            except KeyboardInterrupt:
                pass  # Expected for test

        # Verify logging calls
        mock_logging_info.assert_any_call("Waiting for 5 seconds before the next ping.")
        mock_ping_url.assert_called_with("https://example.com")

    @patch("random_ping.ping_url")
    @patch("random_ping.time.sleep", side_effect=KeyboardInterrupt)  # Raise exception to exit loop after 1 iteration
    def test_run_random_ping_interrupt(self, mock_sleep, mock_ping_url):
        with self.assertRaises(KeyboardInterrupt):
            random_ping.run_random_ping("https://example.com", 10)

        # Ensure that ping_url was called only once
        mock_ping_url.assert_called_once_with("https://example.com")

if __name__ == "__main__":
    unittest.main()
