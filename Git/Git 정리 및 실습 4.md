![스크린샷 2022-03-22 17.34.39](/Users/hyunjinkim/Desktop/스크린샷 2022-03-22 17.34.39.png)

git log --oneline --graph



merge pull request



깃허브에서는  pull request

깃 랩에서는 merge request



1. 다 같은 파일 master

2. 각자 팀원들 본인 로컬로 클론 

3. 자신의 브렌치를 새로 만들어서 새로운 브랜치에서 작업 진행 

		- git branch 새브렌치 : 브렌치 생성 
		- git switch 새브렌치 : 브렌치 변환 

3. 로컬->온라인에 새로운 브렌치(쿠션)로 푸쉬, master 브렌치로 X

	- git push origin 새브렌치 => 온라인에 없던 새브렌치 새로 생김 

3. 온라인 쿠션(새 브렌치)에서 병합할지 팀원들끼리 논의
   - 온라인 (깃허브)애서 보면 머지할껀지? 창 뜸 
4. 받아들여짐 or 기각 -> 새 브렌치 삭제