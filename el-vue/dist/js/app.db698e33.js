(function(e){function t(t){for(var o,l,a=t[0],c=t[1],s=t[2],d=0,u=[];d<a.length;d++)l=a[d],Object.prototype.hasOwnProperty.call(r,l)&&r[l]&&u.push(r[l][0]),r[l]=0;for(o in c)Object.prototype.hasOwnProperty.call(c,o)&&(e[o]=c[o]);p&&p(t);while(u.length)u.shift()();return i.push.apply(i,s||[]),n()}function n(){for(var e,t=0;t<i.length;t++){for(var n=i[t],o=!0,a=1;a<n.length;a++){var c=n[a];0!==r[c]&&(o=!1)}o&&(i.splice(t--,1),e=l(l.s=n[0]))}return e}var o={},r={app:0},i=[];function l(t){if(o[t])return o[t].exports;var n=o[t]={i:t,l:!1,exports:{}};return e[t].call(n.exports,n,n.exports,l),n.l=!0,n.exports}l.m=e,l.c=o,l.d=function(e,t,n){l.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:n})},l.r=function(e){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},l.t=function(e,t){if(1&t&&(e=l(e)),8&t)return e;if(4&t&&"object"===typeof e&&e&&e.__esModule)return e;var n=Object.create(null);if(l.r(n),Object.defineProperty(n,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var o in e)l.d(n,o,function(t){return e[t]}.bind(null,o));return n},l.n=function(e){var t=e&&e.__esModule?function(){return e["default"]}:function(){return e};return l.d(t,"a",t),t},l.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},l.p="/";var a=window["webpackJsonp"]=window["webpackJsonp"]||[],c=a.push.bind(a);a.push=t,a=a.slice();for(var s=0;s<a.length;s++)t(a[s]);var p=c;i.push([0,"chunk-vendors"]),n()})({0:function(e,t,n){e.exports=n("56d7")},"034f":function(e,t,n){"use strict";n("85ec")},"56d7":function(e,t,n){"use strict";n.r(t);n("e260"),n("e6cf"),n("cca6"),n("a79d");var o=n("2b0e"),r=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",{staticStyle:{"background-color":"#010101",width:"100%",padding:"0",margin:"0"},style:"height:"+e.pageHeight+"px",attrs:{id:"app"}},[n("router-view")],1)},i=[],l={name:"App",data:function(){return{pageHeight:document.documentElement.clientHeight}},components:{}},a=l,c=(n("034f"),n("2877")),s=Object(c["a"])(a,r,i,!1,null,null,null),p=s.exports,d=n("5c96"),u=n.n(d),f=(n("0fae"),"http://api.poi.wstudio.top:39002/");function h(){console.log("公共方法")}var v,m,y={apiUrl:f,commonFun:h},x=y,g=Object(c["a"])(x,v,m,!1,null,null,null),b=g.exports,_=n("8c4f"),w=function(){var e=this,t=e.$createElement,o=e._self._c||t;return o("div",[o("el-row",{attrs:{type:"flex",justify:"end"}},[o("el-col",{attrs:{span:22}}),o("el-col",{attrs:{span:2}},[o("a",{staticStyle:{color:"#409eff"},attrs:{href:e.templateUrl}},[e._v("模板文件")])])],1),o("el-row",{attrs:{type:"flex",justify:"center"}},[o("el-col",{attrs:{span:6}},[o("img",{staticStyle:{width:"300px",position:"relative",top:"-20px"},attrs:{src:n("cf05")}})])],1),o("el-row",{attrs:{type:"flex",justify:"center"}},[o("el-col",[o("div",{staticStyle:{"font-size":"30px",color:"white",position:"relative",top:"-90px","text-align":"center"}},[e._v("软件开发 定制服务")])])],1),o("el-row",{attrs:{type:"flex",justify:"center"}},[o("el-col",[o("el-upload",{staticClass:"upload-demo",staticStyle:{position:"relative",top:"-60px"},attrs:{action:e.importApi,headers:e.myHeaders,"file-list":e.fileList,"on-preview":e.handlePreview,"on-remove":e.handleRemove,"before-remove":e.beforeRemove,"on-success":e.handleImportSuccess,name:"excel_file",limit:1,"on-exceed":e.handleExceed}},[o("el-button",{staticStyle:{width:"200px"},attrs:{size:"small",type:"primary"},on:{click:e.reset}},[e._v("点击上传Excel文件")]),o("div",{staticClass:"el-upload__tip",attrs:{slot:"tip"},slot:"tip"},[e._v("只能上传excel文件，且不超过10M")])],1)],1)],1),o("transition",{attrs:{name:"el-zoom-in-center"}},[e.showPanel?o("div",{staticStyle:{"background-color":"#2C2C2E",width:"500px",height:"250px","border-radius":"10px",position:"relative",top:"-30px",margin:"auto"}},[o("el-progress",{staticStyle:{width:"95%",position:"relative",top:"20px",left:"10px"},attrs:{"text-inside":!0,"stroke-width":20,percentage:e.percent}}),o("div",{staticStyle:{"margin-top":"50px",color:"white"}},[o("div",{staticStyle:{display:"inline-block",width:"150px"}},[e._v("文件名 ："+e._s(e.fileName))]),o("div",{staticStyle:{display:"inline-block",width:"150px"}},[e._v("记录总数："+e._s(e.recordTotal))]),o("div",{staticStyle:{display:"inline-block",width:"150px"}},[e._v("已处理："+e._s(e.recordHandle))])]),o("div",{staticStyle:{"margin-top":"10px",color:"white"}},[o("div",{staticStyle:{display:"inline-block",width:"150px"}},[e._v("成功记录："+e._s(e.successRecord))]),o("div",{staticStyle:{display:"inline-block",width:"150px"}},[e._v("失败记录："+e._s(e.errorRecord))]),o("div",{staticStyle:{display:"inline-block",width:"150px"}},[e._v("处理效率:"+e._s(e.handlePercent)+"%")]),o("div",[o("el-button",{staticStyle:{width:"200px","margin-top":"40px"},attrs:{size:"small",type:"primary",loading:e.has_file},on:{click:e.exportExcel}},[e._v("导出数据")])],1)])],1):e._e()])],1)},S=[],j=(n("b0c0"),n("bc3a")),k=n.n(j),P={data:function(){return{importApi:"/api/import/",myHeaders:{},percent:1,has_file:!0,showPanel:!1,fileList:[],templateUrl:this._global.apiUrl+"upload/template.xlsx",fileName:"",recordTotal:0,recordHandle:0,successRecord:0,errorRecord:0,handlePercent:0}},methods:{handleRemove:function(e,t){console.log(e,t)},handlePreview:function(e){console.log(e)},handleExceed:function(){this.$message.warning("已上传")},beforeRemove:function(e){return this.$confirm("确定移除 ".concat(e.name,"？"))},handleImportSuccess:function(e){var t=this;t.showPanel=!0;var n=setInterval((function(){k.a.get("/api/job/handle/").then((function(e){t.percent=e.data.percent,t.fileName=e.data.fileName,t.recordTotal=e.data.recordTotal,t.recordHandle=e.data.recordHandle,t.successRecord=e.data.successRecord,t.errorRecord=e.data.errorRecord,t.handlePercent=e.data.handlePercent,e.data.has_file&&(t.has_file=!1,console.log("关闭定时任务"),clearInterval(n))}))}),1e3);console.log(e)},exportExcel:function(e){var t=this;k.a.get("/api/cc/").then((function(e){var n=e.data,o=document.createElement("a");o.setAttribute("href",t._global.apiUrl+"upload/"+n),document.body.appendChild(o),o.click()})),console.log(e)},reset:function(){this.fileList=[],this.percent=0,this.has_file=!0}},mounted:function(){var e=this;this.axios.get("/api/token/").then((function(t){e.myHeaders={"X-CSRFToken":t.data.token}}))}},O=P,R=Object(c["a"])(O,w,S,!1,null,null,null),E=R.exports,H=function(){var e=this,t=e.$createElement,n=e._self._c||t;return n("div",[e._v("Hello")])},T=[],C={},$=Object(c["a"])(C,H,T,!1,null,null,null),M=$.exports;o["default"].use(_["a"]);var U=new _["a"]({mode:"history",routes:[{path:"/",component:E,name:"index"},{path:"/home",component:M,name:"home"}]}),z=n("2106"),A=n.n(z);o["default"].use(A.a,k.a),o["default"].config.productionTip=!1,o["default"].use(u.a),o["default"].prototype._global=b,new o["default"]({router:U,render:function(e){return e(p)}}).$mount("#app")},"85ec":function(e,t,n){},cf05:function(e,t,n){e.exports=n.p+"img/logo.5eb20e19.png"}});
//# sourceMappingURL=app.db698e33.js.map