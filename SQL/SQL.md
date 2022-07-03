

## SQL 쿼리문



## 1. SQL 분류

1. `DML` (Data Manipulation Language)

   - 데이터 **조작** (선택, 삽입, 수정, 삭제) 언어
	
   	- 사용 대상: 테이블 행
	
   	- 이전에 테이블 정의 되어있어야 사용 가능 

    - 해당 SQL 구문: `SELECT`, `INSERT`, `UPDATE`, `DELETE`
       - `Transaction` 발생 SQL도 이에 속함 
         - 테이블 데이터 변경(입력/수정/삭제)시 테이블에 완전 적용 X -> 임시 적용, 취소 가능 

2. `DDL` (Data Definition Language)

   - 데이터 **정의** 언어 
   - Database 객체 (Database, Table, View, Index 등) -> 생성/삭제/변경 역할 
   - `CREATE`, `DROP`, `ALTER` 구문 
   - `Transaction` 발생 X
   - `ROLLBACK`, `COMMIT` 사용 불가
   - 실행 즉시 MySQL에 적용 

3. `DCL` (Data Control Language)
   	- 데이터 **제어** 언어
   	- 사용자에게 권한 부여 및 빼앗을 경우 사용 
   	- `GRANT`, `REVOKE`, `DENY` 구문 



|                     |                                                              |
| ------------------- | :----------------------------------------------------------- |
| `SHOW DATABASES;`   | 현재 서버에 어떤 DB가 존재하는지 확인                        |
| `USE database_name` | - 사용할 데이터베이스 지정  특별한 명시(1. 지정 후 다시 USE 문 사용, 2. 다른 DB사용 명시)하지 않는 이상 모든 SQL문 -> DB에서 수행.  / `Workbench`에서 직접 선택 후 사용 가능   [Navigator]->[SCHEMAS]->DB 선택 |
| `SHOW TABLE;`       | DB에서 테이블 이름 보기                                      |
| 35                  |                                                              |
|                     |                                                              |
|                     |                                                              |
|                     |                                                              |
|                     |                                                              |
|                     |                                                              |







### 데이터 베이스 생성 

```mariadb
CREATE DATABASE 데이터베이스명
```

(예시: `CREATE DATABASE test;` )

기존에 동일한 이름 존재한다면 해당 자료와 에러 발생 



### 데이터 베이스 삭제

```mariadb
DROP DATABASE 데이터베이스명
```

(예시: `DROP DATABASE test;` )



### MariaDB 연결

DB 연결 

```mariadb
use 데이터베이스
```

(예시: `use test;` )



### 테이블 생성

```mariadb
CREATE TABLE 테이블명
(필드1 형식 [크기] [not NULL] [인덱스1], 
 필드2 형식 [크기] [not NULL] [인덱스2],….) 
CONSTRAINT 필드 제약조건
```



### 테이블 변경

```mariadb
ALTER TABLE 테이블명
ADD COLUMIN 추가필드 형식[크기][NOT UILL]
[CONSTRAINT 인덱스이름]
DROP COLUMIN 필드 1 CONSTRAINT 인덱스 이름
```



### 테이블 삭제

```mariadb
DROP TABLE <테이블 이름>
```



### 데이터 추가 (INSERT 구문)

```mariadb
INSERT INTO 테이블명 (필드명1,필드명2,…)
VALUES (값1, 값2, …. ) # 필드명에 대입되는 순서대로 값 넣어줌 
```



### 조회쿼리( SELECT 구문)

```mariadb
# 보통은 조건까지 
SELECT <필드명>     # 보고자 하는 필드
FROM <테이블/쿼리명>  
WHERE <조건>  

# 상황에 따라서 그룹 조건 
GROUP BY <그룹 지을 필드명>  
HAVING <그룹조건>  
ORDER BY <정렬 필드명>;
```

 



### 업데이트 (UPDATE 구문)

```mariadb
UPDATE  테이블명
SET <필드 = 데이터, 필드=데이터,….>
WHERE <조건>
```



### 삭제 (DELETE 구문)

```mariadb
DELETE FROM 테이블명
WHERE <조건>
```









![스크린샷 2022-04-19 10.57.02](/Users/hyunjinkim/Library/Application Support/typora-user-images/스크린샷 2022-04-19 10.57.02.png)

- 업데이트 쿼리

'서정동' 데이터만 수정 

위에서부터 순서대로 수정됨

- 삭제 쿼리

*** Where 조건 안주면 모든 데이터 삭제됨!! 데이터 삭제 방지위해 Where 조건 무조건 써주기

![스크린샷 2022-04-19 11.00.34](/Users/hyunjinkim/Library/Application Support/typora-user-images/스크린샷 2022-04-19 11.00.34.png)

`*` : 모든것 의미

muser로 부터 모근 데이터 삭제하기

한번 지운 데이터는 되돌릴 수 없음 

조건절 whrer 안주는 경우는 DB 초기화하는 경우 