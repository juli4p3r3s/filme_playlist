from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from filmes.forms import FilmeForm, PlaylistForm
from filmes.models import Filmes, Playlist

class PlaylistListView(ListView):
    model = Playlist
    context_object_name = 'playlists'
    template_name = 'playlist/playlist_list.html'

class PlaylistDetailView(DetailView):
    model = Playlist
    context_object_name = 'playlists'
    template_name = 'playlist/playlist_detail.html'

class PlaylistCreateView(CreateView):
    model = Playlist
    form_class = PlaylistForm
    template_name = 'playlist/playlist_form.html'
    success_url = reverse_lazy('playlist_list')

class PlaylistUpdateView(UpdateView):
    model = Playlist
    fields = ['nome', 'filmes']
    template_name = 'playlist/playlist_form.html'
    success_url = reverse_lazy('playlist_list')

class PlaylistDeleteView(DeleteView):
    model = Playlist
    context_object_name = 'playlists'
    success_url = reverse_lazy('playlist_list')
    template_name ='playlist/playlist_confirm_delete.html'


#cadastro filme

class FilmeListView(ListView):
    model = Filmes
    template_name = 'filmes/filme_list.html'

class FilmeDetailView(DetailView):
    model = Filmes
    templates_name = 'filmes/filme_detail.html'

class FilmeCreateView(CreateView):
    model = Filmes
    form_class = FilmeForm
    template_name = 'filmes/filme_form.html'
    success_url = reverse_lazy('filmes_list')

class FilmeUpdateView(UpdateView):
    model = Filmes
    form_class = FilmeForm
    templates_name = 'filmes/filme_form.html'
    success_url = reverse_lazy('filmes_list')

class FilmeDeleteView(DeleteView):
    model = Filmes
    template_name ='filmes/filme_confirm_delete.html'
    success_url = reverse_lazy('filmes_list')
