from .student import *
from .exam import *
from .result import *


class IndexView(generic.TemplateView):
    template_name = 'studentmanager/mainmenu.html'
