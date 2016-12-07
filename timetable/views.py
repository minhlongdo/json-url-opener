# -*- coding: utf-8 -*-
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from storage.jsonstorage import JsonStorage


jsonStorage = JsonStorage()


@api_view(['GET'])
def retrieve_data(request, file):
	print("Received file argument " + file)
	try:
		json_data = jsonStorage.read(file[0:])
		
		if json_data is None:
			return Response("There is no data", status=status.HTTP_204_NO_CONTENT)
		
		return Response(data=json_data, status=status.HTTP_302_FOUND)
	
	except FileNotFoundError:
		return Response("File not found", status=status.HTTP_400_BAD_REQUEST)
	
	except IOError:
		return Response("Issue with IO", status=status.HTTP_400_BAD_REQUEST)
	
	except Exception:
		return Response("Unexpected error", status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST', 'PUT'])
def upload_data(request):
	data = request.data
	
	print("received data %s".format(data))
	
	if data is None:
		return Response("Invalid data", status=status.HTTP_400_BAD_REQUEST)
	
	# Process json data and store it in storage
	try:
		jsonStorage.store(data['filename'], data['content'])
		return Response(status=status.HTTP_201_CREATED)
	
	except IOError:
		return Response("Failed to save the file", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
	
	except Exception:
		return Response("Something unexpected happened", status=status.HTTP_500_INTERNAL_SERVER_ERROR)
