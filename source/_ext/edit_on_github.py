import os

def get_github_url(app, view, path):
    return f"https://github.com/{app.config.edit_on_github_project}/{view}/{app.config.edit_on_github_branch}/{path}"

def html_page_context(app, pagename, templatename, context, doctree):
    if templatename != 'page.html':
        return
    if not app.config.edit_on_github_project:
        return
    path = os.path.relpath(doctree.get('source'), app.builder.srcdir)
    context['show_on_github_url'] = get_github_url(app, 'blob', path)
    context['edit_on_github_url'] = get_github_url(app, 'edit', path)

def setup(app):
    app.add_config_value('edit_on_github_project', '', True)
    app.add_config_value('edit_on_github_branch', 'main', True)
    app.connect('html-page-context', html_page_context)

