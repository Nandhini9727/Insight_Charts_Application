from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# API view to provide candlestick chart data
class CandlestickDataView(APIView):
    def get(self, request):
        # Sample data for the candlestick chart
        data = {
            "data": [
                {"x": "2023-01-01", "open": 30, "high": 40, "low": 25, "close": 35},
                {"x": "2023-01-02", "open": 35, "high": 45, "low": 30, "close": 40},
            ]
        }
        # Return the data with a 200 OK status
        return Response(data, status=status.HTTP_200_OK)

# API view to provide data for the line chart
class LineChartDataView(APIView):
    def get(self, request):
        # Sample data for the line chart
        data = {
            "labels": ["Jan", "Feb", "Mar", "Apr"],  # X-axis labels
            "data": [10, 20, 30, 40]  # Corresponding Y-axis values
        }
        # Return the data with a 200 OK status
        return Response(data, status=status.HTTP_200_OK)

# API view to provide data for the bar chart
class BarChartDataView(APIView):
    def get(self, request):
        # Sample data for the bar chart
        data = {
            "labels": ["Product A", "Product B", "Product C"],  # Categories on the X-axis
            "data": [100, 150, 200]  # Values for each category (Y-axis)
        }
        # Return the data with a 200 OK status
        return Response(data, status=status.HTTP_200_OK)

# API view to provide data for the pie chart
class PieChartDataView(APIView):
    def get(self, request):
        # Sample data for the pie chart
        data = {
            "labels": ["Red", "Blue", "Yellow"],  # Categories for the pie slices
            "data": [300, 50, 100]  # Values corresponding to each slice of the pie
        }
        # Return the data with a 200 OK status
        return Response(data, status=status.HTTP_200_OK)
