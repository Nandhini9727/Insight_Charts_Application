from django.urls import path
from .views import CandlestickDataView, LineChartDataView, BarChartDataView, PieChartDataView

urlpatterns = [
    # URL pattern for accessing candlestick chart data
    path('api/candlestick-data/', CandlestickDataView.as_view(), name='candlestick-data'),
    
    # URL pattern for accessing line chart data
    path('api/line-chart-data/', LineChartDataView.as_view(), name='line-chart-data'),
    
    # URL pattern for accessing bar chart data
    path('api/bar-chart-data/', BarChartDataView.as_view(), name='bar-chart-data'),
    
    # URL pattern for accessing pie chart data
    path('api/pie-chart-data/', PieChartDataView.as_view(), name='pie-chart-data'),
]
