from django.shortcuts import render_to_response

def woyaolv(request):
    return render_to_response('index.html')
def planfix(request):
    return render_to_response('planfix.html')
def wanttravel(request):
    return render_to_response('wanttravel.html')
def paris(request):
    return render_to_response('paris.html')
def seeproposetraveler(request):
	return render_to_response('seeproposetraveler.html') 
def fromairport(request):
	return render_to_response('fromairport.html')
def toairport(request):
	return render_to_response('toairport.html')	   