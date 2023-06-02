from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.db.models import Q
from books.models import Category, Book, Favorite
from api.v1.books.serializers import  BookSerializer,FavoriteSerializer

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def books(request):
    instances = Book.objects.filter()

    q = request.GET.get("q")

    if q:
        instances = instances.filter(Q(name__icontains=q) | Q(publisher_name__icontains=q))

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
            "message": "Success"
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
@permission_classes([AllowAny])
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


@api_view(['PUT'])
@permission_classes([AllowAny])
def update(request, pk):
    try:
        book = Book.objects.get(id=pk)
        serializer = BookSerializer(instance=book, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            response_data = {
                "status_code": 6000,
                "message": "Success",
                "data": serializer.data
            }
        else:
            response_data = {
                "status_code": 6001,
                "message": "Validation Error",
                "data": serializer.errors
            }

        return Response(response_data)
    except Book.DoesNotExist:
        response_data = {
            "status_code": 6001,
            "message": "This Book doesn't exist"
        }
        return Response(response_data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_to_favorites(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
        serializer = FavoriteSerializer(data={'book': book_id, 'user': request.user.id})

        if serializer.is_valid():
            serializer.save()

            response_data = {
                "status_code": 6000,
                "message": "Book added to favorites successfully"
            }
        else:
            response_data = {
                "status_code": 6001,
                "message": "Validation Error",
                "data": serializer.errors
            }

        return Response(response_data)
    except Book.DoesNotExist:
        response_data = {
            "status_code": 6001,
            "message": "This Book doesn't exist"
        }
        return Response(response_data)
