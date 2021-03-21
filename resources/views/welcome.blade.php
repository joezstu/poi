<form action="/export" method="post" enctype="multipart/form-data" >
    {{csrf_field()}}
    <input type="file" name="e_file"/>
    <button>上传</button>
</form>
