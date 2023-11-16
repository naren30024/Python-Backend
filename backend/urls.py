from django.urls import path
from .views import register,registration_data,loginpage
from .crudview import item_detail,item_list
from .collegeview import teacher,geteacherdata,student,getstudentdata,checklogin

urlpatterns = [
    
    path('register/', register , name='register'),
    path('viewrgdata/',registration_data, name='registration_data'),
    path('login/', loginpage,name='loginpage'),
    path('details/',item_list, name='item_list'),
    path('detailscrud/<int:pk>/', item_detail,name='item_detail'),
    # path('upload/<int:file_id>/', upload , name='upload'),
    path('posteacher/',teacher, name='teacher'),
    path('poststudent/',student, name='student'),
    path('geteacher/', geteacherdata,name='geteacherdata'),
    path('getstudent/',getstudentdata, name='getstudentdata'),
    path('checkLogin/',checklogin, name='checkLogin')

]