import{Q as s,k as o,n as l}from"./QCard.212f4abe.js";import{Q as c}from"./QPage.5ef5425b.js";import{a as d}from"./axios.bf56c3c5.js";import{A as m,d as i,E as u,F as _,G as r,H as t}from"./index.6a276c7e.js";import"./vm.d067b5b6.js";import"./render.439e97d9.js";import"./scroll.6d4bada5.js";import"./QBtn.88d81af5.js";const C={__name:"OrdersPage",setup(p){const a=m({cards:[],columns_table:[{name:"card_name_RU",align:"center",label:"\u041D\u0430\u0437\u0432\u0430\u043D\u0438\u0435(RU)",field:e=>e.card_name_RU,sortable:!0},{name:"card_name_EU",align:"center",label:"\u041D\u0430\u0437\u0432\u0430\u043D\u0438\u0435(EU)",field:e=>e.card_name_EU,sortable:!0},{name:"count",align:"center",label:"\u041A\u043E\u043B\u0438\u0447\u0435\u0441\u0442\u0432\u043E",field:e=>e.count,sortable:!0},{name:"user_name",align:"center",label:"\u041A\u0442\u043E \u0434\u043E\u0431\u0430\u0432\u0438\u043B",field:e=>e.user_name,sortable:!0}],backend_url:"https://mtg51.site/api/v1"});function n(){d.get(`${a.backend_url}/orders`).then(e=>{a.cards=e.data.cards})}return i(()=>{n()}),(e,f)=>(u(),_(c,{padding:""},{default:r(()=>[t(l,{class:"my-card"},{default:r(()=>[t(s,null,{default:r(()=>[t(o,{title:"\u0417\u0430\u043A\u0430\u0437\u0430\u043D\u043D\u044B\u0435 \u043A\u0430\u0440\u0442\u044B",rows:a.cards,columns:a.columns_table,"row-key":"name","rows-per-page-options":[0]},null,8,["rows","columns"])]),_:1})]),_:1})]),_:1}))}};export{C as default};