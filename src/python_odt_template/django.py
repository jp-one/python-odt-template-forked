from python_odt_template.renderer import ODTRenderer

from pathlib import Path

from .filters import odt_markdown
from .filters import pad_string
from django import template
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.template import Context
from django.template import Template

register = template.Library()


@register.filter
def image(value):
    try:
        static_path = Path(settings.STATICFILES_DIRS[0]).resolve()
    except IndexError as e:
        msg = "You must add a least one directory to STATICFILES_DIRS in your settings.py file"
        raise ImproperlyConfigured(msg) from e
    file_path = static_path.joinpath(value).resolve()
    file_path.relative_to(static_path)   # validate subpath
    return file_path


register.filter("odt_markdown", odt_markdown)
register.filter("pad", pad_string)


def _render(template_str: str, context: dict) -> str:
    return Template(template_str).render(Context(context))


def get_odt_renderer() -> ODTRenderer:
    return ODTRenderer(
        block_start_string="{%",
        block_end_string="%}",
        variable_start_string="{{",
        variable_end_string="}}",
        render_func=_render,
    )
