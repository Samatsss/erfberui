from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import MealSerializer
from .models import Meal, Ingredients
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly

class MealGetList(ListCreateAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class MealOne(RetrieveUpdateAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer





class MealGet(APIView):
    def get(self, request):
        meals = Meal.objects.all()
        serializer = MealSerializer(meals, many=True)
        return Response({'data': serializer.data})

    def post(self, request):
        serializer = MealSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({'data': serializer.data})
    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if pk is None:
            return Response('Not pk')


        try:
            meal = Meal.objects.get(pk=pk)
        except:
            return Response('meal is no exist')

        serializer = MealSerializers(data=request.data, instance=meal)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response({'data': serializer.data})




