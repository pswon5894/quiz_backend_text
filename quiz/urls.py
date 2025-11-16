from django.urls import path, include
from .views import helloAPI, randomQuiz

urlpatterns = [
  path("hello/", helloAPI),
  path("<int:id>/", randomQuiz),
]

# myapi에 기본 파일로 있는 urls.py와는 다른 파일
# quiz 폴더에 있는 것은 quiz app에 대한 url을 관리
# myapi 폴더에 있는 것은 전체 프로젝트에 대한 url을 관리