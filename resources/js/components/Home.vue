<template>
    <el-upload
        class="upload-demo"
        action="/api/import"
        :headers="myHeaders"
        :on-preview="handlePreview"
        :on-remove="handleRemove"
        :before-remove="beforeRemove"
        :limit="1"
        :name="e_file"
        :on-exceed="handleExceed"
        :on-success="changeButton"
        :file-list="fileList">
        <el-button size="small" type="primary">点击上传</el-button>
        <div slot="tip" class="el-upload__tip">只能上传jpg/png文件，且不超过500kb</div>
    </el-upload>

</template>
<script>

export default {
    data() {
        return {
            fileList: [],
            myHeaders:{ 'X-CSRF-TOKEN': document.getElementById('_token').content },
            e_file: 'e_file',
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
            this.$message.warning('已上传');
        },
        beforeRemove(file, fileList) {
            return this.$confirm(`确定移除 ${ file.name }？`);
        },
        changeButton(res){
            console.log(res);
        }
    }
}
</script>
