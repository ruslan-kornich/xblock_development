"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources
from web_fragments.fragment import Fragment
from xblock.core import XBlock
from xblock.fields import Scope, String
from xblockutils.resources import ResourceLoader
from xblockutils.studio_editable import StudioEditableXBlockMixin


class CollapsibleXBlock(XBlock, StudioEditableXBlockMixin):
    title = String(default="Title XBlock", help="block title, to show something happening",
                   )
    content = String(default="Content XBlock", scope=Scope.content,
                     help="Content of this XBlock",
                     )
    editable_fields = ('title', 'content')

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        loader = ResourceLoader('collapsible')
        context = dict(
            title=self.title,
            content=self.content
        )
        template = loader.render_django_template(
            'static/html/collapsible.html', context=context)
        frag = Fragment(template)
        frag.add_css(self.resource_string("static/css/collapsible.css"))
        frag.add_javascript(self.resource_string("static/js/src/collapsible.js"))
        frag.initialize_js('CollapsibleXBlock')
        return frag

    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("CollapsibleXBlock",
             """<collapsible/>
             """),
            ("Multiple CollapsibleXBlock",
             """<vertical_demo>
                <collapsible/>
                <collapsible/>
                <collapsible/>
                </vertical_demo>
             """),
        ]
