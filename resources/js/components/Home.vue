<template>
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
        :file-list="fileList">
        <el-button size="small" type="primary">点击上传</el-button>
    </el-upload>

</template>
<script>

export default {
    data() {
        return {
            fileList: [],
            myHeaders:{ 'X-CSRF-TOKEN': document.getElementById('_token').content },
            e_file: 'e_file',
            showProcess:0,
            processLength:0,
            action:'http://poi.wstudio.top/api/import'
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
            this.$message.warning('已上传');
        },
        beforeRemove(file, fileList) {
            return this.$confirm(`确定移除 ${ file.name }？`);
        },
        changeButton(res){
            console.log(res);
        },
        handleChange(file,fileList){
            file.percentage = 50
            console.log(999,this,file,fileList)
        },
        handleSuccess(res,file,fileList){
            console.log(123,typeof(res),res,file,fileList)
        }
    }
}
</script>
