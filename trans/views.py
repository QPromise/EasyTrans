import json
import os
from django.conf import settings
from django.shortcuts import render
from . import trans_to_pdf,translate_func
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse,response
from django.http import StreamingHttpResponse
# Create your views here.

def index(request):
    return render(request,'index.html')

# 谷歌翻译调用 方法接口在 translate_func.py文件中
@csrf_exempt
def google_trans(request):
    if request.method == "GET":
        return render(request, "index.html")
    else:
        content = request.POST.get("content")
        google_trans_content = translate_func.google_translate(content)[1]
        print(google_trans_content)
        #error_msg = '翻译失败~'
        #return render(request, 'index.html', {'trans_content': json.dumps(trans_content), 'error_msg': error_msg})
        return HttpResponse(google_trans_content)

# 有道翻译调用 方法接口在 translate_func.py文件中
@csrf_exempt
def youdao_trans(request):
    if request.method == "GET":
        return render(request, "index.html")
    else:
        content = request.POST.get("content")
        youdao_trans_content = translate_func.youdao_translate(content)[1]
        print(youdao_trans_content)
        return HttpResponse(youdao_trans_content)

# 上传要翻译的pdf文件
@csrf_exempt
def upload_func(request):
    if request.method == "GET":
        return render(request, "index.html")
    else:
        file_obj = request.FILES.get('file')
        print(file_obj, type(file_obj))
        if str(file_obj.name).endswith('.pdf') or str(file_obj.name).endswith('.doc') or str(file_obj.name).endswith('.docx'):
            path = os.path.join(settings.BASE_DIR, 'trans', 'input_file', file_obj.name)
            print(path)
            if os.path.exists(path):
                print(path+'已存在.')
                return HttpResponse(0)
            else:
                f = open(path, 'wb')
                for chunk in file_obj.chunks():
                    f.write(chunk)
                f.close()
                return HttpResponse(1)
        else:
            print('上传文件类型不符合要求.')
            return HttpResponse(2)
# 翻译上传的pdf文件
@csrf_exempt
def upload_trans(request):
    #文档只支持谷歌翻译
    file_name = request.POST.get("file_name")
    path = os.path.join(settings.BASE_DIR, 'trans', 'input_file',file_name)
    print(path)
    if str(file_name).endswith('.pdf'):#如果后缀为.pdf则执行打开pdf文件的操作
        trans_to_pdf.trans_pdf(file_name, path)#调用pdf翻译类的函数
        pass
    elif str(file_name).endswith('.doc') or str(file_name).endswith('.docx'):#如果后缀为.doc or .docx则执行打开pdf文件的操作
        pass
    return HttpResponse(1)

# 预览要上传的文件 未实现
@csrf_exempt
def upload_preview(request):
    pass
# 查看翻译后的内容 未实现
@csrf_exempt
def view_content(request):
    pass

# 下载翻译后的pdf
@csrf_exempt
def download_pdf(request):
    file_name = request.GET.get('file_name') # 下载文件名
    path = os.path.join(settings.BASE_DIR, 'trans', 'output_file','translated_'+file_name)
    try:
        def readFile(path, buf_size=512):
            with open(path, 'rb') as f:
                while True:
                    c = f.read(buf_size)
                    if c:
                        yield c
                    else:
                        break
        response = HttpResponse(readFile(path))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="{0}"'.format('tranlated_'+file_name)
        os.remove(path)  # 下载pdf之后就移除
        return response
    except:
        return HttpResponse('2')

# 下载翻译后的docx
@csrf_exempt
def download_docx(request):
    file_name = request.GET.get('file_name') # 下载文件名
    path = os.path.join(settings.BASE_DIR, 'trans', 'output_file','translated_'+file_name[:-4]+'.docx')
    try:
        def readFile(path, buf_size=512):
            print(path)
            with open(path, 'rb') as f:
                while True:
                    c = f.read(buf_size)
                    if c:
                        yield c
                    else:
                        break
        response = HttpResponse(readFile(path))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="{0}"'.format('tranlated_'+file_name[:-4]+'.docx')
        os.remove(path)  # 下载docx之后就移除
        return response
    except:
        return HttpResponse('无法下载')


