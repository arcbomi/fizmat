# 简介
这是fizmat-app中很大的一个板块,但跟kundelik交互时会很多的问题

在这里提供两种交互方案：
- 使用kundelik v2 api
- corc kundelik

## corc kundelik
fizmat-app 在浏览器端使用kundelik时会有类似跨域访问的问题,包括flutter会有一些在浏览器端的限制，他们会把 X-Frame-Options设为deny，所以在浏览器端无法访问kundelik，但可以建立一个代理服务器把X-Frame-Options头给去掉

在此我试用过 corsproxy.io, worker作为和kundelik交互的方法,但无一例外都失败了，我未能成功登录kundelik

如果你能成功的话，你可以使用一下script来获取信息

### Script
kundelik.kz
https://kundelik.kz/marks/school/[schoolId]/student/[personId]/period?periodId=final
#### 检测是否登录
```
dnevnik.auth.isAuthenticated 
```

#### 获取 schoolId
```
window.__USER__START__PAGE__INITIAL__STATE__.userSchedule.currentChild.schoolId
```
#### 获取 personId
```
window.__USER__START__PAGE__INITIAL__STATE__.userSchedule.currentChild.personId
```
#### 获取 firstName
```
window.__USER__START__PAGE__INITIAL__STATE__.userContext.currentContextPerson.firstName
```
#### 获取 lastName
```
window.__USER__START__PAGE__INITIAL__STATE__.userContext.currentContextPerson.lastName
```
#### 获取 isStudent
```
window.__USER__START__PAGE__INITIAL__STATE__.userContext.userContextInfo.isStudent
```
#### 获取 sex
```
window.__USER__START__PAGE__INITIAL__STATE__.userContext.userContextInfo.sex
```




## kundelik v2 api
github 上有一个项目https://github.com/Bs0Dd/KunAPIPy，使用python编写，在将此作为基础.

### API

#### 获取孩子的信息
/v2/user/{userID}/children
```
[
  {
    "id": 1000010305374, = personid
    "id_str": "1000010305374",
    "userId": 1000008972014,
    "userId_str": "1000008972014",
    "shortName": "Дәурен М",
    "sex": "Male"
  }
]
```


#### 获取自己的信息
/v2/users/me 
```
{
  "id": 1000008972374,
  "id_str": "1000008972374",
  "personId": 1000010305403,
  "personId_str": "1000010305403",
  "login": "gulshagizhaksybai",
  "shortName": "Гүлшағи Ж",
  "locale": "ru-RU",
  "timezone": "+5:00",
  "sex": "Female",
  "birthday": "1971-02-04T00:00:00",
  "roles": [
    "EduParent"
  ],
  "phone": ""
}
```

#### 获取角色
/v2/users/me/roles 
```
[
  "EduParent"
]
```
#### 多所学校的个人资料列表
/v2/schools  
```
[
  {
    "id": 1000004956244,
    "id_str": "1000004956244",
    "name": "РФММ Алматы",
    "educationType": "Regular",
    "tsoCityId": 2566,
    "tsoRegionTreePath": "12."
  }
]
```

#### 获取学校的课程
/v2/schools/{school}/subjects 
```
[
  {
    "id": 1343883032131044600,
    "id_str": "1343883032131044633",
    "name": "Русская литература",
    "knowledgeArea": "Язык и литература",
    "fgosSubjectId": null,
    "espSubjectName": null,
    "halfYear": false
  },
  {
    "id": 1343883032131044600,
    "id_str": "1343883032131044634",
    "name": "Русский язык",
    "knowledgeArea": "Язык и литература",
    "fgosSubjectId": null,
    "espSubjectName": null,
    "halfYear": false
  },
  {
    "id": 1343883032131044600,
    "id_str": "1343883032131044635",
    "name": "Казахский язык",
    "knowledgeArea": "Язык и литература",
    "fgosSubjectId": null,
    "espSubjectName": null,
    "halfYear": false
  },
  {
    "id": 1343883032131044600,
    "id_str": "1343883032131044636",
    "name": "Казахская литература",
    "knowledgeArea": "Язык и литература",
    "fgosSubjectId": null,
    "espSubjectName": null,
    "halfYear": false
  },
  {
    "id": 1343883032131044600,
    "id_str": "1343883032131044637",
    "name": "Английский язык",
    "knowledgeArea": "Язык и литература",
    "fgosSubjectId": null,
    "espSubjectName": null,
    "halfYear": false
  },
  {
    "id": 1343883032131044600,
    "id_str": "1343883032131044638",
    "name": "Алгебра",
    "knowledgeArea": "Математика и информатика",
    "fgosSubjectId": null,
    "espSubjectName": null,
    "halfYear": false
  },
  ```

