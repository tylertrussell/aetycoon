from jinja2 import Environment, FileSystemLoader


def create_jinja_environment(template_path, **kwargs):
  """Get a Jinja environment for rendering a template.

  Args:
    template_path: required str; base location of templates
    **kwargs: other kwargs passed to jinja2.Environment

  Returns:
    jinja2.Environment
  """
  return Environment(loader=FileSystemLoader(template_path), **kwargs)
