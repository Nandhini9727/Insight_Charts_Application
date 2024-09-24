from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class ChartDataViewTests(APITestCase):
    def test_candlestick_data_view(self):
        """Test the API response for the CandlestickDataView endpoint."""
        # Use the URL name 'candlestick-data' to reverse-resolve the URL for the API endpoint
        url = reverse('candlestick-data')
        # Send a GET request to the endpoint
        response = self.client.get(url)
        # Assert that the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Define the expected response data
        expected_data = {
            "data": [
                {"x": "2023-01-01", "open": 30, "high": 40, "low": 25, "close": 35},
                {"x": "2023-01-02", "open": 35, "high": 45, "low": 30, "close": 40},
            ]
        }
        # Assert that the JSON response matches the expected data
        self.assertEqual(response.json(), expected_data)

    def test_line_chart_data_view(self):
        """Test the API response for the LineChartDataView endpoint."""
        # Use the URL name 'line-chart-data' to reverse-resolve the URL for the API endpoint
        url = reverse('line-chart-data')
        # Send a GET request to the endpoint
        response = self.client.get(url)
        # Assert that the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Define the expected response data
        expected_data = {
            "labels": ["Jan", "Feb", "Mar", "Apr"],
            "data": [10, 20, 30, 40]
        }
        # Assert that the JSON response matches the expected data
        self.assertEqual(response.json(), expected_data)

    def test_bar_chart_data_view(self):
        """Test the API response for the BarChartDataView endpoint."""
        # Use the URL name 'bar-chart-data' to reverse-resolve the URL for the API endpoint
        url = reverse('bar-chart-data')
        # Send a GET request to the endpoint
        response = self.client.get(url)
        # Assert that the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Define the expected response data
        expected_data = {
            "labels": ["Product A", "Product B", "Product C"],
            "data": [100, 150, 200]
        }
        # Assert that the JSON response matches the expected data
        self.assertEqual(response.json(), expected_data)

    def test_pie_chart_data_view(self):
        """Test the API response for the PieChartDataView endpoint."""
        # Use the URL name 'pie-chart-data' to reverse-resolve the URL for the API endpoint
        url = reverse('pie-chart-data')
        # Send a GET request to the endpoint
        response = self.client.get(url)
        # Assert that the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Define the expected response data
        expected_data = {
            "labels": ["Red", "Blue", "Yellow"],
            "data": [300, 50, 100]
        }
        # Assert that the JSON response matches the expected data
        self.assertEqual(response.json(), expected_data)