#### 当前的群组

  /v2/persons/{person}/edu-groups
```
  [
  {
    "id": 2260325488551004000,
    "id_str": "2260325488551003873",
    "parentIds": [
      2260325488551004000
    ],
    "parentIds_str": [
      "2260325488551003872"
    ],
    "type": "Subgroup",
    "name": "Алг1 С.Г",
    "fullName": "Согамбаева Г.Б.",
    "parallel": 11,
    "timetable": 1343854728296550400,
    "timetable_str": "1343854728296550454",
    "status": "Active",
    "studyyear": 2024,
    "subjects": [],
    "journaltype": "Criteria"
  },
  {
    "id": 2260325488551004000,
    "id_str": "2260325488551003876",
    "parentIds": [
      2260325488551004000
    ],
    "parentIds_str": [
      "2260325488551003872"
    ],
    "type": "Subgroup",
    "name": "Анг.я1 А.С",
    "fullName": "",
    "parallel": 11,
    "timetable": 1343854728296550400,
    "timetable_str": "1343854728296550454",
    "status": "Active",
    "studyyear": 2024,
    "subjects": [],
    "journaltype": "Criteria"
  },
  {
    "id": 2260325488551004000,
    "id_str": "2260325488551003877",
    "parentIds": [
      2260325488551004000
    ],
    "parentIds_str": [
      "2260325488551003872"
    ],
    "type": "Subgroup",
    "name": "Инфор1 Д.У",
    "fullName": "",
    "parallel": 11,
    "timetable": 1343854728296550400,
    "timetable_str": "1343854728296550454",
    "status": "Active",
    "studyyear": 2024,
    "subjects": [],
    "journaltype": "Criteria"
  },
```

#### 获取所有课程
  /v2/persons/{person}/edu-groups/all
```
[
  {
    "id": 1717526546724972300,
    "id_str": "1717526546724972248",
    "parentIds": [],
    "parentIds_str": [],
    "type": "Group",
    "name": "7-H",
    "fullName": "",
    "parallel": 7,
    "timetable": 1343854728296550400,
    "timetable_str": "1343854728296550454",
    "status": "Archive",
    "studyyear": 2020,
    "educationType": "Regular",
    "subjects": [
      {
        "id": 1345403132726249500,
        "id_str": "1345403132726249444",
        "name": "Қазақ тілі",
        "knowledgeArea": "Язык и литература",
        "fgosSubjectId": null,
        "espSubjectName": null,
        "halfYear": false
      },
```


#### 当前的edu-groups
/v2/persons/{person}/schools/{school}/edu-groups
Учебные группы персоны в школе
```
[
  {
    "id": 2260325488551004000,
    "id_str": "2260325488551003872", //group name
    "parentIds": null,
    "parentIds_str": null,
    "type": "Group",
    "name": "11-H",
    "fullName": "",
    "parallel": 11,
    "timetable": 1343854728296550400,
    "timetable_str": "1343854728296550454",
    "status": "Active",
    "studyyear": 2024,
    "subjects": [],
    "journaltype": "Criteria"
  }
]
```


#### 获取group里的成员
/v2/edu-groups/{group}/persons
```
会显示一堆group里的成员，也就是你的同班同学
```
