
from django.http import JsonResponse
from django.views import View
from carapi.settings import ELASTICSEARCH_CLIENT
from .models import Car
from django.core import serializers
import json
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator



@method_decorator(login_required, name='dispatch')
class CarSearchView(View):
    def get(self, request):
    
        cars = Car.objects.all()
        data = serializers.serialize('json', cars)
        parsed_data = json.loads(data)

        # Index the data in Elasticsearch
        for car in parsed_data:
            # Assuming each car is a JSON object
            index_name = 'car_sales'  # Specify the Elasticsearch index name

            #print(parsed_data)
            document_id = car['pk']  # Specify the unique identifier for the document
            ELASTICSEARCH_CLIENT.index(index=index_name, id=document_id, document=car["fields"])

        print(ELASTICSEARCH_CLIENT.search(index='car_sales'))
        # Get search parameters from query parameters
        car_color = request.GET.get('car_color')
        number_of_cylinders = request.GET.get('number_of_cylinders')
        owner_name = request.GET.get('owner_name')

        print(car_color)
        print(number_of_cylinders)
        print(owner_name)

        # Build the Elasticsearch query
        query = {
                "bool": {
                    "must": [],
                }
            }


        # Add filters to the query
        if car_color:
            query["bool"]["must"].append({"match": {"car_color": car_color}})
        if number_of_cylinders:
            query["bool"]["must"].append({"match": {"number_of_cylinders": number_of_cylinders}})
        if owner_name:
            query["bool"]["must"].append({"match": {"owner_name": owner_name}})

        # Execute the search query
        response = ELASTICSEARCH_CLIENT.search(index='car_sales', query=query)
        print(response)
        # Process the search results
        hits = response['hits']['hits']
        results = []
        for hit in hits:
            car = hit['_source']
            results.append(car)

        # Return the search results as JSON
        return JsonResponse(results, safe=False)






