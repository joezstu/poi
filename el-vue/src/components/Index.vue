<template>
  <div>
    <el-row type="flex" justify="end">
      <el-col :span="22"></el-col>
      <el-col :span="2">
        <a style="color:#409eff" href="http://api.poi.wstudio.top:39002/upload/template.xlsx">模板文件</a>
      </el-col>
    </el-row>
    <el-row type="flex" justify="center">
      <el-col :span="6">
        <img src="../assets/logo.png" style="width:300px;position:relative;top:-20px" />
      </el-col>
    </el-row>
    <el-row type="flex" justify="center">
      <el-col>
        <div style="font-size:30px;color:white;position:relative;top:-90px;text-align: center">软件开发 定制服务</div>
      </el-col>
    </el-row>
    <el-row type="flex" justify="center">
      <el-col>
        <el-upload
            class="upload-demo"
            :action="importApi"
            :headers="myHeaders"
            :file-list="fileList"
            :on-preview="handlePreview"
            :on-remove="handleRemove"
            :before-remove="beforeRemove"
            :on-success="handleImportSuccess"
            name="excel_file"
            :limit="1"
            :on-exceed="handleExceed"
            style="position:relative;top:-60px"
        >
          <el-button size="small" type="primary" style="width:200px" @click="reset">点击上传Excel文件</el-button>
          <div slot="tip" class="el-upload__tip">只能上传excel文件，且不超过10M</div>
        </el-upload>
      </el-col>
    </el-row>

    <transition name="el-zoom-in-center">
    <div v-if="showPanel" style="background-color:#2C2C2E;width:500px;height:250px;border-radius: 10px;position:relative;top:-30px;margin:auto">
      <el-progress :text-inside="true" :stroke-width="20" :percentage="percent" style="width:95%;position:relative;top:20px;left:10px"></el-progress>
      <div style="margin-top:50px;color:white;">
        <div style="display: inline-block;width:150px">文件名 ：excel.xlsx</div>
        <div style="display: inline-block;width:150px">记录总数：4000</div>
        <div style="display: inline-block;width:150px">有返回数据：2000</div>
      </div>
      <div style="margin-top:10px;color:white;">
        <div style="display: inline-block;width:150px">成功记录：excel.xlsx</div>
        <div style="display: inline-block;width:150px">失败记录：1000</div>
        <div style="display: inline-block;width:150px">无返回数据：1000</div>

      </div>
      <div style="margin-top:10px;color:white;">
        <div style="display: inline-block;width:150px">处理效率：75%</div>
        <div style="display: inline-block;width:150px">实际效率：50%</div>
      </div>
      <div>
        <el-button size="small" type="primary" style="width:200px;margin-top:40px" @click="exportExcel" :loading="has_file">导出数据</el-button>
      </div>
    </div>
    </transition>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
            importApi : '/api/import/',
            myHeaders : {},
            percent:1,//数据处理进度
            has_file:true,//服务器是否已经存储处理后的excel文件
            showPanel:false,//是否显示数据面板
            fileList:[],

          };
  },
  methods: {
    handleRemove(file, fileList) {
      console.log(file, fileList);
    },
    handlePreview(file) {
      console.log(file);
    },
    handleExceed() {
      this.$message.warning('已上传');
    },
    beforeRemove(file) {
      return this.$confirm(`确定移除 ${ file.name }？`);
    },
    handleImportSuccess(res){
      var _this = this

      //显示数据面板
      _this.showPanel = true

      const tmp = setInterval(function(){
        axios.get('/api/job/handle/').then((res)=>{
          _this.percent = res.data.percent

          if(res.data.has_file){
            _this.has_file = false
            console.log('关闭定时任务')
            clearInterval(tmp)
          }
        })
      },1000)
      console.log(res)
    },
    exportExcel(e){
      axios.get('/api/cc/').then((res)=>{
        const file_name = res.data

        const a = document.createElement('a');
        a.setAttribute('href', this._global.apiUrl + 'upload/'+file_name);
        document.body.appendChild(a);
        a.click();

      })
      console.log(e)
    },
    reset(){
      //重置数据面板
      this.fileList = []
      this.percent = 0
      this.has_file = true
    }
  },
  mounted() {
    this.axios.get('/api/token/').then((res)=>{

      this.myHeaders = {"X-CSRFToken":res.data.token}
      //
      // this.axios({
      //   url:'api/import/',
      //   method:'post',
      //   headers: {
      //     'X-CSRFToken': res.data.token
      //   }
      // }).then((res)=>{
      //   console.log(res)
      // })
    })
    console.log('888',this._global.apiUrl)
  }
}
</script>
