from .models import Recipe


menu = [
    {"title": "Топ 100", "url_name": "top"}]


class DataMixin():
    def get_user_context(self, **kwards):
        context = kwards
        context['menu'] = menu
        context["recipes"] = Recipe.objects.all()
        return context
