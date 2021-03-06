from django.db import models
import datetime
from datetime import timedelta
from django.core.validators import MinValueValidator, MaxValueValidator
# 1. product 앱의 product 테이블 구성을 <작성자, 썸네일, 상품 설명, 등록일자, 노출 종료 일자, 가격, 수정 일자, 활성화 여부>로 변경해주세요
# 2. django serializer를 사용해 validate / create / update 하는 기능을 구현해주세요
#     1. custom validation 기능을 사용해 노출 종료 일자가 현재보다 더 이전 시점이라면 상품을 등록할 수 없도록 해주세요
#     2. custom creator 기능을 사용해 상품 설명의 마지막에 "<등록 일자>에 등록된 상품입니다." 라는 문구를 추가해주세요
#     3. custom update 기능을 사용해 상품이 update 됐을 때 상품 설명의 가장 첫줄에 "<수정 일자>에 수정되었습니다." 라는 문구를 추가해주세요
# 3. product 앱에서 <작성자, 상품, 내용, 평점, 작성일>을 담고 있는 review 테이블을 만들어주세요
# 4. review 테이블을 관리자 페이지에서 자유롭게 추가/수정 할 수 있도록 설정해주세요
# 5. 현재 날짜를 기준으로, 노출 종료 날짜가 지나지 않았고 활성화 여부가 True이거나 로그인 한 사용자가 등록 한 상품들의 정보를 serializer를 사용해 리턴해주세요
# 6. 5번 상품 정보를 리턴 할 때 상품에 달린 review와 평균 점수를 함께 리턴해주세요
#     1. 평균 점수는 (리뷰 평점의 합/리뷰 갯수)로 구해주세요
#     2. 작성 된 리뷰는 모두 return하는 것이 아닌, 가장 최근 리뷰 1개만 리턴해주세요
# 7. 로그인 하지 않은 사용자는 상품 조회만 가능하고, 회원가입 이후 3일 이상 지난 사용자만 상품을 등록 할 수 있도록 권한을 설정해주세요

class product(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to = '')  
    create_date = models.DateTimeField("등록일자", auto_now_add=True)
    Contents = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    is_activate = models.BooleanField("활성화여부",default=True)
    modify_date = models.DateTimeField("수정일자", auto_now=True)
    start_date =models.DateTimeField("노출 시작", default=datetime.datetime.now())
    end_date = models.DateTimeField("노출 종료", default=(datetime.datetime.now()+timedelta(days=7)))


class review(models.Model):
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    comment = models.CharField("내용",max_length=100)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    Create_date = models.DateTimeField("등록일자", auto_now_add=True)