from .exam import *
from .result import *
from .student import *


class IndexView(generic.TemplateView):
    template_name = 'studentmanager/mainmenu.html'
