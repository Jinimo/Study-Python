

[참고1](https://github.com/anuraghazra/github-readme-stats)



### 1. GitHub Stats Card



```
![화면 출력 이름's github stats](https://github-readme-stats.vercel.app/api?username=유저네임)
```

![Jinimo's github stats](https://github-readme-stats.vercel.app/api?username=Jinimo)



#### 1.1 Hiding individual stats

> `&hide=`  숨기고 싶은 파라미터들 콤마(,)로 연결

```
![유저네임's GitHub stats](https://github-readme-stats.vercel.app/api?username=유저네임&hide=contribs,prs)
```

![Jinimo's GitHub stats](https://github-readme-stats.vercel.app/api?username=Jinimo&hide=contribs,prs)



#### 1.2 Adding private contributions count to total commits count

> `&count_private=true`   private contributions 총 커밋 수에 추가되어 출력 

```
![유저네임's GitHub stats](https://github-readme-stats.vercel.app/api?username=Jinimo&count_private=true)
```

- `&count_private=true`

![Jinimo's GitHub stats](https://github-readme-stats.vercel.app/api?username=Jinimo&count_private=true)

- `&count_private=false`

![유저네임's GitHub stats](https://github-readme-stats.vercel.app/api?username=Jinimo&count_private=false)



#### 1.3 Showing icons

> `&show_icons=true` 아이콘 표시 

```
![유저네임's GitHub stats](https://github-readme-stats.vercel.app/api?username=유저네임&show_icons=true)
```

![Jinimo's GitHub stats](https://github-readme-stats.vercel.app/api?username=Jinimo&show_icons=true)



#### 1.4 Themes

> `&theme=radical` 테마 설정 

**All inbuilt themes**

: dark, radical, merko, gruvbox, tokyonight, onedark, cobalt, synthwave, highcontrast, dracula 등 다양함 

```
![유저네임's GitHub stats](https://github-readme-stats.vercel.app/api?username=유저네임&show_icons=true&theme=테마)
```

<img src="https://github-readme-stats.vercel.app/api?username=Jinimo&show_icons=true&theme=radical" alt="Jinimo's GitHub stats" style="zoom:30%;" /><img src="https://github-readme-stats.vercel.app/api?username=Jinimo&show_icons=true&theme=dark" alt="Jinimo's GitHub stats" style="zoom:30%;" /><img src="https://github-readme-stats.vercel.app/api?username=Jinimo&show_icons=true&theme=merko" alt="Jinimo's GitHub stats" style="zoom:30%;" />

<img src="https://github-readme-stats.vercel.app/api?username=Jinimo&show_icons=true&theme=gruvbox" alt="Jinimo's GitHub stats" style="zoom:30%;" /><img src="https://github-readme-stats.vercel.app/api?username=Jinimo&show_icons=true&theme=tokyonight" alt="Jinimo's GitHub stats" style="zoom:30%;" /><img src="https://github-readme-stats.vercel.app/api?username=Jinimo&show_icons=true&theme=onedark" alt="Jinimo's GitHub stats" style="zoom:30%;" /><img src="https://github-readme-stats.vercel.app/api?username=Jinimo&show_icons=true&theme=cobalt" alt="Jinimo's GitHub stats" style="zoom:30%;" /><img src="https://github-readme-stats.vercel.app/api?username=Jinimo&show_icons=true&theme=synthwave" alt="Jinimo's GitHub stats" style="zoom:30%;" /><img src="https://github-readme-stats.vercel.app/api?username=Jinimo&show_icons=true&theme=highcontrast" alt="Jinimo's GitHub stats" style="zoom:30%;" /><img src="https://github-readme-stats.vercel.app/api?username=Jinimo&show_icons=true&theme=dracula" alt="Jinimo's GitHub stats" style="zoom:30%;" />



[all available themes | anuraghazra's GitHub](https://github.com/anuraghazra/github-readme-stats/blob/master/themes/README.md) 

[theme config file | anuraghazra's GitHub](https://github.com/anuraghazra/github-readme-stats/blob/master/themes/index.js)



#### 1.5 Customization

> `Stats Card` / `Repo Card` 커스터마이징 가능 

[Customization | anuraghazra's GitHub](https://github.com/anuraghazra/github-readme-stats#customization)





### 2. Top Languages Card

> GitHub에서 사용자가 가장 자주 사용하는 언어 표시
>
> 언어의 Skill level 과 같은 것은 표시 X 

#### 2.1 Usage

> `api/top-langs/?username=유저네임` 

``` 
[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=유저네임)](https://github.com/anuraghazra/github-readme-stats)
```

[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=Jinimo)](https://github.com/anuraghazra/github-readme-stats)



#### 2.2 Exclude individual repositories

> `?exclude_repo=repo1,repo2` 제외하고자 하는 레파지토리 선택

```
[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=유저네임&exclude_repo=github-readme-stats,유저네임.github.io)](https://github.com/anuraghazra/github-readme-stats)
```

[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=Jinimo&exclude_repo=github-readme-stats,Jinimo.github.io)](https://github.com/anuraghazra/github-readme-stats)



#### 2.3 Hide individual languages

> `?hide=language1,language2` 숨기고자 하는 언어 선택

```
[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=유저네임&hide=언어1,언어2)](https://github.com/anuraghazra/github-readme-stats)
```

[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=Jinimo&hide=python)](https://github.com/anuraghazra/github-readme-stats)



#### 2.4 Show more languages

> `&langs_count=8` 언어의 수 표시 (1~10개까지 가능)

```
[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=유저네임&langs_count=수)](https://github.com/anuraghazra/github-readme-stats)
```

[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=Jinimo&langs_count=1)](https://github.com/anuraghazra/github-readme-stats)

#### 2.5 Compact Language Card Layout

> `&layout=compact` 레이아웃 compact로 변경 

```
[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=유저네임&layout=compact)](https://github.com/anuraghazra/github-readme-stats)
```

[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=Jinimo&layout=compact)](https://github.com/anuraghazra/github-readme-stats)



### 3. Wakatime Week Stats 

[Wakatime | anuraghazra's GitHub](https://github.com/anuraghazra/github-readme-stats#wakatime-week-stats)

```
[![willianrod's wakatime stats](https://github-readme-stats.vercel.app/api/wakatime?username=willianrod)](https://github.com/anuraghazra/github-readme-stats)
```













![스크린샷 2022-03-22 10.43.39](/Users/hyunjinkim/Desktop/스크린샷 2022-03-22 10.43.39.png)

![스크린샷 2022-03-22 10.44.34](/Users/hyunjinkim/Library/Application Support/typora-user-images/스크린샷 2022-03-22 10.44.34.png)



