# branch



git branch : 현재 브렌치 확인  

git branch 이름 : 브렌치 이름 설정하여 생성 

git branch : 생성됬는지 다시 확인

(현재 master) ![스크린샷 2022-03-22 16.21.59](/Users/hyunjinkim/Library/Application Support/typora-user-images/스크린샷 2022-03-22 16.21.59.png)



Git switch 이름 : 지정한 브렌치로 변경하기

git branch : 변경됬는지 확인

(Master -> water)

![스크린샷 2022-03-22 16.25.03](/Users/hyunjinkim/Desktop/스크린샷 2022-03-22 16.25.03.png)

![스크린샷 2022-03-22 16.31.03](/Users/hyunjinkim/Desktop/스크린샷 2022-03-22 16.31.03.png)

![스크린샷 2022-03-22 16.31.29](/Users/hyunjinkim/Desktop/스크린샷 2022-03-22 16.31.29.png)

git merge water : 브렌치 병합하기

(master에서 water와 병합하기!! )

merge 너무 오랜시간 뒤에 하면 오류 많이 나와!!



![스크린샷 2022-03-22 16.33.34](/Users/hyunjinkim/Desktop/스크린샷 2022-03-22 16.33.34.png)





1. 기본 master 브렌치
2. 파일 생성 -> 수정 ->저장 ->add ->commit
3. 새로운 브렌치 생성 
4. 파일 수정 -> 저장 -> ->add ->commit
5. 스위치하여 서로 다른 파일 내용 확인 
6. 2개 브렌치 별합 : git merge 새로운 브렌치명 
7. Git branch -d 새로운 브렌치명 