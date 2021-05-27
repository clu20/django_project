from django.shortcuts import render

# Similates grabbing data from database
posts = [
    {
        'author' :'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'August 26, 2019'
    },
    {
        'author' :'Jonthan eas',
        'title': 'Blog Post 2',
        'content': '2nd Post Content',
        'date_posted': 'August 29, 2019'
    }
]
# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})