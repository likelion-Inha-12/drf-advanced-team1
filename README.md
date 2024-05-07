# drf-advanced-team1
drf실습 1팀 과제 레포입니다.



## API 명세서
![API 명세서](https://purple-channel-bb4.notion.site/API-2307c95918714315be37ae837ceb0b89)

## API 스크린샷
### #1 과제 생성(오다솔)
![Api1](<https://github.com/likelion-Inha-12/drf-advanced-team1/blob/main/images/api1.png>)



### #2 특정 과제 제출물 생성(오다솔)
![Api2](<https://github.com/likelion-Inha-12/drf-advanced-team1/blob/main/images/api2.png>)



### #3 과제 목록 조회(손가영)
![Api3](<https://github.com/likelion-Inha-12/drf-advanced-team1/blob/main/images/api3.png>)
3번 과제 목록 조회 api입니다.
assignment list api view 클래스를 이용해 구현한 class based view 입니다.
사용자가 전체 과제 목록을 조회할 수 있게 해줍니다. Assignment.objects.all()을 사용하여 모든 과제를 가져오고, AssignmentSerializer를 통해 시리얼라이즈하여 JSON 형태로 응답합니다.


### #4 과제 내용 조회(손가영)
![Api4](<https://github.com/likelion-Inha-12/drf-advanced-team1/blob/main/images/api4.png>)
4번 기능 특정 과제 조회 API입니다. 
이또한 CBV를 이용해 AssignmentAPIView 클래스를 사용하여 구현되었습니다.
CBV를 이용해 6번 기능의 메소드도 함께 각 HTTP 메소드에 대응하는 로직을 내부에 구현하였습니다. 사용자가 과제의 ID를 제공하면, 해당 ID를 가진 과제를 데이터베이스에서 찾아 반환합니다. 만약 해당 ID의 과제가 없을 경우 404 에러를 반환하여, 요청한 과제가 존재하지 않음을 알려줍니다.



### #5 특정 과제 수정(손가영)
PUT
![Alt text](images/api5_put.png)

PATCH
![Api5_PATCH](<https://github.com/likelion-Inha-12/drf-advanced-team1/blob/main/images/api5.png>)
5번 특정 과제를 수정하는 api입니다.
이는 Function based view 즉 FBV를 사용했습니다. 그래서 이 api는 update_assignment 함수를 통해 제공됩니다. 여기서는 PUT과 PATCH 두 가지 HTTP 메소드를 지원합니다. PUT은 모든 정보를 업데이트할 때 사용되고, PATCH는 일부 정보만 업데이트할 때 사용됩니다. 사용자가 요청한 데이터를 받아 AssignmentSerializer로 처리하며, 유효성 검사를 통과하면 데이터를 저장합니다.


### #6 특정 과제 삭제(손가영)
![Api6](https://github.com/likelion-Inha-12/drf-advanced-team1/blob/main/images/api6.png)
6번 특정 과제 삭제 기능입니다. 이 기능도 FBV로 delete_assignment 함수를 통해 구현되었습니다. 사용자가 과제의 ID를 제공하면, 해당 과제를 찾아 데이터베이스에서 삭제합니다. 성공적으로 삭제되면, 삭제되었다는 메시지를 JSON 형태로 반환합니다.


### #7 과제 파트별 조회(배민혁)
- 전체 조회

![Api7_ALL](https://github.com/likelion-Inha-12/drf-advanced-team1/blob/main/images/api7_ALL.png)

- 백엔드 조회 

![Api7_BE](https://github.com/likelion-Inha-12/drf-advanced-team1/blob/main/images/api7_BE.png)

- 프론트엔드 조회  

![Api7_FE](https://github.com/likelion-Inha-12/drf-advanced-team1/blob/main/images/api7_FE.png)



### #8 과제 태그별 조회(배민혁)
- 태그 조회 성공  

![Api8_Success](https://github.com/likelion-Inha-12/drf-advanced-team1/blob/main/images/api8_성공.png)

- 태그 조회 실패  

![Api8_Fail](https://github.com/likelion-Inha-12/drf-advanced-team1/blob/main/images/api8_실패.png)

