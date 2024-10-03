from django.shortcuts import render,redirect

from django.views.generic import View

from myapp.forms import MovieForm

from myapp.models import Movies

# Create your views here.

class MovieCreateForm(View):

    def get(self,request,*args,**kwargs):

        form_instance=MovieForm()

        return render(request,"movie_add.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_instance=MovieForm(request.POST)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            Movies.objects.create(**data)

            return render(request,"movie_add.html",{"form":form_instance})
        
        else:

            return render(request,"movie_add.html",{"form":form_instance})
        
class MovieListView(View):

    def get(self,request,*args,**kwargs):

        qs=Movies.objects.all()

        return render(request,"movie_list.html",{"movies":qs})

class MovieDetailView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        qs=Movies.objects.get(id=id)

        return render(request,"movie_detail.html",{'movie':qs})

class MovieDeleteView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        Movies.objects.get(id=id).delete()

        return redirect("movie-list")
    
class MovieUpdateView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        movie_obj=Movies.objects.get(id=id)

        data={

            "title":movie_obj.title,
            "genre":movie_obj.genre,
            "language":movie_obj.language,
            "year":movie_obj.year,
            "run_time":movie_obj.run_time,
            "director":movie_obj.director
        }

        form_instance=MovieForm(initial=data)

        return render(request,"movie_edit.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_instance=MovieForm(request.POST)

        if form_instance.is_valid():

            id=kwargs.get("pk")

            data=form_instance.cleaned_data

            Movies.objects.filter(id=id).update(**data)

            return redirect('movie-list')

