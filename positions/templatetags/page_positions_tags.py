from django import template

from views.models import PageView


register = template.Library()

@register.simple_tag(takes_context=True)
def page_position(context, page_slug, position_slug):
    '''
    Find the Page Views configured here and render the View content
    '''

    page_views = PageView.objects.filter(
        position__slug=position_slug,
        page__slug=page_slug)

    view_renders = []
    for page_view in page_views:
        view_renders.append(page_view.view.render(context))

    return ''.join(view_renders)
 