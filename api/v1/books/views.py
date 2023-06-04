from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.db.models import Q
from books.models import Category, Book
from api.v1.books.serializers import BookSerializer


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def books(request):
    instances = Book.objects.filter()

    q = request.GET.get("q")

    if q:
        instances = instances.filter(
            Q(name__icontains=q) | Q(publisher_name__icontains=q))

    context = {
        "request": request
    }
    serializer = BookSerializer(instances, many=True, context=context)
    response_data = {
        "status_code": 6000,
        "data": serializer.data
    }
    return Response(response_data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def bookssingle(request, pk):
    if Book.objects.filter(pk=pk).exists():
        instance = Book.objects.get(pk=pk)
        context = {
            "request": request
        }

        serializer = BookSerializer(instance, context=context)
        response_data = {
            "status_code": 6000,
            "data": serializer.data
        }
        return Response(response_data)
    else:
        response_data = {
            "status_code": 6001,
            "message": "This Book doesn't exist"
        }
        return Response(response_data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create(request):
    serializer = BookSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        response_data = {
            "status_code": 6000,
            "message": "book added successfully"
        }

        return Response(response_data)
    else:
        response_data = {
            "status_code": 6001,
            "message": "Validation Error",
            "data": serializer.errors
        }

        return Response(response_data)


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete(request, pk):
    try:
        book = Book.objects.get(id=pk)
        book.delete()
        response_data = {
            "status_code": 6000,
            "message": "Book deleted successfully!"
        }
    except Book.DoesNotExist:
        response_data = {
            "status_code": 6001,
            "message": "This Book doesn't exist"
        }

    return Response(response_data)


# @api_view(['PUT'])
# @permission_classes([IsAuthenticated])
# def update(request, pk):
#     try:
#         book = Book.objects.get(pk=pk)
#         print(book)

#         serializer = BookSerializer(instance=book, data=request.data, partial=True)

#         if serializer.is_valid():
#             serializer.save()
#             response_data = {
#                 "status_code": 6000,
#                 "message": "Success",
#                 "data": serializer.data
#             }
#         else:
#             response_data = {
#                 "status_code": 6001,
#                 "message": "Validation Error",
#                 "data": serializer.errors
#             }

#         return Response(response_data)
#     except Book.DoesNotExist:
#         response_data = {
#             "status_code": 6001,
#             "message": "This Book doesn't exist"
#         }
#         return Response(response_data)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update(request, pk):
    if Book.objects.filter(pk=pk).exists():
        instance = Book.objects.get(pk=pk)
        print(instance, "==instance")
        serializer = BookSerializer(
            instance=instance, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            response_data = {
                'status': 6000,
                "message": "Book is updated successfully",
            }
            return Response(response_data)
    else:
        response_data = {
            'status': 6001,
            "message": "Book does not exist"

        }
        return Response(response_data)


@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def add_to_favorites(request, pk):
    if Book.objects.filter(pk=pk).exists():
        instance = Book.objects.get(pk=pk)
        instance.is_favourite = True
        response_data = {
            "status_code": 6000,
            "message": "Added to favorites"
        }
        return Response(response_data)
    else:
        response_data = {
            'status': 6001,
            "message": "Book does not exist"

        }
        return Response(response_data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_favorites(request):
    # Get the first matching book
    instance = Book.objects.filter(is_favourite=True).first()
    if instance:
        serializer = BookSerializer(instance, many=True)
        response_data = {
            "status_code": 6000,
            "data": serializer.data
        }
    else:
        response_data = {
            "status_code": 6001,
            "message": "No favorite books found"
        }
    return Response(response_data)
