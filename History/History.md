```dataviewjs
// ======= 配置开始 =======
const query = `#timeline`;
const dateKey = `beginDate`
const rightCol = `company`
// ======= 配置结束 =======

const pages = dv.pages(query).sort(p => p[dateKey]);
for (const p of pages) {
  let title = p.title ?? p.file.name;
  let time = p[dateKey]!==undefined?moment(p[dateKey].toString()).format("YY年MM月"):"";
  let content = `- ${time}\n- [[${p.file.name}|${title}]]<span style="font-size:14px;float:right;transform: translateY(30%);">— — ${p[rightCol]}</span>\n- ![[${p.file.name}#^desc]]`
  dv.span(content);
  // console.log(p.authors.map(a => a.name));
// console.log(await this.app.vault.adapter.read(p.file.path));
}
```
