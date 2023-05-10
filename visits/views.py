from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods
from .models import Visit
import json
from datetime import datetime, timedelta

# 에러났을 때, ordering, 삭제했을 때 방명록id

#### 방명록 리스트 조회, 방명록 작성 ####
# GET url/
# POST url/
@require_http_methods(["GET", "POST"])
def visit(request):
    if request.method == "GET":
        visits = Visit.objects.all()
        visits_json_list = []
        
        for visit in visits:
            visits_json_list.append({
                "visit_id": visit.visit_id,
                "writer": visit.writer,
                "content": visit.content
            })
        
        return JsonResponse({
            'status': 200,
            'message': '방명록 리스트 조회 성공',
            'data': visits_json_list
        })
        
    elif request.method == "POST":
        try:
            body = json.loads(request.body.decode('utf-8')) # decode
            
            new_visit = Visit.objects.create(
                writer = body['writer'],
                content = body['content']
            )
            
            new_visit_json = {
                "visit_id": new_visit.visit_id,
                "writer": new_visit.writer,
                "content": new_visit.content
            }
            
            return JsonResponse({
                'status': 200,
                'message': '방명록 글 생성 성공',
                'data': new_visit_json
            })
        except:
            return JsonResponse({
                'status': 422,
                'message': 'Body 부분 양식이 올바르지 않습니다.',
                'data': None,
            })

#### 방명록 삭제 또는 개별 방명록 조회 ####
# DELETE url/{visit_id}
# GET url/{visit_id}
@require_http_methods(["DELETE", "GET"])
def visit_detail(request, id):
    if request.method == "DELETE":
        delete_visit = get_object_or_404(Visit, pk=id)
        delete_visit.delete()
        
        delete_visit_json = {
            "visit_id": id
        }
        
        return JsonResponse({
            'status': 200,
            'message': '방명록 삭제 성공',
            'data': delete_visit_json
        })
    elif request.method == "GET":
        visit = get_object_or_404(Visit, pk=id)
    
        visit_json = {
            'visit_id': visit.visit_id,
            'writer': visit.writer,
            'content': visit.content
        }
        return JsonResponse({
            'status': 200,
            'message': '개별 방문록 조회 성공',
            'data': visit_json
        })