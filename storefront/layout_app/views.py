from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Furniture

def index(request):
    return render(request, 'index.html')

def get_furnitures(request):
    if request.method == 'GET':
        furnitures = Furniture.objects.all()
        data = [{
            'id': f.id,
            'x': f.x,
            'y': f.y,
            'width': f.width,
            'height': f.height,
            'color': f.color,
        } for f in furnitures]
        return JsonResponse({'furnitures': data})

@csrf_exempt 
def save_furniture(request):
    if request.method == 'POST':
        data = request.POST 
        fid = data.get('id', None)
        x = float(data.get('x', 0))
        y = float(data.get('y', 0))
        width = float(data.get('width', 50))
        height = float(data.get('height', 50))

        if fid:
            furniture = Furniture.objects.get(id=fid)
        else:
            furniture = Furniture()

        # Check for overlapping
        overlaps = False
        others = Furniture.objects.exclude(id=fid) if fid else Furniture.objects.all()
        for other in others:
            if is_overlapping(x, y, width, height, other.x, other.y, other.width, other.height):
                overlaps = True
                break

        if overlaps:
            return JsonResponse({'status': 'error', 'msg': 'Overlap detected!'}, status=400)

        # Save if no overlap.
        furniture.x = x
        furniture.y = y
        furniture.width = width
        furniture.height = height
        furniture.save()

        return JsonResponse({'status': 'ok', 'furniture_id': furniture.id})

def is_overlapping(x1, y1, w1, h1, x2, y2, w2, h2):
    if x1 + w1 <= x2 or x2 + w2 <= x1:
        return False
    if y1 + h1 <= y2 or y2 + h2 <= y1:
        return False
    return True

@csrf_exempt  
def reset_layout(request):
    if request.method == 'POST':
        Furniture.objects.all().delete() 
        return JsonResponse({'status': 'ok'})
    return JsonResponse({'status': 'error', 'msg': 'Invalid method'}, status=400)
