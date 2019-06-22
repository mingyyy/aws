from django.views.generic import ListView
from blog.models import Post


class SearchView(ListView):
    template_name = 'search/view.html'
    paginate_by = 5
    count = 0

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['count'] = self.count or 0
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q', None)
        if query is not None:

            res = Post.objects.search(query)

            print(f'res is: {res}')

            qs = sorted(res, key=lambda instance: instance.pk, reverse=True)
            self.count = len(qs)
            return qs
        return Post.objects.none()
