        KindEditor.ready(function(K) {
                window.editor = K.create('textarea[name=content]',{
                    width:800,
                    height:500,
                    uploadJson:'/admin/upload/kindeditor',

                });
        });