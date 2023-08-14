from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view, action
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .serializers import RequestBaseModelSerializer, RequestHelpModelSerializer, RequestAcceptModelSerializer

from .models import Request
from accounts.models import User

from haversine import haversine


# class RequestModelViewSet(ModelViewSet):
#     queryset = Request.objects.all()
#     serializer_class = RequestBaseModelSerializer

#     @action(detail=False, methods=['GET'])
#     def get_request_all(self, request):
#         lat = request.GET.get('mentoLatitude', 0)
#         lon = request.GET.get('mentoLongitude', 0)
#         print(self)
#         data = {
#             'requests' : [{'category' : '주문기기','content' : '후기입니다','name' : 3,'acceptTime' : '2023.08.9 오후 1:00',},]
#         }
#         return Response(data)

class RequestList(APIView):
    def get(self, request):
        request_all = Request.objects.all()
        serializer = RequestBaseModelSerializer(request_all, many = True)
        return Response(serializer.data)

class RequestMento(APIView):
    def get(self, request): # 실시간 내게 들어온 요청(멘토)
        mento_lat = request.GET.get('mentoLatitude', 0)
        mento_lon = request.GET.get('mentoLongitude', 0)
        mento = (float(mento_lat), float(mento_lon))
        helps = Request.objects.values()
        print(helps)
        # print('\n\n\n')
        requests_list = []
        # 만약 멘토 멘티 거리가 설정한 거리 내이면 data dict에 넣기 아니면 넘어가기
        # 반복문을 Request db에 있는 개수만큼 돌리기
        # 이미 완료한 Request도 있기 때문에 acceptTime이나 mento 값 유무 기준으로 걸러서 없는 Request만 반복문 돌려야됨
        for i in range(len(helps)):
            if helps[i]['mento_id'] != None:
                continue
            menti_lat = helps[i]['mentiLatitude']
            menti_lon = helps[i]['mentiLongitude']
            menti = (float(menti_lat), float(menti_lon))
            distance = haversine(mento, menti, unit = 'km')
            if float(distance) <= 2.0:
                mentiName = User.objects.get(id=helps[i]['menti_id']).name
                requests_list.append({'category': helps[i]['category'],'content': helps[i]['content'],'mentiName': mentiName,'distance': distance})
        data = {'requests' : requests_list}
        print(data)
        return Response(data)
    
    
class RequestMenti(APIView):
    def post(self, request): # 멘티의 도움 요청
        data = request.data
        serializer = RequestHelpModelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class RequestDatail(APIView):
    def get(self, request, pk): # 멘티 위치 상세보기
        menti_lat = Request.objects.get(id=pk).mentiLatitude
        menti_lon = Request.objects.get(id=pk).mentiLongitude
        data = {'mentiLatitude': menti_lat, 'mentiLongitude': menti_lon}
        return Response(data)
        
    
    def delete(self, request, pk): # 멘티의 요청 취소
        help = Request.objects.get(id=pk)
        help.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def patch(self, request, pk): # 멘토의 요청 수락
        data = request.data
        help = Request.objects.get(id=pk)
        serializer = RequestAcceptModelSerializer(help ,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
        


class RequestRecord(APIView):
    def get(self, request, pk): # 멘티이면 요청내역, 멘토이면 도움내역 근데 주는 건 같음
        role = User.objects.get(id=pk).role
        record_list = []

        if role =='멘티':
            records = Request.objects.filter(menti = pk).values()
            for i in range(len(records)):
                if records[i]['mento_id'] == None: # 아직 멘토가 수락하지 않은 요청 (미완료라고 표시)
                    mentoName = None
                else:
                    mentoName = User.objects.get(id=records[i]['mento_id']).name
                record_list.append({'category': records[i]['category'],'content': records[i]['content'],'mentoName': mentoName,'requestTime': records[i]['requestTime']})
        
        elif role == '멘토':
            records = Request.objects.filter(mento = pk).values()
            for i in range(len(records)):
                mentiName = User.objects.get(id=records[i]['menti_id']).name
                record_list.append({'category': records[i]['category'],'content': records[i]['content'],'mentiName': mentiName,'acceptTime': records[i]['acceptTime']})
        
        data = {'records' : record_list}
        return Response(data)
    