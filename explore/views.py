from django.views import generic
#importing the post from our models(basically everything in the db)
from .models import Post

#using generic listview to format the data we are getting from "Post"
class ExploreList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

#When read more is tapped we get this guy
class PostDetail(generic.DetailView):
    model = Post
    template_name = 'detail.html'
