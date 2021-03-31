<template>
    <div>
        <el-row>
            <el-col :span="24">
                <el-upload
                    class="upload-demo"
                    :action="action"
                    :headers="myHeaders"
                    :on-preview="handlePreview"
                    :on-remove="handleRemove"
                    :before-remove="beforeRemove"
                    :limit="1"
                    :name="e_file"
                    :showProcess="1"
                    :on-exceed="handleExceed"
                    :on-change="handleChange"
                    :on-success="handleSuccess"
                    :disabled="able"
                    :file-list="fileList">
                    <el-button size="small" type="primary" :loading="isLoading">{{buttonContent}}</el-button>

                </el-upload>
            </el-col>
        </el-row>
        <el-row>
            <el-progress :text-inside="true" :stroke-width="26" :percentage="percent" v-if="showProgress"></el-progress>
        </el-row>
        <el-row>
            <a
                type="button"
                href="http://poi.wstudio.top/api/output/"
                download="file.xlsx"
                v-if="canExport"
            >
                <button
                    @click="re_load_page"
                    class="btn btn-primary"
                >
                    导出excel
                </button>
            </a>
        </el-row>
    </div>

</template>
<script>
import axios from "axios";

export default {
    data() {
        return {
            fileList: [],
            myHeaders:{ 'X-CSRF-TOKEN': document.getElementById('_token').content },
            e_file: 'e_file',
            showProcess:0,
            processLength:0,
            action:'http://poi.wstudio.top/api/import',
            showOutput:1,
            percent:0,
            able:false,
            canExport:false,
            showProgress:false,
            buttonContent:'点击上传',
            isLoading:false
        };
    },
    methods: {
        handleRemove(file, fileList) {
            console.log(888,file, fileList);
        },
        handlePreview(file) {
            console.log(file);
        },
        handleExceed(files, fileList) {
            this.$message.warning('正在上传');
        },
        beforeRemove(file, fileList) {
            return this.$confirm(`确定移除 ${ file.name }？`);
        },
        changeButton(res){
            console.log(res);
        },
        handleChange(file,fileList){
            this.showProgress = true
            this.able = true
            this.buttonContent = '正在处理'
            this.isLoading = true
            console.log(999,this,file,fileList)
        },
        handleSuccess(res,file,fileList){
            console.log(123,typeof(res),res,file,fileList)
        },
        re_load_page(){
            this.showProgress = false
            this.able = false
            location.reload()
        }

    },
    mounted() {console.log(888)

        var _this = this;

        axios.get('http://poi.wstudio.top/api/reset')
            .then(function (response) {
                _this.timer = setInterval(function(){
                    axios.get('http://poi.wstudio.top/api/getPercent')
                        .then(function (response) {
                            _this.percent = response.data
                            console.log(888,response);
                        })
                        .catch(function (error) {
                            console.log(error);
                        });
                    if(_this.percent == '100'){
                        _this.canExport = true;
                        _this.buttonContent = '处理完成'
                        _this.isLoading = false
                        clearInterval(_this.timer);
                    }
                }, 1000);
            })
            .catch(function (error) {
                console.log(error);
            });


    },
    beforeDestroy() {
        clearInterval(this.timer);
    }
}
</script>
