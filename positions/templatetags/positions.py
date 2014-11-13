from django import template


try:
    from displays.models import Display
except ImportError:
    Display = None

try:
    from channels.models import Channel
except ImportError:
    Channel = None


register = template.Library()

@register.simple_tag()
def position(slug):
    '''
    Find DisplayInstances registered at this position, call render on the Displays 
    and return the HTML
    '''

    try:
        position = Position.objects.get(slug=slug)
    except Postion.DoesNotExist:
        return ''
    else:

        displays_instances_kwargs = {
            'position': position
        }

        if Channel is not None:
            # if we're using channels and we can detect the current one
            # add this to the kwargs            
            displays_kwargs.update(
                channels=Channel.objects.get_current_channel()) # not implemented in Channels?

        display_instances = DisplayInstances.objects.filter(position=position)

        if len(displays) != 1:
            return ''

        html_renders = []
        for display_instance in display_instances:
            html_renders.append(display_instance.display.render_html())

        return ''.join(html_renders)