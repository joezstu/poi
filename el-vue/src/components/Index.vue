<template>
  <div>
    <el-row type="flex" justify="end">
      <el-col :span="22"></el-col>
      <el-col :span="2">
        <a style="color:#409eff" href="#">模板文件</a>
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
            :on-preview="handlePreview"
            :on-remove="handleRemove"
            :before-remove="beforeRemove"
            :on-success="handleImportSuccess"
            multiple
            :limit="3"
            :on-exceed="handleExceed"
            style="position:relative;top:-60px"
        >
          <el-button size="small" type="primary" style="width:200px">点击上传Excel文件</el-button>
          <div slot="tip" class="el-upload__tip">只能上传excel文件，且不超过10M</div>
        </el-upload>
      </el-col>
    </el-row>

    <div style="background-color:#2C2C2E;width:500px;height:250px;border-radius: 10px;position:relative;top:-30px;margin:auto">
      <el-progress :text-inside="true" :stroke-width="20" :percentage="70" style="width:95%;position:relative;top:20px;left:10px"></el-progress>
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
        <el-button size="small" type="primary" style="width:200px;margin-top:40px">导出数据</el-button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
            importApi : '/api/import/',
            myHeaders : {}
          };
  },
  methods: {
    handleRemove(file, fileList) {
      console.log(file, fileList);
    },
    handlePreview(file) {
      console.log(file);
    },
    handleExceed(files, fileList) {
      this.$message.warning(`当前限制选择 3 个文件，本次选择了 ${files.length} 个文件，共选择了 ${files.length + fileList.length} 个文件`);
    },
    beforeRemove(file) {
      return this.$confirm(`确定移除 ${ file.name }？`);
    },
    handleImportSuccess(res){
      console.log(res)
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
