from django.db import models

# Create your models here.
# Modae = Table > Class 사용 

# 클래스 이름 = 테이블 명
class Curriculum(models.Model) :
    # 변수명 = 컬럼명
    name = models.CharField(max_length=255)