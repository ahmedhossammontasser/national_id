from django.shortcuts import render
from .serializers import *
from rest_framework import permissions, status
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from .services import NationalIdService


class NationalIDViewSet(generics.GenericAPIView):

	def get(self, request, *args, **kwargs):
		nationalid = self.request.query_params.get('nationalid', None)
		content = {
			"data": None,
			"msg": "failed"
		}
		national_id_service = NationalIdService(nationalid)
		if not national_id_service.is_valid():
			content["data"] = "Invalid National ID"
			return Response(content, status=status.HTTP_400_BAD_REQUEST)

		info_is_valid, natioanl_id_info = national_id_service.extract_informations_valid()
		if not info_is_valid:
			content["data"] = "Invalid National ID"
			return Response(content, status=status.HTTP_400_BAD_REQUEST)		 

		return Response(NationalIDInfoSerializer(natioanl_id_info).data)
