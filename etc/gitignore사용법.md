

1. 이미 git repasitory에 포함되어 있는 경우

```
#1. git 정보 검색, 삭제 
$ find .-name .DS_Store -print0 | xargs -0 git rm -f --cached --ignore-unmatch

#2. commit
$ git commit -m 'del DS_Store'
#3. push
$ git push origin master
```



2. 전역으로 gitignore 처리

```
#1. 전역 .gitignore 파일 생성 
$ echo .DS_Store >> ~/.gitignore_global
#2. git에서 사용가능하도록 설정 
$ git config --global core.excludesfile ~/.gitignore_global
```

