from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth import get_user_model
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from whitecart.models import UserBoxCoord, WhiteCartUser
import json
import copy

# Create your views here.

@login_required
def screens(request):

    selected_squares = getAllCoordinates()
    print(selected_squares)
    array = getBaseSquareArray()

    context = {
        'array': setSelectedSquares(array, selected_squares),
        'rows': 10,
        'columns': 5
    }

    return render(request, 'screens.html', context=context)

def getAllCoordinates():
    allUserCoord = UserBoxCoord.objects.all()
    coords = []
    for coord in allUserCoord:
        coords += [{'x':coord.x_coord,'y': coord.y_coord}]
    return coords

def setSelectedSquares(array, selected_squares):
    for selection in selected_squares:
        print(selection)
        array[selection['x']][selection['y']]['class'] ='white-button'
    print(array)
    return array

def getBaseSquareArray():
    num_rows = 10
    num_columns = 5

    rows = []
    columns = []

    y = 0
    for _ in range(num_rows):
        columns += [{'colour':'black', 'class': 'black-button', 'x': 0, 'y': y}]
        y += 1

    x = 0
    for _ in range(num_columns):
        this_column = copy.deepcopy(columns)
        for item in this_column:
            item['x'] = x

        rows += [this_column.copy()]
        x += 1

    return rows


def register(request):
    username = request.POST['username']
    if username == '':
        return HttpResponse()

    if checkDoesUserAlreadyExist(username):
        user = get_user_model().objects.create_user(username, username)
        WhiteCartUser.objects.create(username=username)
        login(request, user)
        return redirect('screens/', screens(request))
    else:
        context = {}
        context["message"] = username + " has already visited."
        return render(request,'alreadyvisited.html', context)



def checkDoesUserAlreadyExist(username):
    number_of_results = get_user_model().objects.filter(username=username).count()
    return number_of_results < 1


def selectSquare(request):
    success = 'false'
    if request.user.is_authenticated:
        username = request.user.username
        user = WhiteCartUser.objects.get(username=username)
        coord = UserBoxCoord.objects.filter(user=user).first()
        body = request.body
        data = json.loads(body)

        if coord == None and not data == None:
            x=data['x']
            y=data['y']
            print('saving new coord for ' + user.username)
            UserBoxCoord.objects.create(x_coord=x,y_coord=y,user=user)
            success = 'true'

    return HttpResponse(json.dumps([{'success': success}]))



