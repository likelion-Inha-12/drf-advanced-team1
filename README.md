# drf-advanced-team1
drf실습 1팀 과제 레포입니다.



## API 명세서
[https://purple-channel-bb4.notion.site/API-2307c95918714315be37ae837ceb0b89](https://purple-channel-bb4.notion.site/API-2307c95918714315be37ae837ceb0b89)


## API 스크린샷
### #1 과제 생성(오다솔)
![Api1](<https://github.com/likelion-Inha-12/drf-advanced-team1/blob/main/images/api1.png>)



### #2 특정 과제 제출물 생성(오다솔)
![Api2](<https://github.com/likelion-Inha-12/drf-advanced-team1/blob/main/images/api2.png>)



### #3 과제 목록 조회(손가영)
![Api3](<https://github.com/likelion-Inha-12/drf-advanced-team1/blob/main/images/api3.png>)
CBV

## #4 과제 내용 조회(손가영)
![Api4](<https://github.com/likelion-Inha-12/drf-advanced-team1/blob/main/images/api4.png>)
CBV

### #5 특정 과제 수정(손가영)
PUT
![Alt text](images/api5_put.png)

PATCH
![Api5_PATCH](<https://github.com/likelion-Inha-12/drf-advanced-team1/blob/main/images/api5.png>)
FBV


### #6 특정 과제 삭제(손가영)
![Api6](https://github.com/likelion-Inha-12/drf-advanced-team1/blob/main/images/api6.png)
CBV


### #7 과제 파트별 조회(배민혁)
- 전체 조회

![Api7_ALL](https://github.com/likelion-Inha-12/drf-advanced-team1/blob/main/images/api7_ALL.png)

- 백엔드 조회 

![Api7_BE](https://github.com/likelion-Inha-12/drf-advanced-team1/blob/main/images/api7_BE.png)

- 프론트엔드 조회  

![Api7_FE](https://github.com/likelion-Inha-12/drf-advanced-team1/blob/main/images/api7_FE.png)

먼저 url로 part를 입력 받습니다. 미리 코드 안에 있던 파트셋에 입력받은 파트가 있다면 Assingment 객체 중 입력 받은 파트와 일치하는 모든 과제들을 assignments에 저장합니다. serializer을 통해서 직렬화를 수행하고 반환합니다.


### #8 과제 태그별 조회(배민혁)
- 태그 조회 성공  

![Api8_Success](https://github.com/likelion-Inha-12/drf-advanced-team1/blob/main/images/api8_성공.png)

- 태그 조회 실패  

![Api8_Fail](https://github.com/likelion-Inha-12/drf-advanced-team1/blob/main/images/api8_실패.png)

파트별 조회와 마찬가지로 url로 tag를 입력 받습니다.  Category의 객체 중 입력한 tag와 일치하는 객체가 있다면 category에 저장하고, 그것을 바탕으로 일치하는 과제들을 모두 찾고, assignments에 저장한다음 직렬화하여 반환합니다.
만약 일치하는 태그가 없다면 없다고 알려주고 Category 안에 있는 모든 태그들을 불러와 현재 있는 태그를 알려줍니다.
