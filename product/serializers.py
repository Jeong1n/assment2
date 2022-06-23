from rest_framework import serializers
from .models import review, product
from datetime import datetime
from django.db.models import Avg
from django.forms import model_to_dict

class reviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = review
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    review_set = serializers.SerializerMethodField()
    rating_avg = serializers.SerializerMethodField()
    def get_review_set(self,obj):
        try:
            Review = review.objects.filter(product=obj).order_by("-Create_date").first()
        except ImportError:
            return None
        return model_to_dict(Review)

    def get_rating_avg(self, obj):
        score = obj.review_set.all()
        if score.count() == 0:
            return(0)
        return score.aggregate(rating_avg=Avg('rating'))['rating_avg']

    def validate(self, data):
        today = datetime.today().strftime("%Y-%m-%d")
        if str(data.get("end_date")) < today:
           # validation에 통과하지 못할 경우 ValidationError class 호출
           raise serializers.ValidationError(
             # custom validation error message
             detail={"error": "노출 일자가 지났습니다."},
           )
        if data.get("is_activate") == True :
            raise serializers.ValidationError(
             # custom validation error message
             detail={"error": "활성화가 되지않았습니다."},
           )
        return data

    def create(self, validated_data):
        # User object 생성
        today = datetime.today().strftime("%Y-%m-%d")


        validated_data["Contents"] += f'{today}에 등록된 상품입니다.'
        Product = product(**validated_data)
        Product.save()
        return validated_data

    def update(self, instance, validated_data):
      today = datetime.today().strftime("%Y-%m-%d")
      for key, value in validated_data.items():
         if key == "Contents":
            value += f' {today}에 수정된 상품입니다.'
            continue            
         setattr(instance, key, value)
      instance.save()
      return instance
    ...
    class Meta:
        model = product
        fields = "__all__"