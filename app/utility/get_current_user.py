def get_current_user(request):
    user = request.state.user
    id  = user["id"]
    return id