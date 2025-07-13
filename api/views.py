from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.views import APIView
from django.utils.dateparse import parse_date
from .models import WheelSpecification
from .serializers import WheelSpecificationSerializer, BogieChecksheetSerializer

class WheelSpecCreateView(APIView):
    def post(self, request):
        serializer = WheelSpecificationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(status="Saved")
        return Response({
            "success": True,
            "message": "Wheel specification submitted successfully.",
            "data": {
                "formNumber": serializer.data['formNumber'],
                "submittedBy": serializer.data['submittedBy'],
                "submittedDate": serializer.data['submittedDate'],
                "status": serializer.data['status']
            }
        }, status=status.HTTP_201_CREATED)

    def get(self, request):
        form_number = request.GET.get('formNumber')
        submitted_by = request.GET.get('submittedBy')
        submitted_date = request.GET.get('submittedDate')

        filters = {}
        if form_number:
            filters['formNumber'] = form_number
        if submitted_by:
            filters['submittedBy'] = submitted_by
        if submitted_date:
            filters['submittedDate'] = parse_date(submitted_date)

        queryset = WheelSpecification.objects.filter(**filters)
        serializer = WheelSpecificationSerializer(queryset, many=True)

        return Response({
            "success": True,
            "message": "Filtered wheel specification forms fetched successfully.",
            "data": serializer.data
        }, status=200)


class BogieChecksheetCreateView(generics.CreateAPIView):
    serializer_class = BogieChecksheetSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(status="Saved")
        return Response({
            "success": True,
            "message": "Bogie checksheet submitted successfully.",
            "data": {
                "formNumber": serializer.data['formNumber'],
                "inspectionBy": serializer.data['inspectionBy'],
                "inspectionDate": serializer.data['inspectionDate'],
                "status": serializer.data['status']
            }
        }, status=status.HTTP_201_CREATED)
