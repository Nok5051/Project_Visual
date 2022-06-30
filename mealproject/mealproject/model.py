from django.db import models


class MyBoard(models.Model):
    myname = models.CharField(max_length=100)
    mytitle = models.CharField(max_length=500)
    mycontent = models.CharField(max_length=2000)
    mydate = models.DateTimeField()

    # 변수에 MyBoard객에 넣고 print하면 저장된 위치, 얘가 뭔지 나오는데
    # def __str__ 은 오버라이딩, 재정의 해줌. 각각 뭔지 나오게 재정의함
    def __str__(self):
        return str({'myname': self.myname,
                    'mytitle': self.mytitle,
                    'mycontent': self.mycontent,
                    'mydate': self.mydate})
